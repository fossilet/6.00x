from itertools import chain, combinations


def yieldAllCombos(items):
    """
    Generates all combinations of N items into two bags, whereby each item is in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as a list of which item(s) are in each bag.
    """
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in xrange(3 ** N):
        bag1, bag2 = [], []
        for j in xrange(N):
            # test bit jth of integer i
            if (i / (3**j)) % 3 == 1:
                bag1.append(items[j])
            elif (i / (3**j)) % 3 == 2:
                bag2.append(items[j])
        yield bag1, bag2


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
