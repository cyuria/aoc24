
with open('input.txt', 'r') as f:
    rules, updates = f.read().split('\n\n')
    rules = [
        (int(rule.split('|')[0]), int(rule.split('|')[1]))
        for rule in rules.split('\n')
        if rule
    ]
    updates = [
        [int(page) for page in update.split(',')]
        for update in updates.split('\n')
        if update
    ]

def position(rules: list[tuple[int, int]], update: list[int]) -> tuple[int, int] | None:
    for i, page in enumerate(update):
        for rule in rules:
            if rule[1] == page:
                if rule[0] not in update[:i]:
                    return i, update.index(rule[0])
    return None

def correct(rules: list[tuple[int, int]], update: list[int]) -> bool:
    rules = [rule for rule in rules if rule[0] in update and rule[1] in update]
    return position(rules, update) is None

def corrected(rules: list[tuple[int, int]], update: list[int]) -> list[int]:
    rules = [rule for rule in rules if rule[0] in update and rule[1] in update]
    while i := position(rules, update):
        tmp = update[i[0]]
        update[i[0]] = update[i[1]]
        update[i[1]] = tmp
    return update

print(sum(
    update[len(update) // 2]
    for update in (
        corrected(rules, update)
        for update in updates
        if not correct(rules, update)
    )
))
