with open('input.txt', 'r') as f:
    reports = [
        [int(level) for level in line.split(' ')]
        for line in
        f.read().split('\n')
        if line
    ]

def up(level: list[int]) -> bool:
    return all(
        a - b >= 1 and a - b <= 3
        for a, b in
        zip(level[:-1], level[1:])
    )
def down(level: list[int]) -> bool:
    return all(
        a - b >= 1 and a - b <= 3
        for a, b in
        zip(level[1:], level[:-1])
    )

def damp(fn, level: list[int]) -> bool:
    return not all(
        not fn(level[:i] + level[i+1:])
        for i in range(len(level))
    )

print(sum(damp(up, level) or damp(down, level) for level in reports))
