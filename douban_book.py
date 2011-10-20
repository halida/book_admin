#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
module: douban_book
"""
import douban

API_KEY = "07e380339b73b26517aa809ad25b172f"
SECRET = "139f04342751706c"
SERVER = ""

def init():
    client = douban.service.DoubanService(server=SERVER, api_key=API_KEY,secret=SECRET)
    return client

def main():
    pass
    
if __name__=="__main__":
    main()
