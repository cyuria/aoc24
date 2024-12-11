
with open('input.txt', 'r') as f:
    stones = [int(stone) for stone in f.read().split(' ')]

def blink(stones: list[int]) -> list[int]:
    def replace(stone: int) -> list[int]:
        if stone == 0:
            return [1]
        digits = str(stone)
        if len(digits) % 2 == 0:
            return [
                int(digits[:len(digits) // 2]),
                int(digits[len(digits) // 2:])
            ]
        return [stone * 2024]
    return [
        stone
        for number in stones
        for stone in replace(number)
    ]

for _ in range(30):
    stones = blink(stones)

print(len(stones))
