import string
def mono_encrypt(text, key_map):
    return "".join(key_map.get(c, c) for c in text)
def mono_decrypt(text, key_map):
    inv_map = {v: k for k, v in key_map.items()}
    return "".join(inv_map.get(c, c) for c in text)
plain_alpha = string.ascii_uppercase
cipher_alpha = "QWERTYUIOPASDFGHJKLZXCVBNM"
enc_map = {p: c for p, c in zip(plain_alpha, cipher_alpha)}
enc_map.update({p.lower(): c.lower() for p, c in zip(plain_alpha, cipher_alpha)})
msg = "Defend the East Wall"
enc = mono_encrypt(msg, enc_map)
dec = mono_decrypt(enc, enc_map)
print(f"Encrypted: {enc}")
print(f"Decrypted: {dec}")
