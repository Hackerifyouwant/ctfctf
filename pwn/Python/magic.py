from pwn import *

conn=remote('140.110.112.31',2116)
conn.send(p32(127174655))
conn.recvuntil('\n')
conn.recvuntil('\n')
# q=conn.recvuntil('?')
# print('#' + str(q))

s=' '
a=0
b=0
c=' '
for i in range (1000):
    a = int(conn.recvuntil(' '))
    c = conn.recvuntil(' ')[0]
    b = int(conn.recvuntil(' '))
    conn.recvuntil('?')
    # for i in q:
    #     if i == ' ':
    #         if a>0 and c!=' ' :
    #             b=int(s)
    #         else:
    #             a=int(s)
    #             s=' '    
    #     elif i == '+' or i == '-' or i == '*':
    #         c=i
    #     else:
    #         s+=q
    #
    print(str(a) + c + str(b))
    if c == '+':
        conn.send(str(a+b) + '\n')
    elif c == '-':
        conn.send(str(a-b) + '\n')
    else:
        conn.send(str(a*b) + '\n')
    print('complete')

conn.interactive()




