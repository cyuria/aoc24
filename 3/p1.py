import re

with open('input.txt', 'r') as f:
    data = f.read()

print(sum(
    int(m.group(1)) * int(m.group(2))
    for m in re.finditer(
        r"mul\(([0-9]+),([0-9]+)\)",
        data
    )
))
