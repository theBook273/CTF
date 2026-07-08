content = 0
with open("flag.txt", "r") as f:
    content = f.read()

for i in range(0, 26):
    temp = []
    res = "picoCTF"
    for j in content:
        if j.isalpha():
            if j.islower():
                temp.append(chr((ord(j) - ord("a") + i) % 26 + ord("a")))
            else:
                temp.append(chr((ord(j) - ord("A") + i) % 26 + ord("A")))
        else:
            temp.append(j)
    joined = "".join(temp)
    if res in joined:
        print(joined)
