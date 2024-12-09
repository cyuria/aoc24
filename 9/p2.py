from itertools import groupby

with open('input.txt', 'r') as f:
    map = [int(digit) for digit in f.read() if digit in '0123456789']

def popfrag(data: list[int], map: list[int]):
    size = map.pop()
    id = len(map) // 2
    offset = sum(map)
    map.pop()

    try:
        index = next(
            g[0][0]
            for k, g in (
                (k, list(g))
                for k, g in
                groupby(enumerate(data[:offset]), key=lambda v: v[1])
            )
            if k == -1 and len(g) >= size
        )
    except StopIteration:
        return

    data[offset:offset+size] = [-1] * size
    data[index:index+size] = [id] * size
    

def defrag(map: list[int]):
    map = [0] + map

    free = [
        [-1] * count
        for count in map[::2]
    ]
    files = [
        [i] * count
        for i, count in enumerate(map[1::2])
    ]

    data = [
        block
        for pair in zip(free, files)
        for file in pair
        for block in file
    ]

    while map:
        popfrag(data, map)
    return data

print(sum(i * e for i, e in enumerate(defrag(map)) if e != -1))

