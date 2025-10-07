
ln = int(input())
test_case= int(input())
for i in range(test_case):
    s = input()
max_len = 0
curr_len = 0
for char in s:
    if char == '0':
        curr_len += 1
    else:
        max_len = max(max_len,curr_len)
        curr_len = 0

max_len = max(max_len,curr_len)
print(max_len)







