
"""

Largest palindromic number by permuting digits
Last Updated : 20 Mar, 2025
Given a very large integer n in the form of string, the task is to return the largest palindromic number obtainable by permuting the digits of n. If it is not possible to make a palindromic number, then return an empty string.

Examples :

Input : “313551”
Output : “531135”
Explanations : 531135 is the largest number which is a palindrome. 135531, 315513 and other numbers can also be formed but we need the largest of all of the palindromes.

Input : “331”
Output : “313”
Explanation: 313 is the only possible palindrome.

Input : “3444”
Output : “”
Explanation: Palindrome is not possible.


[Naive Approach] Try All Permutations
The naive approach will be to try all the permutations possible, and print the largest of such combinations, which is a palindrome.

[Efficient Approach] Using Greedy Method – O(n) time and O(n) space
The idea is to create the largest possible palindrome by placing the larger digits in the more significant positions and ensuring the palindrome property is maintained.


This greedy approach works because to maximize the numerical value of a palindrome, we want to place the largest available digits at the most significant positions, then the next largest digits in the next positions, and so on. Since palindromes must read the same from both ends, we need to place the same digit at corresponding positions from both ends, and can only have at most one digit that occurs an odd number of times (which would be placed in the middle).


Step by step approach:

Check if forming a palindrome is possible by counting digit occurrences and ensuring at most one digit appears an odd number of times.
If possible, initialize an array to store the result and start placing digits from the outside in.
For any digit that appears an odd number of times, place one occurrence in the middle position.
Working from 9 down to 0, place matching pairs of each digit symmetrically from the outside inward.
Convert the resulting array back to a string representation of the largest possible palindrome.



1
// CPP program to print the largest palindromic
2
// number by permuting digits of a number
3
#include <bits/stdc++.h>
4
using namespace std;
5

6
// function to check if a number can be
7
// permuted to form a palindrome number
8
bool possibility(vector<int> &cnt) {
9

10
    // counts the occurrence of number which is odd
11
    int countodd = 0;
12
    for (int i = 0; i < 10; i++) {
13
​
14
        // if occurrence is odd
15
        if (cnt[i] & 1)
16
            countodd++;
17

18
    }
19

20
    // If atmost 1 odd occurrence is
21
    // present, return true.
22
    return countodd <= 1;
23
}
24

25
// function to print the largest palindromic number
26
// by permuting digits of a number
27
string largestPalindrome(string s) {
28

29
    // string length
30
    int n = s.length();
31

32
    // map that count the occurrence of digits
33
    vector<int> cnt(10, 0);
34
    for (int i = 0; i < n; i++)
35
        cnt[s[i] - '0']++;
36

37
    // check the possibility of a palindromic number
38
    if (possibility(cnt) == false) {
39
        return "";
40
    }
41

42
    // integer array that stores the largest
43
    // permuted palindromic number
44
    vector<int> largest(n);
45

46
    // pointer of front
47
    int front = 0;
48

49
    // greedily start from 9 to 0 and place the
50
    // greater number in front and odd in the
51
    // middle
52
    for (int i = 9; i >= 0; i--) {
53

54
        // if the occurrence of number is odd
55
        if (cnt[i] & 1) {
56

57
            // place one odd occurring number
58
            // in the middle
59
            largest[n / 2] = i;
60

61
            // decrease the count
62
            cnt[i]--;
63
        }
64

65
​
66
        // if all numbers occur even times,
67
        // then place greedily
68
        while (cnt[i] > 0) {
69
​
70
            // place greedily at front
71
            largest[front] = i;
72
            largest[n - front - 1] = i;
73
​
74
            // 2 numbers are placed, so
75
            // decrease the count
76
            cnt[i] -= 2;
77
​
78
            // increase placing position
79
            front++;
80
        }
81

82
    }
83

84
    // Store the palindrome in a string
85
    string res = "";
86
    for (int i=0; i<n; i++) res.push_back('0'+largest[i]);
87

88
    return res;
89
}
90

91
int main() {
92
    string s = "313551";
93
    string res = largestPalindrome(s);
94
    cout << res;
95
    return 0;
96
}

Output
531135
"""









