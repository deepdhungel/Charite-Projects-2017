# calculates the chemical properties of the drug

import pandas as pd
#read the csv 
df = pd.read_csv('C:\\Users\\OnoTation\\Desktop\\AllCsvs\\atc_drugs_2016.csv')
df.values
print df

df1 = pd.read_csv('C:\\Users\\OnoTation\\Desktop\\AllCsvs\\atc_id_TO_cocktailID.csv')
df1.values

who_id_select_1 = df1.who_id
cocktail_id_select_1 = df1.cocktail_id
#join the who_id with the cocktail_id 
result1 = pd.concat([who_id_select_1,cocktail_id_select_1], axis=1, join='inner')
#print result1

outerJoin = result1.merge(df, left_on='who_id', right_on='who_id', how='outer')

grouped = outerJoin.groupby(['who_name','smile','molwt','atoms','hba','hbd','rot_bonds','formula','logp']).cocktail_id.count()
