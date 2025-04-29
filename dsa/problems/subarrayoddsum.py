
# Python 3 program to
# find count of sub-arrays
# with odd sum
def countOddSum(ar, n):

    # A temporary array of size
    # 2. temp[0] is going to
    # store count of even subarrays
    # and temp[1] count of odd.
    # temp[0] is initialized as 1
    # because there is a single odd
    # element is also counted as
    # a subarray
    temp = [ 1, 0 ]

    # Initialize count. sum is sum
    # of elements under modulo 2
    # and ending with arr[i].
    result = 0
    val = 0

    # i'th iteration computes
    # sum of arr[0..i] under
    # modulo 2 and increments
    # even/odd count according
    # to sum's value
    for i in range(n):
        # 2 is added to handle
        # negative numbers
        val = ((val + ar[i]) % 2 + 2) % 2
        # Increment even/odd count
        temp[val] += 1

    # An odd can be formed
    # by even-odd pair
    result = (temp[0] * temp[1])

    return result

def inpt():

        n = int(input())
        ar = list(map(int, input().split(" ")))
        print(str(countOddSum(ar, n)))
inpt()







