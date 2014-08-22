class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        self.before = before
    def setAfter(self, after):
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

    def __repr__(self):
        before = self.getBefore()
        before = before.myName() if before else '*'
        me = self.name.upper()
        after = self.getAfter()
        after = after.myName() if after else '*'
        return '%s--%s--%s' % (before, me, after)


def get_ins_pos(p, q):
    # FIXME: should return a ternary.
    '''Return new pair of Frobs to mutate.
    
    p: current Frob.
    q: new Frob to insert.
    '''
    # To put q before p
    if q.myName() < p.myName():
        # p does not have a head
        if p.getBefore() is None:
            return (q, p)
        # p has a head
        else:
            return get_ins_pos(p.getBefore(), q)
    # To put q after p
    else:
        # p does not have a tail
        if p.getAfter() is None:
            return (p, q)
        else:
            return get_ins_pos(p.getAfter(), q)


def get_ins_pos_bisect(p, l):
    '''Return a ternary of Frobs to mutate in the order they are to be
    appearing in the linkedlist.
    
    p: current Frob.
    q: new Frob to insert.
    '''
    from bisect import bisect
    bisect(p)


def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links
    This procedure appropriately inserts newFrob into the linked list that atMe
    is a part of.    
    """
    from bisect import bisect

    p, q = atMe, newFrob
    frobs = get_all_frobs(p)
    frob_names = [f.myName() for f in frobs]
    index = bisect(frob_names, q.myName())
    frobs.insert(index, q)
    #print index
    #print len(frobs)

    try:
        p = frobs[index - 1]
    except IndexError:
        p = None

    c = frobs[index]

    try:
        q = frobs[index + 1]
    except IndexError:
        q = None

    #print p, c, q
    # FIXME: this is buggy. But I quit here. Jun 1 2013
    p.setAfter(c)
    c.setBefore(p)
    c.setAfter(q)
    q.setBefore(c)

    #b, a = get_ins_pos(atMe, newFrob)
    #b.setAfter(a)
    #a.setBefore(b)


def get_all_frobs(f):
    from collections import deque
    l = deque([f])
    b = f.getBefore()
    # Not at the head of the linkedlist
    while b is not None:
        l.appendleft(b)
        b = b.getBefore()
    a = f.getAfter()
    while a is not None:
        l.append(a)
        a = a.getAfter()
    return list(l)


def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    if start.getBefore() is None:
        return start
    else:
        return findFront(start.getBefore())

if __name__ == '__main__':
    eric = Frob('eric')
    andrew = Frob('andrew')
    ruth = Frob('ruth')
    fred = Frob('fred')
    martha = Frob('martha')
    zed = Frob('zed')

    def print_list():
        for frob in andrew, eric, fred, martha, ruth, zed:
            print frob

    insert(eric, andrew)
    print_list()
    insert(eric, ruth)
    print_list()
    #insert(eric, fred)
    #print_list()
    #insert(ruth, martha)
    #print_list()
    #insert(andrew, zed)
    #print_list()
    print '***'
    #print findFront(ruth)
    #print get_all_frobs(eric)
