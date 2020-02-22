#!/usr/bin/python
from pwn import *
import re

s = remote('2018shell.picoctf.com', 15853)

statement = s.recv()
print statement
binary = re.findall(r'the (.*) as a word',statement)[0]
binary = binary.replace(' ','')
aws = hex(int(binary,2))[2:].decode('hex') #binary -> int -> hex -> decode
print aws
s.sendline(aws)

statement = s.recv()
print statement
hexword = re.findall(r'the (.*) as a word', statement)[0]
aws = hexword.decode('hex')
print aws
s.sendline(aws)

statement = s.recv()
print statement
octal = re.findall(r'the (.*) as a word',statement)[0]
aws = ''.join([chr(int(x,8)) for x in octal.split()])
print aws
s.sendline(aws)

statement = s.recv()
print statement
s.close()