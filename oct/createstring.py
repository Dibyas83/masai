# string
b = "Hello, World!"
print(b[2:5])
b = "Hello, World!"
print(b[:5])



txt = "The best things in life are free!"
print("free" in txt)

txt2 = "The best things in life are free!"
print("expensive" not in txt2)

a = "Hello, World!"
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
print(a.split(","))

q = "Hello"
w = "World"
e = q + " " + w
print(e)

age = 36
#txt = "My name is John, I am " + age
txt22 = "My name is John, I am " + str(age)
print(txt22)

"""
But we can combine strings and numbers by using f-strings or the format() method!

F-Strings
F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and 
add curly brackets {} as placeholders for variables and other operations.

A placeholder can contain variables, operations, functions, and modifiers to format the value
A placeholder can include a modifier to format the value.

A modifier is included by adding a colon : followed by a legal formatting type, like .2f
 which means fixed point number with 2 decimals:

"""

age = 36
txt11 = f"My name is John, I am {age}"
print(txt11)

price = 59
txt14 = f"The price is {price:.2f} dollars"
print(txt14)

txt22 = f"The price is {20 * 59} dollars"
print(txt22)

"""
Escape Character
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash "\ " followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:


"""
# txt = "We are the so-called "Vikings" from the north."
txt = "We are the so-called \"Vikings\" from the north."

"""
String Methods
Python has a set of built-in methods that you can use on strings.

Note: All string methods return new values. They do not change the original string.

Method	Description
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning


The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
"""

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

x = 200
print(isinstance(x, int))

b="dhdfj"
#if b[3] == "f":
  #b[3] = ""
print(b)

s = "apple apple apple"

# Replace "apple" with "orange" only once
s1 = b.replace(b[3], "", 1)

print(s1)


s = "hello world"

# Use a list comprehension to create a new string by joining
# characters that are not 'o' from original string 's'
s = "".join([c for c in s if c != "o"])
print(s)
#-----------------
s = "hello world"

# Initialize an empty string to store modified version of 's'
s1 = ""

# Iterate over each character in string 's'
for c in s:

  # Check if current character is not 'o'
  if c != "o":
    # If it's not 'o', append character to 's1'
    s1 += c

print(s1)

s = "hello world"

# Use filter function with a lambda to create a new string
# by excluding characters that are 'o'
s = "".join(filter(lambda c: c != "o", s))
print(s)
"""
Using slicing
Slicing is typically used to extract parts of a string but we can also use it to exclude a particular letter by slicing around it. This method works best when removing a letter at a known position, such as the first or last occurrence.

For example removing the first occurrence of any letter:
"""
s = "hello world"

# Find index of first occurrence of 'o' in string
idx = s.find("o")

# Check if 'o' was found (index is not -1)
if idx != -1:
  # Create a new string by removing first occurrence of 'o'
  s = s[:idx] + s[idx + 1:]

print(s)





