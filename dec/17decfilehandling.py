
"""


open(_, _) : function to open a file.
"r" - Read - Default value. Opens a file for reading; error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist.
"w" - Write - Opens a file for writing, creates the file if it does not exist.
"x" - Create - Creates the specified file, returns an error if the file exists.
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
read() method for reading the content of the file.
"""
import json

f = open("students.txt","rt")  # rt is default read text
f1 = open("sample.txt","r")
print(f.read())  # willl read first 10 char, will read all content and print
print(f1.readline())  # reads one line at a time
print(f1.readline())  # reads one line at a time
print(f.readline())  # reads one line at a time
f1.close()

x= open("test.txt","r")
for y in x:
    print(y,end="")
# print(x.readline())

x.close()
x = open("test.txt","a")
x.write("\n in time \n")
x.write("\n finished")
x = open("test.txt","r")
print(x.read())
x.close()
a =open("write.txt","r")
print(a.readline())
a = open("write.txt","w")
a.write("deleted")
a = open("write.txt","r")
print(a)
print(a.readline())
a.close()
#  b= open("created.txt","x") # once created  cmd cannot run again
#  b.write("start \n run \n finish \n medal")
#  b.close()
b = open("created.txt","r")
print(b.readline())
print(b.readline())
print(b.readline())

f = open("demo.txt","a") # append mode ,can create new file,text will be added at the end
f1 = open("demo.txt","w") # write mode ,can create new file,text will be added at the beg
f2 = open("demo.txt","w") # create mode , create new file


# serialize the data to a json file
data = {
    "name":"john",
    "age": 34
}
with open("data.json","w") as js:
    json.dump(data,js)


# deserialize the data from the json file
with open("data.json","r") as js:
    ndata = json.load(js)
print(ndata)

import pickle
with open("data.pkl","wb") as pik_file:
    pickle.dump(data,pik_file)


# deserialize the data from the json file
# when we need to store large file or data
with open("data.pkl","rb") as pik_file:
    pdata = pickle.load(pik_file)
print(pdata)






