#! /usr/bin/env python

'''Bisection search

Since Feb 18 2013
'''

low = 0
high = 100
ans = ''
guess = (low + high) / 2
print('Please think of a number between 0 and 100!')

while ans != 'c':
	print('Is your secret number %s?' % guess)
	ans = raw_input("Enter 'h' to indicate the guess is too high. "
			"Enter 'l' to indicate the guess is too low. "
			"Enter 'c' to indicate I guessed correctly. ")
	if ans == 'h':
		high = guess
	elif ans == 'l':
		low = guess
	elif ans == 'c':
		break
	else:
		print('Sorry, I did not understand your input.')
		continue
	guess = (low + high) / 2

print('Game over. Your secret number was: %s' % ans)
