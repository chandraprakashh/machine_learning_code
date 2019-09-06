# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 14:51:11 2019

@author: Administrator
"""

import pandas as pd

a = pd.Series((1,2,3,4,5,6,7,8,9))
print (a)

date = {'gender': ['f','f','m'], 'emp_id':['001','002','003'], 'age': [10,12,13]}

df = pd.DataFrame(date,columns=['emp_id','gender','age'])
print (df)