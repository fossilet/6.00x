# Test for L11_hand

from week6.Lecture11.L11_hand import Hand

myHand = Hand(12)
myHand.setDummyHand('eecoohaoinda')
assert not myHand.update('chayote')
print myHand
