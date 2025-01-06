s = str(1122255566788)
print(len(str(s)))
count = 1
end = 0
start = 0

# for i in range(len(str(s))):
for i in range(0,len(s)):
    if s[i] == s[i - 1]:
        count += 1
        end = i
        start = i - count + 1
    print(s[i], start, end, count)

else:
    count = 1
    end = i
    start = i - count + 1
    print(s[i], start, end, count)
    count = 1


print("--------------------------------")
for i in range(0,len(s)):
    if s[i] == "5":
        if s[i] == s[i - 1]:
            count += 1
            end = i
            start = i - count + 1
            #print(s[i], start, end, count)

        else:
            count = 1
            end = i
            start = i - count + 1
            #print(s[i], start, end, count)

    else:
        continue
print(start, end, count)



























