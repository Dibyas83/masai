

def solve(n,k,arr,curr,ans,res,idx):
    if curr > k:
        return
    if curr == k:
        res.append(ans[:])
        print(res,"res")
        return
    for i in range(idx,n):
        print(ans,"ans")
        ans.append(arr[i])
        solve(n,k,arr,curr + arr[i],ans,res, i) # finds cur sum,only processes,if greater or equal it returns to curr and pops.
        # when curr>=k it come to pops after succesfully processing if less it goes into loop again

        print(curr,"curr")
        p=ans.pop() # if solves then
        print(p,"pop")


if __name__=="__main__":
    n,c= map(int,input().split(" "))
    arr = list(map(int,input().split(" ")))
    ans = []
    res = []
    solve(n,c,arr,0,ans,res,0)
    if not res:
        print(-1)
    else:
        res = sorted(res)
        for comb in res:
            print(" ".join(map(str,comb)))

# if freq of one candy is different from the curr combi it is unique
# input arr is sorted in ascending
# arrr of cost of candies








