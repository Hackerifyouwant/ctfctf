import pwn

s="You have now entered the Duck Web, and you',27h,'re in for a honk.\nCan you figure out my trick?"
x="\x29\x06\x16\x4F\x2B\x35\x30\x1E\x51\x1B\x5B\x14\x4B\x08\x5D\x2B\x52\x17\x01\x57\x16\x11\x5C\x07\x5D\x00"

print pwn.xor(s,x)


