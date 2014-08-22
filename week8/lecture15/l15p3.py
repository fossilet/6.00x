# Since Apr 16 2013

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if L == []:
        return float('NaN')
    else:
        lengths = [len(s) for s in L]
        mu = float(sum(lengths))/len(L)
        std_dev = (sum((len_ - mu) ** 2 for len_ in lengths) / float(len(L))) ** 0.5
        return std_dev

print stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples'])
print stdDevOfLengths([])
