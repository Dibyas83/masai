

"""
-pandas is a package providing fast,flexible and expressive data structures to make working
with relational or labeled data both easy and intuitive

- it has func for analyzing,cleaning,exploring and manipulating data
- for scientific and mathematical calculation
- also called panel data and python data analysis

applications
-easy handling of missing data
- ssize mutability - col can be inserted and deleted from dataframe and higher dimensional objects

-automatic and explcitdata alignment  means we can create row and col ,and set alignment automatically
 when datas given it auto stores respective row and col

- flexible group by func like pivot table in excel to get data summary and relationships
-intwlligent label-based slicing ,fancy indexing and subsetting of large data sets.

-intuitive merging  and joining data sets
-flexible reshaping and pivoting of data sets- get small data set from big data set
- series is one col with single data type- single dimensional
data frame - series of colmns

panda series is a one dimensional labeled array capable of holding data of any type.axis labels are called index
panda series is nothing but a column in an excel sheet.
supports int and labeled based indexing.

pandas dataframe is two dimensional size mutable ,potentially heterogeneous tabular data structure with
labeled axes(rows and col)
it can be created from csv files,excel,sql data.
using dataframe func we can use data in dictionary,list format
"""

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

def extract(value):
    return value[0:3]

#a["short_mth"] = a["months"].str.a[0:3]
a["short_mth"] = a["months"].map(extract)
print(a)

# group by - to get summary

gp1 = df.groupby("Team").agg({"Gender":"count"})
gp2 = df.groupby(["Team","Gender"]).agg({"Gender":"count"})
gp3 = df.groupby(["Team","Gender"]).agg({"Senior Management":"count"}) # count is func applied,team and gender are subdiviged or grouped  is subdivision
# gp3 = df.groupby(["country"]).agg({"Salary":"mean","age":"min"}) # mean,max,min are func appled,and two rows of mean salary and min age
print(gp1)
print(gp2)
print(gp3)



