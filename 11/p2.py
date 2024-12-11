with open('input.txt', 'r') as f:
    stones = [int(stone) for stone in f.read().split(' ')]

cache = {}
def memoise(func):
    def cached(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return cached

@memoise
def countstones(stone: int, count = 0) -> int:
    if count == 75:
        return 1
    count += 1
    if stone == 0:
        return countstones(1, count)
    digits = str(stone)
    if len(digits) % 2 == 0:
        step = len(digits) // 2
        return sum(
            countstones(int(digits[i:i + step]), count)
            for i in range(0, len(digits), step)
        )
    return countstones(stone * 2024, count)

print(sum(countstones(stone) for stone in stones))
