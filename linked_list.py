#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
module: linked_list
"""
class LinkedList():
    def __init__(self, *args):
        self.data = [None, None]
        self.tail = self.data
        self.length = 0
        if len(args) > 0:
            for v in args:
                self.append(v)

    def appand(self, v):
        d = [v, self.data[1]]
        self.data[1] = d
        self.length += 1
        return self.length
        
    def append(self, v):
        d = [v, None]
        self.tail[1] = d
        self.tail = d
        self.length+=1
        return self.length

    def upto(self, k):
        if self.length <= k:
            raise Exception("k: %d is out of list scope: %d" % (k, self.length))
        if k < 0:
            raise Exception("k: %d < 0" % k)
        d = self.data
        while k > 0:
            d = d[1]
            k -= 1
        return d

    def __getitem__(self, k):
        d = self.upto(k)
        return d[1][0]

    def __iter__(self):
        v = self.data[1]
        while v != None:
            yield v[0]
            v = v[1]

    def remove(self, k):
        d = self.upto(k)
        d[1] = d[1][1]
        self.length -= 1
        if self.tail == d[1]:
            self.tail = d
        return self.length

    def insert(self, k, v):
        d = self.upto(k)
        d[1] = [v, d[1]]
        self.length += 1
        return self.length

    def update(self, k, v):
        d = self.upto(k)
        d[1][0] = v

    def update_iter(self, condition, replace):
        d = self.data[1]
        count = 0
        while d != None:
            if condition(d[0]):
                d[0] = replace(d[0])
                count += 1
            d = d[1]
        return count

    def remove_iter(self, condition):
        d = self.data
        count = 0
        while d[1] != None:
            if condition(d[1][0]):
                d[1] = d[1][1]
                if self.tail == d[1]:
                    self.tail = d
                count += 1
            d = d[1]                
        return count

        
def test():
    """
    usage:
    >>> ll = LinkedList()
    >>> [ll.append(v) for v in (1,2,3,4,5)]
    [1, 2, 3, 4, 5]
    >>> [ll.appand(v) for v in (3,2)]
    [6, 7]
    >>> ll.length
    7
    >>> list(ll)
    [2, 3, 1, 2, 3, 4, 5]
    >>> ll[0]
    2

    edit:
    >>> ll.remove(3)
    6
    >>> list(ll)
    [2, 3, 1, 3, 4, 5]
    
    >>> ll.insert(4, 12)
    7
    >>> list(ll)
    [2, 3, 1, 3, 12, 4, 5]
    >>> ll.update(6, 12)
    >>> list(ll)
    [2, 3, 1, 3, 12, 4, 12]

    iter:
    >>> ll = LinkedList(1,2,3,4,5,6,7)
    >>> ll.update_iter(lambda v: v%2 == 0, lambda v: v/2)
    3
    >>> list(ll)
    [1, 1, 3, 2, 5, 3, 7]

    >>> ll = LinkedList(1,2,3,4,5,6,7)
    >>> ll.remove_iter(lambda v: v%2 == 0)
    3
    >>> list(ll)
    [1, 3, 5, 7]
    
    error:
    >>> ll[12]
    Traceback (most recent call last):
        ...
    Exception: k: 12 is out of list scope: 7
    >>> ll[-1]
    Traceback (most recent call last):
        ...
    Exception: k: -1 < 0
    """
    import doctest
    doctest.testmod()

def main():
    test()
    
if __name__=="__main__":
    main()

