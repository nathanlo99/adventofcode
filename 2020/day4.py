
import sys

def valid_height(height):
    prefix = "" if len(height) < 2 else height[-2:]
    number = height[:-2]
    if prefix == "cm":
        return 150 <= int(number) <= 193
    elif prefix == "in":
        return 59 <= int(number) <= 76
    else:
        return False

def valid_hair_colour(colour):
    return len(colour) == 7 and colour[0] == "#" and all(c in "0123456789abcdef" for c in colour[1:7])

def valid(fields):
    birthyear = "byr" in fields and fields["byr"].isnumeric() and 1920 <= int(fields["byr"]) <= 2002
    issueyear = "iyr" in fields and fields["iyr"].isnumeric() and 2010 <= int(fields["iyr"]) <= 2020
    expirationyear = "eyr" in fields and fields["eyr"].isnumeric() and 2020 <= int(fields["eyr"]) <= 2030
    height = "hgt" in fields and valid_height(fields["hgt"])
    hcl = "hcl" in fields and valid_hair_colour(fields["hcl"])
    ecl = "ecl" in fields and fields["ecl"] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    pid = "pid" in fields and fields["pid"].isnumeric() and len(fields["pid"]) == 9

    return birthyear and issueyear and expirationyear and height and hcl and ecl and pid

ans = 0
fields = dict()
for line in sys.stdin.readlines():
    if line.strip() == "":
        if valid(fields):
            ans += 1
        fields = dict()
    else:
        for pair in line.split():
            k, v = pair.split(":")
            fields[k] = v

if valid(fields):
    ans += 1

print(ans)
