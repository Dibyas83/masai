
"""
- data visualisation is the graphical representation of information and data
-in world of big data ,data visualisation tools are essential to analyze massive amts of information and make data-driven decisions

-differeent types of chart(pychart,scatterplot,heatmap,box plot,)  for diff types of data(int,string)
"""
import  matplotlib.pyplot as plt
import pandas as pd
y = [98,80,85,95,70,100]
x = ["part1","part2","part3","part4","part5","part6"]
colors = ["red","green","yellow","blue","orange","pink"]
plt.bar(x,y,color=colors)
plt.xlabel("parts of hp",fontsize = 5)
plt.ylabel("popularity",fontsize = 50)
plt.title("popularity of different parts",fontsize = 100)
plt.show()

data = pd.read_csv("employees.csv")
df= pd.DataFrame(data)
print(df)
grouped_by = df.groupby("Senior Management")["Salary"].sum()
#plt.bar(df["Senior Management"],df["Salary"])
#plt.bar(df["Team"],df["Salary"])
plt.bar(grouped_by.index,grouped_by.values)
plt.show()


