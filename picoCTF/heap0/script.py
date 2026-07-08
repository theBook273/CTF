import pwn

payload = pwn.cyclic(44)
with open("payload", "wb") as f:
    f.write(payload)
