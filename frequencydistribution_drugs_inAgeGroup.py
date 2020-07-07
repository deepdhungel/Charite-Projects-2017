#import the libraries 
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pylab
plt.style.use('fivethirtyeight')

#read the csv as df 
df = pd.read_csv('C:\Users\OnoTation\Desktop\AllCsvs\cocktail_ids_age_gender.csv')
df.values
#Return the indices of the bins to which each value in input array belongs
bins = np.arange(1, 10) * 10
df['category'] = np.digitize(df.Age, bins, right=True)

#group the dataframes by category and gender and calculate frequency distribution by age 
counts = df.groupby(['category', 'Gender']).Age.count().unstack()

#plot 
ax = counts.plot(kind='bar',stacked = True, colormap = 'Paired',rot = 45)

for p in ax.patches:
        ax.annotate(np.round(p.get_height(),decimals=0).astype(np.int64), (p.get_x()+p.get_width()/2., p.get_y()), ha='center', va='center', xytext=(10, 20), textcoords='offset points',fontsize=20)
       #ax.annotate(p.get_height(), (p.get_x() + p.get_width(), p.get_y()), xytext=(5, 10), textcoords='offset points')
xticks = pylab.setp(ax, xticklabels=['10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80',
                                      '80-90'])

plt.xlabel ('Age Group',fontsize=20)
plt.ylabel ('Frequency Of Cocktails',fontsize=40)
plt.title('Frequency Distribution Of Cocktails In Age Groups',fontsize=40)

ax.set_xticklabels(xticks, fontsize=20)
plt.show()
