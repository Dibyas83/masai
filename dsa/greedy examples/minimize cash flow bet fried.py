
"""
Minimize Cash Flow among a given set of friends who have borrowed money from each other
Last Updated : 24 Apr, 2025
Given n number of friends who have to give or take some amount of money from one another. The task is to design an algorithm by which the total cash flow among all the friends is minimized to settle all debts.

Examples:

Input: transaction = [[0, 1000, 2000], [0, 0, 5000], [0, 0, 0]]


cashFlow


Output: [[0, 0, 3000], [0, 0, 4000], [0, 0, 0]]


cashFlow


Input: transaction = [[0, 100, 0], [0, 0, 100], [100, 0, 0]]
Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


Try it on GfG Practice
redirect icon
Approach:

The idea is to calculate each person’s net balance and then optimizing cash flow between individuals who owe money (debtors) and those who are owed money (creditors), ensuring that money flows directly from the highest debtors to the highest creditors until all debts are settled.


Step by step approach:

Calculate the net amount for each person by subtracting outgoing money from incoming money
Separate people into two groups – those who need to pay and those who need to receive
Sort both groups by amount (highest values first) using priority queues
Repeatedly match the highest debtor with the highest creditor
Transfer the minimum of what one needs to pay and what one needs to receive
Continue until all debts are settled with minimized transactions



1
// C++ program to Minimize Cash Flow among a given set
2
// of friends who have borrowed money from each other.
3
#include <bits/stdc++.h>
4
using namespace std;
5
​
6
vector<vector<int>> minCashFlow(vector<vector<int>> &transaction) {
7
    int n = transaction.size();
8

9
    // Priority queues to track people who
10
    // need to give money and receive money
11
    // Vector format: {amount, personIndex}
12
    priority_queue<vector<int>> debtors, creditors;
13

14
    // Calculate net amount for each person
15
    for (int personId = 0; personId < n; personId++) {
16
        int netAmount = 0;
17

18
        // Add all incoming money
19
        for (int fromPerson = 0; fromPerson < n; fromPerson++)
20
            netAmount += transaction[fromPerson][personId];
21

22
        // Subtract all outgoing money
23
        for (int toPerson = 0; toPerson < n; toPerson++)
24
            netAmount -= transaction[personId][toPerson];
25

26
        // If net amount is negative, person needs to give money
27
        if (netAmount < 0)
28
            debtors.push({abs(netAmount), personId});
29

30
        // If net amount is positive, person needs to receive money
31
        else if (netAmount > 0)
32
            creditors.push({netAmount, personId});
33
    }
34

35
    // Initialize result matrix with zeros
36
    vector<vector<int>> result(n, vector<int>(n, 0));
37

38
    // Process all transactions until no more debtors left
39
    while (!debtors.empty()) {
40
        int debtAmount = debtors.top()[0];
41
        int creditAmount = creditors.top()[0];
42
        int debtorId = debtors.top()[1];
43
        int creditorId = creditors.top()[1];
44

45
        // Remove top entries from both queues
46
        debtors.pop();
47
        creditors.pop();
48

49
        // Find minimum of debt and credit amounts
50
        int transferAmount = min(debtAmount, creditAmount);
51

52
        // Record the transaction in result matrix
53
        result[debtorId][creditorId] = transferAmount;
54

55
        // Update remaining amounts
56
        debtAmount -= transferAmount;
57
        creditAmount -= transferAmount;
58

59
        // If debtor still has debt remaining, put back in queue
60
        if (debtAmount > 0) {
61
            debtors.push({debtAmount, debtorId});
62
        }
63

64
        // If creditor still needs to receive more, put back in queue
65
        else if (creditAmount > 0) {
66
            creditors.push({creditAmount, creditorId});
67
        }
68
    }
69

70
    return result;
71
}
72
​
73
int main() {
74
    int n = 3;
75
    vector<vector<int>> transaction = {
76
        {0, 1000, 2000},
77
        {0, 0, 5000},
78
        {0, 0, 0}};
79
​
80
    vector<vector<int>> result = minCashFlow(transaction);
81
    for (int i = 0; i < n; i++) {
82
        for (int j = 0; j < n; j++) {
83
            cout << result[i][j] << " ";
84
        }
85
        cout << endl;
86
    }
87

88
    return 0;
89
}

Output
0 0 3000
0 0 4000
0 0 0
Time Complexity: O(n^2) due to nested loops (where n is the number of friends).
Auxiliary Space: O(n^2) to store the result.

"""















