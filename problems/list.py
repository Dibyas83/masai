li =[4,7,8,3,2,4,5]
print(li[0])
print(li[1])

my_list = [1, 2, 3, 4, 5]
string_list = [str(element) for element in my_list]
result_string = ", ".join(string_list)
print(result_string)

list_of_strings = ['1', '2', '3', '4', '5']

string_of_digits = "".join(list_of_strings)

final_integer = int(string_of_digits)

print(final_integer)

#-------------

list_of_integers = [1, 2, 3, 4, 5]

string_of_integers = "".join(map(str, list_of_integers))

final_integer = int(string_of_integers)

print(final_integer)

#-----------
time_str = "9:00"
hour = int(time_str.split(":")[0])  # Extract the hour part and convert to integer
time_float = float(hour)  # Convert the hour to a float
print(time_float)

#---------
time_list = ["9:00", "10:30", "12:45"]

for i in range(len(time_list)):
    time_str = time_list[i]
    hours, minutes = map(int, time_str.split(":"))
    time_list[i] = hours + minutes / 60.0

print(time_list)
# Expected output: [9.0, 10.5, 12.75]

#-----------
positive_infinity = float('inf')
negative_infinity = float('-inf')

print(positive_infinity) # Output: inf
print(negative_infinity) # Output: -inf

import math

positive_infinity = math.inf
print('Positive Infinity: ', positive_infinity)

negative_infinity = -math.inf
print('Negative Infinity: ', negative_infinity)















