vowels = {'a', 'e', 'i', 'o', 'u'}
s= "asshole"
modified = True
while modified:
    modified = False
    result = []
    n = len(s)
    for i in range(n):
        if s[i] in vowels:
            if i < n - 1 and s[i + 1] not in vowels:
                modified = True
                continue
            else:
                result.append(s[i])
        else:
            result.append(s[i])
    s = ''.join(result)
print(s)
# write your code here

