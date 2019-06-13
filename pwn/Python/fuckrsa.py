from pwn import *

r=remote('2018shell3.picoctf.com', 18148)

r.recvuntil('\n')
r.recvuntil('\n')
r.recvuntil('\n')
r.recvuntil('\n')
r.recvuntil('\n')
r.recvuntil('\n')

s1=r.recvuntil(' ')
r.recvuntil(' ')
n1=r.recvuntil('\n')
s2=r.recvuntil(' ')
r.recvuntil(' ')
n2=r.recvuntil('\n')
r.recvuntil('\n')
r.recvuntil('\n')
r.recvuntil(':')
r.send('Y')
x=int(n1)*int(n2)
r.send(str(x))



r.interactive()
