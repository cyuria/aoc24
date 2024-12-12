
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

def adjacent(map: list[list[str]], x: int, y: int) -> list[tuple[int, int]]:
    def valid(map: list[list[str]], x: int, y: int) -> bool:
        if x < 0 or y < 0:
            return False
        if y >= len(map) or x >= len(map[y]):
            return False
        return True

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

def perimeter(map: list[list[str]], region: frozenset[tuple[int, int]]) -> int:
    return sum(
        4 - len(adjacent(map, x, y))
        for x, y in region
    )

def area(region: frozenset[tuple[int, int]]):
    return len(region)

regions = set()
for y in range(len(map)):
    for x in range(len(map[y])):
        if any((x, y) in region for region in regions):
            continue
        regions.add(frozenset(expand(map, x, y, set())))

print(sum(
    perimeter(map, region) * area(region)
    for region in regions
))
