def vigenere_encrypt(text, key):
    key = key.upper()
    res, ki = [], 0
    for c in text:
        if c.isalpha():
            base = 65 if c.isupper() else 97
            shift = ord(key[ki % len(key)]) - 65
            res.append(chr((ord(c) - base + shift) % 26 + base))
            ki += 1
        else:
            res.append(c)
    return "".join(res)
def vigenere_decrypt(text, key):
    key = key.upper()
    res, ki = [], 0
    for c in text:
        if c.isalpha():
            base = 65 if c.isupper() else 97
            shift = ord(key[ki % len(key)]) - 65
            res.append(chr((ord(c) - base - shift) % 26 + base))
            ki += 1
        else:
            res.append(c)
    return "".join(res)
msg = "GEEKSFORGEEKS"
k = "AYUSH"
enc = vigenere_encrypt(msg, k)
dec = vigenere_decrypt(enc, k)
print(f"Encrypted: {enc}")
print(f"Decrypted: {dec}")
