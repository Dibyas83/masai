
import pandas as pd
# pivot
dict = {"K":["e1","e2","e1","e2","e1","e2"],
         "N":["ram","shyam","rahul","vishal","vicky","akash"],
         "Q":["red","bl","gf","t","jt","rty"],
        "T":["a","b","c","d","e","f"]}


df8 = pd.DataFrame(dict)
print(df8)
o = df8.pivot(index="K", columns="N", values=["Q","T"])
print(o)

#melting - convert table name to variable
print(pd.melt(df8, id_vars=["K"],value_vars=["T","Q"]))
print(pd.melt(df8, id_vars=["K"],value_vars=["T","Q"],var_name="T&Q",value_name="vals"))

