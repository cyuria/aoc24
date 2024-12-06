
with open('input.txt', 'r') as f:
    map = [
        list(line)
        for line in f.read().split('\n')
        if line
    ]

def find_guard(map):
    for y, row in enumerate(map):
        for x, tile in enumerate(row):
            if tile in '^>v<':
                return x, y, '^>v<'.index(tile)
    raise Exception('no guard')

def move_loop(map) -> bool:
    try:
        x, y, t = find_guard(map)
    except Exception:
        return False
    dir = [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0),
    ]

    while True:
        if map[y][x] == t:
            return True

        if map[y][x] not in range(4):
            map[y][x] = t

        y += dir[t][1]
        x += dir[t][0]

        if x < 0 or y < 0:
            return False
        if y >= len(map) or x >= len(map[y]):
            return False

        if map[y][x] == '#':
            y -= dir[t][1]
            x -= dir[t][0]
            t += 1
            t %= 4


def get_coords(map):
    cpy = [row[::] for row in map]
    move_loop(cpy)
    return (
        (x, y)
        for y, row in enumerate(cpy)
        for x, tile in enumerate(row)
        if tile in range(4)
    )

def printm(map):
    print('--')
    for row in map:
        print(' ', [str(tile) for tile in row])

def test_map(map, x, y):
    cpy = [row[::] for row in map]
    cpy[y][x] = '#'
    ret = move_loop(cpy)
    return ret

print(sum(
    1 for x, y in get_coords(map)
    if test_map(map, x, y)
))
