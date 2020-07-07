#odds ratio / p value calculation for analysis

#from __future__ import division
#import numpy as np
import scipy.stats as stats
#from scipy.stats import chi2_contingency
import pandas as pd
import matplotlib.pyplot as plt
#import statsmodels.api as sm
#import pylab as pl


plt.style.use('fivethirtyeight')


#read dataframe
df = pd.read_csv('file:///C:/Users/Onotation/Desktop/allMalignantCancerRange_newDB.csv')
df.values

#group unique ages 
ages= df.AgeGroups.unique()

#group dfs by agegroup, factor, cancertypes 
grp = df.groupby(['AgeGroups','Factor','Cancer']).Frequency.sum()

counts = grp.unstack(level=[2])

#print counts

counts1=grp.unstack(level=[1])

#calculate the odds ratio and p-value 
table = counts1.groupby(level="Cancer").sum().values
oddsratio, pvalue = stats.fisher_exact(table)
print("OddsR(w-statin/wo-statin): ", oddsratio, "p-Value:", pvalue)


#counts1['sumwwoStatin']= counts1['w-statin']+counts1['wo-statin']

#counts1['oddRatio']=((counts1['w-statin']/counts1['sumwwoStatin'])/(counts1['wo-statin']/counts1['sumwwoStatin']))

#ax = counts.plot(kind='bar',stacked=True,colormap='Paired',rot = 45)

#for p in ax.patches:
        #ax.annotate(np.round(p.get_height(),decimals=0).astype(np.int64), (p.get_x()+p.get_width()/2., p.get_y()), ha='center', va='center', xytext=(2, 10), textcoords='offset points', fontsize=10)
by_factor = counts.groupby(level='Factor')

k = by_factor.ngroups

#plot 
fig, axes = plt.subplots(1, k, sharex=True, sharey=True, figsize=(15, 8))
for i, (gname, grp) in enumerate(by_factor):
    grp.xs(gname, level='Factor').plot.bar(
        stacked=True, rot=45, ax=axes[i], title=gname)
fig.tight_layout()



















