.intel_syntax noprefix
.bits 32
	
.global asm1

;asm1(0xcd)

asm1:
	push	ebp				;function prologue
	mov	ebp,esp				;function prologue
	cmp	DWORD PTR [ebp+0x8],0xde	
	jg 	part_a				;0xcd > 0xde? --> false
	cmp	DWORD PTR [ebp+0x8],0x8
	jne	part_b				;0xcd != 0x8? --> True
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3
	jmp	part_d
part_a:
	cmp	DWORD PTR [ebp+0x8],0x4e
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]
	sub	eax,0x3
	jmp	part_d
part_b:
	mov	eax,DWORD PTR [ebp+0x8]  	;eax = 0xcd
	sub	eax,0x3				;eax -= 0x3 --> 0xca
	jmp	part_d				;Unconditional jump
	cmp	DWORD PTR [ebp+0x8],0xee
	jne	part_c
	mov	eax,DWORD PTR [ebp+0x8]	
	sub	eax,0x3
	jmp	part_d
part_c:
	mov	eax,DWORD PTR [ebp+0x8]
	add	eax,0x3
part_d:
	pop	ebp
	ret
