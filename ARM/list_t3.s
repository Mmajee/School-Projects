/*
-------------------------------------------------------
list_t3.s
A simple list demo program. Prints all elements of an integer list.
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
.equ SWI_PrChr, 0x00    @ Write a character to Stdout
                        @ inputs - R0: character
.equ SWI_Timer, 0x6d    @ Read current time
                        @ output - R0: current time

.equ InputMode, 0       @ Set file mode to input
.equ OutputMode, 1      @ Set file mode to output
.equ AppendMode, 2      @ Set file mode to append
.equ Stdout, 1          @ Set output target to be Stdout
.equ Stdin, 0           @ Set input source to be STDIN

.text
    LDR    R2, =Data    @ Store address of start of list
    LDR    R3, =_Data   @ Store address of end of list
	
	@Initialize Min and Max with the first value in the list
	LDR R7, [R2]
	LDR R8, [R2]
	
    @ Display number of bytes in the list
    MOV    R0, #Stdout
    LDR    R1, =BytesMsg    @ Print title    
    SWI    SWI_PrStr
	
    SUB    R1, R3, R2   @ Determine number of bytes in list by address difference
    SWI    SWI_PrInt
    LDR    R1, =LF      @ Print carriage return    
    SWI    SWI_PrStr
    
    MOV    R4, #0       @ Initialize the running total

Top1:
    LDR    R1, [R2], #4    @ Read address with post-increment (R1 = *R2, R2 += 4)
    SWI    SWI_PrInt    @ Print integer to Stdout
	ADD    R5, R5, R1   @Add the integer to total
	ADD    R6, #1
	@Compare the Min. value with the current integer and move the integer to R7 if its less than the min. value
	CMP    R1, R7
	MOVLT  R7, R1
	@Compare the Max. value with the current integer and move the integer to R8 if its less than the max. value
	CMP    R1, R8
	MOVGT  R8, R1
    LDR    R1, =LF      @ Print carriage return    
    SWI    SWI_PrStr
    
    CMP    R3, R2       @ Compare current address with end of list
    BNE    Top1         @ If not at end, continue
	
	@Print the sum and count
	LDR R1, =SUM
	SWI	   SWI_PrStr
	MOV R1, R5
	SWI    SWI_PrInt
	LDR    R1, =LF      @ Print carriage return    
    SWI    SWI_PrStr
    LDR R1, =COUNT
	SWI	   SWI_PrStr
	MOV R1, R6
	SWI    SWI_PrInt
	LDR    R1, =LF      @ Print carriage return    
    SWI    SWI_PrStr
	
	@Print the Min value
	LDR R1, =MIN
	SWI	   SWI_PrStr
	MOV R1, R7
	SWI    SWI_PrInt
	LDR    R1, =LF      @ Print carriage return    
    SWI    SWI_PrStr
	
	@Print the Max value
	LDR R1, =MAX
	SWI	   SWI_PrStr
	MOV R1, R8
	SWI    SWI_PrInt
	
    SWI    SWI_Exit

.data
    BytesMsg:    .asciz    "Bytes in list: "
    LF:    .asciz    "\n"
    .align  @ Force list to start on a word boundary
    Data:    .word    4,5,-9,0,3,0,8,-7,0    @ The list of data
    _Data:    @ End of list address
	SUM:     .asciz "Sum: "
	COUNT:   .asciz "Count: "
	MIN:     .asciz "Minimum: "
	MAX:     .asciz "Maximum: "
.end
