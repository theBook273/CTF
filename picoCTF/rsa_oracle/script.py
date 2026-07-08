from pwn import remote
from Crypto.Util.number import long_to_bytes

HOST = "titan.picoctf.net"
PORT = 59778

enc = 2336150584734702647514724021470643922433811330098144930425575029773908475892259185520495303353109615046654428965662643241365308392679139063000973730368839

io = remote(HOST, PORT)

# Encrypt 0x02
io.sendlineafter(b"decrypt.", b"E")
io.sendlineafter(b"keysize):", b"\x02")

# ciphertext (m ^ e mod n) <number>
line = io.recvline_contains(b"ciphertext").decode().strip()
c_a = int(line.split()[-1])

# Oracle decrypt
io.sendlineafter(b"decrypt.", b"D")
io.sendlineafter(b"decrypt:", str(enc * c_a).encode())

# decrypted ciphertext as hex (c ^ d mod n): <hex>
line = io.recvline_contains(b"decrypted ciphertext as hex").decode().strip()
m_hex = line.split(": ", 1)[1]

m = int(m_hex, 16) // 2

print(long_to_bytes(m).decode())
