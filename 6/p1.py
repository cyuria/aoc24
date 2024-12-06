
with open('input.txt', 'r') as f:
    map = [
        list(line)
        for line in f.read().split('\n')
    ]

def find_guard(map):
    for y, row in enumerate(map):
        for x, tile in enumerate(row):
            if tile in '^v<>':
                return x, y
    raise Exception('no guard')

def move(map):
    try:
        while True:
            x, y = find_guard(map)
            guard = map[y][x]
            map[y][x] = 'X'
            match guard:
                case '^':
                    direction = (0, -1)
                case 'v':
                    direction = (0, 1)
                case '<':
                    direction = (-1, 0)
                case '>':
                    direction = (1, 0)
                case _:
                    raise Exception('no guard')

            if map[y + direction[1]][x + direction[0]] == '#':
                match guard:
                    case '^':
                        map[y][x] = '>'
                    case 'v':
                        map[y][x] = '<'
                    case '<':
                        map[y][x] = '^'
                    case '>':
                        map[y][x] = 'v'
            else:
                y += direction[1]
                x += direction[0]
                map[y][x] = guard

    except Exception:
        return

move(map)
print(sum(
    sum(1 for tile in row if tile == 'X')
    for row in map
))
