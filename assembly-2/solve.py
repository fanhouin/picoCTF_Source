#!usr/bin/env python

ebp_plus_c = 0x28
ebp_plus_8 = 0x7

eax = ebp_plus_c
ebp_minus_4 = eax
print "ebp_minus_4:", ebp_minus_4

eax = ebp_plus_8
ebp_minus_8 = eax
print 'ebp_minus_8:', ebp_minus_8

while (1):
	if(ebp_plus_8 <= 0xa1de):
		ebp_minus_4 += 1
		ebp_plus_8 += 0x76
	else:
		eax = ebp_minus_4
		print hex(eax)
		break
