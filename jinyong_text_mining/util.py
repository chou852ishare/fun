# -*- coding:utf-8 -*-

import pandas as pd


def count_occurrence(series, contents, novel='天龙八部'):
	count = pd.Series()
	for u in series[novel].dropna().unique():
		count[u] = contents[novel].count(u)
	return count
