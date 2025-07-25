
"""
when x and y have numerical values
"""
from itertools import groupby

import  matplotlib.pyplot as plt
import pandas as pd
import  numpy as np

x =  np.random.randint(1,10,10)
y = np.random.randint(10,100,10)
color = np.random.randint(5,20,10)
size = np.random.randint(5,20,10)

#plt.scatter(x,y,marker="*",color = "red")
#plt.scatter(x,y,marker="*",cmap= "hot",c = color)
plt.scatter(x,y,marker="*",cmap= "hot",c = color,s = size )
plt.colorbar()
plt.show()
#Index,Name,Description,Brand,Category,Price,Currency,Stock,EAN,Color,Size,Availability,Internal ID
data = pd.read_csv("products.csv")
df= pd.DataFrame(data)

plt.scatter(df["Category"],df["Name"],s = df["Price"])
plt.show()


