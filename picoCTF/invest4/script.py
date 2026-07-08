file = []

with open("Item01_cp.bmp", "rb") as f1:
    f1.seek(2019)
    file.append(f1.read(280))

with open("Item02_cp.bmp", "rb") as f1:
    f1.seek(2019)
    file.append(f1.read(280))

with open("Item03_cp.bmp", "rb") as f1:
    f1.seek(2019)
    file.append(f1.read(280))

with open("Item04_cp.bmp", "rb") as f1:
    f1.seek(2019)
    file.append(f1.read(280))

with open("Item05_cp.bmp", "rb") as f1:
    f1.seek(2019)
    file.append(f1.read(280))

file = file[::-1]

for f in file:
    res = ""
    for i in range(0, 280, 12):
        chunk = f[i : i + 8]
        bit = 0
        for id, b in enumerate(chunk):
            b &= 1
            bit |= b << id
        res += chr(bit)
    print(res, end="")
