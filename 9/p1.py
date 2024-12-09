
with open('input.txt', 'r') as f:
    map = [int(digit) for digit in f.read() if digit in '0123456789']

def defrag(map: list[int]):
    files = [
        [i] * count
        for i, count in enumerate(map[::2])
    ]
    free = [
        [-1] * count
        for count in map[1::2] + [0]
    ]

    data = [
        block
        for pair in zip(files, free)
        for file in pair
        for block in file
    ]

    files = [block for block in data if block != -1]

    return [
        block if block != -1 else files[-data[:i + 1].count(-1)]
        for i, block in enumerate(data[:len(files)])
    ]

print(sum(i * e for i, e in enumerate(defrag(map))))

