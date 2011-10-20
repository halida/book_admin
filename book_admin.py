#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
module: book_admin
"""
import os, uuid
from simpledb import SimpleDB

class BookAdmin():
    DBFILE = 'book_admin.db'

    def __init__(self):
        self.db = SimpleDB()
        if os.path.isfile(self.DBFILE):
            self.db.load(self.DBFILE)
        else:
            self.db['store'].insert({})
            self.db['borrowed'].insert({})
        self.store = self.db['store'].find_one()
        self.borrowed = self.db['borrowed'].find_one()        

    def add_book(self, book):
        self.db['book'].insert(book)

    def add_reader(self, reader):
        reader['ID'] = uuid.uuid1().hex
        self.db['reader'].insert(reader)
        self.borrowed[reader['ID']] = {}

    def save(self):
        self.db.save(self.DBFILE)

    def find_reader(self, **kw):
        for data in self.db['reader'].find(**kw):
            yield Reader(self, data)

    def find_book(self, **kw):
        for data in self.db['book'].find(**kw):
            yield Book(self, data)

    def readers(self):
        return [Reader(self, data)
                for data in self.db['reader'].find()]

    def books(self):
        return [Book(self, data)
                for data in self.db['book'].find()]

    def store_book(self, book, number):
        ISBN = book.ISBN
        if not ISBN in self.store:
            self.store[ISBN] = number
        else:
            self.store[ISBN] += number

    def count_book(self):
        return sum(self.store.values())

    def book_static(self):
        static = dict(store=self.count_book())
        for reader in self.readers():
            static[reader.name] = reader.count_book()
        return static

class BaObject():
    def __init__(self, ba, data):
        self.ba = ba
        self.data = data

    def __getattr__(self, k):
        return self.data[k]


class Book(BaObject):
    pass


class Reader(BaObject):
    def borrow(self, book, number=1):
        v = self.ba.store.get(book.ISBN, 0)
        if v <= 0:
            raise Exception("no book current on store!")
        if number > v:
            raise Exception("book number is lesser then borrows!")
        self.ba.store[book.ISBN] -= number

        u = self.ba.borrowed[self.ID]
        if not book.ISBN in u:
            u[book.ISBN] = number
        else:
            u[book.ISBN] += number

    def back(self, book, number=1):
        u = self.ba.borrowed[self.ID]
        n = u.get(book.ISBN, 0)
        if n <= 0:
            raise Exception("reader don't have this book.")
        if n < number:
            raise Exception("reader don't have this much books.")
        u[book.ISBN] -= number
        self.ba.store[book.ISBN] += number

    def count_book(self):
        u = self.ba.borrowed[self.ID]
        return sum(u.values())
        

DEFAULT_BOOKS = [
    dict(title="SICP", authors=['Harold Abelson','Gerald Jay Sussman','Julie Sussman'], ISBN="0262011530"),
    ]

DEFAULT_READERS = [
    dict(name="linjun", gender="male", phone="13611111111"),
    dict(name="zhaoqiuling", gender="female", phone="13611111112"),
    ]

def get_books():
    "index"
    
def test():
    """
    simple test case:

    init
    >>> os.remove(BookAdmin.DBFILE)
    >>> ba = BookAdmin()
    >>> for book in DEFAULT_BOOKS: ba.add_book(book)
    >>> for reader in DEFAULT_READERS: ba.add_reader(reader)

    save and load
    >>> ba.save()
    >>> ba = BookAdmin()

    add book storage
    >>> reader = ba.find_reader(name='linjun').next()
    >>> book = ba.find_book(title='SICP').next()
    >>> ba.store_book(book, 3)

    borrow and return
    >>> reader.borrow(book, 2)
    >>> reader.count_book()
    2
    >>> ba.count_book()
    1
    >>> reader.back(book)
    >>> reader.count_book()
    1
    >>> ba.count_book()
    2

    static
    >>> ba.book_static()
    {'linjun': 1, 'zhaoqiuling': 0, 'store': 2}
    """
    import doctest
    doctest.testmod()


if __name__=="__main__":
    test()
    
