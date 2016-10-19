"""

@author: Tim Ha
@date: 11.15.15
@assn: test5
"""
# -*- coding: ut-8 -*-
import codecs
import numpy as np

test = {'one': [1,2], 'two': [3,4]}
test2 = {'one': [10, 20], 'two': [3,4]}

ntest = {}

for thing in test:
	ntest[thing] = [0] * 21
	for i in range(2):
		ntest[thing][i] = test2[thing][i] / test[thing][i]
print(ntest)

