# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 21:39:08 2017

@author: OnoTation
"""

import pandas as pd


pd.set_option('precision', 0)
df = pd.read_csv('file:///C:/Users/Onotation/Desktop/allMalignantCancerRange_newDB.csv')
df.values


ages= df.AgeGroups.unique()

grp = df.groupby(['AgeGroups','Factor','Cancer']).Frequency.sum()

counts = grp.unstack(level=[2])


counts['sumwwoCancer']= counts['No']+counts['Yes']

test= counts['cumInci']=((counts['Yes']/counts['sumwwoCancer'])*100)

testUnstacked = test.unstack(level=[1])

ok=testUnstacked['AbsoluteRR']= (testUnstacked['wo-statin']-testUnstacked['w-statin'])

testUnstacked['NNT'] = 1/testUnstacked['AbsoluteRR']
#testUnstacked.NNT = testUnstacked.NNT.round()
#testUnstacked.NNT = np.ceil(testUnstacked.NNT)
print ("Number Needed to Treat for each of the", testUnstacked['NNT']*100)

