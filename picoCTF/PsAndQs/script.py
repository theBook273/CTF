from Crypto.Util.number import long_to_bytes

with open("values", "r") as f:
    content = f.read()

content = content.split()
c = n = e = 0

for i in range(0, len(content)):
    if "c:" in content[i]:
        c = content[i + 1]
    if "n:" in content[i]:
        n = content[i + 1]
    if "e:" in content[i]:
        e = content[i + 1]

c = int(c)
n = int(n)
e = int(e)

p = 1891771437429478964908181306574287207137
q = 501332739776173570344039681219489434626477

phi = (q - 1) * (p - 1)

d = pow(e, -1, phi)
m = pow(c, d, n)

flag = long_to_bytes(m)
print(flag[::-1])
