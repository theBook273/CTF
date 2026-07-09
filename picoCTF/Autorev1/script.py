import pwn

HOST = "mysterious-sea.picoctf.net"
PORT = 50829

p = pwn.remote(HOST, PORT)

for atm in range(20):
    test = p.recvuntil("Here's ")
    temp = test.split()
    for i in range(len(temp)):
        if temp[i] == b"Here's":
            temp = temp[i - 1]
            break
    p.sendline(temp)


p.interactive()
