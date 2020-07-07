#frequency distribution of diagnoses 
import pandas as pd
 
#read the csv of diagnoses as a dataframe 
df = pd.read_csv('C:\\Users\\OnoTation\\Desktop\\AllCsvs\\newdiagnoses.csv')
df.values

df1 = pd.read_csv('C:\\Users\\OnoTation\\Desktop\\AllCsvs\\nayadiag.csv')
df1.values

#count the cocktail id by icd10 codes 
count1 = df.groupby(['icd10']).cocktail_id.count()

count2 = df1.groupby(['icd10']).cocktail_id.count()