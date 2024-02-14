"""
-------------------------------------------------------
functions
-------------------------------------------------------
"""
from Stack_array import Stack


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    
    i = 0
    alist = []
    
    b = source.is_empty()
    
    while b == True:
        b = source.is_empty()
        x = source.pop()
        alist.append(x)
        i += 1
    
    i = 0
    length = len(alist)
    
    while i < length:
        x = alist.pop(0)
        source.push(x)
        i += 1
        
    return
    
    
def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack. 
    When finished, the contents of source1 and source2 are interlaced 
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    
    target = Stack()
    
    
    
    b1 = source1.is_empty()
    b2 = source2.is_empty()
    
    while b1 == False or b2 == False:
        
        if b1 == False:
            x = source1.pop()
            target.push(x)
        
        if b2 == False:
            x = source2.pop()
            target.push(x)
            
        b1 = source1.is_empty()
        b2 = source2.is_empty()

    
    return target


# Constants
BALANCED = 0
MORE_LEFT = 1
MORE_RIGHT = 2
MISMATCHED = 3

def has_balanced_brackets(string):
    """
    -------------------------------------------------------
    Determines if a string contains balanced brackets or not. Non-bracket
    characters are ignored. Uses a stack. Brackets include {}, [], (), <>.
    Use: balanced = has_balanced_brackets(string)
    -------------------------------------------------------
    Parameters:
        string - the string to test (str)
    Returns:
        balanced (int) -
            BALANCED if the brackets in string are balanced
            MISMATCHED if the brackets in string are mismatched
            MORE_RIGHT if there are more right brackets than left in string
            MORE_LEFT if there are more left brackets than right in string
    -------------------------------------------------------
    """
    
    s = Stack()
    
    i = 0
    length = len(string)
    brackets = '{[(<'
    brackets2 = '}])>'
    k = True
    balanced = BALANCED
    
    while k == True and i < length: 
        if string[i] in brackets:
            s.push(string[i]) 
       
        
        if string[i] in brackets2:
            
            b = s.is_empty()
            
            if b == False:
                x = s.pop()
            else:
                x = ''
            
            if x == brackets[0] and string[i] != brackets2[0]:
                balanced = MISMATCHED
                k = False
            elif x == brackets[1] and string[i] != brackets2[1]:
                balanced = MISMATCHED
                k = False
            elif x == brackets[2] and string[i] != brackets2[2]:
                balanced = MISMATCHED
                k = False
            elif x == brackets[3] and string[i] != brackets2[3]:
                balanced = MISMATCHED
                k = False
            elif b == True:
                balanced = MORE_RIGHT
                k = False
                
            
        i += 1
    
    b = s.is_empty()
    
    if b == False and k == True:
        balanced = MORE_LEFT

        
    return balanced


# Constants
OPERATORS = "+-*/"

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    i = 0
    length = len(string)
    s = Stack()
    
    while i < length:
        
        b = s.is_empty()
        
        if string[i].isdigit():
            if string[i + 1].isdigit():
                s.push(string[i:i+2]) 
            elif string[i - 1].isdigit() == False:
                s.push(string[i])
        elif string[i] != ' ':
            
            if b == False:
                x = s.pop()
                x = float(x)
            
            b = s.is_empty()
            
            if b == False:
                y = s.pop()
                y = float(y)
            
            if string[i] == OPERATORS[0]:
                z = y + x 
                s.push(z)
            elif string[i] == OPERATORS[1]:
                z = y - x
                s.push(z)
            elif string[i] == OPERATORS[2]:
                z = y * x
                s.push(z)
            elif string[i] == OPERATORS[3]:
                z = y / x
                s.push(z)
        i += 1
        
    answer = s.pop()
    
    return answer

def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    string2 = ''
    s = Stack()
    length = len(string)
    i = 0
    k = True
    palindrome = True
    string = string.lower()
    
    while i < length:
        c = string[i].isalpha() 
        if c == True:
            s.push(string[i])
            string2 += string[i]
        i += 1

        
    b = s.is_empty()
    i = 0
    
    while k == True and b == False and i < len(string2):
       
        x = s.pop()
        
        if x != string2[i]:
            palindrome = False
            k = False
        
        b = s.is_empty()
        i += 1
        
    return palindrome
