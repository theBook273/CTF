import pwn

elf = pwn.ELF("./vuln")
p = elf.process()

# print(pwn.fmtstr_payload)

print(hex(elf.sym["sus"]))
