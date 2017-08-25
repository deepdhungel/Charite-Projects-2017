#Calculation of Top 10 Diagnoses on the Dataframe


import pandas as pd
df = pd.read_csv('C:\\Users\\OnoTation\\Desktop\\AllCsvs\\atc_id_TO_cocktailID.csv')
df.values

who_id_select_1 = df.who_id
cocktail_id_select_1 = df.cocktail_id

result1 = pd.concat([who_id_select_1,cocktail_id_select_1], axis=1, join='inner')
#print result1

df1 = pd.read_csv('C:\\Users\\OnoTation\\Desktop\\AllCsvs\\cocktail_scoring.csv')


#print df1

cocktail_id_select_2 = df1.cocktail_id
problem_d = df1.problem_d
problem_x = df1.problem_x

result2 = pd.concat([cocktail_id_select_2,problem_d,problem_x], axis=1, join='inner')
#print result2

df2 = pd.read_csv('C:\\Users\\OnoTation\\Desktop\\AllCsvs\\atc_drugs_2016.csv')

#print df1

who_id_select2 = df2.who_id
who_name_select = df2.who_name

result3 = pd.concat([who_id_select2,who_name_select], axis=1, join='inner')
#print result3

result1_result3 = result1.merge(result3, left_on='who_id', right_on='who_id', how='outer')


df3 = pd.read_csv('C:\\Users\\OnoTation\\Desktop\\AllCsvs\\newdiagnoses.csv')


result4 = result1_result3.merge(df3, left_on='cocktail_id', right_on='cocktail_id', how='outer')

counts = result4.groupby(['diagnoseYear','who_name']).who_name.count()



