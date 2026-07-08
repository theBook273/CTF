with open("encoded.bmp", "rb") as f:
    f.seek(2000)
    content = f.read(50 * 8)

for i in range(0, 400, 8):
    chunk = content[i : i + 8]
    charval = 0
    for idx, b in enumerate(chunk):
        bit = b & 1
        charval |= bit << idx
    print(chr(charval + 5), end="")
