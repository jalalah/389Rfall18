section .text         ;declare this section to include executable instructions

global my_memset      ;export the 'my_memset' symbol to be accessible outside of file
my_memset:
        push rbp      ;saves the base pointer for the previous function's stack frame
        mov rbp, rsp  ;moves up the base pointer to the top of the stack to create a new frame		
	              ;rdi has the ptr to the array, sil (rsi) has the char value
	mov rcx, rdx  ;rdx has the string length, set loop counter to this
	mov rax, 0    ;counter to access memory

add_val:
	
	mov byte [rdi+rax], sil ; copying the value into the array
	inc rax       ; increasing counter
	loop add_val  ; this automatically decreases rcx by one
	
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

        mov rax, 0    ; creating a counter variable
copy:
	mov bl, byte[rsi+rax]  ; moving the character from src, to one byte register
	mov byte [rdi+rax], bl ; copying the value pulled from src into dst 
        inc rax                ; increasing our counter
	loop copy      	       ; automatically decreases rcx by one	


        leave         ;moves down the stack pointer to the current base pointer,
                      ;and restores our saved base pointer, effectively
                      ;restoring our previous stack frame
        ret           ;jumps to the top value on the stack, hopefully the return address!
