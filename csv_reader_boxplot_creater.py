
#reads csv and creates boxplot

import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')


df = pd.read_csv('C:\Users\OnoTation\Desktop\AllCsvs\cocktail_ids_age_gender.csv')
df.values

grouped = df.groupby(['Age']).Cocktail_ID.count()

fig, ax = plt.subplots()
boxprops = dict(linestyle='-', linewidth=5, color='k')
medianprops = dict(linestyle='-', linewidth=5, color='blue')
bp = df.boxplot(showmeans=True,medianprops=medianprops,boxprops=boxprops)

plt.title('Box Plot Of Ages',fontsize=40) #
plt.text(x= 0.87, y = 59.9, s ="Median",fontsize=20)
plt.text(x= 0.88, y = 56, s ="Mean",fontsize=20)
plt.text(x= 0.84, y = 71, s ="3rd Quartile",fontsize=20)
plt.text(x= 0.84, y = 45, s ="1st Quartile",fontsize=20)
plt.xlabel ('Age',fontsize=40)
plt.ylabel('Age Range', fontsize=40)
plt.yticks(fontsize = 20)

plt.show()

