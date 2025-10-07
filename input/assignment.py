
# li
# q1
"""
uin = input("enter  one char"\n)[0]  # [1] [ -1]
print("you entered",uin)
"""

print(int(input())+1)
print("---------------------------------------------")
x = (input().strip()).split(",")# Increment the input by 1 5678- 5679
for y in x:
    result =int(y) + 1
# Print the result
    print(result)

# q2
print("---------------------------2")
"""

d =input(),input(),input(),input()
for i in d:
    print(int(i)+1)
"""
numbers = list(map(int, input().strip().split(",")))
# Increment each number by 1 and print them
for num in numbers:
    print(num + 1)
# 3
print("-----------------------3")
"""
Description: Given an array of integers, print the elements of the array on a single line after adding 1 to
each element
"""

# Read the size of the array
n = int(input().strip())
# Read the array elements
array = list(map(int, input().strip().split(",")))
# Add 1 to each element in the array
updated_array = [x + 1 for x in array]# Print the updated array as space-separated values by listomprehension
print(updated_array)
print(" ".join(map(str, updated_array))) # joineed after converting into strings

print("---------------4")
"""
Array - Multiple Test Cases
Description: Given multiple test cases, where each test case consists of an array, print each array on a
single line after adding 1 to each element
"""
# Read the number of test cases
T = int(input().strip())
# Process each test case
for _ in range(T):
    # Read the size of the array (not used in this solution)
    # N = int(input().strip())
    # Read the array elements
    array = list(map(int, input().strip().split(",")))
    # Add 1 to each element in the array
    updated_array = [x + 1 for x in array]
    # Print the updated array as space-separated values
    print(" ".join(map(str, updated_array)))



T = int(input().strip())
ar = []
# Process each test case
for _ in range(T):
    # Read the size of the array (not used in this solution)
    N = int(input().strip())
    for i in range(N):
        # Read the array elements
        array = list(map(int, input().strip().split()))
        # Add 1 to each element in the array
        ar += array

        updated_array = [x + 1 for x in ar]
        # Print the updated array as space-separated values
    print(" ".join(map(str, updated_array)))
print("-----------------------5")
"""
Strings - I
Description: Given a string with its size provided as input, print the string as output
"""
# Read the size of the string (not used in this solution)
N = int(input().strip())
st = ""
while True:
    # Read the string itself
    print("enter", N, "of char")
    # string = input()[0:N].strip()
    string = input().strip()
    if len(string) > N:
        print("enter again")
        # string = input().strip()
    else:
        # Print the string as output
        print(string)
        break
print("-------------------------6")
"""
T = int(input().strip())
# Process each test case
for _ in range(T):
# Read the size of the string (not used here)
N = int(input().strip())
# Read and print the string
string = input().strip()
print(string)
"""
N = int(input().strip())
st = ""
for i in range(N):
    while True:
        # Read the string itself
        print("enter", N, "of char")
        # string = input()[0:N].strip()
        string = input().strip()
        if len(string) > N:
            print("enter again")
            # string = input().strip()
        else:
            # Print the string as output
            print(string)
            break
"""
dfg567rt
"""
s = []
for i in range(5):
    s += input()
print("".join(s))
print("-----------------7")
"""
For multiple test cases, each containing a sentence, print each sentence on a new line
"""
# Read the number of test cases
T = int(input().strip())
# Process each test case
for _ in range(T):
    # Read and print the sentence
    sentence = input().strip()
    print(sentence)

print("-------------------------------8")

"""
For each test case, an array and a value (K) are given. Add (K) to each element of the array and print the
updated array.
"""
# Read the number of test cases
T = int(input().strip())
# Process each test case
for _ in range(T):
    # Read N and K . he first line contains (N) (size of the array) and (K) (value to be added).
    # The next line contains (N) space-separated integers (array elements).
    N, K = map(int, input().strip().split())
    # Read the array
    array = list(map(int, input().strip().split()))  # Add K to each element and print the updated array
    updated_array = [x + K for x in array]
    print(" ".join(map(str, updated_array)))

# Read the number of test cases
T = int(input().strip())
upar =[]
# Process each test case
for _ in range(T):
    # Read N and K . he first line contains (N) (size of the array) and (K) (value to be added).
    # The next line contains (N) space-separated integers (array elements).
    N, K = map(int, input().strip().split(","))
    for i in range(N):
        # Read the array
        array = list(map(int, input().strip().split()))  # Add K to each element and print the updated array
        updated_array = [x + K for x in array]
        upar += updated_array
    print(" ".join(map(str, upar)))
print("------------9")
# L2 assignment

"""
Given a square matrix, add 1 to each element in the matrix and print the updated matrix row by row.
Input Format:
1. The first line contains (N), the dimensions of the square matrix.
2. The next (N) lines each contain (N) space-separated integers, denoting the elements of the matrix
"""
n= int(input("no of row").strip())
mat =[]
for r in range(n):
    row = list(map(int,input(", separated  n nos").strip().split(",")))
    updted_row = [x+1 for x in row]
    mat.append(updted_row)
for row in mat:
    print(" ".join(map(str,row)))
print("-------------------------10")
"""
For multiple test cases, where each test case contains a square matrix, add 1 to each element of the
matrix and print the updated matrix row by row.
Input Format:
1. The first line contains (T), the number of test cases.
2. For each test case:
The first line contains (N), the dimensions of the matrix.
The next (N) lines each contain (N) space-separated integers representing the matrix rows
"""
# Read the number of test cases
T = int(input().strip())
# Process each test case
for t in range(T):
    # Read the dimension of the square matrix
    N = int(input().strip())
    # Process each row of the matrix
    matrix = []
    for _ in range(N):
        # Read the row, add 1 to each element, and store the updated row
        row = list(map(int, input().strip().split()))
        updated_row = [x + 1 for x in row]
        matrix.append(updated_row)

    # Print the updated matrix for this test case
    for row in matrix:
        print(" ".join(map(str, row)))
    # Print a blank line between test cases, except for the last one
    if t < T - 1:
        print()
print("---------------------11")
"""
Given a rectangular matrix, add 1 to each element in the matrix and print the updated matrix row by row.
Input Format:
1. The first line contains (N) (number of rows) and (M) (number of columns) of the matrix.
2. The next (N) lines each contain (M) space-separated integers representing the matrix rows.
"""
# Read the dimensions of the matrix
N, M = map(int, input().strip().split())# Process each row of the matrix
matrix = []
for _ in range(N):
    # Read the row, add 1 to each element, and store the updated row
    row = list(map(int, input().strip().split()))
    updated_row = [x + 1 for x in row]
    matrix.append(updated_row)

# Print the updated matrix
for row in matrix:
    print(" ".join(map(str, row)))

print("-----------------------12")
"""
Given a series of queries, perform operations based on the query type and print the result as specified:
1. Multiply the number (X) by 2.
2. Multiply the number (X) by 3.3. Add 10 to the number (X).
4. Add 25 to the number (X).
5. Print -1.
Input Format:
1. The first line contains (Q), the number of queries.
2. The next (Q) lines contain queries:
The query format is T X , where (T) is the query type (1 to 5) and (X) is the number.
"""

# Read the number of queries
Q = int(input().strip())

# Process each query
for _ in range(Q):
    query = input().strip().split(",")
    query_type = int(query[0])
    if query_type == 1:
        X = int(query[1])
        print(X * 2)
    elif query_type == 2:
        X = int(query[1])
        print(X * 3)
    elif query_type == 3:
        X = int(query[1])
        print(X + 10)
    elif query_type == 4:
        X = int(query[1])
        print(X + 25)
    elif query_type == 5:
        print(-1)
"""
5
3,5
15
2,3
9
2,3
9
3,4
14
2,5
15
"""
print("---------------------13")
# calculator

num1 = float(input("enter num1 : "))
op =("+","/","-","=")
operator = input("enter(+,-,=,*,/): ")
num2 = float(input("enter num2: "))
if operator == "+":
    print("result: ",num1 + num2)
elif operator == "-":
    print("result: ",num1 - num2)
elif operator == "*":
    print("result: ",num1 * num2)
elif operator == "/":
    print("result: ",num1 / num2)
elif operator == "=":
    print("result: ",num1 == num2)
elif operator != op:
    print("of in bracket")
else:
    print("invalid operator")


x11 = int(input().strip())
res11 = x11 + 1

nos11 = list(map(int,input().strip().split()))
for n in nos11:
    print(n+1)
new_arr = [x+1 for x in nos11]
print(" ".join(map(str,new_arr)))

print("-------------------------------in")
tesst =int(input().strip())
for _ in range(tesst):
    siz = int(input().strip())
    arr14 = list(map(int,input().strip().split()))

print("-------------------------------str")
n_str =int(input().strip())
word  = input().strip()

print("-------------------------------sentence")
n_str = int(input().strip())
for _ in range(n_str):
    # sg = ""
    word = int(input("no of words =").strip())
    for i in range(word):
        sti = input().strip()
        sg += sti+" "
    print(sg)
print(sg)

print("-------------------------------no of sentence")
test1123 = int(input("no of sentences =").strip())
for i in range(test1123):
    sti = input().strip()
    print(sti)

print("-------------------------------no of array")

test113 = int(input("no of sentences =").strip())
for i in range(test113):
    N,K = map(int,input().strip().split(" ")) # n size of arr and k to be added
    ar1 = list(map(int,input().strip().split(" ")))
    updated_ar =[x+K for x in ar1]
    print(" ".join(map(str,updated_ar)))


# add 1 to each element of sq matrix
N = int(input().strip())  # no of row and no of ele in each row
matrix = []
for _ in range(N):
    row = list(map(int, input().strip().split(" ")))
    nr0w = [x + 1 for x in row]
    matrix.append(nr0w)
print(matrix)

for row in matrix:
    print(" ".join(map(str, row)))


# rectangular marix

N, M = map(int, input().strip().split(" "))
matrix121 = []
row111 =[]
for _ in range(N):
    print("row ele")
    for i in range(M):
        t = int(input("enter  ele of rows"))
        row111.append(t)
        rp_ar11 = [x + 1 for x in row111]

    matrix121.append(rp_ar11)
    print(matrix121)
    row111 = []

for row in matrix121:
    print(" ".join(map(str, row)))  # joined after converting array list to str

print('2nd method---------------------------')

N, M = map(int, input().strip().split(" "))
matrix121 = []
for _ in range(N):
    row121 = list(map(int, input().strip().split(" ")))
    rp_ar = [x + 1 for x in row121]
    matrix121.append(rp_ar)
print(matrix121)

for row in matrix121:
    print(" ".join(map(str, row)))  # joined after converting array list to str


Q= int(input(" queries or test cases = ").strip())
for i in range(Q):
    querry =input(" type 1-5 and int=").strip().split(" ") # gives list of stings
    query_type = int(querry[0])
    x = int(querry[1])
    if query_type == 1:
        print(x*2)
    elif query_type == 2:
        print(x*3)
    elif query_type == 3:
        print(x+10)
    elif query_type == 4:
        print(x+25)
    else:
        print("-1")





















