
"""
Minimum Cost to cut a board into squares
Last Updated : 21 Mar, 2025
Given a board of dimensions m × n that needs to be cut into m × n squares. The cost of making a cut along a horizontal or vertical edge is provided in two arrays:

x[]: Cutting costs along the vertical edges (length-wise).
y[]: Cutting costs along the horizontal edges (width-wise).
The task is to determine the minimum total cost required to cut the board into squares optimally.

Examples:

Input: m = 6, n= 4, x[] = [2, 1, 3, 1, 4], y[] = [4, 1, 2]
Output: 42
Explanation:
For above board the optimal cutting order minimizes the cost as follows:


Cut horizontally (cost = 4) -> Total Cost = 4
Cut vertically (cost = 4) -> Total Cost = 12
Cut vertically (cost = 3) -> Total Cost = 18
Cut horizontally (cost = 2) -> Total Cost = 24
Cut vertically (cost = 2) -> Total Cost = 30
Cut horizontally (cost = 1) -> Total Cost = 34
Cut vertically (cost = 1) -> Total Cost = 38
Cut vertically (cost = 1) -> Total Cost = 42
Input: m = 4, n = 4, x[] = [1, 1, 1], y[] = [1, 1, 1]
Output: 15
Explanation: The optimal cutting order minimizes the cost as follows:


Cut horizontally (cost = 1) -> Total Cost = 1
Cut horizontally (cost = 1) -> Total Cost = 2
Cut horizontally (cost = 1) -> Total Cost = 3
Cut vertically (cost = 1) -> Total Cost = 7
Cut vertically (cost = 1) -> Total Cost = 11
Cut vertically (cost = 1) -> Total Cost = 15
Try it on GfG Practice
redirect icon
Naive Approach – Try All Permutations
We need to make a total of (m – 1) + (n – 1) cuts. A naive approach is to try all permutations of cuts and see which permutation gives the minimum cost.

Using Greedy Technique – O(m Log m + n log n) Time and O(1) Space
The idea is to make the most expensive cuts first using a greedy approach. The observation is that choosing the highest cost cut at each step reduces future costs by affecting multiple pieces at once. We sort the vertical (x) and horizontal (y) cut costs in descending order, then iteratively pick the larger one to maximize cost savings. The remaining cuts are processed separately to ensure all sections are split optimally.


Steps to implement the above idea:

Sort both x and y arrays in descending order to prioritize higher cost cuts for minimizing future expenses.
Use two pointers, one for x and one for y, starting from the largest value and moving toward smaller values.
Maintain hCount and vCount to track how many segments each cut affects and update them accordingly.
Iterate while both x and y have unprocessed cuts, always choosing the larger cost to minimize overall expenses.
If x has remaining cuts, process them with hCount multiplier; similarly, process remaining y cuts with vCount.
Accumulate total cost at each step using the formula: cut cost * number of affected pieces, ensuring minimal cost.
Return the total cost after processing all cuts, ensuring the board is divided into m × n squares optimally.



1
// C++ program to find the minimum cost to cut a board
2
// into squares using the Greedy Technique.
3
#include <bits/stdc++.h>
4
using namespace std;
5
​
6
int minimumCostOfBreaking(int m, int n,
7
                          vector<int>& x, vector<int>& y) {
8

9
    // Sort the cutting costs in ascending order
10
    sort(x.begin(), x.end());
11
    sort(y.begin(), y.end());
12
​
13
    // Pieces in each direction
14
    int hCount = 1, vCount = 1;
15
    int i = x.size() - 1, j = y.size() - 1;
16
    int totalCost = 0;
17
​
18
    // Process the cuts in greedy manner
19
    while (i >= 0 && j >= 0) {
20

21
        // Choose the larger cost cut to
22
        // minimize future costs
23
        if (x[i] >= y[j]) {
24
            totalCost += x[i] * hCount;
25
            vCount++;
26
            i--;
27
        }
28
        else {
29
            totalCost += y[j] * vCount;
30
            hCount++;
31
            j--;
32
        }
33
    }
34
​
35
    // Process remaining vertical cuts
36
    while (i >= 0) {
37
        totalCost += x[i] * hCount;
38
        vCount++;
39
        i--;
40
    }
41
​
42
    // Process remaining horizontal cuts
43
    while (j >= 0) {
44
        totalCost += y[j] * vCount;
45
        hCount++;
46
        j--;
47
    }
48
​
49
    return totalCost;
50
}
51
​
52
// Driver Code
53
int main() {
54

55
    int m = 6, n = 4;
56
    vector<int> x = {2, 1, 3, 1, 4};
57
    vector<int> y = {4, 1, 2};
58
​
59
    cout << minimumCostOfBreaking(m, n, x, y) << endl;
60
    return 0;
61
}

Output
42


"""












