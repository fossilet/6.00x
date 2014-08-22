class hashSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self, numBuckets): 
        '''
        numBuckets: int. The number of buckets this hash set will have. 
        Raises ValueError if this value is not an integer, or if it is not greater than zero.

        Sets up an empty hash set with numBuckets number of buckets.
        '''
        if type(numBuckets) is not int or numBuckets <=0 :
            raise ValueError
        self.numBuckets = numBuckets
        self.buckets = [[] for i in range(numBuckets)]

    def getNumBuckets(self):
        return self.numBuckets

    def hashValue(self, e):
        '''
        e: an integer

        returns: a hash value for e, which is simply e modulo the number of 
         buckets in this hash set. Raises ValueError if e is not an integer.
        '''
        if type(e) is not int:
            raise ValueError
        return e % self.getNumBuckets()

    def member(self, e):
        '''
        e: an integer
        Returns True if e is in self, and False otherwise. Raises ValueError if e is not an integer.
        '''
        if type(e) is not int:
            raise ValueError
        hash_ = self.hashValue(e)
        return e in self.buckets[hash_]

    def insert(self, e):
        '''
        e: an integer
        Inserts e into the appropriate hash bucket. Raises ValueError if e is not an integer.
        ''' 
        if type(e) is not int:
            raise ValueError
        hash_ = self.hashValue(e)
        self.buckets[hash_].append(e)
        
    def remove(self, e):
        '''
        e: is an integer 
        Removes e from self
        Raises ValueError if e is not in self or if e is not an integer.
        '''
        if type(e) is not int or not self.member(e):
            raise ValueError
        hash_ = self.hashValue(e)
        self.buckets[hash_].remove(e)

    def __str__(self):
        str_ = '{'
        for index in range(self.getNumBuckets()):
            for val in self.buckets[index]:
                str_ += '%s: %s, ' % (index, val)
        str_ += '}'
        return str_

if __name__ == '__main__':
    s = hashSet(3)
    s.insert(2)
    s.insert(3)
    s.insert(4)
    s.insert(7)
    print s
