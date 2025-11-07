


# import modules
import heapq as hq

# dictionary to be heapified
dict_1 = {11: 121, 2: 4, 5: 25, 3: 9}

# convert dictionary to list of tuples
di = list(dict_1.items())

print("dictionary into list :", di)

# converting into heap
hq.heapify(di)

print("Heapified list of tuples :", di)

# converting heap to dictionary
di = dict(di)

print("Dictionary as heap :", di)

print("----------------------------")
# dictionary to be heapified
li_dict = {11: 121, 2: 4, 5: 25, 3: 9}

# List to hold values from dictionary
heap_dict = []

# extract the values from dictionary
for i in li_dict.values():
    heap_dict.append(i)

# heapify the values
hq.heapify(heap_dict)
print("Values of the dict after heapification :", heap_dict)

# list to hold final heapified dictionary
new_dict = []

# mapping and reconstructing final dictionary
for i in range(0, len(heap_dict)):

    # Iterating the oringinal dictionary
    for k, v in li_dict.items():

        if v == heap_dict[i] and (k, v) not in new_dict:
            new_dict.append((k, v))

new_dict = dict(new_dict)

print("Final dictionary :", new_dict)

"""
Consider a list of dictionaries which has to be maintained as a heap. The approach used is: 

Convert each dictionary into a tuple using list comprehension.
Pass the list to heapify().
Convert the resulting list of heapified tuples into the dictionary.
Note: The heapify() on tuples considers the first element in the tuple for the process.
Thus, by default, the dictionaries are maintained in heap, based on the key only.

"""


# list of dictionaries
li_dict=[{11:121},{2:4},{5:25},{3:9}]

#temporary list to hold tuple of key-value pairs
heap_dict22=[]

# convert each dict to tuple
heap_dict22 = [(k,v) for i in li_dict for k,v in i.items() ] # i gives dict and  k,v gives items in dict

print("After extraction :",heap_dict22)

# heapify the list of tuples
hq.heapify(heap_dict22)

print("Heapified key-value pairs :",heap_dict22)

# reconvert to dictionary
final1 = dict(heap_dict22)
print("Heapified dictionaries :",final1)

"""
Nested dictionaries
In the case of nested dictionaries, the task takes more steps to maintain the dictionary in heap. 
If the dictionary has to be maintained based on the key in a inner dictionary, then the following 
approach can be used.

Convert the dictionary into list of tuples where the key of the outer dictionary is tuple[0] and the 
inner dictionary is tuple[1].
Extract the values of the key in inner dictionaries into a list.
Apply heapify() on that list.
Re-construct a new dictionary by ordering them based on the heapified results.

"""


def get_list(d):
    list_li = list(d.items())

    print("Dictionary as list", list_li, "\n")

    return (list_li)


def convert_heap(list_li):
    # list to hold salary values
    sal_li = []

    # extract salary values
    for i in range(0, len(list_li)):
        sal_li.append(list_li[i][1]['Salary'])

    print("Before heapify :", sal_li, "\n")

    # heapify the salary values
    hq.heapify(sal_li)

    print("After heapify :", sal_li, "\n")

    # list to hold the final dictionary as heap
    final = []

    # reconstruction of dictionary as heap
    # yields a list of tuples of key-value pairs
    for i in range(0, len(sal_li)):

        for j in range(0, len(sal_li)):

            if list_li[j][1]['Salary'] == sal_li[i]:
                final.append(list_li[j])

    # list of tuples to dictionary
    final = dict(final)

    return final


nested_dict = {
    "emp01": {
        "name": "Kate",
        "age": 22,
        "designation": "Analyst",
        "Salary": 30000
    },
    "emp02": {
        "name": "Rina",
        "age": 20,
        "designation": "Programmer",
        "Salary": 25000
    },
    "emp03": {
        "name": "Vikas",
        "age": 42,
        "designation": "Manager",
        "Salary": 35000
    },
    "emp04": {
        "name": "manish",
        "age": 42,
        "designation": "Manager",
        "Salary": 15000
    }
}

list_li = get_list(nested_dict)

final = convert_heap(list_li)

print("Dictionary as heap :", final)

"""
Insertion in dictionary maintained as a heap
The insertion of new values can be done directly using heappush() method in the heapq module. Its syntax is as follows.


heapq . heappush ( list , new_value )


Now the list of tuples along with a new tuple can be passed to this function to add the new-key value pair.
"""
import heapq as hq

# list of dictionaries
li_dict2=[{11:121},{2:4},{5:25},{3:9}]

# list to hold tuples
heap_dict11=[]

# convert each dict to tuple of (key,value)
heap_dict11=[(k,v) for i in li_dict2 for k,v in i.items() ]

print("List of tuples :",heap_dict11)

# applying heapify()
hq.heapify(heap_dict11)

print("After heapification :",heap_dict11)

# reconvert to dict
final3=dict(heap_dict11)

print("Dictionary as heap :",final3)

# add new value (1,1)
hq.heappush(heap_dict11,(1,1))

print("After insertion & heapification",heap_dict11)

#reconvert the result
final3=dict(heap_dict11)

print("New dictionary 3 :",final3)

#---------------method 2


def heapify_dict(d):
    # convert to list of tuples
    li5 = list(dict111.items())

    hq.heapify(li5)

    li5 = dict(li5)

    print("Dictionary as heap :", li5)

dict111 = {11: 121, 2: 4, 5: 25, 3: 9}
print("Before adding new values")
heapify_dict(dict111)

# add new values to dictionary
dict111[4] = 16
dict111[1] = 1

print("Updated dictionary2 :", dict111)

print("After adding new values")
heapify_dict(dict111)








