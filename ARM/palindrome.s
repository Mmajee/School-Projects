/*
-------------------------------------------------------
palindrome.s
Working with stack frames.
-------------------------------------------------------
*/
.equ SWI_Exit, 0x11     @ Terminate program code
.equ SWI_Open, 0x66     @ Open a file
                        @ inputs - R0: address of file name, R1: mode (0: input, 1: write, 2: append)
                        @ outputs - R0: file handle, -1 if open fails
.equ SWI_Close, 0x68    @ Close a file
                        @ inputs - R0: file handle
.equ SWI_RdInt, 0x6c    @ Read integer from a file
                        @ inputs - R0: file handle
                        @ outputs - R0: integer
.equ SWI_PrInt, 0x6b    @ Write integer to a file
                        @ inputs - R0: file handle, R1: integer
.equ SWI_RdStr, 0x6a    @ Read string from a file
                        @ inputs - R0: file handle, R1: buffer address, R2: buffer size
                        @ outputs - R0: number of bytes stored
.equ SWI_PrStr, 0x69    @ Write string to a file
                        @ inputs- R0: file handle, R1: address of string
.equ SWI_Timer, 0x6d    @ Read current time
                        @ output - R0: current time

.equ InputMode, 0       @ Set file mode to input
.equ OutputMode, 1      @ Set file mode to output
.equ AppendMode, 2      @ Set file mode to append
.equ Stdout, 1          @ Set output target to be Stdout
.equ Stdin, 0           @ Set input source to be STDIN

.equ False, 0
.equ True, 1

.equ StringSize, 80

@-------------------------------------------------------
@ Main Program

.text
    @ Call ReadStringPrompt subroutine - load parameters from right to left
    MOV    R3, #StringSize   @ Push buffer size onto stack
    STMFD  SP!, {R3}
    LDR    R3, =TestString   @ Push string buffer address onto stack
    STMFD  SP!, {R3}
    LDR    R3, =Prompt       @ Push prompt address onto the stack
    STMFD  SP!, {R3}
    BL     ReadStringPrompt  @ Call the subroutine
    ADD    SP, SP, #12       @ Release the parameter memory from stack

    @ Print the output string
    MOV    R0, #Stdout
    LDR    R1, =PalindromeStr
    SWI    SWI_PrStr

    @ Get the test string length
    LDR    R1, =TestString
    BL     strlen

    @ Call the palindrome subroutine
    @ your code here - put parameters on stack, call palindrome subroutine, clean up stack
	
	MOV		R2, R0
	@Put address of string onto stack
	LDR 	R1, =TestString 
	STMFD	SP!, {R1-R2} 
	BL 		Palindrome
	ADD		SP, SP, #8 @Clear stack memory
    
    BL     PrintTrueFalse
    BL     PrintLF
    
    SWI    SWI_Exit

@-------------------------------------------------------
PrintLF:
    /*
    -------------------------------------------------------
    Prints the end-of-line character (\n)
    -------------------------------------------------------
    Uses:
    R0    - set output to Stdout
    R1    - address of string to print
    -------------------------------------------------------
    */
    STMFD  SP!, {R0-R1, LR}
    MOV    R0, #Stdout   @ Set output to Stdout
    LDR    R1, =LF       @ Load line feed character
    SWI    SWI_PrStr
    LDMFD  SP!, {R0-R1, PC}
    
@-------------------------------------------------------
PrintTrueFalse:
    /*
    -------------------------------------------------------
    Prints "True" or "False" to Stdout as appropriate
    -------------------------------------------------------
    Uses:
    R0 - input parameter, then set to Stdout
    R1 - set to address of "True"
    -------------------------------------------------------
    */
    STMFD   SP!, {R0-R1, LR}
    CMP     R0, #0          @ Is R0 False?
    LDREQ   R1, =FalseStr   @ load "False" message
    LDRNE   R1, =TrueStr    @ load "True" message
    MOV     R0, #Stdout
    SWI     SWI_PrStr       @ Print the string to Stdout
    LDMFD   SP!, {R0-R1, PC}
    
@-------------------------------------------------------
strlen:
    /*
    -------------------------------------------------------
    Determines the length of a string.
    -------------------------------------------------------
    Uses:
    R0 - returned length
    R1 - address of string
    R2 - current character
    -------------------------------------------------------
    */
    STMFD   SP!, {R1-R2, LR}
    MOV     R0, #0          @ Initialize length    

strlenLoop:
    LDRB    R2, [R1], #1    @ Read address with post-increment (R2 = *R1, R1 += 1)
    CMP     R2, #0          @ Compare character with null
    ADDNE   R0, R0, #1
    BNE     strlenLoop      @ If not at end, continue
    
    LDMFD   SP!, {R1-R2, PC}

@-------------------------------------------------------
ReadStringPrompt:
    /*
    -------------------------------------------------------
    Prompts user to enter a string from the keyboard.
    Equivalent of: ReadStringPrompt(*prompt, *buffer, buffer_size)
    -------------------------------------------------------
    Parameters:
      prompt - address of prompt string
      buffer - address of string buffer
      buffer_size - size of string buffer
    Returns:
      R0 - size of string actually read
    Uses:
      R1 - address of strings to process
      R2 - string buffer size
    -------------------------------------------------------
    */
    STMFD  SP!, {FP, LR}    @ push frame pointer and link register onto the stack
    MOV    FP, SP           @ Save current stack top to frame pointer
                            @ allocate local storage (none allocated)
    STMFD  SP!, {R1-R2}     @ preserve other registers

    @ Print the prompt
    MOV    R0, #Stdout
    LDR    R1, [FP, #8]     @ Get address of prompt from parameter
    SWI    SWI_PrStr
    
    @ Read the string from the keyboard
    MOV    R0, #Stdin
    LDR    R1, [FP, #12]    @ Get address of string buffer from parameter
    LDR    R2, [FP, #16]    @ Get string buffer size from parameter
    SWI    SWI_RdStr
    
    LDMFD  SP!, {R1-R2}     @ pop preserved registers
                            @ deallocate local storage (none was allocated)
    LDMFD  SP!, {FP, PC}    @ pop frame pointer and program counter

@-------------------------------------------------------
Palindrome:
    /*
    -------------------------------------------------------
    Determines if a string is a palindrome (iterative)
    Equivalent of: Palindrome(*string, length)
    -------------------------------------------------------
    Parameters:
      string - address of string buffer
      length - length of string
    Returns:
      R0 -  True if palindrome, False otherwise
    Uses:
      R1 - address of string
      R2 - length of string
      R3 - left character
      R4 - right character
    -------------------------------------------------------
    */
    STMFD   SP!, {FP, LR}   @ push frame pointer and link register onto the stack
    MOV     FP, SP          @ Save current stack top to frame pointer
                            @ allocate local storage (none)
    STMFD   SP!, {R1-R4}    @ preserve other registers
    
    LDR     R1, [FP, #8]    @ Get string address
    LDR     R2, [FP, #12]   @ Get length of string
	
    MOV     R0, #True       @ Initialize result to True

PalindromeLoop:    
    CMP     R2, #1          @ Compare string length to 1
    BLE     _Palindrome
    
    LDRB    R3, [R1], #1    @ Get leftmost character, increment string address
    SUB     R2, R2, #2      @ Offset to right-most character (length - 1)
    LDRB    R4, [R1, R2]    @ Get rightmost character
    
    CMP     R3, R4          @ Compare left and right characters
    MOVNE   R0, #False      @ Characters do not match, result is False
    BEQ     PalindromeLoop  @ Characters match - keep looping
    
_Palindrome:
    LDMFD   SP!, {R1-R4}    @ pop preserved registers
                            @ deallocate local storage (none was allocated)
    LDMFD   SP!, {FP, PC}   @ pop frame pointer and program counter

@-------------------------------------------------------
.data
TrueStr:
.asciz    "True"    
FalseStr:
.asciz    "False"
LF:
.asciz    "\n"
Prompt:
.asciz    "Test String: "
PalindromeStr:
.asciz    "Palindrome: "
TestString:
.space    StringSize
.end
