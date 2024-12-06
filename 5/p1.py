
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

def correct(rules: list[tuple[int, int]], update: list[int]) -> bool:
    rules = [rule for rule in rules if rule[0] in update and rule[1] in update]
    for i, page in enumerate(update):
        for rule in rules:
            if rule[1] == page:
                if rule[0] not in update[:i]:
                    return False
    return True

print(sum(
    update[len(update) // 2]
    for update in updates
    if correct(rules, update)
))
