key = "ROYAL NEW ZEALAND NAVY"
m = []
for c in (key + "ABCDEFGHIKLMNOPQRSTUVWXYZ").replace("J", "I"):
    if c.isalpha() and c not in m:
        m.append(c)

grid = [m[i : i + 5] for i in range(0, 25, 5)]
pos = {grid[r][c]: (r, c) for r in range(5) for c in range(5)}

ct = (
    "KXJEYUREBEZWEHEWRYTUHEYFSKREHEGOYFIWTTTUOLKSYCAJPO"
    "BOTEIZONTXBYBNTGONEYCUZWRGDSONSXBOUYWRHEBAAHYUSEDQ"
)

# Fix: Replace all 'J' with 'I' in ciphertext
ct = ct.replace("J", "I")

pt = []
for i in range(0, len(ct), 2):
    r1, c1 = pos[ct[i]]
    r2, c2 = pos[ct[i + 1]]
    if r1 == r2:
        pt.extend([grid[r1][(c1 - 1) % 5], grid[r2][(c2 - 1) % 5]])
    elif c1 == c2:
        pt.extend([grid[(r1 - 1) % 5][c1], grid[(r2 - 1) % 5][c2]])
    else:
        pt.extend([grid[r1][c2], grid[r2][c1]])

print("".join(pt))
