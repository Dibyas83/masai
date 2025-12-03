import string

def anagram(s1,s2):
    freqall = []
    if len(s1) != len(s2):
        return False
    # an array with all alphabets and freq as 0 is created ,its size is constant
    keys = string.ascii_lowercase
    charfreq = dict.fromkeys(keys,0)
    for i in range(len(s1)):
        charfreq[s1[i]] += 1  # s1[i] = c   s2[i] = d    -1 + 1 = 0
        charfreq[s2[i]] -= 1
    print(charfreq)

    if 1 in charfreq.values() or "-1" in charfreq.values():
        return False
    else:
        return "anabell"


s1 = "catdog"
s2 = "dogcag"
print(anagram(s1,s2))



"""
d = {1: 'Geeks', 2: 'For', 'age':22}

# Iterate over keys
for key in d:
    print(key)

# Iterate over values
for value in d.values():
    print(value)

# Iterate over key-value pairs
for key, value in d.items():
    print(f"{key}: {value}")
    
if any(value == 1 or value == "-1" for value in my_dict.values()):
    print("my_dict contains 1 or '-1'")
"""




