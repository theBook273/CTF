import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

with open("flag.txt", "r") as f:
    content = f.read()


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
    return temp


def deshift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 - t2) % len(ALPHABET)]


for key in ALPHABET:
    b16 = ""
    for c in content:
        b16 += deshift(c, key)
    if b16 != "":
        print(b16_decode(b16))
