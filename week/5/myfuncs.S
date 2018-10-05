section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame


			
	              ;rdi has the ptr, sil (rsi) has the value
	mov rcx, rdx  ;rdx has the string length, set loop counter to this

	mov byte [rdi], sil
add_val:
	
	mov byte [rdi+rcx], sil

	loop add_val

	
	
        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!


global my_strncpy     ;export the 'my_strncpy' symbol to be accessible outside of file
my_strncpy:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame


        	      ;rdi has the dest ptr, rsi has src ptr
	mov rcx, rdx  ;rdx has the string length, set loop counter to this
        
        mov al, byte[rsi]
	mov byte [rdi], al
copy:
	mov al, byte[rsi+rcx] ; moving the character from src, to register
	mov byte [rdi+rcx], al ; copying the value pulled from src into dst 
	loop copy


        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
