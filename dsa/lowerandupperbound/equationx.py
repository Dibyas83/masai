# Python3 implementation of the approach

# Function to return the minimum positive
# integer satisfying the given equation
def minimumX(a, b, c, k):

	x = 10**9

	if k <= c:
		return 0

	h = k - c
	l = 0

	# Binary search to find the value of x
	while l <= h:
		m = (l + h) // 2
		if (a * m * m) + (b * m) > (k - c):
			x = min(x, m)
			h = m - 1

		elif (a * m * m) + (b * m) < (k - c):
			l = m + 1
		else:
			return m

	# Return the answer
	return x

# Driver code
a, b, c, k = 3, 2, 4, 15
print(minimumX(a, b, c, k))

# This code is contributed by mohit kumar
