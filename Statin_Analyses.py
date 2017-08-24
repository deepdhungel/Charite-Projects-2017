import pandas as pd
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')
pd.set_option('precision', 0)


doc = pd.read_excel('file:///C:/Users/Onotation/Documents/Internship/AllMalignantCancer/allMalignantCancer_newDB.xls')
J_1 = pd.read_excel('file:///C:/Users/Onotation/Documents/Internship/tables/J-1.xlsx')
I_1 = pd.read_excel('file:///C:/Users/Onotation/Documents/Internship/tables/I-1.xlsx')
H_1 = pd.read_excel('file:///C:/Users/Onotation/Documents/Internship/tables/H-1.xlsx')
D_1 = pd.read_excel('file:///C:/Users/Onotation/Documents/Internship/tables/D-1.xlsx')


J = doc.loc[:,'Cocktails-w-Cancer-w/o-Statins']
I = doc.loc[:,'Cocktails-w/o-Cancer-w-Statins']
H = doc.loc[:,'Cocktails-w/o-Cancer/Statins']
D = doc.loc[:,'Cocktails-w-Statins-and-Cancer']


JJ1 = J_1.merge(J.to_frame('Frequency'),left_on = 'AgeGroups', right_index=True, how ='left')
II1 = I_1.merge(I.to_frame('Frequency'),left_on = 'AgeGroups', right_index=True, how ='left')
HH1 = H_1.merge(H.to_frame('Frequency'),left_on = 'AgeGroups', right_index=True, how ='left')
DD1 = D_1.merge(D.to_frame('Frequency'),left_on = 'AgeGroups', right_index=True, how ='left')

frames = (JJ1, II1, HH1, DD1)
frames_concat = pd.concat(frames)

#frames_concat.to_csv('out.csv',index = False)

#df = pd.read_csv('file:///C:/Users/Onotation/Documents/Internship/out.CSV')
#df.values

frames_concat.AgeGroups = \
             frames_concat.AgeGroups.replace([r'^(\d{1})\_', r'_(\d{1})$'], 
                                  [r'0\1_',r'_0\1'],
                                  regex=True)
             
#frames_concat.to_csv('out_changed0.csv',index = False)

grp = frames_concat.groupby(['AgeGroups','Factor','Cancer']).Frequency.sum()
counts = grp.unstack(level=[2])

counts1=grp.unstack(level=[1])


table = counts1.groupby(level="Cancer").sum().values
oddsratio, pvalue = stats.fisher_exact(table)
print("OddsR(w-statin/wo-statin): ", oddsratio, "p-Value for confidence interval 95%:", pvalue)


#counts1['sumwwoStatin']= counts1['w-statin']+counts1['wo-statin']

#counts1['oddRatio']=((counts1['w-statin']/counts1['sumwwoStatin'])/(counts1['wo-statin']/counts1['sumwwoStatin']))

#ax = counts.plot(kind='bar',stacked=True,colormap='Paired',rot = 45)

#for p in ax.patches:
        #ax.annotate(np.round(p.get_height(),decimals=0).astype(np.int64), (p.get_x()+p.get_width()/2., p.get_y()), ha='center', va='center', xytext=(2, 10), textcoords='offset points', fontsize=10)

by_factor = counts.groupby(level='Factor')

k = by_factor.ngroups


fig, axes = plt.subplots(1, k, sharex=True, sharey=True, figsize=(15, 8))
for i, (gname, grp) in enumerate(by_factor):
    grp.xs(gname, level='Factor').plot.bar(
        stacked=True, rot=45, ax=axes[i], title=gname)
fig.tight_layout()

counts['sumwwoCancer']= counts['No']+counts['Yes']

test= counts['cumInci']=((counts['Yes']/counts['sumwwoCancer'])*100)

testUnstacked = test.unstack(level=[1])

ok=testUnstacked['AbsoluteRR']= (testUnstacked['wo-statin']-testUnstacked['w-statin'])

trialokay = ok.mean()


NumNeedTreat = 1/trialokay
pot = np.ceil(NumNeedTreat)
pot1 = str(int(float(pot)))

testUnstacked['NNT'] = 1/testUnstacked['AbsoluteRR']
#testUnstacked.NNT = testUnstacked.NNT.round()
#testUnstacked.NNT = np.ceil(testUnstacked.NNT)
print ("Number Needed to Treat for each of the", testUnstacked['NNT']*100)







