
"""

"""
from itertools import groupby

import  matplotlib.pyplot as plt
import pandas as pd

y = [98,80,85,95,75,100]
y1 = [90,75,80,90,65,95]
x = ["part1","part2","part3","part4","part5","part6"]
colors = ["red","green","yellow","blue","orange","pink"]
plt.plot(x,y,marker = "D",ls = "--",color = "red",label = "week1")
plt.plot(x,y1,marker = "D",ls = "--",color = "green",label = "week2",alpha=0.5)
plt.legend()
plt.show()

"""
plt.bar(x,y,color=colors)
plt.xlabel("parts of hp",fontsize = 5)
plt.ylabel("popularity",fontsize = 50)
plt.title("popularity of different parts",fontsize = 100)
"""
#Index,Name,Description,Brand,Category,Price,Currency,Stock,EAN,Color,Size,Availability,Internal ID
data = pd.read_csv("products.csv")
df= pd.DataFrame(data)
grouped_by = df.groupby("Category")["Price"].sum()
print(grouped_by)
plt.plot(grouped_by.index,grouped_by.values)
print(df)
plt.show()


