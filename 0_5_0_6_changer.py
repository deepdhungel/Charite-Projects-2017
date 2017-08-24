import pandas as pd

df = pd.read_csv('file:///C:/Users/Onotation/Documents/Internship/out.CSV')
df.values

df.AgeGroups = \
             df.AgeGroups.replace([r'^(\d{1})\_', r'_(\d{1})$'], 
                                  [r'0\1_',r'_0\1'],
                                  regex=True)
             
df.to_csv('out_changed0.csv',index = False)             
