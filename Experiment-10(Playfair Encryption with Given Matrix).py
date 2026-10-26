grid = [
    ['M', 'F', 'H', 'I', 'K'],
    ['U', 'N', 'O', 'P', 'Q'],
    ['Z', 'V', 'W', 'X', 'Y'],
    ['E', 'L', 'A', 'R', 'G'],
    ['D', 'S', 'T', 'B', 'C']
]

pos = {grid[r][c]: (r, c) for r in range(5) for c in range(5)}
pos['J'] = pos['I']

raw = "Must see you over Cadogan West. Coming at once."
chars = [c.upper() if c.upper() != 'J' else 'I' for c in raw if c.isalpha()]

pairs, i = [], 0
while i < len(chars):
    a = chars[i]
    if i + 1 < len(chars):
        b = chars[i + 1]
        if a == b:
            pairs.append((a, 'X'))
            i += 1
        else:
            pairs.append((a, b))
            i += 2
    else:
        pairs.append((a, 'X'))
        i += 1

ct = []
for a, b in pairs:
    r1, c1 = pos[a]
    r2, c2 = pos[b]
    if r1 == r2:
        ct.extend([grid[r1][(c1 + 1) % 5], grid[r2][(c2 + 1) % 5]])
    elif c1 == c2:
        ct.extend([grid[(r1 + 1) % 5][c1], grid[(r2 + 1) % 5][c2]])
    else:
        ct.extend([grid[r1][c2], grid[r2][c1]])

print(" ".join("".join(ct[i:i+2]) for i in range(0, len(ct), 2)))
