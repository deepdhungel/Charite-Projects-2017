import scipy.stats as stats


import pandas as pd 


df = pd.read_csv('C:\Users\OnoTation\Desktop\AllCsvs\cocktail_ids_age_gender.csv') 
df.values



cat1 = df[df['Gender']=='M']
cat2 = df[df['Gender']=='W']


cat1stat= cat1.describe()
cat2stat= cat2.describe()

sample1 = cat1.Age
sample2 = cat2.Age

mannwhtny = stats.mannwhitneyu(sample1,sample2, alternative = 'two-sided')
print ('The Result From Mann Whitney Test : {}'.format(mannwhtny))

#Null Hypothesis Rejection !

