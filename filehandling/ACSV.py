

import os
import csv # ou have most likely named this (or some other script of yours) csv.py, so that the
# import csv is reading that instead of the actual module with that name.
fields =["Name","Branch","year","cgpa"]
rows =[["Nikhil","cd","1","9.1"],
        ["sanch","df","2","9.4"]]
filename = "records.csv"
with open(filename,"w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(fields)
        writer.writerow(rows)
with open(filename,"r") as file:
        csvfile = csv.reader(file)
        for lines in csvfile:
                print(lines)























