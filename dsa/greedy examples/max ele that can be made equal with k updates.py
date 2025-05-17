

"""
Maximum elements that can be made equal with k updates
Last Updated : 16 Mar, 2025
Given an array of integers and an integer k, the task is to determine the maximum number of equal elements that can be achieved in the array by incrementing its elements. The total number of increments performed across all elements must not exceed k.

Examples:

Input : arr = [ 2, 4, 9 ], k = 3
Output : 2
Explanation: We are allowed to do at most three increments. We can make two elements 4 by increasing 2 by 2. Note that we can not make two elements 9 as converting 4 to 9 requires 5 increments.


Input : arr = [ 1, 2, 3, 4], k = 3
Output : 3
Explanation: You can increment the first element by 2 (to make it 3) and the second element by 1 (to make it 3). This results in the array [3,3,3,4], where 3 elements are equal.


[Naive Approach] Using Recursion – O(n^2) Time
In the naive approach, we check for each element how many other elements can be incremented with the given limit on total increments so that they will become equal to the current element.


[Better Approach] Using Sorting – O(n^2) time and O(1) space
The idea is to sort the array and, for each element at index i, iterate backward from i to the start of the array, incrementing elements to match arr[i] while ensuring the total increments used do not exceed k. By calculating the number of elements that can be made equal to arr[i] within the limit k, we determine the maximum number of equal elements achievable for each i, and finally return the maximum count across all i.


We sort the array so that for each element in the array, the values closest to the current element are incremented. Thus, we can maximize the value count by minimizing the use of k.


Step by step approach:

Sort the array in ascending order.
For each element at index i, iterate backward from i to 0, incrementing elements to match arr[i] while keeping total increments ≤ k.
Track the number of elements that can be made equal to arr[i] within the increment limit k.
Update the maximum count of equal elements found during the process.
Return the maximum count of equal elements after processing the entire array.
C++
// C++ program to find the Maximum elements
// that can be made equal with k updates
#include <bits/stdc++.h>
using namespace std;

int maxEqual(vector<int> &arr, int k) {

    int ans = 0, n = arr.size();

    // Sort the array to make sure
    // closest smaller values are
    // incremented first.
    sort(arr.begin(), arr.end());

    // For each value in arr
    for (int i=0; i<n; i++) {

        int j = i;
        int kUsed = 0;

        // Increment arr[j] to arr[i]
        while (j>=0 && arr[i]-arr[j] <= k - kUsed) {
            kUsed += (arr[i]-arr[j]);
            j--;
        }

        // Number of equal elements will
        // be (i-j);
        ans = max(ans, i-j);
    }

    return ans;
}

int main() {
    vector<int> arr = {1, 2, 3, 4};
    int k = 3;

    cout << maxEqual(arr, k);

    return 0;
}
Java
// Java program to find the Maximum elements
// that can be made equal with k updates
import java.util.Arrays;

class GfG {

    static int maxEqual(int[] arr, int k) {

        int ans = 0, n = arr.length;

        // Sort the array to make sure
        // closest smaller values are
        // incremented first.
        Arrays.sort(arr);

        // For each value in arr
        for (int i = 0; i < n; i++) {

            int j = i;
            int kUsed = 0;

            // Increment arr[j] to arr[i]
            while (j >= 0 && arr[i] - arr[j] <= k - kUsed) {
                kUsed += (arr[i] - arr[j]);
                j--;
            }

            // Number of equal elements will
            // be (i - j);
            ans = Math.max(ans, i - j);
        }

        return ans;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4};
        int k = 3;

        System.out.println(maxEqual(arr, k));
    }
}
Python
# Python program to find the Maximum elements
# that can be made equal with k updates

def maxEqual(arr, k):

    ans = 0
    n = len(arr)

    # Sort the array to make sure
    # closest smaller values are
    # incremented first.
    arr.sort()

    # For each value in arr
    for i in range(n):

        j = i
        kUsed = 0

        # Increment arr[j] to arr[i]
        while j >= 0 and arr[i] - arr[j] <= k - kUsed:
            kUsed += (arr[i] - arr[j])
            j -= 1

        # Number of equal elements will
        # be (i - j);
        ans = max(ans, i - j)

    return ans

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    k = 3

    print(maxEqual(arr, k))
C#
// C# program to find the Maximum elements
// that can be made equal with k updates
using System;

class GfG {

    static int maxEqual(int[] arr, int k) {

        int ans = 0, n = arr.Length;

        // Sort the array to make sure
        // closest smaller values are
        // incremented first.
        Array.Sort(arr);

        // For each value in arr
        for (int i = 0; i < n; i++) {

            int j = i;
            int kUsed = 0;

            // Increment arr[j] to arr[i]
            while (j >= 0 && arr[i] - arr[j] <= k - kUsed) {
                kUsed += (arr[i] - arr[j]);
                j--;
            }

            // Number of equal elements will
            // be (i - j);
            ans = Math.Max(ans, i - j);
        }

        return ans;
    }

    static void Main() {
        int[] arr = {1, 2, 3, 4};
        int k = 3;

        Console.WriteLine(maxEqual(arr, k));
    }
}
JavaScript
// JavaScript program to find the Maximum elements
// that can be made equal with k updates

function maxEqual(arr, k) {

    let ans = 0;
    let n = arr.length;

    // Sort the array to make sure
    // closest smaller values are
    // incremented first.
    arr.sort((a, b) => a - b);

    // For each value in arr
    for (let i = 0; i < n; i++) {

        let j = i;
        let kUsed = 0;

        // Increment arr[j] to arr[i]
        while (j >= 0 && arr[i] - arr[j] <= k - kUsed) {
            kUsed += (arr[i] - arr[j]);
            j--;
        }

        // Number of equal elements will
        // be (i - j);
        ans = Math.max(ans, i - j);
    }

    return ans;
}

let arr = [1, 2, 3, 4];
let k = 3;

console.log(maxEqual(arr, k));

Output
3
[Expected Approach] Using Sorting and Two Pointers – O(n * log n) time and O(1) space
The idea is to sort the array and use a two-pointer sliding window approach to find the largest subarray where all elements can be made equal by incrementing them to the value of the rightmost element, while ensuring the total increments do not exceed k. By maintaining a window and adjusting its size dynamically, we efficiently determine the maximum number of equal elements achievable.


Step by step approach:

Sort the array in ascending order.
Use two pointers, i and j, to represent the current window and maintain a sum of elements in the window.
Expand the window by moving i and add arr[i] to the sum.
If the required increments exceed k, shrink the window by moving j and subtract arr[j] from the sum.
Track the maximum window size where all elements can be made equal within the k limit and return it.
C++
// C++ program to find the Maximum elements
// that can be made equal with k updates
#include <bits/stdc++.h>
using namespace std;

int maxEqual(vector<int> &arr, int k) {

	int n = arr.size();

	// Sort the array to make sure
	// closest smaller values are
	// incremented first.
	sort(arr.begin(), arr.end());

	int j = 0;
	int sum = 0;
	int ans = 0;

	for (int i=0; i<n; i++) {
		sum += arr[i];

		// Increment j till it is possible to
		// increment each value in this subarray
		// to arr[i] within the k limit.
		while (j<i && (i-j+1)*arr[i]>sum+k) {
			sum -= arr[j];
			j++;
		}

		// Compare size of current subarray.
		ans = max(ans, i-j+1);

	}

	return ans;
}

int main() {
	vector<int> arr = {1, 2, 3, 4};
	int k = 3;

	cout << maxEqual(arr, k);

	return 0;
}
Java
// Java program to find the Maximum elements
// that can be made equal with k updates
import java.util.Arrays;

class GfG {

    static int maxEqual(int[] arr, int k) {

        int n = arr.length;

        // Sort the array to make sure
        // closest smaller values are
        // incremented first.
        Arrays.sort(arr);

        int j = 0;
        int sum = 0;
        int ans = 0;

        for (int i = 0; i < n; i++) {
            sum += arr[i];

            // Increment j till it is possible to
            // increment each value in this subarray
            // to arr[i] within the k limit.
            while (j < i && (i - j + 1) * arr[i] > sum + k) {
                sum -= arr[j];
                j++;
            }

            // Compare size of current subarray.
            ans = Math.max(ans, i - j + 1);
        }

        return ans;
    }

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4};
        int k = 3;

        System.out.println(maxEqual(arr, k));
    }
}
Python
# Python program to find the Maximum elements
# that can be made equal with k updates

def maxEqual(arr, k):

    n = len(arr)

    # Sort the array to make sure
    # closest smaller values are
    # incremented first.
    arr.sort()

    j = 0
    sum = 0
    ans = 0

    for i in range(n):
        sum += arr[i]

        # Increment j till it is possible to
        # increment each value in this subarray
        # to arr[i] within the k limit.
        while j < i and (i - j + 1) * arr[i] > sum + k:
            sum -= arr[j]
            j += 1

        # Compare size of current subarray.
        ans = max(ans, i - j + 1)

    return ans

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    k = 3

    print(maxEqual(arr, k))
C#
// C# program to find the Maximum elements
// that can be made equal with k updates
using System;

class GfG {

    static int maxEqual(int[] arr, int k) {

        int n = arr.Length;

        // Sort the array to make sure
        // closest smaller values are
        // incremented first.
        Array.Sort(arr);

        int j = 0;
        int sum = 0;
        int ans = 0;

        for (int i = 0; i < n; i++) {
            sum += arr[i];

            // Increment j till it is possible to
            // increment each value in this subarray
            // to arr[i] within the k limit.
            while (j < i && (i - j + 1) * arr[i] > sum + k) {
                sum -= arr[j];
                j++;
            }

            // Compare size of current subarray.
            ans = Math.Max(ans, i - j + 1);
        }

        return ans;
    }

    static void Main() {
        int[] arr = {1, 2, 3, 4};
        int k = 3;

        Console.WriteLine(maxEqual(arr, k));
    }
}
JavaScript
// JavaScript program to find the Maximum elements
// that can be made equal with k updates

function maxEqual(arr, k) {

    let n = arr.length;

    // Sort the array to make sure
    // closest smaller values are
    // incremented first.
    arr.sort((a, b) => a - b);

    let j = 0;
    let sum = 0;
    let ans = 0;

    for (let i = 0; i < n; i++) {
        sum += arr[i];

        // Increment j till it is possible to
        // increment each value in this subarray
        // to arr[i] within the k limit.
        while (j < i && (i - j + 1) * arr[i] > sum + k) {
            sum -= arr[j];
            j++;
        }

        // Compare size of current subarray.
        ans = Math.max(ans, i - j + 1);
    }

    return ans;
}

let arr = [1, 2, 3, 4];
let k = 3;

console.log(maxEqual(arr, k));

Output
3

"""








