with open('input.txt', 'r') as f:
    data = [list(line) for line in f.read().split('\n') if line]

def horizontal(search) -> int:
    return sum(
        ''.join(line).count('XMAS') +
        ''.join(line).count('SAMX')
        for line in search
    )

def diagonal(search) -> int:
    return horizontal(zip(*(
        ['.'] * (len(search) - n - 1) + list(line) + ['.'] * n
        for n, line in enumerate(search)
    )))

print(
    horizontal(data) +
    horizontal(zip(*data)) +
    diagonal(data) +
    diagonal(data[::-1])
)
