class Queue:
    '''Queue class.
    >>> queue = Queue()
    >>> queue.insert(5)
    >>> queue.insert(6)
    >>> queue.remove()
    5
    >>> queue.insert(7)
    >>> queue.remove()
    6
    >>> queue.remove()
    7
    '''
    def __init__(self):
        self.vals = []

    def insert(self, ele):
        self.vals.append(ele)

    def remove(self):
        try:
            return self.vals.pop(0)
        except IndexError:
            raise ValueError()

if __name__ == '__main__':
    import doctest
    doctest.testmod()
