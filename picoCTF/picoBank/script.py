with open("data", "r") as f:
    a = f.read()


a = a.split(",")
res = []
for i in a:
    if "$" in i:
        temp = ""
        for x in i:
            if x == "0" or x == "1":
                temp += x
        res.append(temp)

for i in res:
    print(chr(int(i, 2)), end="")
