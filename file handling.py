
"""
File Handling in Python
Last Updated : 14 Jan, 2025
File handling refers to the process of performing operations on a file such as creating, opening, reading, writing and closing it, through a programming interface. It involves managing the data flow between the program and the file system on the storage device, ensuring that data is handled safely and efficiently.

Opening a File in Python
To open a file we can use open() function, which requires file path and mode as arguments:




# Open the file and read its contents
with open('geeks.txt', 'r') as file:
This code opens file named geeks.txt.

File Modes in Python
When opening a file, we must specify the mode we want to which specifies what we want to do with the file. Here’s a table of the different modes available:

Mode	Description	Behavior
r	Read-only mode.	Opens the file for reading. File must exist; otherwise, it raises an error.
rb	Read-only in binary mode.	Opens the file for reading binary data. File must exist; otherwise, it raises an error.
r+	Read and write mode.	Opens the file for both reading and writing. File must exist; otherwise, it raises an error.
rb+	Read and write in binary mode.	Opens the file for both reading and writing binary data. File must exist; otherwise, it raises an error.
w	Write mode.	Opens the file for writing. Creates a new file or truncates the existing file.
wb	Write in binary mode.	Opens the file for writing binary data. Creates a new file or truncates the existing file.
w+	Write and read mode.	Opens the file for both writing and reading. Creates a new file or truncates the existing file.
wb+	Write and read in binary mode.	Opens the file for both writing and reading binary data. Creates a new file or truncates the existing file.
a	Append mode.	Opens the file for appending data. Creates a new file if it doesn’t exist.
ab	Append in binary mode.	Opens the file for appending binary data. Creates a new file if it doesn’t exist.
a+	Append and read mode.	Opens the file for appending and reading. Creates a new file if it doesn’t exist.
ab+	Append and read in binary mode.	Opens the file for appending and reading binary data. Creates a new file if it doesn’t exist.
x	Exclusive creation mode.	Creates a new file. Raises an error if the file already exists.
xb	Exclusive creation in binary mode.	Creates a new binary file. Raises an error if the file already exists.
x+	Exclusive creation with read and write mode.	Creates a new file for reading and writing. Raises an error if the file exists.
xb+	Exclusive creation with read and write in binary mode.	Creates a new binary file for reading and writing. Raises an error if the file exists.
Table of Content

Reading a File
Writing to a File
Closing a File
Handling Exceptions When Closing a File
For this article we are using text file with text:

Hello world
GeeksforGeeks
123 456


Reading a File
Reading a file can be achieved by file.read() which reads the entire content of the file. After reading the file we can close the file using file.close() which closes the file after reading it, which is necessary to free up system resources.

Example: Reading a File in Read Mode (r)




file = open("geeks.txt", "r")
content = file.read()
print(content)
file.close()
Output:

Hello world
GeeksforGeeks
123 456
Reading a File in Binary Mode (rb)



file = open("geeks.txt", "rb")
content = file.read()
print(content)
file.close()
Output:

b'Hello world\r\nGeeksforGeeks\r\n123 456'
Writing to a File
Writing to a file is done using file.write() which writes the specified string to the file. If the file exists, its content is erased. If it doesn’t exist, a new file is created.

Example: Writing to a File in Write Mode (w)



file = open("geeks.txt", "w")
file.write("Hello, World!")
file.close()
Writing to a File in Append Mode (a)
It is done using file.write() which adds the specified string to the end of the file without erasing its existing content.

Example: For this example, we will use the Python file created in the previous example.




# Python code to illustrate append() mode
file = open('geek.txt', 'a')
file.write("This will add this line")
file.close()
Closing a File
Closing a file is essential to ensure that all resources used by the file are properly released. file.close() method closes the file and ensures that any changes made to the file are saved.




file = open("geeks.txt", "r")
# Perform file operations
file.close()
Using with Statement
with statement is used for resource management. It ensures that file is properly closed after its suite finishes, even if an exception is raised. with open() as method automatically handles closing the file once the block of code is exited, even if an error occurs. This reduces the risk of file corruption and resource leakage.




with open("geeks.txt", "r") as file:
    content = file.read()
    print(content)
Output:

Hello, World!
Appended text.
Handling Exceptions When Closing a File
It’s important to handle exceptions to ensure that files are closed properly, even if an error occurs during file operations.




try:
    file = open("geeks.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()
Output:

Hello, World!
Appended text.
Advantages of File Handling in Python
Versatility : File handling in Python allows us to perform a wide range of operations, such as creating, reading, writing, appending, renaming and deleting files.
Flexibility : File handling in Python is highly flexible, as it allows us to work with different file types (e.g. text files, binary files, CSV files , etc.) and to perform different operations on files (e.g. read, write, append, etc.).
User – friendly : Python provides a user-friendly interface for file handling, making it easy to create, read and manipulate files.
Cross-platform : Python file-handling functions work across different platforms (e.g. Windows, Mac, Linux), allowing for seamless integration and compatibility.
Disadvantages of File Handling in Python
Error-prone: File handling operations in Python can be prone to errors, especially if the code is not carefully written or if there are issues with the file system (e.g. file permissions, file locks, etc.).
Security risks : File handling in Python can also pose security risks, especially if the program accepts user input that can be used to access or modify sensitive files on the system.
Complexity : File handling in Python can be complex, especially when working with more advanced file formats or operations. Careful attention must be paid to the code to ensure that files are handled properly and securely.
Performance : File handling operations in Python can be slower than other programming languages, especially when dealing with large files or performing complex operations.


"""

"""
file reading
How to Read from a File in Python
Last Updated : 13 Mar, 2025
Reading from a file in Python means accessing and retrieving the contents of a file, whether it be text, binary data or a specific data format like CSV or JSON. Python provides built-in functions and methods for reading a file in python efficiently.

Example File: geeks.txt

Hello World 
Hello GeeksforGeeks


Basic File Reading in Python
Basic file reading involves opening a file, reading its contents, and closing it properly to free up system resources.

Steps:

Open the file: open(“filename”, “mode”) opens the file in a specified mode (e.g., read mode “r”).
Read content: Using read(), readline() or readlines() methods.
Close the file: close() ensures system resources are released.
Example: Reading the Entire File


# Open the file in read mode
file = open("geeks.txt", "r")

# Read the entire content of the file
content = file.read()

print(content)

# Close the file
file.close()
Output:

Hello World
Hello GeeksforGeeks
Explanation: This code opens geeks.txt in read mode, reads all its content into a string, prints it and then closes the file to free resources.

Best Practice: Using with statement
Using with open(…) ensures the file is automatically closed.


with open("geeks.txt", "r") as file:
    content = file.read()
    print(content)
Hello World 
Hello GeeksforGeeks
Explanation: This code ensures that the file is automatically closed once the block is exited, preventing resource leaks.

Table of Content

Reading a File Line by Line
Reading Binary Files in Python
Reading Specific Parts of a File
Reading CSV Files in Python
Reading JSON Files in Python
Reading a File Line by Line
We may want to read a file line by line, especially for large files where reading the entire content at once is not practical. It is done with following two methods:

for line in file: Iterates over each line in the file.
line.strip(): Removes any leading or trailing whitespace, including newline characters.
Example 1: Using a Loop to Read Line by Line




# Open the file in read mode
file = open("geeks.txt", "r")

# Read each line one by one
for line in file:
    print(line.strip())  # .strip() to remove newline characters

# Close the file
file.close()
Output:

Hello World
Hello GeeksforGeeks
Explanation: This method reads each line of the file one at a time and prints it after removing leading/trailing whitespace.

Example 2: Using readline()

file.readline() reads one line at a time. while line continues until there are no more lines to read.


# Open the file in read mode
file = open("geeks.txt", "r")

# Read the first line
line = file.readline()

while line:
    print(line.strip())
    line = file.readline()  # Read the next line

# Close the file
file.close()
Output:

Hello World
Hello GeeksforGeeks
Explanation: This method reads a single line at a time using readline(), which is useful when processing files in chunks.

Reading Binary Files in Python
Binary files store data in a format not meant to be read as text. These can include images, executables or any non-text data. We are using following methods to read binary files:

open(“example.bin”, “rb”): Opens the file example.bin in read binary mode.
file.read(): Reads the entire content of the file as bytes.
file.close(): Closes the file to free up system resources.
Example: Reading a Binary File


# Open the binary file in read binary mode
file = open("geeks.txt", "rb")

# Read the entire content of the file
content = file.read()

# Print the content (this will be in bytes)
print(content)

# Close the file
file.close()
Output:

b'Hello World\r\nHello GeeksforGeeks'
Explanation: This code reads a file in binary mode (“rb”) and prints its content as bytes, which is necessary for handling non-text files.

Reading Specific Parts of a File
Sometimes, we may only need to read a specific part of a file, such as the first few bytes, a specific line, or a range of lines. Example: Reading the First N Bytes


# Open the file in read mode
file = open("geeks.txt", "r")

# Read the first 10 bytes
content = file.read(10)

print(content)

# Close the file
file.close()
Output:

Hello World
Explanation: This code reads only the first 10 characters of the file, useful for previewing file contents.

Reading CSV Files in Python
Reading CSV (Comma-Separated Values) files are a common task for working with tabular data. Python’s csv module makes it easy to read CSV files. Example:


import csv

# Open the CSV file
with open("example.csv", newline='') as csvfile:
   
    # Create a CSV reader object
    csvreader = csv.reader(csvfile)
    
    # Read and print each row
    for row in csvreader:
        print(row)
Output:

['2014', 'Level 3', 'CC71', 'Primary Metal and Metal Product Manufacturing', 'Dollars', 'H34', 'Total income per employee count', 'Financial ratios', '769,400', 'ANZSIC06 groups C211, C212, C213 and C214']
['2014', 'Level 3', 'CC71', 'Primary Metal and Metal Product Manufacturing', 'Dollars', 'H35', 'Surplus per employee count', 'Financial ratios', '48,000', 'ANZSIC06 groups C211, C212, C213 and C214']
['2014', 'Level 3', 'CC71', 'Primary Metal and Metal Product Manufacturing', 'Percentage', 'H36', 'Current ratio', 'Financial ratios', 'C', 'ANZSIC06 groups C211, C212, C213 and C214']
['2014', 'Level 3', 'CC71', 'Primary Metal and Metal Product Manufacturing', 'Percentage', 'H37', 'Quick ratio', 'Financial ratios', 'C', 'ANZSIC06 groups C211, C212, C213 and C214']
['2014', 'Level 3', 'CC71', 'Primary Metal and Metal Product Manufacturing', 'Percentage', 'H38', 'Margin on sales of goods for resale', 'Financial ratios', '12', 'ANZSIC06 groups C211, C212, C213 and C214']
['2014', 'Level 3', 'CC71', 'Primary Metal and Metal Product Manufacturing', 'Percentage', 'H39', 'Return on equity', 'Financial ratios', '19', 'ANZSIC06 groups C211, C212, C213 and C214']
Explanation: This code reads a CSV file line by line, parsing it into a list of values for each row.

Reading JSON Files in Python
Reading JSON (JavaScript Object Notation) files are widely used for data interchange. Python’s json module provides methods to read JSON files. Example:


import json

# Open the JSON file
with open("sample1.json", "r") as jsonfile:
    
    # Load the JSON data
    data = json.load(jsonfile)
    print(data)
Output:

{'fruit': 'Apple', 'size': 'Large', 'color': 'Red'}
Explanation: This code reads a JSON file and loads its content into a Python dictionary, which can be used for further processing.


"""

"""
Reading and Writing to text files in Python
Last Updated : 02 Jan, 2025
Python provides built-in functions for creating, writing, and reading files. Two types of files can be handled in Python, normal text files and binary files (written in binary language, 0s, and 1s).

Text files: In this type of file, Each line of text is terminated with a special character called EOL (End of Line), which is the new line character (‘\n’) in Python by default.
Binary files: In this type of file, there is no terminator for a line, and the data is stored after converting it into machine-understandable binary language.
This article will focus on opening, closing, reading, and writing data in a text file. Here, we will also see how to get Python output in a text file.

Table of Content

Opening a Text File
Read Text File
Write to Text File
Appending to a File
Closing a Text File
Opening a Text File in Python
It is done using the open() function. No module is required to be imported for this function.

File_object = open(r"File_Name","Access_Mode")
Example: Here, file1 is created as an object for MyFile1 and file2 as object for MyFile2.


# Open function to open the file "MyFile1.txt"
# (same directory) in append mode and
file1 = open("MyFile1.txt","a")

# store its reference in the variable file1
# and "MyFile2.txt" in D:\Text in file2
file2 = open(r"D:\Text\MyFile2.txt","w+")
Also Read: File Mode in Python

Python Read Text File
There are three ways to read txt file in Python:

Using read()
Using readline()
Using readlines()
Reading From a File Using read()

read(): Returns the read bytes in form of a string. Reads n bytes, if no n specified, reads the entire file.

File_object.read([n])
Reading a Text File Using readline()

readline(): Reads a line of the file and returns in form of a string.For specified n, reads at most n bytes. However, does not reads more than one line, even if n exceeds the length of the line.

File_object.readline([n])
Reading a File Using readlines()

readlines(): Reads all the lines and return them as each line a string element in a list.

  File_object.readlines()
Note: ‘\n’ is treated as a special character of two bytes.

In this example, a file named “myfile.txt” is created and opened in write mode ( "w" ). Data is written to the file using write and writelines methods. The file is then reopened in read and append mode ( "r+" ). Various read operations, including read , readline , readlines , and the use of seek , demonstrate different ways to retrieve data from the file. Finally, the file is closed.


file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# \n is placed to indicate EOL (End of Line)
file1.write("Hello \n")
file1.writelines(L)
file1.close()  # to change file access modes

file1 = open("myfile.txt", "r+")

print("Output of Read function is ")
print(file1.read())
print()

# seek(n) takes the file handle to the nth
# byte from the beginning.
file1.seek(0)

print("Output of Readline function is ")
print(file1.readline())
print()

file1.seek(0)

# To show difference between read and readline
print("Output of Read(9) function is ")
print(file1.read(9))
print()

file1.seek(0)

print("Output of Readline(9) function is ")
print(file1.readline(9))

file1.seek(0)
# readlines function
print("Output of Readlines function is ")
print(file1.readlines())
print()
file1.close()
Output:

Output of Read function is 
Hello 
This is Delhi 
This is Paris 
This is London 
Output of Readline function is 
Hello 
Output of Read(9) function is 
Hello 
Th
Output of Readline(9) function is 
Hello 
Output of Readlines function is 
['Hello \n', 'This is Delhi \n', 'This is Paris \n', 'This is London \n']
Write to Text File in Python
There are two ways to write in a file:

Using write()
Using writelines()
Reference: write() VS writelines()

Writing to a Python Text File Using write()
write(): Inserts the string str1 in a single line in the text file.

File_object.write(str1)

file = open("Employees.txt", "w") 

for i in range(3): 
name = input("Enter the name of the employee: ") 
file.write(name) 
file.write("\n") 
	
file.close() 

print("Data is written into the file.") 
Output:

Data is written into the file.
Writing to a Text File Using writelines()
writelines(): For a list of string elements, each string is inserted in the text file.Used to insert multiple strings at a single time.

File_object.writelines(L) for L = [str1, str2, str3]

file1 = open("Employees.txt", "w") 
lst = [] 
for i in range(3): 
	name = input("Enter the name of the employee: ") 
	lst.append(name + '\n') 
	
file1.writelines(lst) 
file1.close() 
print("Data is written into the file.") 
Output:

Data is written into the file.
Appending to a File in Python
In this example, a file named “myfile.txt” is initially opened in write mode ( "w" ) to write lines of text. The file is then reopened in append mode ( "a" ), and “Today” is added to the existing content. The output after appending is displayed using readlines . Subsequently, the file is reopened in write mode, overwriting the content with “Tomorrow”. The final output after writing is displayed using readlines.


file1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
file1.writelines(L)
file1.close()

# Append-adds at last
file1 = open("myfile.txt", "a")  # append mode
file1.write("Today \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(file1.readlines())
print()
file1.close()

# Write-Overwrites
file1 = open("myfile.txt", "w")  # write mode
file1.write("Tomorrow \n")
file1.close()

file1 = open("myfile.txt", "r")
print("Output of Readlines after writing")
print(file1.readlines())
print()
file1.close()
Output:

Output of Readlines after appending
['This is Delhi \n', 'This is Paris \n', 'This is London \n', 'Today \n']
Output of Readlines after writing
['Tomorrow \n']
Related Article: File Objects in Python

Closing a Text File in Python
Python close() function closes the file and frees the memory space acquired by that file. It is used at the time when the file is no longer needed or if it is to be opened in a different file mode. File_object.close()


# Opening and Closing a file "MyFile.txt"
# for object name file1.
file1 = open("MyFile.txt","a")
file1.close()

"""

"""
Writing to file in Python
Last Updated : 19 Dec, 2024
Writing to a file in Python means saving data generated by your program into a file on your system. This article will cover the how to write to files in Python in detail.

Creating a File
Creating a file is the first step before writing data to it. In Python, we can create a file using the following three modes:

Write (“w”) Mode: This mode creates a new file if it doesn’t exist. If the file already exists, it truncates the file (i.e., deletes the existing content) and starts fresh.
Append (“a”) Mode: This mode creates a new file if it doesn’t exist. If the file exists, it appends new content at the end without modifying the existing data.
Exclusive Creation (“x”) Mode: This mode creates a new file only if it doesn’t already exist. If the file already exists, it raises a FileExistsError.
Example:




# Write mode: Creates a new file or truncates an existing file

with open("file.txt", "w") as f:
    f.write("Created using write mode.")

f = open("file.txt","r")
print(f.read())

# Append mode: Creates a new file or appends to an existing file

with open("file.txt", "a") as f:
    f.write("Content appended to the file.")

f = open("file.txt","r")
print(f.read())

# Exclusive creation mode: Creates a new file, raises error if file exists

try:
    with open("file.txt", "x") as f:
        f.write("Created using exclusive mode.")
except FileExistsError:
    print("Already exists.")

Output
Created using write mode.
Created using write mode.Content appended to the file.
Already exists.
Writing to an Existing File
If we want to modify or add new content to an already existing file, we can use two methodes:

write mode (“w”): This will overwrite any existing content,

writelines(): Allows us to write a list of string to the file in a single call.

Example:




# Writing to an existing file (content will be overwritten)
with open("file1.txt", "w") as f:
    f.write("Written to the file.")
    
f = open("file1.txt","r")
print(f.read())

# Writing multiple lines to an existing file using writelines()
s = ["First line of text.\n", "Second line of text.\n", "Third line of text.\n"]

with open("file1.txt", "w") as f:
    f.writelines(s)
    
f = open("file1.txt","r")
print(f.read())

Output
Written to the file.
First line of text.
Second line of text.
Third line of text.
Explanation:

open(“example.txt”, “w”): Opens the file example.txt in write mode. If the file exists, its content will be erased and replaced with the new data.
file.write(“Written to the file.”): Writes the new content into the file.
file.writelines(lines): This method takes a list of strings and writes them to the file. Unlike write() which writes a single string writelines() writes each element in the list one after the other. It does not automatically add newline characters between lines, so the \n needs to be included in the strings to ensure proper line breaks.
Writing to a Binary File
When dealing with non-text data (e.g., images, audio, or other binary data), Python allows you to write to a file in binary mode. Binary data is not encoded as text, and using binary write mode ("wb") ensures that the file content is handled as raw bytes.

Example:




# Writing binary data to a file
bin = b'\x00\x01\x02\x03\x04'

with open("file.bin", "wb") as f:
    f.write(bin)

f = open("file.bin","r")
print(f.read())

Output

Explanation:

bin= b’\x00\x01\x02\x03\x04′: The b before the string indicates that this is binary data. Each pair represents a byte value.
open(“file.bin”, “wb”): Opens the file file.bin in binary write mode. If the file doesn’t exist, Python will create it.
file.write(bin): Writes the binary data to the file as raw bytes.

"""

"""

Reading and Writing CSV Files in Python
Last Updated : 20 Mar, 2025
CSV (Comma Separated Values) format is one of the most widely used formats for storing and exchanging structured data between different applications, including databases and spreadsheets. CSV files store tabular data, where each data field is separated by a delimiter, typically a comma. Python provides built-in support for handling CSV files through the csv module, making it easy to read, write and manipulate CSV data efficiently.

However, we first need to import the module using:

import csv


Reading a CSV File in Python
To read a CSV file, Python provides the csv.reader class, which reads data in a structured format. The first step involves opening the CSV file using the open() function in read mode (‘r’). The csv.reader() function then reads the file, returning an iterable reader object.

Example CSV File: Giants.csv

csv
.CSV file

Syntax:
csv.reader(csvfile, dialect=’excel’, **fmtparams)


Parameters:
csvfile: The file object containing CSV data.
dialect: Defines a set of parameters to control CSV reading (default is ‘excel’).
**fmtparams: Additional formatting parameters like delimiter, quotechar, etc.
Example:




import csv

# Opening the CSV file
with open('Giants.csv', mode='r') as file:
    # Reading the CSV file
    csvFile = csv.reader(file)
    
    # Skipping the header (uncomment if needed)
    # next(csvFile)  

    # Displaying the contents of the CSV file
    for line in csvFile:
        print(line)
Output

['Steve', 13, 'A']
['John', 14, 'F']
['Nancy', 14, 'C']
['Ravi', 13, 'B']
Explanation: The csv module reads Giants.csv using csv.reader(file), iterating row by row. The with statement ensures proper file closure. Each row is returned as a list of column values. Use next(csvFile) to skip the header.

Writing to a csv file in python
Python provides the csv.writer class to write data to a CSV file. It converts user data into delimited strings before writing them to a file. While opening the file, using newline=” prevents unnecessary newlines when writing.

Syntax:
csv.writer(csvfile, dialect=’excel’, **fmtparams)


Parameters:
csvfile: The file object where CSV data will be written.
dialect: Defines a set of parameters to control CSV writing (default is ‘excel’).
**fmtparams: Additional formatting options such as delimiter, quotechar,etc.
Writing a single row:
writerow(fields)


Writing multiple rows:
writerows(rows)


Example:


import csv

# Field names
f = ['Name', 'Branch', 'Year', 'CGPA']

# Data rows of CSV file
r = [
    ['Nikhil', 'COE', '2', '9.0'],
    ['Sanchit', 'COE', '2', '9.1'],
    ['Aditya', 'IT', '2', '9.3'],
    ['Sagar', 'SE', '1', '9.5'],
    ['Prateek', 'MCE', '3', '7.8'],
    ['Sahil', 'EP', '2', '9.1']
]

# Name of the CSV file
fn = "university_records.csv"

# Writing to CSV file
with open(fn, 'w', newline='') as csvfile:
    # Creating a CSV writer object
    csvwriter = csv.writer(csvfile)
    
    # Writing the field names
    csvwriter.writerow(f)
    
    # Writing the data rows
    csvwriter.writerows(r)
Output: A file named university_records.csv will be created containing the following data.

Output1000
Output

Explanation: This example shows how to write a list of dictionaries to a CSV file using csv.DictWriter. Each dictionary is a student record, with fieldnames as column headers. The file is opened in write mode (‘w’), writeheader() writes headers and writerows(d) writes records.

Writing a dictionary to a csv file
The csv.DictWriter class allows writing a dictionary to a CSV file. It maps dictionary keys to field names.

Syntax:
csv.DictWriter(csvfile, fieldnames, restval=”, extrasaction=’raise’, dialect=’excel’, *args, **kwds)


Parameters:
csvfile: The file object where CSV data will be written.
fieldnames: A list of column headers that correspond to dictionary keys.
restval: Default value for missing dictionary keys.
extrasaction: Defines how to handle extra keys (‘raise’ or ‘ignore’).
dialect: Defines a set of parameters to control CSV writing (default is ‘excel’).
Methods:
writeheader(): Writes column headers using the field names.
writerows(mydict): Writes multiple dictionary rows.
Example: A file named university_records.csv will be created containing the following data.




import csv

# Data rows as dictionary objects
d = [
    {'name': 'Nikhil', 'branch': 'COE', 'year': '2', 'cgpa': '9.0'},
    {'name': 'Sanchit', 'branch': 'COE', 'year': '2', 'cgpa': '9.1'},
    {'name': 'Aditya', 'branch': 'IT', 'year': '2', 'cgpa': '9.3'},
    {'name': 'Sagar', 'branch': 'SE', 'year': '1', 'cgpa': '9.5'},
    {'name': 'Prateek', 'branch': 'MCE', 'year': '3', 'cgpa': '7.8'},
    {'name': 'Sahil', 'branch': 'EP', 'year': '2', 'cgpa': '9.1'}
]

# Field names
f = ['Name', 'Branch', 'Year', 'CGPA']

# Name of the CSV file
fn = "university_records.csv"

# Writing to CSV file
with open(fn, 'w', newline='') as csvfile:
    # Creating a CSV DictWriter object
    writer = csv.DictWriter(csvfile, fieldnames=f)
    
    # Writing headers (field names)
    writer.writeheader()
    
    # Writing data rows
    writer.writerows(d)
Output

Output1000
Output

Explanation: This example demonstrates writing a list of student records to a CSV file using csv.DictWriter. The file is opened in write mode (‘w’), fieldnames define column headers, writeheader() writes them and writerows(d) adds records. Keys must match fieldnames to ensure alignment.
"""

"""
Reading and Writing JSON to a File in Python
Last Updated : 19 Jul, 2022
The full form of JSON is Javascript Object Notation. It means that a script (executable) file which is made of text in a programming language, is used to store and transfer the data. Python supports JSON through a built-in package called JSON. To use this feature, we import the JSON package in Python script. The text in JSON is done through quoted-string which contains the value in key-value mapping within { }. It is similar to the dictionary in Python.

Writing JSON to a file in Python
Serializing JSON refers to the transformation of data into a series of bytes (hence serial) to be stored or transmitted across a network. To handle the data flow in a file, the JSON library in Python uses dump() or dumps() function to convert the Python objects into their respective JSON object, so it makes it easy to write data to files. See the following table given below.

PYTHON OBJECT	JSON OBJECT
Dict	object
list, tuple	array
str	string
int, long, float	numbers
True	true
False	false
None	null
Method 1: Writing JSON to a file in Python using json.dumps() 
The JSON package in Python has a function called json.dumps() that helps in converting a dictionary to a JSON object. It takes two parameters:

dictionary – the name of a dictionary which should be converted to a JSON object.
indent – defines the number of units for indentation
After converting the dictionary to a JSON object, simply write it to a file using the “write” function.




import json
 
# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}
 
# Serializing json
json_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
Output: 


 

Method 2: Writing JSON to a file in Python using json.dump() 
Another way of writing JSON to a file is by using json.dump() method The JSON package has the “dump” function which directly writes the dictionary to a file in the form of JSON, without needing to convert it into an actual JSON object. It takes 2 parameters:

dictionary – the name of a dictionary which should be converted to a JSON object.
file pointer – pointer of the file opened in write or append mode.



# Python program to write JSON
# to a file
 
 
import json
 
# Data to be written
dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}
 
with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)
Output: 


 

Reading JSON from a file using Python
Deserialization is the opposite of Serialization, i.e. conversion of JSON objects into their respective Python objects. The load() method is used for it. If you have used JSON data from another program or obtained it as a string format of JSON, then it can easily be deserialized with load(), which is usually used to load from a string, otherwise, the root object is in a list or Dict. 

Reading JSON from a file using  json.load() 
The JSON package has json.load() function that loads the JSON content from a JSON file into a dictionary. It takes one parameter:

File pointer: A file pointer that points to a JSON file.



import json
 
# Opening JSON file
with open('sample.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)
 
print(json_object)
print(type(json_object))
Output: 


 


"""
"""
Take input from user and store in .txt file in Python
Last Updated : 26 Apr, 2025
In this article, we will see how to take input from users and store it in a .txt file in Python. To do this we will use python open() function to open any file and store data in the file, we put all the code in Python try-except block. Let’s see the implementation below.

Stepwise Implementation 
Step 1: First, we will take the data from the user and store it in a temporary variable ‘temp’.

Step 2: We will open the file with the file name using the Python open() function with the write mode enabled.

Note: If the file doesn’t exist it will automatically create the file for us.

# this means the file will open
# with write mode enabled
x = open(gfg.txt,w)
Step 3: Now we will write the data into the file we just created.

x.write(temp)
Step 4: Finally, we will keep the file operations under a try-except block to check for exceptions.

Example 1:
 
temp = input("Please enter your information!!   ") 
try: 
    with open('gfg.txt', 'w') as gfg: 
        gfg.write(temp) 
except Exception as e: 
    print("There is a Problem", str(e)) 
Output:


 


gfg.txt

Example 2:
 
temp = input("Please enter your information!!   ") 
try: 
    with open('gfg.txt', 'w') as gfg: 
        gfg.write(temp) 
except Exception as e: 
    print("There is a Problem", str(e)) 
Output:


input text



"""












