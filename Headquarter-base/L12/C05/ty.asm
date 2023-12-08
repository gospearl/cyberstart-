;  Clicking button saves & builds using commands:
;    nasm -f elf -g -F stabs evil.asm
;    ld -o evil evil.o
section .data
Snippet: db "@E9>06G@Q:CN3C57I<)<)*"
SnipLen: equ $-Snippet
section .text
bits 32
global _start
_start:
        nop
        mov ecx,Snippet
        mov edx,SnipLen
        mov eax,4
DoMore: add byte [ecx],0xaf
        inc ecx
        inc eax
        dec edx
        jnz DoMore
        mov eax,4
        mov ebx,1
        sub ecx,SnipLen
        mov edx,SnipLen
        int 80H
        mov eax,1
        mov ebx,0
        int 80H
        nop
