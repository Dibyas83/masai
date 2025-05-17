
"""
Lexicographically largest subsequence such that every character occurs at least k times
Last Updated : 20 Mar, 2025
Given a string s and an integer k, the task is to find lexicographically largest subsequence of S, say T, such that every character in T must occur at least k times.

Examples:

Input : s = “banana”, k = 2.
Output : “nn”
Explanation:
Possible subsequence where each character exists at least 2 times are:


Check if a line touches or intersects a circle


From the above subsequences, “nn” is the lexicographically largest.


Input: s = “zzyyxx”, k = 2
Output: “zzyyxx”


Input: s = “xxyyzz”, k = 2
Output: “zz”


Approach:

The idea is to use a greedy approach by iterating from the highest character (‘z’) to the lowest (‘a’). For each character, we count its occurrences starting from the last valid position and include it in the result if it appears at least k times. This ensures that higher characters are prioritized, maintaining the lexicographical order, and the frequency constraint is satisfied by only considering valid segments of the string.


Step by step approach:

Iterate from ‘z’ to ‘a’ to prioritize higher characters for the lexicographical order.
For each character, count its occurrences starting from the last valid position in the string.
If the character appears at least k times, append all its occurrences to the result. Update the starting position to the index immediately after the last occurrence of the current character to avoid overlaps.
Repeat the process until all characters are processed, ensuring the result is the largest valid subsequence.



1
// C++ program to find Lexicographically
2
// largestsubsequence such that every
3
// character occurs at least k times
4
#include <bits/stdc++.h>
5
using namespace std;
6

7
string largestSubsequence(string &s, int k) {
8
    int n = s.length();
9

10
    string res = "";
11
    int last = 0;
12

13
    for (char ch='z'; ch>='a'; ch--) {
14
        int cnt = 0;
15
        int index = -1;
16

17
        // Count frequency of char ch
18
        // after the last index.
19
        for (int i=last; i<n; i++) {
20
            if (s[i] == ch) {
21
                cnt++;
22

23
                // Store the index of last
24
                // occurrence
25
                index = i;
26
            }
27
        }
28

29
        // If frequency is greater than
30
        // equal to k.
31
        if (cnt >= k) {
32

33
            // Append the current char
34
            // cnt times
35
            for (int i=0; i<cnt; i++) {
36
                res.push_back(ch);
37
            }
38

39
            // Update the last index
40
            last = index + 1;
41
        }
42
    }
43

44
    return res;
45
}
46

47
int main() {
48
    string s = "banana";
49
    int k = 2;
50
    string res = largestSubsequence(s, k);
51
    cout << res;
52
    return 0;
53
}

Output
nn
Time Complexity: O(n), as string is traversed once, and characters are appended to result at most n times.
Auxiliary Space: O(n)

"""




