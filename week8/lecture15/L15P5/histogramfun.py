import pylab


WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    vowels = [c for c in 'aeiou']
    fracs = []
    for word in wordList:
        frac = sum(1 if c in vowels else 0 for c in word)/float(len(word))
        fracs.append(frac)
    pylab.figure()
    pylab.hist(fracs, bins=numBins)
    pylab.title('Histogram of the proportion of vowels in each word')
    pylab.xlabel('Vowel proportions')
    pylab.ylabel('Number of words with the vowel proportion')
    pylab.show()
    

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
