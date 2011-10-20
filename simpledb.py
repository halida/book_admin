#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
module: simpledb
"""
import cPickle as pickle
from linked_list import LinkedList

class SimpleDB():
    def __init__(self):
        self.tables = {}

    def __getitem__(self, name):
        return Table(self, name)

    def save(self, filename):
        pickle.dump(self.tables, open(filename, 'w+'))

    def load(self, filename):
        self.tables = pickle.load(open(filename))


class Table():
    def __init__(self, db, name):
        self.db = db
        self.name = name
        if not name in self.db.tables:
            self.db.tables[name] = LinkedList()
        self.table = self.db.tables[name]

    def insert(self, *args, **kw):
        if len(args) > 0:
            for v in args:
                self.table.append(v)
            return len(args)
        
        if len(kw.keys()) > 0:
            self.table.append(kw)
            return 1

    def find(self, **kw):
        for item in self.table:
            if match(kw, item):
                yield(item)

    def find_one(self, **kw):
        return self.find().next()

    def update(self, kw, value):
        def condition(item):
            return match(kw, item)
        def replace(v):
            return value
        return self.table.update_iter(condition, replace)

    def set(self, kw, value):
        def condition(item):
            return match(kw, item)
        def replace(v):
            for k in value:
                v[k] = value[k]
            return v
        return self.table.update_iter(condition, replace)

    def remove(self, **kw):
        def condition(item):
            return match(kw, item)
        return self.table.remove_iter(condition)


def match(kw, item):
    for key, v in kw.iteritems():
        if not key in item:
            return
        if type(key) in [unicode, str]:
            if not v in item[key]:
                return
        else:
            if v != args[key]:
                return
    return True

def test():
    """
    >>> db = SimpleDB()
    >>> book = db['book']
    >>> book.insert(title="test", desc="xxx")
    1
    >>> book.insert(dict(title="p"), dict(title="q"))
    2
    >>> book.find_one(title="test")
    {'desc': 'xxx', 'title': 'test'}
    >>> book.update(dict(title="test"), dict(title="xxx", desc="xxx"))
    1
    >>> book.set(dict(title="xxx"), dict(desc="x"))
    1
    >>> book.remove(title="xxx")
    1
    
    save and load
    >>> db.save('xxx.db')
    >>> db.load('xxx.db')
    >>> list(db['book'].find(title="p"))
    [{'title': 'p'}]
    """
    import doctest
    doctest.testmod()

def main():
    test()
    
if __name__=="__main__":
    main()
