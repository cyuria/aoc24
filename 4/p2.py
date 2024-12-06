
with open('input.txt', 'r') as f:
    data = [list(line) for line in f.read().split('\n') if line]

queries = 'MAS', 'SAM'
def search(window) -> bool:
    return (
        ''.join(l[n] for n, l in enumerate(window)) in queries and
        ''.join(l[n] for n, l in enumerate(window[::-1])) in queries
    )

print(sum(
    search([line[x:x+3] for line in data[y:y+3]])
    for y in range(len(data) - 2)
    for x in range(len(data[y]) - 2)
))
