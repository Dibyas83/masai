
# increase until there is pos no,
# - * - is +, again - it becomes +

# we maintain both -(min) and +(max) val ,if next no is neg it gives + res(with min), if pos it gives pos(with max)
# if 0 make it 1

class Solut:
    def maxprodsubarr(self, nums: list[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            if n==0:
                curMin, curMax = 1, 1
                continue
            temp = curMax*n
            curMax = max(n * curMax,  n * curMin, n) #[-1,8] if next no is -1 they become min,then comes 8 so 8 is the max
            curMin = min(n * temp,  n * curMin, n) #[-1,-8] temp is the unchanged max
            res = max(res, curMax)
        return res








