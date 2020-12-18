
import sys

def tokenize(src):
    if len(src) == 1:
        return [src], []
    tokens = []
    ops = []
    idx = 0
    while idx < len(src):
        if src[idx].isnumeric():
            tokens.append(src[idx])
            if idx + 2 < len(src):
                ops.append(src[idx + 2])
            idx += 4
        else:
            num_parens = 1
            start_idx = idx
            idx += 1
            while num_parens > 0:
                if src[idx] == "(":
                    num_parens += 1
                elif src[idx] == ")":
                    num_parens -= 1
                idx += 1
            next_token = src[start_idx + 1 : idx - 1]
            tokens.append(tokenize(next_token))
            if idx + 1 < len(src):
                ops.append(src[idx + 1])
            idx += 3
    return tokens, ops

def prioritize_adds(tree):
    if isinstance(tree, str):
        return tree
    tokens, ops = tree
    tokens = list(map(prioritize_adds, tokens))

    result_tokens = []
    result_ops = []
    idx = 0
    while True:
        try:
            first_mult = ops.index("*", idx)
        except:
            break
        first_node = (tokens[idx:first_mult + 1], ops[idx:first_mult])
        result_tokens.append(first_node)
        idx = first_mult + 1
    last_node = (tokens[idx:], ops[idx:])
    result_tokens.append(last_node)
    return result_tokens, ["*"] * (len(result_tokens) - 1)

def evaluate(tree):
    if isinstance(tree, str):
        return int(tree)
    tokens, ops = tree
    values = list(map(evaluate, tokens))
    ans = values[0]
    for op, value in zip(ops, values[1:]):
        if op == "*":
            ans *= value
        else:
            ans += value
    return ans



ans = 0
second_ans = 0
for line in sys.stdin.readlines():
    tree = tokenize(line.strip())
    ans += evaluate(tree)
    prior = prioritize_adds(tree)
    second_ans += evaluate(prior)
print(ans)
print(second_ans)
