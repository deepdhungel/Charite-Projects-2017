#Numbers Needed to Treat / Absolute Risk Reduction Calculation

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 21:39:08 2017

@author: OnoTation
"""
#import library 
import pandas as pd

#csv as df 
pd.set_option('precision', 0)
df = pd.read_csv('file:///C:/Users/Onotation/Desktop/allMalignantCancerRange_newDB.csv')
df.values

#group by unique age groups 
ages= df.AgeGroups.unique()

#group by agegroups, factor, cancer 
grp = df.groupby(['AgeGroups','Factor','Cancer']).Frequency.sum()

counts = grp.unstack(level=[2])

counts['sumwwoCancer']= counts['No']+counts['Yes']

#calculate cumulative incidence 
test= counts['cumInci']=((counts['Yes']/counts['sumwwoCancer'])*100)

testUnstacked = test.unstack(level=[1])

#calculate absolute risk ratio
ok=testUnstacked['AbsoluteRR']= (testUnstacked['wo-statin']-testUnstacked['w-statin'])

testUnstacked['NNT'] = 1/testUnstacked['AbsoluteRR']
#testUnstacked.NNT = testUnstacked.NNT.round()
#testUnstacked.NNT = np.ceil(testUnstacked.NNT)
#print the numbers needed to treat 
print ("Number Needed to Treat for each of the", testUnstacked['NNT']*100)

