
def corner(corner, side_a, side_b) -> bool:
    if side_a == 0 and side_b == 0:
        return True
    return corner == 0 and side_a == side_b

table = [0] * 256
for i in range(256):
    bits = [
        (i >> n) & 1
        for n in range(8)
    ]
    table[i] = sum((
        corner(bits[0], bits[1], bits[3]),
        corner(bits[2], bits[1], bits[4]),
        corner(bits[5], bits[6], bits[3]),
        corner(bits[7], bits[6], bits[4]),
    ))

print(table)
