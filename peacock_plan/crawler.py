#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import urllib
import urllib2
from bs4 import BeautifulSoup

from settings import *


def fetch_soup(url, encoding='u8'):
    src  = urllib2.urlopen(url)
    page = src.read().decode(encoding)
    soup = BeautifulSoup(page, 'lxml')
    return soup


def get_annoucement_list(site):
    annouce = []
    for suffix in ['', '_1', '_2', '_3', '_4']:
        home = SITE + 'index%s.htm' % suffix
        soup = fetch_soup(home, 'gbk')
        for li in soup.find(class_='conRight_text_ul1').find_all('li'):
            attrs = li.find('a').attrs
            url   = SITE + attrs['href'].replace(r'./','')
            title = attrs['title']
            date  = li.find('span').text
            annouce.append([url, title, date])
    annouce = pd.DataFrame(annouce, columns=['url','title','date'])
    return annouce
    

def save_namexls(annouce):
    for i in annouce.index:
        url = annouce.loc[i,'url']
        soup = fetch_soup(url, 'gbk')
        for a in soup('a'):
            try:
                if 'xls' in a.attrs['href']:
                    prefx = '/'.join(url.split('/')[:-1])
                    fname = a['href'].replace(r'./','')
                    xlsurl = prefx + '/' + fname
                    urllib.urlretrieve(xlsurl, FPATH+fname)
                    print xlsurl
            except:
                pass


if __name__ == '__main__':
    annouce = get_annoucement_list(SITE)
    save_namexls(annouce) 

