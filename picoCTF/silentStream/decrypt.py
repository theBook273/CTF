with open("data.bin", "rb") as f:
    flag = f.read()


flag = bytes((b - 42) % 256 for b in flag)

with open("flag", "wb") as f:
    f.write(flag)
