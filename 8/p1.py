
with open('input.txt', 'r') as f:
    map = [list(line) for line in f.read().split('\n') if line]

def antinode(map, x, y) -> bool:
    for j, row in enumerate(map):
        for i, tile in enumerate(row):
            if i == x and j == y:
                continue
            if tile == '.':
                continue
            py = 2 * j - y
            px = 2 * i - x
            if py < 0 or px < 0:
                continue
            if py >= len(map) or px >= len(map[py]):
                continue
            if map[py][px] == tile:
                return True
    return False

print(sum(
    sum(
        1
        for x in range(len(map[y]))
        if antinode(map, x, y)
    )
    for y in range(len(map))
))
