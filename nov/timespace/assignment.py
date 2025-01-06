"""
function compute_factorial is recursive and calls itself times before reaching the base
case ( ).
Each call performs a constant amount of work (multiplication).
Hence, the time complexity is proportional to the number of recursive calls, which is O(n)

Each recursive call adds a frame to the call stack. Since the function makes recursive calls (one
for each ), the space used by the call stack grows linearly with .
Therefore, the space complexity is O(n)
"""

"""
Generally we have 3 cases in time complexity

Best case: Minimum time required
Average case: Average time required
Worst case: Maximum time it need to compute
It’s is a standard method for estimating time complexity. It’s usually expressed in big-O notation, which represents 
the upper bound of the worst-case scenario. Big-O notation helps us to compare the performance of different algorithms
 and data structures in terms of their scalability.

Python counts the number of operations a data structure or method needs to perform in order to take a given task 
to end. Data structures in Python can have a variety of time complexity, including:

1. O(1) – Constant Time Complexity: This denotes that the amount of time required to complete an operation is constant
 and independent of the amount of input data. For example: When we access an element in an array by index, it has 
 an O(1) time complexity. because the time required to access an element is constant regardless of the size of the array.

2. (log n) – Logarithmic Time Complexity: OThis describes how the time required to complete an operation grows 
exponentially with the size of the input data. For example, Since the search time increases exponentially with the
 number of items in the tree, a binary search tree has a temporal complexity of O(log n) when looking for an element.

3. O(n) – Linear Time Complexity: This specifies that as the size of the input data increases, the time required to
 complete an operation climbs linearly. As an example, running algorithm over an array or linked list is having time 
 omplexity of O(n) because the amount of time needed to run over each member grows linearly as the size of the array 
 or linked list does. Due to which iterating over them has an O(n) time complexity.

4. O (n log n) – Log-Linear Time Complexity: This describes how an operation’s time complexity is a blend of linear 
and logarithmic. As an example, the time complexity of sorting an array with a merge sort is O(n log n). It is Because
 of the time needed to divide and merge the array grows logarithmically while the time needed to compare and merge 
 each element grows linearly.

5. O(n2) – Quadratic Time Complexity: This refers to the fact that as the size of the input data increases, an 
operation’s execution time climbs quadratically. For instance, sorting an array using bubble sort has an O(n^2) 
time complexity because it takes more time to compare and swap each element as the array gets larger.

6. O(2^n) – Exponential Time Complexity: This refers to the fact that as the size of the input data increases, 
same will gonna happen with the time required to complete an operation. For instance, because the number of subsets
 grows exponentially with the size of the set, creating all conceivable subsets of a set using recursion has a 
 temporal complexity of O(2n).

7. Factorial time (n!): When every possible combination of a collection is calculated during a single operation,
 an algorithm is said to have a factorial time complexity. As a result, the time required to complete a single 
 operation is factorial of the collection’s item size. The Traveling Salesman Problem and the Heap’s algorithm 
 (which creates every combination of n objects imaginable) are both O(n!) time tough problems. Its slowness is an issue.

Python data structures’ time complexity must be understood in order to write scalable and effective code, especially 
for applications that work with big volumes of data. We can enhance the performance and efficiency of our code by 
selecting the proper data structure and algorithm with the best time complexity.
"""
def comp_fact(n):
    if n == 0:
        return 1
    else:
        return n*comp_fact(n-1)

print(comp_fact(4))
print("----------------------------32")


def uni_pairs(arr):
    n = len(arr)
    count717 = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] != arr[j]:
                count717 += 1
    return count717

a = [2,3,4,2,3,5,6]
print(uni_pairs(a))
#  simplifies to O(n**2)as it is a quadratic function

print("-------------1213")
# find 3 min and 3 max

def min_max(N21,arr21):
    if N21 == 0:
        print("not possible")
        print("not possible")
        return
    distinct_elements = sorted(set(arr21))
    print(distinct_elements)
    if len(distinct_elements) >= 3:
        three_min = distinct_elements[:3]
        print(" ".join(map(str,three_min)))
    else:
        print("not possible")
    if len(distinct_elements) >= 3:
        three_max= distinct_elements[-3:]
        print(three_max)
        print(" ".join(map(str, three_max)))
    else:print("not")

N = 6
arr21 = [1,5,2,3,4,8,6,7]
min_max(N,arr21)
print("-----------------------------------4")

"""
 Its length is even.
2. Every character at an odd position is different from the next character.
For example:
Strings like "good", "string", and "xyyx" are good strings.
Strings like "bad", "aa", and "aabc" are not good.
The task is to delete the minimum number of characters from the given string to make it good
"""

def make_good(n,s):
    # initialize variables
    result = [] # store string char by char
    delettions = 0 # no of delets
    for i in range(n):

        if len(result)%2 == 0 or result[-1] != s[i]:
            result.append(s[i])
        else:
            delettions += 1

    if len(result)%2 != 0:  # If the current character forms a "bad pair" with the last character in the result (i.e., they are
#the same), we skip it and increment the deletions counter.
#Otherwise, the character is added to the result
        result.pop()
        delettions += 1

    print(delettions)
    print(" ".join(result))


def make_string_good2(n1, s1):
    if n1%2 == 0:
        print("good")
        for i in range(n1):
            if i % 2 == 0 and s1[i] != s1[i + 1]:
                print("good")

            elif i % 2 == 0 and s1[i] == s1[i + 1]:
                print("bad")
                break
    elif n1%2 != 0:
        print("bad")
n=5
s= "rtyuie"
make_string_good2(n,s)
print("------------------------------88")

def make_string_good1(n1, s1,s2,s3):
    s2 = ""
    s3 = ""
    minused = 0
    if n1 % 2 == 0:
        for i in range(n1):
            if i % 2 == 0 and s1[i] == s1[i + 1]:
                s2 = s1.replace( s1[i],"",1)
                minused += 1
        if len(s1)%2 != 0:
            s2 = s1.replace( s1[-1], "", 1)
        print(minused)
        print(s2)
    if n1%2 != 0:
        for i in range(n1):
            if i % 2 == 0 and s1[i] == s1[i + 1]:
                s2 = s1.replace( s1[i],"",1)
                minused += 1
            if i % 2 == 0 and s1[i] != s1[i + 1]:
                s2 = s1.replace( s1[-1], "", 1)
                minused += 1
    if len(s2)%2 != 0:
        s3 = s2.replace( s1[-1], "", 1)
        minused += 1
        print(minused)
        print(s3)
s2 =""
s3 =""
n11 = 6
s11 = "acvvio"
make_string_good1(n11,s11,s2,s3)

print("-------------------------------------565")
def make_string_good(n,s):
    new = []
    changed = 0
    for i in range(n):
        if len(new)%2 == 0 or new[-1] != s[i]:
            new.append(s[i])
        else:
            changed += 1

    if len(new)%2 != 0:
        new.pop()
        changed += 1

    print(changed)
    print(" ".join(new))

n= 8
s="werrtedd"
make_string_good(n,s)

print("-----------------------5thques")
"""
n= no of ques
m= no of days
problems = time taken for each ques
"""
def minimum_training_time(n, m, problems):
    def can_div_days(max_time):
        days_used = 1
        current_time = 0
        for time in problems:
            if current_time + time > max_time:
                days_used += 1 # time taken to next day ,if next q time + current time doesnot exceed T ,day is not added

                current_time = time
                if days_used > m:
                    return False
            else:
                current_time += time
        return True

    # binary search for the min T
    left = max(problems)
    right = sum(problems)
    result = right

    while left <= right:
        mid = (left + right) // 2
        if can_div_days(mid):
            result = mid
            right = mid - 1 # try for smaller max time ,if feasible
        else:
            left = mid + 1

        print(result)










