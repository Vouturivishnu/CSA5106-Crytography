keyword = "CIPHER"
seen = set()
cipher_map = []
for c in (keyword + "ABCDEFGHIJKLMNOPQRSTUVWXYZ").upper():
    if c not in seen:
        seen.add(c)
        cipher_map.append(c)
cipher_alpha = "".join(cipher_map)
table_enc = str.maketrans("abcdefghijklmnopqrstuvwxyz", cipher_alpha.lower())
table_dec = str.maketrans(cipher_alpha.lower(), "abcdefghijklmnopqrstuvwxyz")
print(f"Cipher alphabet: {cipher_alpha}")
msg = "attack at dawn"
enc = msg.translate(table_enc)
dec = enc.translate(table_dec)
print(f"Encrypted: {enc}")
print(f"Decrypted: {dec}")
