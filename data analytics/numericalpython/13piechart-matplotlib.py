
"""
when x and y have numerical values
"""
from itertools import groupby

import  matplotlib.pyplot as plt
import pandas as pd
import  numpy as np

y = [98,60,95,55,85,45]
y1 = [90,75,80,90,65,95]
x = ["part1","part2","part3","part4","part5","part6"]
c = ["red","green","yellow","blue","orange","pink"]
ex =[0.1,0.1,0.1,0.2,0.4,0.1]
col = np.random.randint(5,20,10)
size = np.random.randint(5,20,10)
#Index,Name,Description,Brand,Category,Price,Currency,Stock,EAN,Color,Size,Availability,Internal ID

plt.pie(y,labels= x,colors= c,explode= ex,shadow= True,autopct= "%.2f",startangle= 90 )
plt.show()

data = pd.read_csv("products.csv")
df= pd.DataFrame(data)
grouped_by1 = df.groupby("Category")["Price"].sum()
grouped_by2 = df.groupby("Availability")["Index"].sum()
print(grouped_by2)
#plt.pie(df["Price"],labels= df["Category"]) # only single colm can be taken
#plt.pie(df["Availability"]) # only single colm can be taken
plt.pie(grouped_by2.values,labels = grouped_by2.index ) # only single colm can be taken
plt.show()


