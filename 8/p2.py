
with open('input.txt', 'r') as f:
    map = [list(line) for line in f.read().split('\n') if line]

def antinode(map, x, y) -> bool:
    for j, row in enumerate(map):
        for i, tile in enumerate(row):
            if i == x and j == y:
                continue
            if tile == '.':
                continue
            c = 2
            while True:
                dy = y + c * (j - y)
                dx = x + c * (i - x)
                if dy < 0 or dx < 0:
                    break
                if dy >= len(map) or dx >= len(map[dy]):
                    break
                if map[dy][dx] == tile:
                    return True
    return False

def populate(map) -> list[list[bool]]:
    antinodes = [[False for _ in row] for row in map]
    antennas = [
        {
            (x, y)
            for y, row in enumerate(map)
            for x, tile in enumerate(row)
            if tile == symbol
        }
        for symbol in
        'abcdefghijklmnopqrstuvwxyz'
        'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        '0123456789'
    ]
    for frequency in antennas:
        for a in frequency:
            for b in frequency.difference({a}):
                x, y = b[0], b[1]
                dx, dy = b[0] - a[0], b[1] - a[1]
                c = 0
                while True:
                    if y + c * dy < 0 or x + c * dx < 0:
                        break
                    if y + c * dy >= len(map) or x + c * dx >= len(map[y + c * dy]):
                        break
                    antinodes[y + c * dy][x + c * dx] = True
                    c += 1
    return antinodes

print(sum(sum(row) for row in populate(map)))
