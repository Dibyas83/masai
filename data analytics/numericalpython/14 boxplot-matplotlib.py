
"""
 used for statistical analysis ,see where freq is going,quartile(%),median r

iqr = range(q1,q3)= 2.5 - 7.5 = 5
min/LF = q1 -1.5(inter quartile range)=2.5 -7.5=-5 . .closest no to -5 or the min in list = 20
q1 = 25% = 25/100   *  n+1
median = sum/size
q3 = 75% = 75/100   *  n+1
max/UF =q3 +1.5(inter quartile range)iqr = 15 .closest value less than 15
"""
from itertools import groupby

import  matplotlib.pyplot as plt
import pandas as pd
import  numpy as np

y = [40,98,60,95,30,55,85,45,20]
y1 = [30,90,75,40,80,90,65,95,50]
x = ["part1","part2","part3","part4","part5","part6"]
c = ["red","green","yellow","blue","orange","pink"]
ex =[0.1,0.1,0.1,0.2,0.4,0.1]
col = np.random.randint(5,20,10)
size = np.random.randint(5,20,10)
#Index,Name,Description,Brand,Category,Price,Currency,Stock,EAN,Color,Size,Availability,Internal ID



data = pd.read_csv("products.csv")
df= pd.DataFrame(data)
grouped_by1 = df.groupby("Category")["Price"].sum()
grouped_by2 = df.groupby("Availability")["Index"].sum()



