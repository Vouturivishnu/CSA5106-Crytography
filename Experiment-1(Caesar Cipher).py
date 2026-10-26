def caesar_encrypt(text, k):
    res = []
    for c in text:
        if c.isupper():
            res.append(chr((ord(c) - 65 + k) % 26 + 65))
        elif c.islower():
            res.append(chr((ord(c) - 97 + k) % 26 + 97))
        else:
            res.append(c)
    return "".join(res)
def caesar_decrypt(text, k):
    return caesar_encrypt(text, -k)
msg = "Hello, World!"
k = 3
enc = caesar_encrypt(msg, k)
dec = caesar_decrypt(enc, k)
print(f"Encrypted: {enc}")
print(f"Decrypted: {dec}")
