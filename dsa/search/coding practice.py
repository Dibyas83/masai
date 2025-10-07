"""
n - problems
limit m days and t time limit per day (try to dec the t by guessing a mid)
times - set of time taken for each problem

"""

def  min_timereq(problems, m ,mid):
    days_needed = 1
    curr_time = 0

    for time in problems:
        if time > mid:
            return False
        if curr_time + time > mid:
            days_needed += 1
            curr_time = time # starts with same problem
            if days_needed > m:
                return False
        else:
            curr_time += time

    return days_needed <= m

def min_t( m, problems):
    left, right = 0, sum(problems)
    result = right
    print(right)

    while left <= right:  # untill left reaches right
        print("l",left)
        print("r",right)
        mid = left + (right-left) // 2
        print(mid)
        if min_timereq(problems, m, mid):

            result = mid
            right = mid - 1 # dec daily time limit
        else:
            left = mid + 1 # inc daily time limit
    print(result)


def inp():
    m = int(input())
    problems = list(map(int,input().split(" ")))
    print(min_t(m, problems))

inp()


"""
4
1 2 3 4 5 5
5
10
7
6
6
None

4
1 2 2 2 2 2 2 2 2 2 2 2 2
ans
4
1 2 2 2 2 2 2 2 2 2 2 2 2
2
12
8
7
7
None
"""


