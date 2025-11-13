
# to solve in binary algo we  need to have sorted array ,but it is rotated
# it was once sorted,using two pointer to find  where it stops increasing,
# take middle as right pointer if increasing ,go to right.if dec go to left

class Solut:
    def findmin(self, nums: list[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) -1

        while l <= r:
            if nums[l] < nums[r]: # means sorted
                res = min(res, nums[1])
                break
            m = (l+r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]: # part of rotated portion
                l = m +1
            else:
                r = m-1
        return res









