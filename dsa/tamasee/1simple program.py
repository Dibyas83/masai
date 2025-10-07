
# goodrich

print( 'Welcome to the GPA calculator' )
print( 'Please enter all your letter grades, one per line.' )
print( 'Enter a blank line to designate the end.' )
# map from letter grade to point value
points = { 'A+' :4.0, 'A' :4.0, 'A-' :3.67, 'B+' :3.33, 'B' :3.0, 'B-' :2.67,
'C+' :2.33, 'C' :2.0, 'C-' :1.67, 'D+' :1.33, 'D' :1.0, 'F' :0.0}

num_courses = 0
tot_points = 0
done = False
while not done:
    grade = input()

    if grade == '':
        done = True
    elif grade not in points:
        print("unknown grade '{0}' being ignored".format(grade))
    else:
        num_courses +=1
        tot_points += points[grade]
if num_courses > 0:
    print('your gpa is {0:.3}'.format(tot_points/num_courses))
"""
The .format() method in Python is used for string formatting. It allows you to insert values into a string at specific positions using placeholders. Here's how it works:
Basic Usage
Placeholders:
Use curly braces {} as placeholders within the string where you want to insert values.
.format() method:
Call the .format() method on the string and pass the values you want to insert as arguments.
Order of values:
The values are inserted into the placeholders based on their order in the .format() method's arguments.
Python

name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is Alice and I am 30 years old.
Positional Arguments
You can explicitly specify the position of the value to be inserted using numerical indices within the curly braces.
Python

print("The first number is {1}, and the second number is {0}".format(10, 20))
# Output: The first number is 20, and the second number is 10
"""
#--------------------------------------

"""

Creating and Using Objects
Instantiation
The process of creating a new instance of a class is known as instantiation. In
general, the syntax for instantiating an object is to invoke the constructor of a class.
For example, if there were a class named Widget, we could create an instance of
that class using a syntax such as w = Widget( ), assuming that the constructor does
not require any parameters. If the constructor does require parameters, we might
use a syntax such as Widget(a, b, c) to construct a new instance

yet another way to indirectly create a new
instance of a class is to call a function that creates and returns such an instance. For
example, Python has a built-in function named sorted (see Section 1.5.2) that takes
a sequence of comparable elements as a parameter and returns a new instance of
the list class containing those elements in sorted order.

Python supports traditional functions (see Section 1.5) that are invoked with a syn￾tax such as sorted(data), in which case data is a parameter sent to the function.
Python’s classes may also define one or more methods (also known as member
functions), which are invoked on a specific instance of a class using the dot (“.”)
operator

When using a method of a class, it is important to understand its behavior.
Some methods return information about the state of an object, but do not change
that state. These are known as accessors. Other methods, such as the sort method
of the list class, do change the state of an object. These methods are known as
mutators or update methods.

 the float class is immutable. Once
an instance has been created, its value cannot be changed (although an identifier
referencing that object can be reassigned to a different value)

The bool class is used to manipulate logical (Boolean) values, and the only two
instances of that class are expressed as the literals True and False. The default
constructor, bool( ), returns False, but there is no reason to use that syntax rather
than the more direct literal form
Sequences and other container types, such as strings and lists,
evaluate to False if empty and True if nonempty

 If s represents a string, then int(s) produces the integral value
that string represents. For example, the expression int( 137 ) produces the inte￾ger value 137. If an invalid string is given as a parameter, as in int( hello ), a
ValueError is raised (see Section 1.7 for discussion of Python’s exceptions). By de￾fault, the string must use base 10. If conversion from a different base is desired, that
base can be indicated as a second, optional, parameter. For example, the expression
int( 7f , 16) evaluates to the integer 127

We note that the floating-point equivalent of an integral number can be expressed
directly as 2.0. Technically, the trailing zero is optional, so some programmers
might use the expression 2. to designate this floating-point literal. One other form
of literal for floating-point values uses scientific notation. For example, the literal
6.022e23 represents the mathematical value 6.022×1023.

The list, tuple, and str classes are sequence types in Python, representing a col￾lection of values in which the order is significant.
We note that Python does not have a
separate class for characters; they are just strings with length one

list class -A list instance stores a sequence of objects. A list is a referential structure, as it
technically stores a sequence of references to its elements (see Figure 1.4). El￾ements of a list may be arbitrary objects (including the None object). Lists are
array-based sequences and are zero-indexed, thus a list of length n has elements
indexed from 0 to n−1 inclusive. LLists are perhaps the most used container type in
Python
Python uses the characters [ ] as delimiters for a list literal, with [ ] itself being
an empty list. As another example, [ red , green , blue ] is a list containing
three string instanc
The list( ) constructor produces an empty list by default. However, the construc￾tor will accept any parameter that is of an iterable type
 For example, the syntax
list( hello ) produces a list of individual characters, [ h , e , l , l , o ].

While Python uses the [ ] characters to delimit a list, parentheses delimit a
tuple, with ( ) being an empty tuple. There is one important subtlety. To express
a tuple of length one as a literal, a comma must be placed after the element, but
within the parentheses. For example, (17,) is a one-element tuple. The reason for
this requirement is that, without the trailing comma, the expression (17) is viewed
as a simple parenthesized numeric expressio

String literals can be enclosed in single quotes, as in hello , or double
quotes, as in "hello". This choice is convenient, especially when using an￾other of the quotation characters as an actual character in the sequence, as in
"Don t worry". Alternatively, the quote delimiter can be designated using a
backslash as a so-called escape character, as in 'Don\' t worry' .
n 'C:\\Python\\' , for a string that would be displayed as C:\Python\.

Other commonly escaped characters are \n for newline
and \t for tab. Unicode characters can be included, such as '20\u20AC' for the
string 20E .
print(”””Welcome to the GPA calculator.
Please enter all your letter grades, one per line.
Enter a blank line to designate the end.”””)
=======-------------------
The major advantage of using a set, as opposed to a list, is that it has a highly
optimized method for checking whether a specific element is contained in the set.
This is based on a data structure known as a hash table (which will be the primary
topic of Chapter 10). However, there are two important restrictions due to the
algorithmic underpinnings. The first is that the set does not maintain the elements
in any particular order. The second is that only instances of immutable types can be
added to a Python set. Therefore, objects such as integers, floating-point numbers,
and character strings are eligible to be elements of a set. It is possible to maintain a
set of tuples, but not a set of lists or a set of sets, as lists and sets are mutable. The
frozenset class is an immutable form of the set type, so it is legal to have a set of
frozensets.
Python uses curly braces { and } as delimiters for a set, for example, as {17}
or { red , green , blue }. The exception to this rule is that { } does not
represent an empty set; for historical reasons, it represents an empty dictionary
(see next paragraph). Instead, the constructor syntax set( ) produces an empty set.
If an iterable parameter is sent to the constructor, then the set of distinct elements
is produced. For example, set( hello ) produces { h , e , l , o }.

=========---------------------
Python’s dict class represents a dictionary, or mapping, from a set of distinct keys
to associated values. For example, a dictionary might map from unique student ID
numbers, to larger student records (such as the student’s name, address, and course
grades). Python implements a dict using an almost identical approach to that of a
set, but with storage of the associated values
A dictionary literal also uses curly braces, and because dictionaries were intro￾duced in Python prior to sets, the literal form { } produces an empty dictionary.
A nonempty dictionary is expressed using a comma-separated series of key:value
pairs. For example, the dictionary { 'ga' : 'Irish' , 'de' : 'German' } maps
'ga' to 'Irish' and 'de' to 'German'
the constructor accepts a sequence of key-value pairs as a pa￾rameter, as in dict(pairs) with pairs = [( 'ga' , 'Irish' ), ( 'de' , 'German' )].

-----------------
/ true division
// integer division

Bitwise Operators
Python provides the following bitwise operators for integers:
∼ bitwise complement (prefix unary operator)
& bitwise and
| bitwise or
ˆ bitwise exclusive-or
<< shift bits left, filling in with zeros
>> shift bits right, filling in with sign bi

Sequence Operators
Each of Python’s built-in sequence types (str, tuple, and list) support the following
operator syntaxes:
s[j] element at index j
s[start:stop] slice including indices [start,stop)
s[start:stop:step] slice including indices start, start + step,
start + 2 step, . . . , up to but not equalling or stop
s+t concatenation of sequences
k s shorthand for s + s + s + ... (k times)
val in s containment check
val not in s non-containment check
Python relies on zero-indexing of sequences, thus a sequence of length n has ele￾ments indexed from 0 to n− 1 inclusive. Python also supports the use of negative
indices, which denote a distance from the end of the sequence; index −1 denotes
the last element, index −2 the second to last

 data[3:8] denotes a subsequence including the five indices:
3,4,5,6,7. An optional “step” value, possibly negative, can be indicated as a third
parameter of the slice.

All sequences define comparison operations based on lexicographic order, per￾forming an element by element comparison until the first difference is found. For
example, [5, 6, 9] < [5, 7] because of the entries at index 1.



"""

t = int('7f',16)
print(t)

if [5,6,9] < [5,7]: # subset
    print("true")
else:
    print("f")

"""
Operators for Sets and Dictionaries
Sets and frozensets support the following operators:
key in s containment check
key not in s non-containment check
s1 == s2 s1 is equivalent to s2
s1 != s2 s1 is not equivalent to s2
s1 <= s2 s1 is subset of s2
s1 < s2 s1 is proper subset of s2
s1 >= s2 s1 is superset of s2
s1 > s2 s1 is proper superset of s2
s1 | s2 the union of s1 and s2
s1 & s2 the intersection of s1 and s2
s1 − s2 the set of elements in s1 but not s2
s1 ˆ s2 the set of elements in precisely one of s1 or s2
Note well that sets do not guarantee a particular order of their elements, so the
comparison operators, such as <, are not lexicographic; rather, they are based on
the mathematical notion of a subset.

Dictionaries, like sets, do not maintain a well-defined order on their elements.
Furthermore, the concept of a subset is not typically meaningful for dictionaries, so
the dict class does not support operators such as <. Dictionaries support the notion
of equivalence, with d1 == d2 if the two dictionaries contain the same set of key￾value pairs
 The supported
operators are as follows:
d[key] value associated with given key
d[key] = value set (or reset) the value associated with given key
del d[key] remove key and its associated value from dictionary
key in d containment check
key not in d non-containment check
d1 == d2 d1 is equivalent to d2
d1 != d2 d1 is not equivalent to d2


 However, it is possible for a type to redefine such
semantics to mutate the object, as the list class does for the += operator.
alpha = [1, 2, 3]
beta = alpha # an alias for alpha
beta += [4, 5] # extends the original list with two more elements
beta = beta + [6, 7] # reassigns beta to a new list [1, 2, 3, 4, 5, 6, 7]
print(alpha) # will be [1, 2, 3, 4, 5]
This example demonstrates the subtle difference between the list semantics for the
syntax beta += foo versus beta = beta + foo

-------------------------------
if door is closed:
  open door( )
advance( )
Notice that the final command, advance( ), is not indented and therefore not part of
the conditional body. It will be executed unconditionally (although after opening a
closed door).
We may nest one control structure within another, relying on indentation to
make clear the extent of the various bodies. Revisiting our robot example, here is a
more complex control that accounts for unlocking a closed door.
if door is closed:
  if door is locked:
    unlock door( )
  open door( )
advance( )
--------------------
The
execution of a while loop begins with a test of the Boolean condition. If that condi￾tion evaluates to True, the body of the loop is performed. After each execution of
the body, the loop condition is retested, and if it evaluates to True, another iteration
of the body is performed. When the conditional test evaluates to False (assuming
it ever does), the loop is exited and the flow of control continues just beyond the
body of the loop.
here is a loop that advances an index through a sequence of
characters until finding an entry with value X or reaching the end of the sequence.
j=0
while j < len(data) and data[j] != X :
  j += 1
  
---------------------------
The for-loop syntax can be used on any
type of iterable structure, such as a list, tuple str, set, dict, or file (we will discuss
iterators more formally in Section 1.8). Its general syntax appears as follows.

for element in iterable:
  body                 # body may refer to element as an identifier 
  
For readers familiar with Java, the semantics of Python’s for loop is similar to the
“for each” loop style introduced in Java

Python provides a built-in class named range that generates integer sequences
big index = 0
for j in range(len(data)):
  if data[j] > data[big index]:
    big index = j
-----------------------------
function
def count(data, target):   namespace (see
Section 1.10) to manage all identifiers that have local scope within the current call
 n=0
 for item in data:
   if item == target: # found a match
     n += 1
 return n
The first line, beginning with the keyword def, serves as the function’s signature.
This establishes a new identifier as the name of the function (count, in this exam￾ple), and it establishes the number of parameters that it expects, as well as names
identifying those parameters (data and target, in this example). Unlike Java and
C++, Python is a dynamically typed language, and therefore a Python signature
does not designate the types of those parameters, nor the type (if any) of a return
value.
A return statement is used within the body of a function to indicate that the func￾tion should immediately cease execution, and that an expressed value should be
returned to the caller

def contains(data, target):
 for item in target:
  if item == target: # found a match
    return True
 return False
 
purpose is to multiply all entries of a numeric data set by a given factor.
def scale(data, factor):
  for j in range(len(data)):
    data[j] *= factor
    
def foo(a, b=15, c=27):




"""

def gpa(grade,points={'A':4.0,'b':2.0 }):
    num = 0
    tot_poin = 0
    for g in grade:
        if g in points:
            num += 1
            tot_poin += points[g]
    return tot_poin/num

grades1 =['A','b']
points1 = { 'A':4.0,'b':3 }

print(gpa(grades1, points1))

"""
This combination of forms seems to violate the rules for default parameters.
In particular, when a single parameter is sent, as in range(n), it serves as the stop
value (which is the second parameter); the value of start is effectively 0 in that
case. However, this effect can be achieved with some sleight of hand, as follows:
def range(start, stop=None, step=1):
 if stop is None:
  stop = start
  start = 0
  
if we are interested in finding a numeric value with magnitude that is
maximal (i.e., considering −35 to be larger than +20), we can use the calling syn￾tax max(a, b, key=abs). In this case, the built-in abs function is itself sent as the
value associated with the keyword parameter key. (Functions are first-class objects
in Python; see Section 1.10.) When max is called in this way, it will compare abs(a)
to abs(b), rather than a to b. The motivation for the keyword syntax as an alternate
to positional arguments is important in the case of max. This function is polymor￾phic in the number of arguments, allowing a call such as max(a,b,c,d); therefore,
it is not possible to designate a key function as a traditional positional element.

----------------------------
The open function accepts an optional second parameter that determines the
access mode. The default mode is r for reading. Other common modes are w
for writing to the file (causing any existing file with that name to be overwritten),
or a for appending to the end of an existing file. Although we focus on use of
text files, it is possible to work with binary files, using access modes such as rb
or wb .
------------------------------
filehandling
The most basic command for reading via a proxy is the read method. When invoked
on file proxy fp, as fp.read(k), the command returns a string representing the next k
bytes of the file, starting at the current position. 

When processing a file, the proxy maintains a current position within the file as
an offset from the beginning, measured in number of bytes. When opening a file
with mode r or w , the position is initially 0; if opened in append mode, a ,
the position is initially at the end of the file. The syntax fp.close( ) closes the file
associated with proxy fp, ensuring that any written contents are saved. A summary
of methods for reading and writing a file is given in Table 1.5
Calling Syntax Description
fp.read( ) Return the (remaining) contents of a readable file as a string.
fp.read(k) Return the next k bytes of a readable file as a string.
fp.readline( ) Return (remainder of) the current line of a readable file as a string.
fp.readlines( ) Return all (remaining) lines of a readable file as a list of strings.
for line in fp: Iterate all (remaining) lines of a readable file.
fp.seek(k) Change the current position to be at the kth byte of the file.
fp.tell( ) Return the current position, measured as byte-offset from the start.
fp.write(string) Write given string at current position of the writable file.
fp.writelines(seq)-Write each of the strings of the given sequence at the current
position of the writable file. This command does not insert
any newlines, beyond those that are embedded in the strings.
print(..., file=fp) - Redirect output of print function to the file.

When a file proxy is writable, for example, if created with access mode w or
a , text can be written using methods write or writelines. For example, if we de-
fine fp = open( results.txt , w ), the syntax fp.write( Hello World.\n )
writes a single line to the file with the given string

from pathlib import Path
1 path = Path('pi_digits.txt')
2 contents = path.read_text()
  print(contents)
To work with the contents of a file, we need to tell Python the path to 
the file. A path is the exact location of a file or folder on a system. Python 
provides a module called pathlib that makes it easier to work with files and 
directories, no matter which operating system you or your program’s users 
are working with. A module that provides specific functionality like this is 
often called a library, hence the name pathlib.


  
  
  

from pathlib import Path
path = Path('dsa1.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)
-----read from file handling-------
----------------------------------------------
exception
use of an undefined identifier in an expression causes a NameError, and errant use
of the dot notation, as in foo.bar( ), will generate an AttributeError if object foo
does not support a member named bar

Class Description
Exception A base class for most error types
AttributeError Raised by syntax obj.foo, if obj has no member named foo
EOFError Raised if “end of file” reached for console or file input
IOError Raised upon failure of I/O operation (e.g., opening file)
IndexError Raised if index to sequence is out of bounds
KeyError Raised if nonexistent key requested for set or dictionary
KeyboardInterrupt Raised if user types ctrl-C while program is executing
NameError Raised if nonexistent identifier used
StopIteration Raised by next(iterator) if no element; see Section 1.8
TypeError Raised when wrong type of parameter is sent to a function
ValueError Raised when parameter has invalid value (e.g., sqrt(−5))
ZeroDivisionError Raised when any division operator used with 0 as divisor

e, a call to abs( hello ) will raise a
TypeError because the parameter is not numeric, and a call to abs(3, 5) will raise
a TypeError because one parameter is expected. A ValueError is typically raised
when the correct number and type of parameters are sent, but a value is illegitimate
for the context of the function. 

the int constructor accepts a string, as with int( '137' ), but a ValueError is raised if that string does not represent an
integer, as with int( '3.14' ) or int( 'hello' ).
Python’s sequence types (e.g., list, tuple, and str) raise an IndexError when
syntax such as data[k] is used with an integer k that is not a valid index for the given
sequence (as described in Section 1.2.3)

:raise
The raise statement in exception handling is used to explicitly trigger an exception, interrupting the normal flow of program execution and signaling an exceptional situation. This allows developers to create custom error messages or raise specific exceptions when unexpected events occur, improving error handling and debugging. 
Here's a more detailed explanation:
Triggering Exceptions: The raise statement initiates an exception, which is an error or unusual condition that disrupts the normal program flow. 
Custom Exceptions: You can define your own exception types using the class keyword in Python, allowing for more granular error handling and specific error messages. 
Example:
Python

    # Raise a ValueError if the input is not an integer
    try:
        input_value = int(input("Enter an integer: "))
    except ValueError:
        raise ValueError("Invalid input. Please enter an integer.")
Error Messages:
When raising an exception, you can include a descriptive message, providing valuable context for debugging and error handling. 
Control Flow:
The raise statement stops the current code block and transfers control to the nearest except block, allowing you to handle the exception. 
Reraising Exceptions:
Inside an except block, you can raise the same exception (or a different one) to propagate it further up the call stack, allowing other parts of the program to handle it. 
------------
Checking the type and value of each parameter demands additional execution time
and, if taken to an extreme, seems counter to the nature of Python. Consider the
built-in sum function, which computes a sum of a collection of numbers.
"""
def sum(values):
    if not isinstance(values, 'collections.Iterable'):
        raise TypeError( 'parameter must be an iterable type' )
    total = 0
    for v in values:

        if not isinstance(v, (int, float)):
            raise TypeError( 'elements must be numeric' )
        total = total+ v
    return total

"""

The abstract base class, collections.Iterable, includes all of Python’s iterable con￾tainers types that guarantee support for the for-loop syntax (e.g., list, tuple, set);
we discuss iterables in Section 1.8, and the use of modules, such as collections, in
Section 1.11. Within the body of the for loop, each element is verified as numeric
before being added to the total. A far more direct and clear implementation of this
function can be written as follows:
"""
def summ(values):
    total = 0
    for v in values:
        total = total + v
    return total
"""
Interestingly, this simple implementation performs exactly like Python’s built-in
version of the function. Even without the explicit checks, appropriate exceptions
are raised naturally by the code. In particular, if values is not an iterable type, the
attempt to use the for-loop syntax raises a TypeError reporting that the object is not
iterable. In the case when a user sends an iterable type that includes a nonnumer￾ical element
such as sum([3.14, oops ]), a TypeError is naturally raised by the
evaluation of expression total + v. The error message

 if a division x/y is to be computed, there
is clear risk that a ZeroDivisionError will be raised when variable y has value 0. In
an ideal situation, the logic of the program may dictate that y has a nonzero value,
thereby removing the concern for error. However, for more complex code, or in
a case where the value of y depends on some external input to the program, there
remains some possibility of an error.
One philosophy for managing exceptional cases is to “look before you leap.”
The goal is to entirely avoid the possibility of an exception being raised through
the use of a proactive conditional test. Revisiting our division example, we might
avoid the offending situation by writing:
"""
x,y=int(input())
if y != 0:
    ratio = x / y
else:
    print('.. do something else ...')

age = -1 # an initially invalid choice
while age <= 0:
    try:
        age = int(input(' Enter your age in years:'))
        if age <= 0:
            print(' Your age must be positive')
    except (ValueError, EOFError):
        print( 'Invalid response ')

a = 5

if a % 2 != 0:
    raise Exception("The number shouldn't be an odd integer")

s = 'apple'

try:
    num = int(s)
except ValueError:
    raise ValueError("String can't be changed into integer")

s = 'appl'

try:
    num = int(s)
except:
    raise
"""

Advantages of the raise keyword
It helps us raise error exceptions when we may run into situations where execution can't proceed.
It helps us raise error in Python that is caught.
Raise allows us to throw one exception at any time.
It is useful when we want to work with input validations.

In order to provide different responses to different types of errors, we may use
two or more except-clauses as part of a try-structure. In our previous example, an
EOFError suggests a more insurmountable error than simply an errant value being
entered. In that case, we might wish to provide a more specific error message, or
perhaps to allow the exception to interrupt the loop and be propagated to a higher
context. We could implement such behavior as follows:
"""
age = -1 # an initially invalid choice
while age <= 0:
    try:
        age = int(input(' Enter your age in years: '))
        if age <= 0:
            print( 'Your age must be positive ')
    except ValueError:
        print( 'That is an invalid age specification' )
    except EOFError:
        print( 'There was an unexpected error reading input.' )
        raise # let s re-raise this exception

"""
In this implementation, we have separate except-clauses for the ValueError and
EOFError cases. The body of the clause for handling an EOFError relies on another
technique in Python. It uses the raise statement without any subsequent argument,
to re-raise the same exception that is currently being handled. This allows us to
provide our own response to the exception, and then to interrupt the while loop and
propagate the exception upward.

"""
#------------------------
while True:
    ans = input("are you bored yet? y/n ")
    if ans == "y":
        print("my bad!")
        break

for _ in range(1,4):
    for _ in range(1,3):
        print("hip")
    print("hooray")
try:
    f= open("dsa1.txt")
except FileNotFoundError:
    print("file not there")

"""
dictionary class supports methods keys( ), values( ), and items( ), which respec￾tively produce a “view” of all keys, values, or (key,value) pairs within a dictionary.
None of these methods produces an explicit list of results. Instead, the views that
are produced are iterable objects based upon the actual contents of the dictionary.
An explicit list of values from such an iteration can be immediately constructed by
calling the list class constructor with the iteration as a parameter. For example, the
syntax list(range(1000)) produces a list instance with values from 0 to 999, while
the syntax list(d.values( )) produces a list that has elements based upon the current
values of dictionary d.
"""
#------------------------
"""
A generator is implemented with a syntax that
is very similar to a function, but instead of returning values, a yield statement is
executed to indicate each element of the series. As an example, consider the goal
of determining all factors of a positive integer.
"""
def factors(n): # traditional function that computes factors
    results = [ ] # store factors in a new list
    for k in range(1,n+1):
        if n % k == 0: # divides evenly, thus k is a factor
            results.append(k) # add k to the list of factors
    return results # return the entire list
#In contrast, an implementation of a generator for computing those factors could be
# implemented as follows:
def factorss(n): # generator that computes factors
    for k in range(1,n+1):
        if n % k == 0: # divides evenly, thus k is a factor
            yield k

n = 100
print(factorss(n))
for factor in factorss(100):
    print(factor)

"""
Notice use of the keyword yield rather than return to indicate a result. This indi￾cates to Python that we are defining a generator, rather than a traditional function. It
is illegal to combine yield and return statements in the same implementation, other
than a zero-argument return statement to cause a generator to end its execution. If
a programmer writes a loop such as for factor in factors(100):, an instance of our
generator is created.
"""
def factors1(n): # generator that computes factors
    k=1
    while k *k < n: # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k* k == n: # special case if n is perfect square
        yield k

n = 100
print(factors1(n))
for factor in factors1(100):
    print(factor)
"""
1
100
2
50
4
25
5
20
10
k= 1,2,4,5,10
"""
def fibo(n):
    a = 1
    b = 1
    ct = 0
    while ct < n:
        yield a  # 1,1,2,3,5
        future = a + b # 2,3,5,8
        a = b # 1,2,3,5
        b = future # 2,3,5,8
        ct += 1

n=5
for factor in fibo(n):
    print(factor)
# conditional expressions
n=int(input())
y = n if n>0 else -n
print(y)

#comprehension
result = []
n = int(input())
for value in range(n):
    if n<6:
        result.append("success")
print(result)

m = int(input())
res = ["suc" for val in range(m) if m<6]

"""
Packing and Unpacking of Sequences

Python provides two additional conveniences involving the treatment of tuples and
other sequence types. The first is rather cosmetic. If a series of comma-separated
expressions are given in a larger context, they will be treated as a single tuple, even
if no enclosing parentheses are provided. For example, the assignment
"""

data = 2, 4, 6, 8
"""
results in identifier, data, being assigned to the tuple (2, 4, 6, 8). This behavior
is called automatic packing of a tuple. One common use of packing in Python is
when returning multiple values from a function. If the body of a function executes
the command,
"""
return x, y

"""
it will be formally returning a single object that is the tuple (x, y).
As a dual to the packing behavior, Python can automatically unpack a se￾quence, allowing one to assign a series of individual identifiers to the elements
of sequence. As an example, we can write
"""
a, b, c, d = range(7, 11)
"""
This technique can be used to unpack tuples returned by a function. For exam￾ple, the built-in function, divmod(a, b), returns the pair of values (a // b, a % b)
associated with an integer division. Although the caller can consider the return
value to be a single tuple, it is possible to write
quotient, remainder = divmod(a, b)
to separately identify the two entries of the returned tuple. This syntax can also be
used in the context of a for loop, when iterating over a sequence of iterables, as in
for x, y in [ (7, 2), (5, 8), (6, 4) ]:

This style of loop is quite commonly used to iterate through
key-value pairs that are returned by the items( ) method of the dict class, as in:
for k, v in mapping.items( ):




"""
a,b,c =1,2,3
d=0
d=c  # like linked list
c = a
b= b
a = d
print(a,b,c)




def fibonacci( ):
    a, b = 0, 1
    ct=0
    while ct<6:
        yield a
        a, b = b, a+b
        ct += 1

for factor in fibonacci():
    print(factor)


"""
Scopes and Namespaces

When computing a sum with the syntax x+y in Python, the names x and y must
have been previously associated with objects that serve as values; a NameError
will be raised if no such definitions are found. The process of determining the
value associated with an identifier is known as name resolution.

Whenever an identifier is assigned to a value, that definition is made with a
specific scope. Top-level assignments are typically made in what is known as global
scope. Assignments made within the body of a function typically have scope that is
local to that function call. Therefore, an assignment, x=5, within a function has
no effect on the identifier, x, in the broader scope.

Each distinct scope in Python is represented using an abstraction known as a
/namespace/. A namespace manages all identifiers that are currently defined in a
given scope. Figure 1.8 portrays two namespaces, one being that of a caller to our
count function from Section 1.5, and the other being the local namespace during
the execution of that function.
Python implements a namespace with its own dictionary that maps each iden￾tifying string 
(e.g., n ) to its associated value. Python provides several ways toexamine a given namespace.
The function, /dir/, reports the names of the identifiers in a given namespace (i.e., the keys
of the dictionary), while the function,/ vars/, returns the full dictionary. By default, calls 
to dir( ) and vars( ) report on the most locally enclosing namespace in which they are executed


first-class objects
 are instances of a type that can be assigned to an identifier, passed as a parameter, or returned by
a function.While there is little motivation for pre￾cisely this example, it demonstrates the mechanism that
 is used by Python to al￾low one function to be passed as a parameter to another


"""
scream = print # assign name ’scream’ to the function denoted as ’print’
scream( Hello )

max(a, b, key=abs)
#Within the body of that function, the formal parameter, key, is an identifier
#that will be assigned to the actual parameter, abs


"""
Modules and the Import Statement

We have already introduced many functions (e.g., max) and classes (e.g., list)
that are defined within Python’s built-in namespace. Depending on the version of
Python, there are approximately 130–150 definitions that were deemed significant
enough to be included in that built-in namespace.
Beyond the built-in definitions, the standard Python distribution includes per￾haps tens of thousands of other values, functions, and classes that are organized in
additional libraries, known as modules, that can be imported from within a pro￾gram. As an example, we consider the math module. While the built-in namespace
includes a few mathematical functions (e.g., abs, min, max, round), many more
are relegated to the math module (e.g., sin, cos, sqrt). 

from math import pi, sqrt

This command adds both pi and sqrt, as defined in the math module, into the cur￾rent namespace, allowing direct use of the identifier, pi, or a call of the function,
sqrt(2). If there are many definitions from the same module to be imported, an
asterisk may be used as a wild card, as in, from math import , but this form
should be used sparingly. The danger is that some of the names defined in the mod￾ule may conflict with names already in the current namespace (or being imported
from another module

To create a new module

 one simply has to put the relevant definitions in a file
named with a .py suffix. Those definitions can be imported from any other .py
file within the same project directory. For example, if we were to put the definition
of our count function (see Section 1.5) into a file named utility.py, we could
import that function using the syntax, from utility import count

There is a special construct for embedding commands within the module
that will be executed if the module is directly invoked as a script, but not when
the module is imported from another script. Such commands should be placed in a
body of a conditional statement of the following form,
if __name__ == '__main__' :
Using our hypothetical utility.py module as an example, such commands will
be executed if the interpreter is started with a command python utility.py, but
not when the utility module is imported into another context. This approach is often
used to embed what are known as unit tests within the module

Existing Modules

Module Name Description
array Provides compact array storage for primitive types.
collections Defines additional data structures and abstract base classes
involving collections of objects.
copy Defines general functions for making copies of objects.
heapq Provides heap-based priority queue functions (see Section 9.3.7).
math Defines common mathematical constants and functions.
os Provides support for interactions with the operating system.
random Provides random number generation.
re Provides support for processing regular expressions.
sys Provides additional level of interaction with the Python interpreter.
time Provides support for measuring time, or delaying a program

pseudo-random number generator chooses its
next number based solely on the most recently chosen number and some additional
parameters using the following formula.
next = (a*current + b) % n;
where a, b, and n are appropriately chosen integers. Python uses a more advanced
technique known as a Mersenne twister.

Since the next number in a pseudo-random generator is determined by the pre￾vious number(s), such a generator always needs a place to start, which is called its
seed. The sequence of numbers generated for a given seed will always be the same.
One common trick to get a different sequence each time a program is run is to use
a seed that will be different for each run. For example, we could use some timed
input from a user or the current system time in milliseconds

For convenience, all of the methods
supported by the Random class are also supported as stand-alone functions of the
random module (essentially using a single generator instance for all top-level calls).
Syntax Description
seed(hashable) Initializes the pseudo-random number generator
based upon the hash value of the parameter
random( ) Returns a pseudo-random floating-point
value in the interval [0.0,1.0).
randint(a,b) Returns a pseudo-random integer
in the closed interval [a,b].
randrange(start, stop, step) Returns a pseudo-random integer in the standard
Python range indicated by the parameters.
choice(seq) Returns an element of the given sequence
chosen pseudo-randomly.
shuffle(seq) Reorders the elements of the given
sequence pseudo-randomly.
Table 1.8: Methods supported by instances of the Random class




"""







