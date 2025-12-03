from collections import defaultdict

res = defaultdict(list)

# Accessing a non-existent key automatically creates an empty list
res['fruits'].append('apple')
res['fruits'].append('banana')
res['vegetables'].append('carrot')

print(res)
# Output: defaultdict(<class 'list'>, {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']}

# Accessing another non-existent key
print(res['juices'])
# Output: []

#----------------------------------------------------------------------
import string

s = "asdfg"
# Initialize a list of 26 zeros (for a-z)
# list comprehension is a common Python pattern for this
count = [0] * 26

for c in s:
    # Ensure the character is a lowercase letter before processing
    if 'a' <= c <= 'z':
        # Calculate the index (0 for 'a', 1 for 'b', etc.) and increment
        index = ord(c) - ord("a")
        count[index] += 1

print(count)
# Output: [1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

#----------------------------------------------------------------------------
# tan - nat  anagrams if samee string formed from rotating
# by sreatin hash map for each  words  with keys as char and value as count of char, and compare the hash set

"""
The line res = defaultdict(list) initializes a defaultdict from Python's collections module.
A defaultdict is a subclass of the built-in dict class that provides a default value for a key that 
does not exist when it is accessed. This means you do not need to explicitly check if a key exists before 
trying to access or modify its value, which can prevent KeyError exceptions.

In this specific case:
from collections import defaultdict: This line imports the defaultdict class from the collections module. 
This is necessary to use defaultdict in your code.
res = defaultdict(list): This line creates an instance of defaultdict named res. The argument list passed to 
defaultdict is the "default factory." This means that whenever you try to access a key in res that does not 
yet exist, defaultdict will automatically create that key and assign an empty list ([]) as its default value.
"""

class Solut:
    def groupanagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list) # hashmap mapping char count to list of anagrams

        for s in strs:
            count =[0]*26

            for c in s:
                index = ord(c) - ord("a")
                count[index] += 1   # Calculate the index (0 for 'a', 1 for 'b', etc.) and increment.index = ord(c) - ord("a")
            res[tuple(count)].append(s)   # {[2,5,8]: byju, [5,7,9]: name}

        return list(res.values())


"""
res[tuple(count)].append(s): Uses the count list converted to an immutable tuple as the dictionary key 
to group identical character counts.
return list(res.values()): Returns only the values of the dictionary, which are the lists containing 
the grouped anagrams
"""