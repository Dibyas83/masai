# by brute force check every , every point has two choices to include or not 2*2*2*2 =2^n
# DFS by cache            1       2     4     3
# [1,2,4,3]      1,2    1,4   1,3        -  2,4,3 are greater than 1
#         1,2,4  1,2,3                   -  4,3  are greater than 2
# no ele greater than 4 or after 3
# start at last index 3 ,longest seq = 1
#  at last index 2 ,longest seq = 1 + if num[2] < num[3]
#  at last index 1 ,longest seq = max(1 , 1+ num[2] ,1+ num[3])=2
#  at last index 0 ,longest seq = max(1 , 1+ num[2] ,1+ num[3], 1+ num[1])
# O(n^2)

class Solut:
    def length_inc_sub(self, nums: list[int]) -> int:
        n= len(nums)
        res = [1] * n # cache of list initialized to 1

        for i in range(n-1,-1,-1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    res[i] = max(res[i], 1 + res[i])
        return  max(res)










