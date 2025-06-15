"""
Classes Are Like Modules
 module as a specialized dictionary that can store Python
code so you can access it with the . operator. Python also has another construct
that serves a similar purpose called a class.A class is a way to take a grouping of
functions and data and place them inside a container so you can access them
with the . (dot) operator.

Modules Are Like Dictionaries - that it is a way to map one
thing to another
"""


mystuff = {'apple':'i am apple'}
print(mystuff['apple'])

def apple():
    print('i am appledef')
tangerine= 'living reflection of dream'

apple()
"""
import mystuff
mystuff.apple()
print(mystuff.tangerine)
"""

class MyStuff(object):
    def __int__(self):
        self.tangerine = "thousand old"

    def apple(self):
        print('i appled')
"""
this is like a
“mini-module” with MyStuff having an apple() function in it. What is
probably confusing is the __init__() function and use of
self.tangerine for setting the tangerine instance variable

Here’s why classes are used instead of modules: You can take this MyStuff
class and use it to craft many of them, millions at a time if you want, and each
one won’t interfere with each other. When you import a module there is only one
for the entire program unless you do some monster hacks.
Before you can understand this, though, you need to know what an “object” is
and how to work with MyStuff just like you do with the mystuff.py
module
Objects Are Like Import
If a class is like a “mini-module,” then there has to be a concept similar to
import but for classes. That concept is called “instantiate,” which is just a
fancy, obnoxious, overly smart way to say “create.” When you instantiate a class
what you get is called an object.
You instantiate (create) a class by calling the class like it’s a function, like this:

The first line is the “instantiate”
operation, and it’s a lot like calling a function
"""
thing = MyStuff()
thing.apple()
print(thing.tangerine)

















