import functools

try:
    numm = int("hello")
except ValueError:
    print("wrong value")
except Exception: # default for all error
    print("other error")


def check_age(age):
    if age < 0:
        raise ValueError("age cannot be negetive!")
    return f"your age is :{age}"

try:
    print(check_age(-5))
except ValueError as e:
#except ValueError:
    #print("dfg")
    print(e)

file = open("example.txt","r") # r means read mode can open .csv file also
content = file.read() # for reading
print(content)
file.close()

f1 = open("sample.txt","w") # write cancreate file
f1.write("8\n")
f1.write("4\n")
f1.write("hi")
f1.close()
print("---------------------------------------12")

f1 = open("sample.txt","r")

print(f1.read()) # reads all at once
f1.close()
print("---------------------------------------13")
f1 = open("sample.txt","r")
print(f1.readline()) # one line or char ,-1 or () read all ,the default
print(f1.readline()) # gives list as output
print(f1.readline(2))# reads 2 byte or char of data in the firstline
f1.close()


#
with open("demo.txt","r") as f3: # no need of f.close
    for line in f3:  # lin by line
        print(line.strip())


with open("sample.txt","r") as f4:
    for line in f4:  # lin by line
        print(line)
        print(line.strip())

f5 = open("demo.txt","r")
print(f5.readlines(2)) # print n no of lines
print(f5.readlines())
f5.close()
# "a" - append

with open("sample.txt","w") as f6: # write erases previous content
    pass

with open("sample.txt","a") as f4:
    f4.write("i got it\n")

print(f4)
# append adds to the end of content

import os
if os.path.exists("C://Users/a2z/PycharmProjects/masai/dec/sample1.txt"):
    os.remove("sample1.txt")

# pwd in terminal

import csv
with open("rd.csv","r") as f7:
    reader = csv.reader(f7)
    for row in reader:
        print(row)


#  frequency
#  to write csv fie.- csv.writer()  .writerow() to write a list as row

import csv
with open("rw.csv","w",newline='') as f8: # creates a new csv.file
    writer = csv.writer(f8)
    writer.writerow(["Name","Score"])
    writer.writerow(["Alice","90"])
    writer.writerow(["avi","300"])


import json
data = {"name":"Bob","age":25}
with open("gata.json","w") as f9:
    json.dump(data,f9)

import json
with open("gata.json","r") as f9:
    info = json.load(f9)

    print(info["name"])
print("------------------------------5")
#  create
f10  = open("students.txt","w")
f10.write("shiva\nrachna\nguru\n")
f10.close()

#  reade to print
with open("students.txt","r") as f11:
    for line in f11:
        print("Student:",line.strip())


# serialization
"""
-turning a python object into a storable/sharable format,later turn it back into the original object
- keep data after program ends and share structured data easily.
- and cache results to avoid recomputing
"""
#
# deserialization
"""
pickle.load() -rebuilds the object exactly as it was
format is in binary,json in txt format
used for quick save/load  ,json for dataexch
it is serialized file ,json is not
all objects and variables can be stored using pickle,only dict can be stored in python
"""


d = {"id": 1,"course": ["math","art"]}  # first create dictionary
import pickle
with open("bata.pkl","wb") as f12: # b for binary
    pickle.dump(d,f12)


import pickle
with open("bata.pkl","rb") as f13:
    restored = pickle.load(f13)
print(restored["course"])


import os
os.path.exists("C://Users/a2z/PycharmProjects/masai/dec/sample1.txt")
print("yes")

if os.path.exists("sample.txt"):
    print("wert")
    os.remove("sample.txt")
with open("sample.txt","w") as f3:
    f3.write("ty\n")
    f3.write("tu\n")
    f3.write("ta\n")

with open("sample.txt", "r") as f8:  # no need of f.close
    for line in f8:  # lin by line
        print(line.strip())



os.path.exists("C://Users/a2z/PycharmProjects/masai/dec/sample1.txt")
print("yes")

f15 = open("csyes.csv","w") # only , separated values
f15.write("1,2,3\n")
f15.write("4,5,6\n")
f15.write("ww,ert,rty\n")
f15.close()

with open("csyes.csv","r") as f33:
    for line in f33:
        print(line.strip())

import csv
with open("csyes.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open("csyes.csv","w") as f44:
    writer = csv.writer(f44)
    writer.writerow(["nv","dfd"])
    writer.writerow(["ee","ghd"])


with open("csyes.csv","r") as f24:
    reader = csv.reader(f24)
    for row in reader:
        print(row)


import  json
data = {"d":4,"g":9,"score":10,"stud":"deep"}
with open("mjs.json","w") as f52:
    json.dump(data,f52)

# f59 = open("mjs.json", "w")
# f59.write({"gy":8}) # write() argument must be str, not dict

with open("mjs.json","r") as f53:
    info = json.load(f53)
    print(info["d"])

with open("mjs.json","r") as f57:
    print(f57.readlines(3))
    #for line in f57:
        #print("stud",line.strip())

f27 = open("stud.txt","w")
f27.write("shiva\ndiva\nguru\n")
f27.close()

with open("stud.txt","r") as f78:
    for line in f78:
        print("sudent:",line.strip())

d= {"id":1,"courses":["math","art"]}
import pickle

with open("myfil.pkl","wb") as f94:
    pickle.dump(d,f94) # converts dict into json like write

import pickle
with open("myfil.pkl","rb") as f68: # pickle for serialisation
    restored = pickle.load(f68) # like read
    print(restored["courses"])






