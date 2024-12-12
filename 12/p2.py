
with open('input.txt', 'r') as f:
    map = [
        list(line)
        for line in f.read().split('\n')
        if line
    ]

def expand(map: list[list[str]], x: int, y: int, region: set[tuple[int, int]]) -> set[tuple[int, int]]:
    if (x, y) in region:
        return region
    region.add((x, y))
    for x, y in adjacent(map, x, y):
        expand(map, x, y, region)
    return region

def valid(map: list[list[str]], x: int, y: int) -> bool:
    if x < 0 or y < 0:
        return False
    if y >= len(map) or x >= len(map[y]):
        return False
    return True

def adjacent(map: list[list[str]], x: int, y: int) -> list[tuple[int, int]]:
    offsets = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]

    return [
        (x + dx, y + dy)
        for dx, dy in offsets
        if valid(map, x + dx, y + dy)
        if map[y + dy][x + dx] == map[y][x]
    ]


def sides(map: list[list[str]], region: frozenset[tuple[int, int]]) -> int:
    table = [
        4, 4, 2, 2, 4, 4, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1,
        2, 2, 2, 2, 2, 2, 1, 1, 0, 0, 2, 1, 0, 0, 1, 0,
        4, 4, 2, 2, 4, 4, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1,
        2, 2, 2, 2, 2, 2, 1, 1, 0, 0, 2, 1, 0, 0, 1, 0,
        2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 2, 1, 2, 2, 2, 1,
        2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 4, 3, 2, 2, 3, 2,
        2, 2, 0, 0, 2, 2, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0,
        2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 3, 2, 1, 1, 2, 1,
        4, 4, 2, 2, 4, 4, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1,
        2, 2, 2, 2, 2, 2, 1, 1, 0, 0, 2, 1, 0, 0, 1, 0,
        4, 4, 2, 2, 4, 4, 2, 2, 2, 2, 2, 1, 2, 2, 2, 1,
        2, 2, 2, 2, 2, 2, 1, 1, 0, 0, 2, 1, 0, 0, 1, 0,
        2, 2, 0, 0, 2, 2, 0, 0, 2, 2, 2, 1, 2, 2, 2, 1,
        1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 3, 2, 1, 1, 2, 1,
        2, 2, 0, 0, 2, 2, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0,
        1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 1, 0, 0, 1, 0
    ]
    def index(tile_x, tile_y) -> int:
        bits = (
            int(map[y][x] == map[tile_y][tile_x])
            if valid(map, x, y)
            else 0
            for y in range(tile_y - 1, tile_y + 2)
            for x in range(tile_x - 1, tile_x + 2)
            if (x, y) != (tile_x, tile_y)
        )
        return sum(
            bit << (7 - n)
            for n, bit in enumerate(bits)
        )

    corners = sum(
        table[index(x, y)]
        for x, y in region
    )
    return corners

def area(region: frozenset[tuple[int, int]]):
    return len(region)

regions = set()
for y in range(len(map)):
    for x in range(len(map[y])):
        if any((x, y) in region for region in regions):
            continue
        regions.add(frozenset(expand(map, x, y, set())))

print(sum(
    sides(map, region) * area(region)
    for region in regions
))
