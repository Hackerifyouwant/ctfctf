#!/usr/bin/python3
import sys
import random


with open('flag.txt', 'rb') as f:
    flag = f.read().strip()
flag = list(flag.ljust(64, b'\0'))
key = 31337

assert(len(flag) == 64)
random.seed(key)

for _ in range(64):
    sub = list(range(256))
    random.shuffle(sub)

    idx = list(range(len(flag)))
    random.shuffle(idx)
    idx = [idx[i:i+2] for i in range(0, len(idx), 2)]

    nxt = flag[:]

    for i, (ia, ib) in enumerate(idx):
        dest = random.sample(idx[:i] + idx[i+1:], len(idx) // 2)
        dest = [k for p in dest for k in p]
        x = sub[flag[ia] ^ flag[ib]]
        x = sub[(x * 13 + 37) & 0xff]
        x = sub[(x + random.randrange(256)) & 0xff]
        x = sub[((x >> 3) | (x << 5)) & 0xff]
        for d in dest:
            nxt[d] ^= x

    flag = nxt

flag = bytes(flag).hex()

print('Version:')
print(sys.version)
print('')
print('Flag:')
print(flag)
