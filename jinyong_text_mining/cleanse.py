#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import pandas as pd
from glob import glob


def load_x(fpath):
    ''' load role/gang/kongfu names of each book.
        
        Return
        ------
        pandas.DataFrame: columns-book names, index-number
    '''
    with open(fpath) as f:
        lines = f.readlines()

    names = pd.DataFrame()
    for line in lines:
        item = line.strip().decode('u8').split(' ')
        bookname = re.match(r'<(.*)>', item[0]).group(1)
        xname = item[1:]
        tmp = pd.Series(xname, name=bookname)
        names = pd.concat([names,tmp], axis=1) 

    return names


def get_all_content():
    contents = {}
    for f in glob('jinyong_novels/*'):
        novel_name = re.match(r'jinyong_novels/(.*)\.txt', f).group(1).decode('u8')
        content = open(f).read().decode('gb18030').encode('u8').decode('u8')
        contents[novel_name] = content
    return contents 


def get_entities():
    names = load_x('rolenames.txt')
    gangs = load_x('gangs.txt')
    kongs = load_x('kongfu.txt')
    return names, gangs, kongs


if __name__ == '__main__':
    get_entities()
