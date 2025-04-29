

"""
[Naive Approach] Using Two Nested Loops – O(n^2) time and O(1) space
The idea is to iterate through each train and for that train, check how many other trains have overlappingtimings with it – where current train’s arrival time falls between the other train’s arrival and departure times. We keep track of this count for each train and continuously update our answer with the maximum count found.





# Python program to find minimum Platforms Required
# for Given Arrival and Departure Times

# Function to find the minimum
# number of platforms required
def minPlatform(arr, dep):
    n = len(arr)
    res = 0

    # Run a nested for-loop to find the overlap
    for i in range(n):

        # Initially one platform is needed
        cnt = 1
        for j in range(n):
            if i != j:

                # Increment cnt if trains have overlapping
                # time.
                if arr[i] >= arr[j] and dep[j] >= arr[i]:
                    cnt += 1

        # Update the result
        res = max(cnt, res)
    return res

if __name__ == "__main__":
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    print(minPlatform(arr, dep))

Output
3
[Expected Approach 1] Using Sorting and Two Pointers – O(n log(n)) time and O(1) space
This approach uses sorting and two-pointer to reduce the complexity. First, we sort the arrival and departure times of all trains. Then, using two pointers, we traverse through both arrays.


The idea is to maintain a count of platforms needed at any point in time.

Time      	Event Type      	Total Platforms Needed at this Time
9:00	Arrival	1
9:10	Departure 	0
9:40	Arrival	1
9:50	Arrival	2
11:00	Arrival	3
11:20	Departure 	2
11:30	Departure 	1
12:00	Departure 	0
15:00	Arrival	1
18:00	Arrival	2
19:00	Departure 	1
20:00	Departure 	0
Minimum Platforms needed on railway station = Maximum platforms needed at any time = 3

Step by Step implementation:

Sort the arrival and departure times so we can process train timings in order.
Initialize two pointers:
One for tracking arrivals (i = 0).
One for tracking departures (j = 0).
Iterate through the arrival times:
If the current train arrives before or at the departure of an earlier train, allocate a new platform (cnt++).
Otherwise, if the arrival time is greater than the departure time, it means a train has left, freeing up a platform (cnt--), and move the departure pointer forward (j++).
Update the maximum number of platforms required after each step.
Continue this process until all trains are processed.



# Python program to find minimum Platforms Required
# for Given Arrival and Departure Times

# Function to find the minimum
# number of platforms required
def minPlatform(arr, dep):
    n = len(arr)
    res = 0

    # Sort the arrays
    arr.sort()
    dep.sort()

    # Pointer to track the departure times
    j = 0;

    # Tracks the number of platforms needed at any given time
    cnt = 0;

    # Check for each train
    for i in range(n):

        # Decrement count if other
        # trains have left
        while j < n and dep[j] < arr[i]:
            cnt -= 1
            j += 1

        # one platform for current train
        cnt += 1

        res = max(res, cnt)

    return res

if __name__ == "__main__":
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    print(minPlatform(arr, dep))

Output
3
[Expected Approach 2] Using Sweep line algorithm
The Sweep Line Algorithm is an efficient technique for solving interval-based problems. It works by treating each train’s arrival and departure times as events on a timeline. By processing these events in chronological order, we can track the number of trains at the station at any moment, which directly indicates the number of platforms required at that time. The maximum number of overlapping trains during this process determines the minimum number of platforms needed.


Step by Step implementation:

Create an array v[] of size greater than the maximum departure time. This array will help track the number of platforms needed at each time.
Mark arrivals and departures:
For each arrival time, increment v[arrival_time] by 1, indicating that a platform is needed.
For each departure time, decrement v[departure_time + 1] by 1, indicating that a platform is freed as the train has left.
Iterate through v[] and compute the cumulative sum.
The running sum keeps track of the number of trains present at any given time.
The maximum value encountered represents the minimum number of platforms required.



# Python program to find minimum Platforms Required
# for Given Arrival and Departure Times

# Function to find the minimum
# number of platforms required
def minPlatform(arr, dep):
    n = len(arr)
    res = 0

    # Find the max Departure time
    maxDep = max(dep)

    # Create a list to store the count of trains at each
    # time
    v = [0] * (maxDep + 2)

    # Increment the count at the arrival time and decrement
    # at the departure time
    for i in range(n):
        v[arr[i]] += 1
        v[dep[i] + 1] -= 1

    count = 0

    # Iterate over the list and keep track of the maximum
    # sum seen so far
    for i in range(maxDep + 2):
        count += v[i]
        res = max(res, count)

    return res

if __name__ == "__main__":
    arr = [900, 940, 950, 1100, 1500, 1800]
    dep = [910, 1200, 1120, 1130, 1900, 2000]
    print(minPlatform(arr, dep))


"""


def minPlatform(arr, dep):
    n = len(arr)
    res = 0

    # Sort the arrays
    arr.sort()
    dep.sort()

    # Pointer to track the departure times
    j = 0

    # Tracks the number of platforms needed at any given time
    cnt = 0

    # Check for each train
    for i in range(n):

        # Decrement count if other
        # trains have left
        while j < n and dep[j] < arr[i]:
            cnt -= 1
            j += 1

        # one platform for current train
        cnt += 1

        res = max(res, cnt)

    return res


if __name__ == "__main__":
    n = int(input())
    arr = list(map(str,input().split(" ")))  # Extract the hour part and convert to integer
    for i in range(len(arr)):

        time_str = arr[i]
        hours, minutes = map(int, time_str.split(":"))
        arr[i] = hours + minutes / 60.0
    dep = list(map(str, input().split(" ")))
    for i in range(len(dep)):
        time_str = dep[i]
        hours, minutes = map(int,time_str.split(":"))
        dep[i] = hours + minutes / 60.0

    # arr = [900, 940, 950, 1100, 1500, 1800]
    # dep = [910, 1200, 1120, 1130, 1900, 2000]
    print(minPlatform(arr, dep))

"""
if __name__ == "__main__":
    n = int(input())
    
    arr1 = map(int, input().split(" "))
    arr = list(arr1)
    dep1 = map(int, input().split(" "))
    dep =list(dep1)
    # arr = [900, 940, 950, 1100, 1500, 1800]
    # dep = [910, 1200, 1120, 1130, 1900, 2000]
    print(minPlatform(arr, dep))
"""



