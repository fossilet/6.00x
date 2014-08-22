def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here

    if aStr == '':
        return False
    else:
        lo = aStr[0]
        hi = aStr[-1]
        guess = aStr[len(aStr) / 2]

        if len(aStr) == 1:
            return char == aStr
        elif char == guess:
            return True
        elif char < guess:
            return isIn(char, aStr[0:aStr.index(guess)])
        else:
            return isIn(char, aStr[aStr.index(guess):])


print isIn('c', 'abcdef')
