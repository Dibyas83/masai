
"""

Given a 2D array jobs[][] of order n*3, where each element jobs[i] defines start time, end time, and the profit associated with the job. The task is to find the maximum profit you can take such that there are no two jobs with overlapping time ranges.

Note: If the job ends at time X, it is allowed to choose another job that starts at time X.

Examples:

Input: jobs[][] = [[1, 2, 50],
                             [3, 5, 20],
                             [6, 19, 100],
                             [2, 100, 200]]
Output: 250
Explanation: The first and fourth jobs with the time range [1, 2] and [2, 100] can be chosen to give maximum profit of 50 + 200 = 250.


Input: jobs[][] = [[1, 3, 60],
                             [2, 5, 50],
                             [4, 6, 70],
                             [5, 7, 30]]
Output: 130
Explanation: The first and third jobs with the time range [1, 3] and [4, 6] can be chosen to give maximum profit of 60 + 70 = 130.


Table of Content

[Naive Approach] – Using Recursion – O(n ^ n) Time and O(1) Space
[Expected Approach – 1] – Using Memoization – O(n ^ 2) Time and O(n) Space
[Expected Approach – 2] – Using Tabulation – O(n * n) Time and O(n) Space
[Optimized Approach – 1] – Using Binary Search with Tabulation – O(n * log(n)) Time and O(n) Space
[Optimized Approach – 2] – Using Binary Search with Memoization – O(n * log(n)) Time and O(n) Space
[Naive Approach] – Using Recursion – O(n ^ n) Time and O(n) Space
The idea is to schedule the jobs in all possible ways using recursion and find the profit associated with each scheduling, the maximum among them is the result. To do so, sort the jobs in ascending order based on their start time and for each job, consider the job’s profit, and find the maximum profit from all the next non-overlapping jobs i.e. maxProfit(i, jobs) = max(maxProfit(j, jobs)), where i < j < n.





1
# Python program to implement
2
# Weighted Job Scheduling
3
​
4
# Recursive function to find the maximum
5
# profit from weighted job scheduling
6
def maxProfitRecur(jobs, ind, last):
7
    if ind == len(jobs):
8
        return 0
9
​
10
    # skip the current job
11
    ans = maxProfitRecur(jobs, ind + 1, last)
12
​
13
    # if start of current is greater than or
14
    # equals to end time of previous job
15
    if jobs[ind][0] >= last:
16
        ans = max(ans, jobs[ind][2] +
17
              maxProfitRecur(jobs, ind + 1, jobs[ind][1]))
18
​
19
    return ans
20
​
21
# Function to find the maximum profit
22
# from weighted job scheduling
23
def maxProfit(jobs):
24

25
    # Sort the jobs based on start time
26
    jobs.sort()
27
​
28
    return maxProfitRecur(jobs, 0, -1)
29
​
30
if __name__ == "__main__":
31
    jobs = [
32
        [1, 2, 50],
33
        [3, 5, 20],
34
        [6, 19, 100],
35
        [2, 100, 200]
36
    ]
37
    print(maxProfit(jobs))

Output
250
[Expected Approach – 1] – Using Memoization – O(n ^ 2) Time and O(n) Space
The above approach can be optimized using memoization to avoid computing the overlapping subproblems multiple times. To do so, create an array memo[] of size n, where each element memo[i] stores the maximum possible profit for jobs in range [i, n-1]. For each recursive call, check if the subproblem is already computed, if so return the stored value, else proceed similar to above approach.





1
# Python program to implement
2
# Weighted Job Scheduling
3
​
4
# Recursive function to find the maximum
5
# profit from weighted job scheduling
6
def maxProfitRecur(jobs, ind, last, memo):
7
    if ind == len(jobs):
8
        return 0
9
​
10
    # if the job can be taken
11
    if jobs[ind][0] >= last:
12
​
13
        # if the value is not calculated
14
        if memo[ind] == -1:
15
​
16
            # take the job
17
            memo[ind] = jobs[ind][2] + \
18
                maxProfitRecur(jobs, ind + 1, jobs[ind][1], memo)
19
​
20
            # leave the job and find max
21
            memo[ind] = max(memo[ind],
22
                      maxProfitRecur(jobs, ind + 1, last, memo))
23
​
24
        return memo[ind]
25
​
26
    # if the job can't be taken
27
    return maxProfitRecur(jobs, ind + 1, last, memo)
28
​
29
# Function to find the maximum profit
30
# from weighted job scheduling
31
def maxProfit(jobs):
32

33
    # Sort the jobs based on start time
34
    jobs.sort()
35
​
36
    # create memoization array and
37
    # initialize it with -1
38
    memo = [-1] * len(jobs)
39
​
40
    return maxProfitRecur(jobs, 0, -1, memo)
41
​
42
if __name__ == "__main__":
43
    jobs = [
44
        [1, 2, 50],
45
        [3, 5, 20],
46
        [6, 19, 100],
47
        [2, 100, 200]
48
    ]
49
    print(maxProfit(jobs))

Output
250
[Expected Approach – 2] – Using Tabulation – O(n * n) Time and O(n) Space
The above approach can further be optimized using bottom-up dp (tabulation) to minimize the space required for recursive stack. To do so, create an array dp[] of size n, where each element dp[i] stores the maximum possible profit for jobs in range [i, n-1]. Start from the last index i.e. n-1, and for each index i compute the maximum profit for subarray i to n-1 and store the result in dp[i]. The maximum of all the values stored in dp[] is the result.





1
# Python program to implement
2
# Weighted Job Scheduling
3
​
4
# Function to find the maximum profit
5
# from weighted job scheduling
6
def maxProfit(jobs):
7
    n = len(jobs)
8
​
9
    # Sort the jobs based on start time
10
    jobs.sort()
11
​
12
    # create a dp table
13
    dp = [0] * n
14
​
15
    # stores the maximum profit
16
    res = 0
17
​
18
    # iterate over all the jobs
19
    for i in range(n - 1, -1, -1):
20
        dp[i] = jobs[i][2]
21
​
22
        # find the maximum profit
23
        for j in range(i + 1, n):
24
            if jobs[i][1] <= jobs[j][0]:
25
                dp[i] = max(dp[i], dp[j] + jobs[i][2])
26
​
27
        res = max(res, dp[i])
28
​
29
    return res
30
​
31
if __name__ == "__main__":
32
    jobs = [
33
        [1, 2, 50],
34
        [3, 5, 20],
35
        [6, 19, 100],
36
        [2, 100, 200]
37
    ]
38
    print(maxProfit(jobs))

Output
250
[Optimized Approach – 1] – Using Binary Search with Tabulation – O(n * log(n)) Time and O(n) Space
In above approach, for each index i, we are iterating from index i + 1 to n-1 to find the job with greater start time and maximum profit. As the jobs are sorted in ascending order, instead of iterating over all the elements we can perform binary search to find the index of the job with start time greater than or equal to end time of current job. Now dp[i] will store the maximum of dp[i] and dp[i+1]. And the final result will be stored in dp[0].





1
# Python program to implement
2
# Weighted Job Scheduling
3
​
4
# Function to find the closest next job.
5
def findNextJob(i, jobs):
6
    end = jobs[i][1]
7
    ans = len(jobs)
8
    s, e = i + 1, len(jobs) - 1
9
    while s <= e:
10
        mid = s + (e - s) // 2
11
        if jobs[mid][0] >= end:
12
            ans = mid
13
            e = mid - 1
14
        else:
15
            s = mid + 1
16
    return ans
17
​
18
# Function to find the maximum profit
19
# from weighted job scheduling
20
def maxProfit(jobs):
21
    n = len(jobs)
22
​
23
    # Sort the jobs based on start time
24
    jobs.sort()
25
​
26
    # create a dp table
27
    dp = [0] * n
28
​
29
    # iterate over all the jobs
30
    for i in range(n - 1, -1, -1):
31
        dp[i] = jobs[i][2]
32
​
33
        # find the index of next job
34
        next = findNextJob(i, jobs)
35
​
36
        # if next job exists
37
        if next < n:
38
            dp[i] += dp[next]
39
​
40
        # store the maximum profit
41
        if i < n - 1:
42
            dp[i] = max(dp[i], dp[i + 1])
43
​
44
    return dp[0]
45
​
46
if __name__ == "__main__":
47
    jobs = [
48
        [1, 2, 50],
49
        [3, 5, 20],
50
        [6, 19, 100],
51
        [2, 100, 200]
52
    ]
53
    print(maxProfit(jobs))

Output
250
[Optimized Approach – 2] – Using Binary Search with Memoization – O(n * log(n)) Time and O(n) Space
Similar to the above approach, binary search can be implemented on memoization approach to reduce the iterative calls. This approach has been discussed in artice Weighted Job Scheduling in O(n Log n) time.


"""








