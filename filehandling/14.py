def inter_sec2():

    T = int(input())
    for _ in range(T):
        N = int(input())
        ct = [0]
        arrA = list(input().split(" "))
        arrA = list(map(int,arrA))
        print(arrA)
        print(len(arrA))
        for i in range(1,N):
            if arrA[i] > arrA[i-1] and arrA[i] > ct[-1]:

                #ct.append(arrA[i-1])
                ct.append(arrA[i])
               #if arrA[i+1] > arrA[i]:
                   # ct.append(arrA[i+1])



            #for m in arrA:
                #if arrA[i] > m in arrA:
        #ct.append(arrA[arrA.index(ct[1])-1])
        ct.insert(0,arrA[arrA.index(ct[1])-1])
        ct.remove(0)
        print(ct)

inter_sec2()








