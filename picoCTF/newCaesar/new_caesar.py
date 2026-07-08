import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc


def b16_decode(plain):
    word = []
    temp = ""
    for i in plain:
        word.append(i)
        if len(word) == 2:
            head = "{0:04b}".format(ord(word[0]) - LOWERCASE_OFFSET)
            tail = "{0:04b}".format(ord(word[1]) - LOWERCASE_OFFSET)
            complete = head + tail
            temp += chr(int(complete, 2))
            word.clear()
    return "".join(temp)


def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]


def deshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]


flag = "abc"
key = "b"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
enc = ""

print(shift("g", "b"))

for i, c in enumerate(b16):
    enc += shift(c, key)

de = ""
for i, c in enumerate(enc):
    de += deshift(c, key)

print(de)
