import regex as re

with open('input.txt', 'r') as f:
    data = f.read().replace('\n', ' ')

print(sum(
    int(match.group('a')) * int(match.group('b'))
    for match in re.finditer(
        r"(?<=(^|do\(\))((?!don't\(\)).)*)mul\((?P<a>[0-9]+),(?P<b>[0-9]+)\)",
        data
    )
))
