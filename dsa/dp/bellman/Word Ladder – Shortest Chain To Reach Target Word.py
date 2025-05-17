

"""
Given an array of strings arr[], and two different strings start and target, representing two words. The task is to find the length of the smallest chain from string start to target, such that only one character of the adjacent words differs and each word exists in arr[].

Note: Print 0 if it is not possible to form a chain. Each word in array arr[] is of same size m and contains only lowercase English alphabets.

Examples:

Input: start = “toon”, target = “plea”, arr[] = [“poon”, “plee”, “same”, “poie”, “plea”, “plie”, “poin”]
Output: 7
Explanation: toon  → poon  → poin  → poie  → plie  → plee  → plea


Input: start = “abcv”, target = “ebad”, arr[] = [“abcd”, “ebad”, “ebcd”, “xyza”]
Output: 4
Explanation: abcv  → abcd  → ebcd  → ebad


[Naive Approach]: Using backtracking, explore all possible path
We use backtracking to solve this problem because it allows us to systematically explore all possible transformation sequences from the start word to the target word while ensuring we don’t revisit the same word within a given path. In each step, we try every possible one-letter change in the current word and proceed recursively if the resulting word exists in the dictionary and hasn’t been visited yet.Backtracking enables the algorithm to “go back” once it reaches a dead end or completes a path, and then try a different option.


This is especially useful in problems like this where multiple paths exist, and we need to find the shortest valid transformation sequence. Although this method is not the most optimized, it is conceptually simple and effective for smaller datasets where performance is not a critical issue. By exploring all valid transformation paths, it guarantees that the minimum number of steps is found among all possible sequences.




1
# Recursive function to find the shortest transformation chain
2
def minWordTransform(start, target, mp):
3
    # If start word is the same as target, no transformation is needed
4
    if start == target:
5
        return 1
6
​
7
    mini = float('inf')
8
​
9
    # Mark current word as visited
10
    mp[start] = 1
11
​
12
    # Try changing each character of the word
13
    for i in range(len(start)):
14
        original_char = start[i]
15
​
16
        # Try all possible lowercase letters at position i
17
        for ch in 'abcdefghijklmnopqrstuvwxyz':
18
            new_word = start[:i] + ch + start[i+1:]
19
​
20
            # If the new word exists in dictionary and is not visited
21
            if new_word in mp and mp[new_word] == 0:
22
                # Recursive call for next transformation
23
                mini = min(mini, 1 + minWordTransform(new_word, target, mp))
24
​
25
    # Mark current word as unvisited (backtracking)
26
    mp[start] = 0
27
​
28
    return mini
29
​
30
# Wrapper function to prepare the map and call recursive function
31
def wordLadder(start, target, arr):
32
    mp = {word: 0 for word in arr}
33
​
34
    result = minWordTransform(start, target, mp)
35
    if(result == float('inf')):
36
        result = 0
37
    return result
38
​
39
# Driver code
40
arr = ["poon", "plee", "same", "poie", "plie", "poin", "plea"]
41
start = "toon"
42
target = "plea"
43
​
44
print(wordLadder(start, target, arr))

Output
6
Time Complexity: O(N⋅26L)), where N is the number of words in the dictionary and L is the length of each word.
Space Complexity: O(N) for storing the dictionary map and the recursive call stack, which can go up to N in the worst case.

Using Breadth First Search
The idea is to use BFS to find the smallest chain between start and target. To do so, create a queue words to store the word to visit and push start initially. At each level, go through all the elements stored in queue words, and for each element, alter all of its character for ‘a’ to ‘z‘ and one by one and check if the new word is in dictionary or not. If found, push the new word in queue, else continue. Each level of queue defines the length of chain, and once the target is found return the value of that level + 1.





1
# Python program to find length of the shortest
2
# chain transformation from start to target
3
from collections import deque
4
​
5
def wordLadder(start, target, arr):
6

7
    if (start == target):
8
        return 0
9
    # set to keep track of unvisited words
10
    st = set(arr)
11

12
    # store the current chain length
13
    res = 0
14
    m = len(start)
15

16
    # queue to store words to visit
17
    words = deque()
18
    words.append(start)
19

20
    while words:
21
        res+=1
22
        length = len(words)
23

24
        # iterate through all words at same level
25
        for _ in range(length):
26
            word = words.popleft()
27

28
            # For every character of the word
29
            for j in range(m):
30
                # Retain the original character
31
                # at the current position
32
                ch = word[j]
33

34
                # Replace the current character with
35
                # every possible lowercase alphabet
36
                for c in range(ord('a'), ord('z') + 1):
37
                    word = word[:j] + chr(c) + word[j+1:]
38

39
                    # skip the word if already added
40
                    # or not present in set
41
                    if word not in st:
42
                        continue
43

44
                    # If target word is found
45
                    if word == target:
46
                        return res + 1
47

48
                    # remove the word from set
49
                    st.remove(word)
50

51
                    # And push the newly generated word
52
                    # which will be a part of the chain
53
                    words.append(word)
54

55
                # Restore the original character
56
                # at the current position
57
                word = word[:j] + ch + word[j+1:]
58

59
    return 0
60
​
61
if __name__ == "__main__":
62
    arr = ["poon", "plee", "same", "poie", "plie", "poin", "plea"]
63
    start = "toon"
64
    target = "plea"
65
    print(wordLadder(start, target, arr))

Output
7
Time Complexity: O(26 * n * m * m) = O(n * m * m), where n is the size of arr[] and m is the length of each word.
Auxiliary Space: O(n * m)

"""


