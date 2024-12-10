
with open('input.txt', 'r') as f:
    map = [
        [int(d) for d in line]
        for line in f.read().split('\n')
        if line
    ]


def routes(map, x, y) -> list[list[tuple[int, int]]]:
    height = map[y][x]
    if height == 9:
        return [[(x, y)]]
    def valid(coord):
        if coord[0] < 0 or coord[1] < 0:
            return False
        if coord[1] >= len(map) or coord[0] >= len(map[coord[1]]):
            return False
        return True
    offsets = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
    ]
    return [
        [(x, y)] + trail
        for dx, dy in offsets
        if valid((x + dx, y + dy)) and map[y + dy][x + dx] == height + 1
        for trail in routes(map, x + dx, y + dy)
    ]

trails = [
    trail
    for y in range(len(map))
    for x in range(len(map[y]))
    if map[y][x] == 0
    for trail in routes(map, x, y)
]

print(len({
    (trail[0], trail[-1])
    for trail in trails
}))