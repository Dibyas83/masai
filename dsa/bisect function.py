
"""
The bisect module in Python provides functions for performing binary search on sorted lists. It's primarily used to maintain lists in sorted order without needing to sort them after each insertion. This module is especially useful for large lists where frequent sorting would be inefficient.
Key functions in the bisect module include:
bisect.bisect_left(list, element): Finds the index where an element should be inserted to maintain the sorted order, returning the leftmost suitable position.
bisect.bisect_right(list, element): Similar to bisect\_left but returns the rightmost suitable position for insertion.
bisect.insort_left(list, element): Inserts an element into a sorted list at the position found by bisect\_left, maintaining the sorted order.
bisect.insort_right(list, element): Inserts an element into a sorted list at the position found by bisect\_right, maintaining the sorted order.
The bisect module uses a bisection algorithm, which is a form of binary search. This algorithm works by repeatedly dividing the search interval in half. It is more efficient than linear search for large, sorted lists.

Important Bisection Functions
1. bisect(list, num, beg, end) :- This function returns the position in the sorted list, where the number passed in argument can be placed so as to maintain the resultant list in sorted order. If the element is already present in the list, the rightmost position where element has to be inserted is returned.

This function takes 4 arguments, list which has to be worked with, a number to insert, starting position in list to consider, ending position which has to be considered.

2. bisect_left(list, num, beg, end) :- This function returns the position in the sorted list, where the number passed in argument can be placed so as to maintain the resultant list in sorted order. If the element is already present in the list, the leftmost position where element has to be inserted is returned.

This function takes 4 arguments, list which has to be worked with, number to insert, starting position in list to consider, ending position which has to be considered.

3. bisect_right(list, num, beg, end) :- This function works similar to the "bisect()" and mentioned above.


"""
# Python code to demonstrate the working of
# bisect(), bisect_left() and bisect_right()

# importing "bisect" for bisection operations
import bisect

# initializing list
li = [1, 3, 4, 4, 4, 6, 7]

# using bisect() to find index to insert new element
# returns 5 ( right most possible index )
print ("Rightmost index to insert, so list remains sorted is : ",
       end="")
print (bisect.bisect(li, 4))

# using bisect_left() to find index to insert new element
# returns 2 ( left most possible index )
print ("Leftmost index to insert, so list remains sorted is : ",
       end="")
print (bisect.bisect_left(li, 4))

# using bisect_right() to find index to insert new element
# returns 4 ( right most possible index )
print ("Rightmost index to insert, so list remains sorted is : ",
       end="")
print (bisect.bisect_right(li, 4, 0, 4))

"""

Output
Rightmost index to insert, so list remains sorted is : 5
Leftmost index to insert, so list remains sorted is : 2
Rightmost index to insert, so list remains sorted is : 4
Time Complexity: O(log(n)), Bisect method works on the concept of binary search
Auxiliary Space:  O(1)

4. insort(list, num, beg, end) :- This function returns the sorted list after inserting number in appropriate position, if the element is already present in the list, the element is inserted at the rightmost possible position. 

This function takes 4 arguments, list which has to be worked with, number to insert, starting position in list to consider, ending position which has to be considered. 

5. insort_left(list, num, beg, end) :- This function returns the sorted list after inserting number in appropriate position, if the element is already present in the list, the element is inserted at the leftmost possible position. 

This function takes 4 arguments, list which has to be worked with, number to insert, starting position in list to consider, ending position which has to be considered. 

6. insort_right(list, num, beg, end) :- This function works similar to the "insort()" as mentioned above

"""
# Python code to demonstrate the working of
# insort(), insort_left() and insort_right()

# importing "bisect" for bisection operations
import bisect

# initializing list
li1 = [1, 3, 4, 4, 4, 6, 7]

# initializing list
li2 = [1, 3, 4, 4, 4, 6, 7]

# initializing list
li3 = [1, 3, 4, 4, 4, 6, 7]

# using insort() to insert 5 at appropriate position
# inserts at 6th position
bisect.insort(li1, 5)

print ("The list after inserting new element using insort() is : ")
for i in range(0, 7):
    print(li1[i], end=" ")

# using insort_left() to insert 5 at appropriate position
# inserts at 6th position
bisect.insort_left(li2, 5)

print("\r")

print ("The list after inserting new element using insort_left() is : ")
for i in range(0, 7):
    print(li2[i], end=" ")

print("\r")

# using insort_right() to insert 5 at appropriate position
# inserts at 5th position
bisect.insort_right(li3, 5, 0, 4)

print ("The list after inserting new element using insort_right() is : ")
for i in range(0, 7):
    print(li3[i], end=" ")





