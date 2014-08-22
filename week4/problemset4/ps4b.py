from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    def isValidWord1(word, hand):
        '''Like isValidWord is ps4a.py, but do not check if the word is in the
        wordList. 'in' operation on list is O(n).
        '''
        hd = hand.copy()
        for c in word:
            try:
                hd[c] -= 1
            except KeyError:
                return False
        if any(map(lambda x: x < 0, hd.itervalues())):
            return False

        return True

    # Create a new variable to store the maximum score seen so far (initially 0)
    best_score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
       #if isValidWord(word, hand, wordList):
       if isValidWord1(word, hand):
            # Find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if score > best_score:
                # Update your best score, and best word accordingly
                best_score = score
                best_word = word

    # return the best word you found.
    return best_word


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    total_score = 0
    # As long as there are still letters left in the hand:
    while set(hand.values()) != set([0]):
        # Display the hand
        print('\nCurrent hand:  '),
        displayHand(hand) 
        word = compChooseWord(hand, wordList, n)
        if word is None:
            break
        else:
            ws = getWordScore(word, n)
            total_score += ws
            print('"%s" earned %d points. Total: %d points.\n' % (word, 
                ws, total_score))
            # Update the hand 
            hand = updateHand(hand, word)
    
    print('Total score: %s points. ' % total_score)
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    def get_play_func():
        while True:
            rep1 = raw_input('\nEnter u to have yourself play, '
                'c to have the computer play: ')
            if rep1 == 'u':
                play_func = playHand
                break
            elif rep1 == 'c':
                play_func = compPlayHand
                break
            else:
                print('Invalid command.')

        return play_func

    last_hand = {}
    while True:
        if last_hand != {}:
            print('')
        rep = raw_input('Enter n to deal a new hand, '
                'r to replay the last hand, or e to end game: ')
        if rep == 'e':
            break
        elif rep not in ('n', 'r'):
            print('Invalid command.')
        else:
            if rep == 'n':
                play_func = get_play_func()
                hand = dealHand(HAND_SIZE)
                last_hand = hand
                play_func(hand, wordList, HAND_SIZE)
            elif last_hand == {}:  # rep == 'r': 
                print('You have not played a hand yet. '
                            'Please play a new hand first!')
                continue
            else:  # replay last hand
                play_func = get_play_func()
                hand = last_hand
                play_func(hand, wordList, HAND_SIZE)

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    word_scores = {word: getWordScore(word, HAND_SIZE) for word in wordList}
    #playGame(wordList)
    playGame(word_scores)
