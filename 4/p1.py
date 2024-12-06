
with open('input.txt', 'r') as f:
    data = [list(line) for line in f.read().split('\n') if line]

queries = 'XMAS', 'SAMX'
def hori(window) -> bool:
    return ''.join(next(iter(window))) in queries

def diag(window) -> bool:
    if len(window) < 4 or len(window[0]) < 4:
        return False
    return ''.join(l[n] for n, l in enumerate(window)) in queries

def search(window: list[list[str]]) -> int:
    return sum([
        hori(window),
        hori(zip(*window)),
        diag(window),
        diag(window[::-1])
    ])

print(sum(
    search([line[x:x+4] for line in data[y:y+4]])
    for y in range(len(data))
    for x in range(len(data[y]))
))
