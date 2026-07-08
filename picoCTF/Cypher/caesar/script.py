content = 0
with open("data.enc", "r", encoding="utf-8") as file:
    content = file.read()

solve = []
check = 0
for i in content:
    if check:
        solve.append(i)
    if i == "{":
        check = 1

solve.pop()
solve.pop()

for i in range(0, 27):
    for j in solve:
        if j.isalpha():
            if "a" <= j and j <= "z":
                print(chr((ord(j) - ord("a") - i) % 26 + ord("a")), end="")
            elif "A" <= j and j <= "Z":
                print(chr((ord(j) - ord("A") - i) % 26 + ord("A")), end="")
    print()
