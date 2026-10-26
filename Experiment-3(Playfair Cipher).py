def create_playfair_matrix(key):
    used = set(["J"])
    mat = []
    for ch in (key.upper() + "ABCDEFGHIJKLMNOPQRSTUVWXYZ").replace("J", "I"):
        if ch.isalpha() and ch not in used:
            used.add(ch)
            mat.append(ch)
    return [mat[i:i+5] for i in range(0, 25, 5)]
def playfair_process(text, matrix, mode="enc"):
    pos = {matrix[r][c]: (r, c) for r in range(5) for c in range(5)}
    shift = 1 if mode == "enc" else -1
    chars = [c.upper() if c.upper() != "J" else "I" for c in text if c.isalpha()]
    pairs, i = [], 0
    if mode == "enc":
        while i < len(chars):
            a = chars[i]
            if i + 1 < len(chars):
                b = chars[i + 1]
                if a == b:
                    pairs.append((a, "X"))
                    i += 1
                else:
                    pairs.append((a, b))
                    i += 2
            else:
                pairs.append((a, "X"))
                i += 1
    else:
        pairs = [(chars[i], chars[i+1]) for i in range(0, len(chars), 2)]
    out = []
    for a, b in pairs:
        r1, c1 = pos[a]
        r2, c2 = pos[b]
        if r1 == r2:
            out.extend([matrix[r1][(c1 + shift) % 5], matrix[r2][(c2 + shift) % 5]])
        elif c1 == c2:
            out.extend([matrix[(r1 + shift) % 5][c1], matrix[(r2 + shift) % 5][c2]])
        else:
            out.extend([matrix[r1][c2], matrix[r2][c1]])
    return "".join(out)
matrix = create_playfair_matrix("MONARCHY")
msg = "INSTRUMENTS"
enc = playfair_process(msg, matrix, "enc")
dec = playfair_process(enc, matrix, "dec")
print(f"Encrypted: {enc}")
print(f"Decrypted: {dec}")
