/*
-------------------------------------------------------
min_max.s
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


@-------------------------------------------------------
@ Main Program

.text
       @ push the parameters onto the stack
	   
	LDR	  R3, =Max
	STMFD SP!, {R3}
	LDR	  R3, =Min
	STMFD SP!, {R3}
	LDR   R3, =_Data
	STMFD SP!, {R3}
	LDR   R3, =Data
	STMFD SP!, {R3}
	
    BL    MinMax       @ Call the subroutine

       @ Release the parameter memory from the stack
	ADD   SP, SP, #16
    
    @ Print results
    MOV    R0, #Stdout
    LDR    R1, =MinStr
    SWI    SWI_PrStr
    LDR    R1, =Min
    LDR    R1, [R1]
    SWI    SWI_PrInt
    BL     PrintLF
    
    LDR    R1, =MaxStr
    SWI    SWI_PrStr
    LDR    R1, =Max
    LDR    R1, [R1]
    SWI    SWI_PrInt
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
MinMax:
    /*
    -------------------------------------------------------
    Finds the minimum and maximum values in a list.
    Equivalent of: MinMax(*start, *end, *min, *max)
    Passes addresses of list, end of list, max, and min as parameters.
    -------------------------------------------------------
    Parameters:
      start - start address of list
      end - end address of list
      min - address of minimum result
      max - address of maximum result
    Uses:
      R0 - address of start of list
      R1 - address of end of list
      R2 - minimum value so far
      R3 - maximum value so far
      R4 - address of value to process
    -------------------------------------------------------
    */

    @ your code here
	STMFD	SP!, {FP, LR}
	MOV		FP, SP
	
	STMFD	SP!, {R0-R6}
	
	@Load all parameter addresses into registers
	LDR 	R0, [FP, #8] 
	LDR		R1, [FP, #12]
	LDR     R5, [FP, #16]
	LDR     R6, [FP, #20]
	
	@Initialize min and max values
	MOV		R2, #0
	MOV		R3, #0
	
MinMaxLoop:    
    CMP    R0, R1   @ Compare addresses
    BEQ    _MinMax
    LDR    R4, [R0], #4
    CMP    R4, R2
    MOVLT  R2, R4
    CMP    R4, R3
    MOVGT  R3, R4
    B      MinMaxLoop
    
_MinMax:
    @ Store results to address parameters
	STR	    R2, [R5]
	STR	    R3, [R6]
    @ your code here
	
	LDMFD	SP!, {R0-R6}
	LDMFD	SP!, {FP, PC}
    
 
@-------------------------------------------------------
.data
LF:
.asciz    "\n"
		 .align
Data:    .word    4,5,-9,0,3,0,8,-7,12    @ The list of data
_Data:    @ End of list address
Min:    .space 4
Max:    .space 4
MinStr:
.asciz  "Minimum: "
MaxStr:
.asciz  "Maximum: "
.end
