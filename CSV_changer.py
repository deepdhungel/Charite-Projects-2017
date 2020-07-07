#changes xlsx data to csv data 
#
# -*- coding: utf-8 -*-
"""
Created on Thu May 04 16:06:23 2017

@author: Onotation
"""

import pandas as pd
#import numpy as np
#read the xlsx 
doc = pd.read_excel('file:///C:/Users/Onotation/Documents/Internship/Colorectal_ALL/C10AA/Malignant_Colorectal_Carcinom_5.xls')
J_1 = pd.read_excel('file:///C:/Users/Onotation/Documents/Internship/tables/J-1.xlsx')
I_1 = pd.read_excel('file:///C:/Users/Onotation/Documents/Internship/tables/I-1.xlsx')
H_1 = pd.read_excel('file:///C:/Users/Onotation/Documents/Internship/tables/H-1.xlsx')
D_1 = pd.read_excel('file:///C:/Users/Onotation/Documents/Internship/tables/D-1.xlsx')


J = doc.loc[:,'Cocktails-w-Cancer-w/o-Statins']
I = doc.loc[:,'Cocktails-w/o-Cancer-w-Statins']
H = doc.loc[:,'Cocktails-w/o-Cancer/Statins']
D = doc.loc[:,'Cocktails-w-Statins-and-Cancer']

#merge the dataframes by age groups 
JJ1 = J_1.merge(J.to_frame('Frequency'),left_on = 'AgeGroups', right_index=True, how ='left')
II1 = I_1.merge(I.to_frame('Frequency'),left_on = 'AgeGroups', right_index=True, how ='left')
HH1 = H_1.merge(H.to_frame('Frequency'),left_on = 'AgeGroups', right_index=True, how ='left')
DD1 = D_1.merge(D.to_frame('Frequency'),left_on = 'AgeGroups', right_index=True, how ='left')

frames = (JJ1, II1, HH1, DD1)
frames_concat = pd.concat(frames)
#export the csv 
frames_concat.to_csv('out.csv',index = False)
