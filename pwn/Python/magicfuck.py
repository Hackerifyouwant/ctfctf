from pwn import*

conn=remote('120.114.62.40',5119)
conn.recvuntil('?')


for i in  range (100):
    
    conn.recvuntil('-\n')
    a = int(conn.recvuntil(' '))
    
    conn.recvuntil(' ')
    
    b=int(conn.recvuntil(' '))
    
    conn.recvuntil(' ')
    
    c=int(conn.recvuntil('\n'))
    conn.recvuntil('?')
    if a == c-b:
        conn.send('+'+'\n')
        print '+'
    elif a == c+b:
        conn.send('-'+'\n')
        print '-'
    else:
        conn.send('*'+'\n')
        print '*'

conn.interactive()



