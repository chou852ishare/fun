#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
from glob import glob

from settings import *

def unify_roster():
    roster = pd.DataFrame(columns=RCOL1)
    fs = glob(FPATH+'/*')
    for f in sorted(fs, reverse=True):
        df = pd.read_excel(f).fillna('NULL')
        batch = df.columns[~df.columns.str.contains('Unname')][0]
        df.columns = df.iloc[0, :].map(lambda s: s.replace(' ',''))
        df = df.drop(df.columns.name)
        df.index = df.iloc[:, 0]
        df = df.drop(df.index.name, axis=1)
	df[BATCH] = [batch] * df.shape[0]
	if df.columns.shape[0] == 5:
	    roster = pd.concat([roster, df[RCOL1]])
	else:
	    df_ = df[RCOL2]
	    df_.columns = RCOL1
	    roster = pd.concat([roster, df_])
        print
        print '-----------', batch
        print f
        print roster[RCOL1].head(1)
	print '\t'.join(roster.columns)
	print roster.iloc[0,:].values
        

if __name__ == '__main__':
    print RCOL1
    unify_roster()
