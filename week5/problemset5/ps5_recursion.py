# 6.00x Problem Set 5
#
# Part 2 - RECURSION

#
# Problem 3: Recursive String Reversal
#

def reverseString(aStr):
    """
    Given a string, recursively returns a reversed copy of the string.
    For example, if the string is 'abc', the function returns 'cba'.
    The only string operations you are allowed to use are indexing,
    slicing, and concatenation.
    
    aStr: a string
    returns: a reversed string
    """
    # Pseudo code
    if len(aStr) in (0, 1):
        return aStr
    else:
        return aStr[-1] + reverseString(aStr[:-1])

#
# Problem 4: X-ian
#
def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >>> x_ian('eric', 'meritocracy')
    True
    >>> x_ian('eric', 'cerium')
    False
    >>> x_ian('john', 'mahjong')
    False
    
    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    # Pseudo code first
    if len(x) == 0:
        return True
    if len(x) == 1:
        return x[0] in word
    else:
        ind = word.find(x[0])
        if ind != -1:
            return x_ian(x[1:], word[(ind + 1):])
        return False

#
# Problem 5: Typewriter
#
def insertNewlines(text, lineLength):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately. 
    """
    ### TODO.
    if len(text) <= lineLength:
        return text
    else:
        # Returns the first part of the text whose length is lineLength plus
        # the rest inserted of new lines.
        new_text = ''
        char = text[lineLength - 1]
        # Insert newline character after the next space
        # Index in the slice after char
        space_sub_ind = text[(lineLength-1):].find(' ')
        if space_sub_ind == -1:
            return text
        else:
            # Index in the text
            space_ind = space_sub_ind + lineLength - 1
            new_text += text[:(space_ind + 1)] + '\n'
            new_text += insertNewlines(text[(space_ind + 1):], lineLength)
            return new_text
