import random
import string

charset = string.ascii_letters

print(
    ":3",
    "".join(random.choice(charset) for _ in range(2)),
    "M",
    "".join(random.choice(charset) for _ in range(5)),
    sep="",
)
