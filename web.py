#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
module: web
"""
import bottle
from bottle import route, run, template, request, response

bottle.debug(True)

from book_admin import BookAdmin

ba = BookAdmin()
ba.add_book(dict(title="aaa", ISBN="xxx"))

@route('/')
def index():
    return template('index')

@route('/book')
def book():
    return template('book')

@route('/book/update')
def book():
    title = request.GET['title']
    author = request.GET['author']
    ISBN = request.GET['ISBN']
    ba.add_book(dict(title=title, author=author, ISBN=ISBN))
    return " "

@route('/search')
def search():
    if request.GET['type'] == 'book':
        result = list(ba.find_book(title=request.GET['text']))
        return {'book': [book.data for book in result]}
    elif request.GET['type'] == 'reader':
        result = list(ba.find_reader(name=request.GET['text']))
        return {'reader': [reader.data for reader in result]}


from bottle import static_file
@route('/:filename')
def send_static(filename):
    return static_file(filename, root='public')


run(host='localhost', port=8080)
