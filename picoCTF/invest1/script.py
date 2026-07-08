with open("flag.txt", "r", encoding="utf-8") as f:
    content = f.readlines()

pic1 = content[0].strip()
pic2 = content[1].strip()
pic3 = content[2].strip()

dem1 = dem2 = dem3 = 0

print(chr(ord(pic2[dem2]) - 21), end="")
dem2 += 1

print(pic3[dem3], end="")
dem3 += 1

print(pic3[dem3], end="")
dem3 += 1

print(chr(ord(pic2[dem2]) - 4), end="")

dem3 += 1
dem1 += 1

for i in range(6, 10):
    print(pic1[dem1], end="")
    dem1 += 1

for i in range(10, 15):
    print(pic3[dem3], end="")
    dem3 += 1

for i in range(15, 26):
    print(pic1[dem1], end="")
    dem1 += 1
