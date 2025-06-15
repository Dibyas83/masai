
#The String to Reverse
txt = "Hello World" [::-1]
print(txt)
#Create a slice that starts at the end of the string, and moves backwards.

#In this particular example, the slice statement [::-1] means start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backwards

#-------------------
#Create a function that takes a String as an argument.Slice the string starting at the end of the string and move backwards
def my_function(x):
  return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)

s = "GeeksforGeeks"
rev = ''.join(reversed(s))
print(rev)
print("------------------------")
s = "GeeksforGeeks"

# Initialize an empty string to hold reversed result
rev = ""

# Loop through each character in original string
for ch in s:
  # Add current character to front of reversed string
  rev = ch + rev #  check rev + ch

print(rev)

"""
Using list comprehension and join()
A more creative approach involves using list comprehension to reverse the string by iterating through
 its indices. This approach is useful when we need more control during iteration like above approach (for loop).

"""


s = "GeeksforGeeks"
rev = ''.join([s[i] for i in range(len(s) - 1, -1, -1)])
print(rev)

"""
Python String Methods
Last Updated : 02 Jan, 2025
Python string methods is a collection of in-built Python functions that operates on strings.

Note: Every string method in Python does not change the original string instead returns a new string with the changed attributes. 


Python string is a sequence of Unicode characters that is enclosed in quotation marks. In this article, we will discuss the in-built string functions i.e. the functions provided by Python to operate on strings.

Case Changing of Python String Methods
The below Python functions are used to change the case of the strings. Let’s look at some Python string methods with examples:

lower(): Converts all uppercase characters in a string into lowercase
upper(): Converts all lowercase characters in a string into uppercase
title(): Convert string to title case
swapcase(): Swap the cases of all characters in a string
capitalize(): Convert the first character of a string to uppercase
Example: Changing the case of Python String Methods




# Python3 program to show the
# working of upper() function
text = 'geeKs For geEkS'

# upper() function to convert
# string to upper case
print("\nConverted String:")
print(text.upper())

# lower() function to convert
# string to lower case
print("\nConverted String:")
print(text.lower())

# converts the first character to 
# upper case and rest to lower case 
print("\nConverted String:")
print(text.title())

# swaps the case of all characters in the string
# upper case character to lowercase and viceversa
print("\nConverted String:")
print(text.swapcase())

# convert the first character of a string to uppercase
print("\nConverted String:")
print(text.capitalize())

# original string never changes
print("\nOriginal String")
print(text)

Output
Converted String:
GEEKS FOR GEEKS

Converted String:
geeks for geeks

Converted String:
Geeks For Geeks

Converted String:
GEEkS fOR GEeKs

Original String
geeKs For geEkS
Time complexity: O(n) where n is the length of the string ‘text’
Auxiliary space: O(1)

List of String Methods in Python
Here is the list of in-built Python string methods, that you can use to perform actions on string:

Function Name 	Description
capitalize()	Converts the first character of the string to a capital (uppercase) letter
casefold()	Implements caseless string matching
center()	Pad the string with the specified character.
count()	Returns the number of occurrences of a substring in the string.
encode()	Encodes strings with the specified encoded scheme
endswith()	Returns “True” if a string ends with the given suffix
expandtabs()	Specifies the amount of space to be substituted with the “\t” symbol in the string
find()	Returns the lowest index of the substring if it is found
format()	Formats the string for printing it to console
format_map()	Formats specified values in a string using a dictionary
index()	Returns the position of the first occurrence of a substring in a string
isalnum()	Checks whether all the characters in a given string is alphanumeric or not
isalpha()	Returns “True” if all characters in the string are alphabets
isdecimal()	Returns true if all characters in a string are decimal
isdigit()	Returns “True” if all characters in the string are digits
isidentifier()	Check whether a string is a valid identifier or not
islower()	Checks if all characters in the string are lowercase
isnumeric()	Returns “True” if all characters in the string are numeric characters
isprintable()	Returns “True” if all characters in the string are printable or the string is empty
isspace()	Returns “True” if all characters in the string are whitespace characters
istitle()	Returns “True” if the string is a title cased string
isupper()	Checks if all characters in the string are uppercase
join()	Returns a concatenated String
ljust()	Left aligns the string according to the width specified
lower()	Converts all uppercase characters in a string into lowercase
lstrip()	Returns the string with leading characters removed
maketrans()	 Returns a translation table
partition()	Splits the string at the first occurrence of the separator 
replace()	Replaces all occurrences of a substring with another substring
rfind()	Returns the highest index of the substring
rindex()	Returns the highest index of the substring inside the string
rjust()	Right aligns the string according to the width specified
rpartition()	Split the given string into three parts
rsplit()	Split the string from the right by the specified separator
rstrip()	Removes trailing characters
splitlines()	Split the lines at line boundaries
startswith()	Returns “True” if a string starts with the given prefix
strip()	Returns the string with both leading and trailing characters
swapcase()	Converts all uppercase characters to lowercase and vice versa
title()	Convert string to title case
translate()	Modify string according to given translation mappings
upper()	Converts all lowercase characters in a string into uppercase
zfill()	Returns a copy of the string with ‘0’ characters padded to the left side of the string
Note: For more information about Python Strings, refer to Python String Tutorial.





Comment

More info

Campus Training Program
"""

"""
Python Program to Replace all Occurrences of ‘a’ with $ in a String
Last Updated : 18 Apr, 2023
Given a string, the task is to write a Python program to replace all occurrence of ‘a’ with $.

Examples:

Input: Ali has all aces
Output: $li h$s $ll $ces

Input: All Exams are over
Output: $ll Ex$ms $re Over
Method 1:  uses splitting of the given specified string into a set of characters. An empty string variable is used to store modified string . We loop over the character array and check if the character at this index is equivalent to ‘a’ , and then append ‘$’ sign, in case the condition is satisfied. Otherwise, the original character is copied into the new string.  




# declaring a string variable
str = "Amdani athani kharcha rupaiya."
 
# declaring an empty string variable for storing modified string
modified_str = ''
 
# iterating over the string
for char in range(0, len(str)):
    # checking if the character at char index is equivalent to 'a'
    if(str[char] == 'a' or str[char] == 'a'.upper()):
        # append $ to modified string
        modified_str += '$'
    else:
        # append original string character
        modified_str += str[char]
 
print("Modified string : ")
print(modified_str)
Output:

Modified string :
$md$ni $th$ni kh$rch$ rup$iy$.
Time Complexity: O(n), where n is length of str string.

Auxiliary Space: O(n), where n is length of modified_str string to store result.

Method 2: uses the inbuilt method replace() to replace all the occurrences of a particular character in the string with the new specified character. The method has the following syntax : 

replace( oldchar , newchar)
This method doesn’t change the original string, and the result has to be explicitly stored in the String variable. 




# declaring a string variable
str = "An apple A day keeps doctor Away."
 
# replacing character a with $ sign
str = str.replace('a', '$')
str = str.replace('a'.upper(),'$')
print("Modified string : ")
print(str)
Output
Modified string : 
$n $pple $ d$y keeps doctor $w$y.
Time Complexity: O(n)
Auxiliary Space: O(n)

Method 3: Using Python re module


The re.sub() function from the re module is used to replace all occurrences of a particular pattern in a string with a specified replacement. In this case, we are using the pattern ‘a’ and the replacement ‘$’ to replace all occurrences of ‘a’ in the string str. The result of the re.sub() function is stored in the variable modified_str.
 





import re
 
#declaring a string variable
str = "Amdani athani kharcha rupaiya."
 
#using re.sub() function to replace all occurrences of 'a' with '$'
modified_str = re.sub("a", "$", str.lower())
 
#print("Modified string : ")
print(modified_str)
Output
$md$ni $th$ni kh$rch$ rup$iy$.
Time Complexity: O(n)
Auxiliary Space: O(n)

Method 4: Using list comprehension:


This approach uses a list comprehension to iterate over each character in the lowercase version of the input string str. If the character is equal to ‘a’, it is replaced with a ‘$’ symbol. Otherwise, the original character is used. The resulting list of characters is then joined back into a string using the join() method.





# declaring a string variable
str = "Amdani athani kharcha rupaiya."
 
# using list comprehension to replace all occurrences of 'a' with '$'
modified_str = ''.join(['$' if c == 'a' else c for c in str.lower()])
 
# print modified string
print(modified_str)

"""

a = "Stt.Uiyhu.jho.kp.lmn.kk"
b = a.split(".")
print(b)
c = sorted(a)
print(c)
rep = a.replace("i","a")
print(rep)
stop = a.replace("."," ")
print(stop)
ct = a.count("kk")
print(ct)
revs=a[::-1]
print(revs)
sp=a.split(".")
revjoi=" ".join(sp[::-1])
re=sp[::-1]
print(re)
print(revjoi)
p = input()
pr= p.isdigit()
pri = p.isnumeric()
if pr == True:
  print("it contains only digits")
if pri == True:
  print("nume")
#-------------------------------
cnt = 0
v = "aeiou"
for i in a:
  if i in v:
    cnt += 1
print(cnt,"vowels")
print(a.istitle())
m = "Dy Dy"
m2 = "Dy DY"

print(m.istitle())
print(m2.istitle())











