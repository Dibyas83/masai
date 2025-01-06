bag = ""
v = "aeiou"
#s = "adefghii"
def make_perfect_string(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
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




