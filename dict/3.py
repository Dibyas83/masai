

def stri(n,m ,st1,st2):
    freq = {}
    n = int(input())
    m = int(input())
    target_st = input().strip()
    st2 = input().strip()

    from collections import Counter
    target_st_count = Counter(target_st)
    st2_count =Counter(st2)
    print(target_st_count)


    for char in target_st_count:
        print(target_st_count[char])
        print(st2_count.get(char,0))
        if target_st_count[char] > st2_count.get(char,0):
            print("no")
            return
    print("yes")





n =4
m = 8
st1 = "qwer"
st2 = "qwerqwer"
stri(n,m,st1,st2)















