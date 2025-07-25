
"""
can_construct(abcdef,[ab,abc,cd,def,a,ef,c]) true
can_construct(abcdef,[ab,abc,cd,abcd]) false
can_construct("",[ab,abc,cd,def,abcd]) =  true

                                    [[ab][cd][ef]]
                                    +
                            abcdef  [[abc][def]]
                                    +
                                    []

     cdef(ab) [[cd][ef],[c][def]]     def(abc) [[def]]       bcdef(a) []

 ef(cd)[[ef]]  def(c)[[def]]              ""  [[]]                "" []

""[[]]          ""[[]]
will return [] if not found
will return [[]] if target is "" ie taaking no word from wordbank
---------------------------------------------------------
skateboard[bo,rd,ate,t,ska,e,sk,boar] =false
                            skateboard

        teboard(ska)                        ateboard(sk)

        eboard(t)                           board(board)

         board(e)                          ard(bo)     d(boar)
board can be stored in memo process
"""


def all_construct(target, word_bank):
    if target == "":
        return [[]]

    total_ways = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank)
            target_ways = [[word] + way for way in suffix_ways] # first the word minused then from wordbank
            total_ways.extend(target_ways)

    return total_ways

print(all_construct("abcdef", ["ab", "abc", "cdef", "def", "cd", "ef"]))
"""
def ways2d(target,wordbank,count):
    if target == "":
        return  [[]]
    for word in wordbank:
        if target[0] == word[0]:
            suffix = target[len(word):]
            twodways = ways2d(suffix,wordbank,count)

    return count

print(ways2d("abcdef",["ab","abc","cdef","def","cd","ef"],0))
print(ways2d("abcdef",["ab","abc","cd","de","ef"],0))
# m (height)char in word and n or > m words to compare in  wordbank = n**m.space is m**2


"""
def mways(target,wordbank,memo):
    if target in memo:
        return memo[target]
    if target in wordbank:
        return [[]]
    total_ways = []
    for word in wordbank:
        if target[0] == word[0]:
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, wordbank)
            target_ways = [[word] + way for way in suffix_ways]  # first the word minused then from wordbank
            total_ways.extend(target_ways)

    memo[target] = total_ways
    return total_ways
#memo = {} # its storing true or false for other examples, which may return false values
# check in tutor
print(mways("abcdef",["ab","abc","cdef","def","cd","ef"],memo={}))
print(mways("abcdef",["ab","abc","cd","abcd"],memo={}))
# n*m**2

rows = 3
cols = 4
my_2d_array = []

# Initialize the 2D array
for _ in range(rows):
    my_2d_array.append([0] * cols)

# Map elements using nested loops
value = 1
for r in range(rows):
    for c in range(cols):
        my_2d_array[r][c] = value
        value += 1

print(my_2d_array)
#----------------------------
rows = int(input("Enter the number of rows: "))

matrix = []
print("Enter the elements for each row, space-separated:")
for _ in range(rows):
    row_input = input()  # Reads the entire line as a string
    row = list(map(int, row_input.split())) # Splits by space and converts to int
    matrix.append(row)

print("\nYour 2D array (matrix):")
for row in matrix:
    print(row)

#----------------------------------
my_2d_list = [[1, 2], [3, 4], [5, 6]]
new_row = [7, 8]

# Insert new_row at index 1 (second position)
my_2d_list.insert(1, new_row)
print(my_2d_list)
# Output: [[1, 2], [7, 8], [3, 4], [5, 6]]

my_2d_list = [[1, 2], [3, 4], [5, 6]]

# Insert 99 at index 1 (second position) in the sublist at index 0 (first row)
my_2d_list[0].insert(1, 99)
print(my_2d_list)
# Output: [[1, 99, 2], [3, 4], [5, 6]]

my_2d_list = [[1, 2], [3, 4], [5, 6]]

# Change the element at row 1, column 0 to 100
my_2d_list[1][0] = 100
print(my_2d_list)
# Output: [[1, 2], [100, 4], [5, 6]]

#--------------------------------------


original_2d_list = [[1, 2], [3, 4], [5, 6]]

# Function to insert an element at a specific index in a sublist
def insert_element(sublist):
    sublist.insert(1, 0) # Inserting 0 at index 1
    return sublist

# Use map to apply the function to each sublist
modified_2d_list = list(map(insert_element, original_2d_list))

print(modified_2d_list)
# Output: [[1, 0, 2], [3, 0, 4], [5, 0, 6]]
#--------------------------
original_2d_list = [[1, 2], [3, 4], [5, 6]]

# Function to add a value to each element in a sublist
def add_value(item):
    return item + 10

# Use map to apply the function to each element of each sublist
# This requires a nested map or list comprehension for the inner lists
modified_2d_list = [list(map(add_value, sublist)) for sublist in original_2d_list]

print(modified_2d_list)
# Output: [[11, 12], [13, 14], [15, 16]]

original_2d_list = [[1, 2], [3, 4], [5, 6]]

# Function to insert an element at a specific index in a sublist
def insert_element(sublist):
    sublist.insert(1, 0) # Inserting 0 at index 1
    return sublist

# Use map to apply the function to each sublist
modified_2d_list = list(map(insert_element, original_2d_list))

print(modified_2d_list)
# Output: [[1, 0, 2], [3, 0, 4], [5, 0, 6]]




