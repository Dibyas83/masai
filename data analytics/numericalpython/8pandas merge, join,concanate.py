

import pandas as pd
import  numpy as np

df  = pd.read_csv("employees.csv")
print(df,"2csv") # default 5 values


#col transformation
# creating a new col to know if people get bonus or not
df.loc[(df["Bonus %"] == 0),"getsbonus"] = "no bonus"
df.loc[(df["Bonus %"] > 0),"getsbonus"] = " bonus"
print(df.head(10)) # in new getsbonus col it will show bonus or no bonus

df["fullname"] = df["First Name"].str.capitalize() + " " + df["Gender"].str.capitalize()
print(df)
df["Bonus"] = (df["Salary"]/100)*20
print(df)

data = {"months":["january","february","march","april"]}
a = pd.DataFrame(data)
print(a)
data1 = {"empid":["e1","e2","e3","e4","e5","e6"],
         "names":["ram","shyam","rahul","vishal","vicky","akash"],
         "quantity":[11,22,33,44,55,66]}

data2 = {"empid":["e1","e2","e3","e4","e5","e6"],
         "salary":[11111,22222,33333,44444,55555,66666],
         "quantity":[11,22,33,44,55,66]}

data3 = {"empid":["e1","e7","e3","e4","e5","e9"],
         "salary":[11111,22222,33333,44444,55555,66666],
         "months":["january","february","march","april","may","april"]}

data4 = {"empid":["e8","e7","e10","e11","e12","e9"],
         "names":["a","b","c","d","e","f"],
         "age":[1,2,3,4,5,6]}

data22 = {"empid":["e1","e2","e3","e4","e5","e6"],
         "salary":[11888,24444,36000,48888,58888,76666],
         "quantity":[15,25,35,45,56,68]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)
df4 = pd.DataFrame(data4)
df22 = pd.DataFrame(data22)
df23 = df22.copy()
df23.loc[0,"salary"] = 21111
df23.loc[1,"salary"] = 31111
df23.loc[3,"salary"] = 51111

print(df1)
print(df2)
print(pd.merge(df1,df2,on = "empid" ))
print(pd.merge(df1,df3,on = "empid" ))
print(pd.merge(left=df1,right=df3,on = "empid" ,how = "left")) # based on left,default is inner
print(pd.merge(left=df1,right=df3,on = "empid" ,how = "right")) # based on right,default is inner
print(pd.concat([df1,df4]))


# data comparison
print(df2.compare(df22),"comp--------------")
print(df2.compare(df22,keep_shape=False),"f------------")
print(df22.compare(df23))  # will only show the difference and not same things
print(df22.compare(df23,keep_shape=True),"t----------------")  # will  show  same things






