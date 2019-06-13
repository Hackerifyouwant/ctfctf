#!/usr/bin/python3
import hashlib
import time


with open('flag.txt', 'rb') as f:
    flag = f.read().strip()
key = hashlib.sha256(str(int(time.time())).encode()).digest()

assert len(flag) <= len(key)

enc = bytes(c ^ k for c, k in zip(flag, key)).hex()

print(enc)
