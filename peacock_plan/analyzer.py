#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
from glob import glob

from settings import *

def unify_roster():
	fs = glob(FPATH+'/*')
	for f in sorted(fs, reverse=True):
		df = pd.read_excel(f)
		print f
		batch = df.columns[~df.columns.str.contains('Unname')][0]
		df.columns = df.iloc[0, :]
		df = df.drop(df.columns.name)
		df.index = df.iloc[:, 0]
		df = df.drop(df.index.name, axis=1)
		print
		print '-----------', batch
		print df.columns
		

if __name__ == '__main__':
	unify_roster()
