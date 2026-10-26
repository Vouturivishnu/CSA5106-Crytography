import math
allowed_a = [i for i in range(26) if math.gcd(i, 26) == 1]
disallowed_a = [i for i in range(26) if math.gcd(i, 26) != 1]
print(f"a. Limitations on b: None (any integer mod 26).")
print(f"b. Disallowed values of a: {disallowed_a}")
print(f"   Allowed values of a:    {allowed_a}")
def affine_encrypt(text, a, b):
    return "".join(chr(((a * (ord(c) - 65) + b) % 26) + 65) for c in text.upper() if c.isalpha())
def affine_decrypt(text, a, b):
    a_inv = pow(a, -1, 26)
    return "".join(chr((a_inv * (ord(c) - 65 - b) % 26) + 65) for c in text.upper() if c.isalpha())
a, b = 7, 3
msg = "AFFINECIPHER"
enc = affine_encrypt(msg, a, b)
dec = affine_decrypt(enc, a, b)
print(f"Encrypted: {enc}")
print(f"Decrypted: {dec}")
