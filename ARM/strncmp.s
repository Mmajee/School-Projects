/*
-------------------------------------------------------
strncmp.s
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

.equ StringSize, 80

@-------------------------------------------------------
@ Main Program

.text
    @ Call ReadStringPrompt subroutine - load parameters from right to left
    MOV    R3, #StringSize   @ Push buffer size onto stack
    STMFD  SP!, {R3}
    LDR    R3, =Str1         @ Push string buffer address onto stack
    STMFD  SP!, {R3}
    LDR    R3, =Prompt       @ Push prompt address onto the stack
    STMFD  SP!, {R3}
    BL     ReadStringPrompt  @ Call the subroutine
    ADD    SP, SP, #12       @ Release the parameter memory from stack

    @ Call ReadStringPrompt subroutine - load parameters from right to left
    MOV    R3, #StringSize   @ Push buffer size onto stack
    STMFD  SP!, {R3}
    LDR    R3, =Str2         @ Push string buffer address onto stack
    STMFD  SP!, {R3}
    LDR    R3, =Prompt       @ Push prompt address onto the stack
    STMFD  SP!, {R3}
    BL     ReadStringPrompt  @ Call the subroutine
    ADD    SP, SP, #12       @ Release the parameter memory from stack

    MOV    R3, #StringSize   @ Set the maximum comparison length
    STMFD  SP!, {R3}         @ Push the maximum length
    LDR    R3, =Str2
    STMFD  SP!, {R3}         @ Push the second string address
    LDR    R3, =Str1
    STMFD  SP!, {R3}         @ Push the first string address
    BL     strncmp
    ADD    SP, SP, #12       @ Release the parameter memory from stack
    
    MOV    R2, R0            @ Save result
    
    MOV    R0, #Stdout
    LDR    R1, =StrncmpStr
    SWI    SWI_PrStr
    MOV    R0, R2            @ Recover result
    BL     PrintLEG
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
PrintLEG:
    /*
    -------------------------------------------------------
    Prints "Lesser", "Equals", or "Greater" to Stdout as appropriate
    -------------------------------------------------------
    Parameters:
      R0 - value to compare against 0
    Uses:
      R0 - for file variable
      R1 - set to address of "True"
    -------------------------------------------------------
    */
    STMFD   SP!, {R0-R1, LR}
    CMP     R0, #0           @ Is R0 Equals?
    LDRLT   R1, =LesserStr   @ load "Lesser" message
    LDRGT   R1, =GreaterStr  @ load "Greater" message
    LDREQ   R1, =EqualsStr   @ load "Equals" message
    MOV     R0, #Stdout
    SWI     SWI_PrStr        @ Print the string to Stdout
    LDMFD   SP!, {R0-R1, PC}

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
strncmp:
    /*
    -------------------------------------------------------
    Determines if two strings are equal up to a max length (iterative)
    Equivalent of: strncmp(*str1, *str1, max_buffer_size)
    -------------------------------------------------------
    Parameters:
      str1 - address of first string
      str2 - address of second buffer
      max_buffer_size - maximum size of str1 and str2
    Returns:
      R0 - < 0 if first string comes first, > 0 if first string comes second,
         0 if two strings are equal up to maximum length
    Uses:
      R1 - address of first string
      R2 - address of second string
      R3 - current maximum length
      R4 - character from first string
      R5 - character from second string
    -------------------------------------------------------
    */

    @ your code here
    @ initialize stack, frame pointer, and extract parameters from stack
	
	STMFD	SP!, {FP, LR}
    MOV		FP, SP
	
	STMFD	SP!, {R1-R5}
	
	
	LDR 	R1, [FP, #8]
	LDR		R2, [FP, #12]
	LDR		R3, [FP, #16]
    MOV     R0, #0          @ Initialize result to strings equal

strncmpLoop:
    CMP     R3, #0
    BEQ     _strncmp        @ Max length met - finish comparison
    LDRB    R4, [R1], #1    @ Get character from first string
    LDRB    R5, [R2], #1    @ Get character from second string
    CMP     R4, R5
    SUBNE   R0, R4, R5      @ Calculate difference between two characters if not the same
    BNE     _strncmp        @ Return difference if not the same
    CMP     R4, #0          @ Look for end of strings
    BEQ     _strncmp        @ Return if at end of strings
    SUB     R3, R3, #1      @ Decrement max length count
    B       strncmpLoop
    
_strncmp:

    @ your code here
    @ clean up stack
	
	LDMFD	SP!, {R1-R5}
	LDMFD	SP!, {FP, PC}

@-------------------------------------------------------
.data
LF:
.asciz    "\n"
Prompt:
.asciz    "Test String: "
LengthStr:
.asciz    "Max Length: "
StrncmpStr:
.asciz    "Comparison: "
LesserStr:
.asciz    "Lesser"    
EqualsStr:
.asciz    "Equals"
GreaterStr:
.asciz    "Greater"
Str1:
.space    StringSize
Str2:
.space    StringSize
.end
