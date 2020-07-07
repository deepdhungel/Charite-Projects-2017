#import the libraries 
import scipy.stats as stats
import pandas as pd 

#import the csv as df 
df = pd.read_csv('C:\Users\OnoTation\Desktop\AllCsvs\cocktail_ids_age_gender.csv') 
df.values

#create two different categorical samples by gender either m or w 
cat1 = df[df['Gender']=='M']
cat2 = df[df['Gender']=='W']

#describe the sample 
cat1stat= cat1.describe()
cat2stat= cat2.describe()

#get ages 
sample1 = cat1.Age
sample2 = cat2.Age

#apply two sided man whitney test to calculate the t value to the sample 
mannwhtny = stats.mannwhitneyu(sample1,sample2, alternative = 'two-sided')
print ('The Result From Mann Whitney Test : {}'.format(mannwhtny))

#Null Hypothesis Rejection !

