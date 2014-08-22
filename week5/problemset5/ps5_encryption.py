# 6.00x Problem Set 5
#
# Part 1 - HAIL CAESAR!

import string
import random
#import cgitb
#cgitb.enable()

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.
    def shift_vals(c, last):
        '''Shift values considering rotating
        '''
        total = 26
        new_ord = ord(c) + shift
        if new_ord <= ord(last):
            new = chr(new_ord)
        else:
            new = chr(new_ord - total)
        return new
    
    d = {}
    for c in string.ascii_letters:
        if c in string.ascii_lowercase:
            d[c] = shift_vals(c, 'z')
        else:
            d[c] = shift_vals(c, 'Z')
    return d


def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO.
    def chargen(text, coder):
        new = []
        for c in text:
            if c in string.ascii_letters:
                yield coder[c]
            else:
                yield c

    return ''.join(chargen(text, coder))
            

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.
    return applyCoder(text, buildCoder(shift))

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    '''
    Psuedo code
    '''
    def text_score(wordList, text):
        '''Determine one text's goodness.
        '''
        #We give the text a score, whose initial vaule is 0.
        score = 0
        #We split the text into words
        words = text.split()
        #For each word
        for word in words:
            #If the word is a valid word, we add one to the score
            if isWord(wordList, word):
                score += 1
        #After this we return the score.
        return score

    # There are 27 possible shift keys
    keys = range(1, 27)
    # We bookkeeping the decryption key, and the maximum score, whose initial
    # value is 0.
    max_key = 0
    max_score = 0
    #For each possible shift key
    for key in keys:
        # For each shift key, the decryption key is 26 - k
        decrypt_key = 26 - key
        # Apply its decryption key, then we get the decrypted text
        decrypt_text = applyShift(text, decrypt_key)
        # The text may be crap. We have to determine the decypted text's
        # probability of being real English text. And find the most probable
        # text.
        score = text_score(wordList, decrypt_text)
        # If the current text's score is larger than the maximum score
        if score > max_score:
        # We let the maximum be the current text's score.
            max_score = score
            max_key = decrypt_key
    # Then return the respective key.
    return max_key
    

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    ### TODO.
    wordList = loadWords()
    crypt_msg = getStoryString()
    orig_msg = applyShift(crypt_msg, findBestShift(wordList, crypt_msg))
    return orig_msg

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    #from ipdb import launch_ipdb_on_exception
    #with launch_ipdb_on_exception():
    # To test findBestShift:
    #wordList = loadWords()
    #s = applyShift('Hello, world!', 8)
    #bestShift = findBestShift(wordList, s)
    #assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    print decryptStory()
