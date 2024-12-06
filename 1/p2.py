with open('input.txt', 'r') as f:
    left, right = zip(*([int(n) for n in line.split(' ')] for line in f.read().split('\n') if line))

print(sum(right.count(n) * n for n in left))
