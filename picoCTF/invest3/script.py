with open("encoded.bmp", "rb") as f:
    f.seek(723)
    content = f.read(450)

i = 0
res = ""
for i in range(0, 450, 9):
    chunk = content[i : i + 8]
    charval = 0
    for idx, b in enumerate(chunk):
        bit = b & 1
        charval |= bit << idx
    res += chr(charval)

print(res)
