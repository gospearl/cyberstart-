section .data
    Snippet db "@E9>06G@Q:CN3C57I<)<)*"
    SnipLen equ $-Snippet

section .text
    bits 32            ; Specify 32-bit mode
    global _start

_start:
    nop
    mov esi, Snippet
    mov ecx, SnipLen
    mov eax, 4
    DoMore:
        add byte [esi], 0xAF
        inc esi
        inc eax
        loop DoMore

    mov eax, 4
    mov ebx, 1
    lea ecx, [Snippet]
    mov edx, SnipLen
    int 0x80

    mov eax, 1
    xor ebx, ebx
    int 0x80

    nop
