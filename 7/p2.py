with open('input.txt', 'r') as f:
    calibrations = [
        (
            int(line.split(': ')[0]),
            [ int(n) for n in line.split(': ')[1].split(' ') ]
        )
        for line in f.read().split('\n')
        if line
    ]

def possible(result: int, values: list[int]) -> bool:
    if len(values) == 1:
        return values[0] == result

    operators = [
        lambda a, b: a + b,
        lambda a, b: a * b,
        lambda a, b: int(str(a) + str(b))
    ]

    return any(
        possible(result, [operator(*values[:2])] + values[2:])
        for operator in operators
    )

print(sum(
    result
    for result, equations in calibrations
    if possible(result, equations)
))
