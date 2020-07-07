#import the libraries 
import matplotlib.pyplot as plt 
import pandas as pd 

#read csv as df 
df = pd.read_csv('C:\Users\OnoTation\Desktop\AllCsvs\cocktail_ids_age_gender.csv') 
df.values

#calculate frequency distribution of cocktails by age and gender 
genders = df.Gender.unique()

counts = df.groupby(['Gender','Age']).count()

totals = counts.sum(level = 0) 
print totals

#plot 
temp2 = df.groupby('Gender').Cocktail_ID.count()
ax = temp2.plot(kind='pie',stacked = False, colormap = 'Paired',figsize=(6, 6),autopct='%.2f',fontsize=10)
ax.legend(loc=3, labels=None)
plt.title('Distribution Of Cocktails By Gender',fontsize=40)
plt.ylabel('')


plt.show()

