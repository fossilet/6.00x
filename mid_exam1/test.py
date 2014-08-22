#! /usr/bin/env python

'''Test suits for 6.00x Midterm Exam 1

Since Mar 23 2013
'''

from mid_exam1.me1_p5 import generateForm
from mid_exam1.me1_p7 import generateTemplates
from mid_exam1.me1_p8 import verifyWord
from mid_exam1.me1_p10 import numPens
from week6.lecture10.l10_p8 import intSet


# Test for me1_p5

story = 'The ravenous zombies started attacking yesterday'
listOfAdjs = ['ravenous']
listOfNouns = ['zombies', 'humans', 'yesterday']
listOfVerbs = ['attacking', 'attacks']
print generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)

story = 'At the creepy thrift store I found a pair of plaid pants that looked like something your grandpa might wear'
listOfAdjs = ['creepy', 'plaid']
listOfNouns = ['store', 'pants', 'something', 'grandpa']
listOfVerbs = ['found', 'looked']
print generateForm(story, listOfAdjs, listOfNouns, listOfVerbs)


# Test for me1_p7

libs = 'The [ADJ] [NOUN] started [VERB] [NOUN]'
print generateTemplates(libs)
libs = 'At the [ADJ] thrift [NOUN] I [VERB] a pair of [ADJ] [NOUN] that [VERB] like [NOUN] your [NOUN] might wear'
print generateTemplates(libs)


# Test for me1_p8

listOfAdjs = ['creepy', 'plaid']
listOfNouns = ['store', 'pants', 'something', 'grandpa']
listOfVerbs = ['found', 'looked']
assert verifyWord('creepy', '[ADJ]', listOfAdjs, listOfNouns, listOfVerbs)
assert not verifyWord('nonon', '[NOUN]', listOfAdjs, listOfNouns, listOfVerbs)
assert verifyWord('found', '[VERB]', listOfAdjs, listOfNouns, listOfVerbs)


# Test for me1_p10

assert not numPens(3)
assert numPens(5)
assert not numPens(7)
assert numPens(8)
assert not numPens(11)
assert numPens(13)
assert not numPens(19)
assert numPens(21)
assert numPens(24)
assert not numPens(27)
assert numPens(29)
assert numPens(30)
assert numPens(31)
assert numPens(32)
assert numPens(36)
assert numPens(39)


# Test for l10_p8

s1 = intSet()
s2 = intSet()

assert s1.intersect(s2) == '{}'
assert s2.intersect(s1) == '{}'
s1.insert(1)
assert s1.intersect(s2) == '{}'
assert s2.intersect(s1) == '{}'

s2.insert(2)
s2.insert(3)
assert s1.intersect(s2) == '{}'
assert s2.intersect(s1) == '{}'

s1.insert(3)
assert s1.intersect(s2) == '{3}'
assert s2.intersect(s1) == '{3}'
