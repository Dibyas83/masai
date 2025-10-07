bag = ""
v = "aeiou"
#s = "adefghii"
def make_perfect_string(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    modified = True
    while modified:

        result = []
        n = len(s)
        for i in range(n):
            if s[i] in vowels:
                if i < n - 1 and s[i + 1] not in vowels:
                    modified = False
                    continue
                else:
                    result.append(s[i])
            else:
                result.append(s[i])
        s1 = ''.join(result)
        print(s1)

s = input()
print(make_perfect_string(s))


