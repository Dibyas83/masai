
# find 3 different ele in array suming to 0.find all permutations 1st

class Solution:
    def threesumm(self,arr):
        arr = [-3,-3,-2,-1,0,1,2,2,3]
        n= len(arr)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    sum = arr[i] + arr[j] + arr[k]
                    if sum == 0 and arr[i] != arr[j] != arr[k]:
                        print(arr[i] , arr[j] , arr[k])


class Solu:
    def threepointersum(self,l: list[int]) -> list[list[int]]: # using 3 pointer moving middle then after sol move midlep to right and rightp to left , when midlep and rightp meet leftp moves to right if same val move anather step to right
        l.sort()
        n = len(l)
        res = []
        for i,a in enumerate(l):  # gives i the index to a all val in list one by one like disct.both i and val changed for next prcess
            print(l)
            print(i,a)
            if i >0 and l[i] == l[i-1]:
                continue
                """#  then use two pointer to adjust sum
                right_p = l[n-1]
                left_p = l[i]
                middle_p = l[i+1]"""
            le,ri = i+1, n -1
            while le < ri:
                threepointersum = a +l[le] + l[ri]
                if threepointersum > 0:
                    ri -= 1
                elif threepointersum < 0:
                    le += 1
                else:
                    res.append([a,l[le], l[ri]])
                    le += 1
                    while l[le] == l[le-1] and le <  ri:
                        le +=1

        return  res


l =[-3,3,6,2,7,1,-4,-2,5]
h = Solu()
print(h.threepointersum(l))

"""
[-4, -3, -2, 1, 2, 3, 5, 6, 7]
0 -4
[-4, -3, -2, 1, 2, 3, 5, 6, 7]
1 -3
[-4, -3, -2, 1, 2, 3, 5, 6, 7]
2 -2
[-4, -3, -2, 1, 2, 3, 5, 6, 7]
3 1
[-4, -3, -2, 1, 2, 3, 5, 6, 7]
4 2
[-4, -3, -2, 1, 2, 3, 5, 6, 7]
5 3
[-4, -3, -2, 1, 2, 3, 5, 6, 7]
6 5
[-4, -3, -2, 1, 2, 3, 5, 6, 7]
7 6
[-4, -3, -2, 1, 2, 3, 5, 6, 7]
8 7
[[-4, -3, 7], [-4, -2, 6], [-4, 1, 3], [-3, -2, 5], [-3, 1, 2]]

"""
class Solt:
    def t3pointersum(self,l: list[int]) -> list[list[int]]: # using 3 pointer moving middle then after sol move midlep to right and rightp to left , when midlep and rightp meet leftp moves to right if same val move anather step to right
        l.sort()
        n = len(l)
        res1 = []
        for i in range(n):
            right_p = n - 1
            left_p = i
            middle_p = i + 1
            if i >0 and l[i] == l[i-1]:
                continue
            while middle_p < right_p:
                threepointersum = l[left_p] +l[middle_p] + l[right_p]
                if threepointersum > 0:
                    right_p -= 1
                elif threepointersum < 0:
                    middle_p += 1
                else:
                    res1.append([l[left_p] , l[middle_p], l[right_p]])
                    middle_p += 1
                    """while l[i] == l[i-1] and middle_p <  right_p:
                        i += 1"""

        return  res1


l =[-3,3,6,2,7,1,-4,-2,5]
h = Solt()
print(h.t3pointersum(l))









