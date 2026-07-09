import pwn

HOST = "candy-mountain.picoctf.net"
PORT = 55319

key = b"S3Cr3t"

p = pwn.remote(HOST, PORT)
temp = p.recvall()
temp = temp.split()
enc = temp[len(temp) - 1]
enc = bytes.fromhex(enc)

res = []

for i, x in enumerate(enc):
    res.append(x ^ key[i % len(key)])

for i in res:
    print(chr(i), end="")
