
def solve(n,k,cur,ans):
    if len(ans) == k:
        print(*ans)
        return
    for i in range(cur,n+1): # cur is const before solve
        ans.append(i)
        print(ans)
        print(cur)
        solve(n,k,i+1,ans) # till len is 5 i inc to 4 then cur becomes i+4=5,5 pops and i becomes 6,when i is 10 ans is 1234 after pop, no 11 so again pop and 123 +cur(4)=5 = i,no solving,i inc to 5 and reaches solve to make cur 6 and i again goes inc.so curr inc when i inc before reaching solve
        # actualy i is const after k=5 ,cur inc as i+1,when again out of range it goes to loop

        ans.pop()

n,k = map(int,input().split(" "))
ans =[]*k
print(solve(n,k,1,ans))






