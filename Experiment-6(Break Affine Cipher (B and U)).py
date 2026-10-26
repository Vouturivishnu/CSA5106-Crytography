# Most frequent letter in English: E (4), second: T (19)
# Ciphertext equivalents: B (1), U (20)
p1, p2 = 4, 19
c1, c2 = 1, 20
delta_p = (p2 - p1) % 26
delta_c = (c2 - c1) % 26
a = (delta_c * pow(delta_p, -1, 26)) % 26
b = (c1 - a * p1) % 26
a_inv = pow(a, -1, 26)
print(f"Recovered Keys: a = {a}, b = {b}")
ciphertext = "BU"
decrypted = "".join(chr((a_inv * (ord(c) - 65 - b) % 26) + 65) for c in ciphertext)
print(f"Decrypted '{ciphertext}': {decrypted}")
