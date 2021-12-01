
import sys
import itertools

rules = dict()
ans = 0

check_memo = dict()
def check(rule_num, string):
    clauses = rules[rule_num]
    if isinstance(clauses, str):
        return string == clauses
    if (rule_num, string) not in check_memo:
        for clause in clauses:
            num_clauses = len(clause)
            for splits in itertools.combinations(range(1, len(string)), num_clauses - 1):
                splits = [0] + list(splits) + [len(string)]
                for child_rule, start, end in zip(clause, splits[:-1], splits[1:]):
                    subproblem = string[start:end]
                    if not check(child_rule, subproblem):
                        break
                else:
                    check_memo[(rule_num, string)] = True
                    return check_memo[(rule_num, string)]
        check_memo[(rule_num, string)] = False
    return check_memo[(rule_num, string)]

for line in map(lambda x : x.strip(), sys.stdin.readlines()):
    line = line.strip()
    if not line:
        rules["8"] = [["42"], ["42", "8"]]
        rules["11"] = [["42", "31"], ["42", "11", "31"]]
        continue
    if ":" in line:
        num, pattern = map(lambda x: x.strip(), line.split(":"))
        if '"' in pattern:
            rules[num] = pattern[1]
        else:
            clauses = list(map(lambda x: x.strip().split(), pattern.split("|")))
            rules[num] = clauses
    else:
        print(line)
        result = check("0", line)
        print(result)
        if result:
            ans += 1

print(ans)
