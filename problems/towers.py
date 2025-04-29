def calculate_range(heights):
    """
    Calculates the transmission range for each tower, considering blockage
    from taller or equal towers to the left.

    Args:
        heights: A list of integers representing the heights of the towers.

    Returns:
        A list of integers representing the transmission range for each tower.
    """
    n = len(heights)
    ranges = [] * n

    for i in range(n):

        ranges_to_left = 0
        for j in range(i-1,-1,-1):

            if j == 0 and heights[j] <= heights[i]:
                ranges_to_left += 1

            if heights[j] > heights[i]:
                ranges_to_left += 1
                break
            elif heights[j] <= heights[i]:
                ranges_to_left += 1

        ranges.append(ranges_to_left)
    ranges[0] = 1

    return ranges

def inpt():
    t = int(input())
    for _ in range(t):
        n = int(input())
        heights = list(map(int, input().split(" ")))
        transmission_ranges = calculate_range(heights)
        string_list = [str(element) for element in transmission_ranges]
        result_string = " ".join(string_list)
        print(result_string)
inpt()
"""
my_list = [1, 2, 3, 4, 5]
string_list = [str(element) for element in my_list]
result_string = ", ".join(string_list)
print(result_string)

# Example usage:
tower_heights = [5, 3, 6, 8, 2, 7]
transmission_ranges = calculate_range(tower_heights)
print(f"Tower Heights: {tower_heights}")
print(f"Transmission Ranges: {transmission_ranges}")
"""





