from binascii import unhexlify

plain = b"picoCTF{fake_flag}"
en = unhexlify("235a201d70201548251358110c552f135409")

keystream = []
for p, e in zip(plain, en):
    keystream.append(p ^ e)

for i in keystream:
    print(chr(i), end="")
