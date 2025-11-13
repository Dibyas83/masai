
# find a target in logn time in a rotated array
# if the middle is bigeer than first ele and
# if middle is < target thenfind on right. if middle > target then compare to the first element if target is even smaller search from middle +1,if target is bigger than first ele search bet first and middle-1
# if the middle is smaller than first ele and
# if middle is < target then find on last if bigger (search bet first and middle-1) if smaller see bet mid +1 and last . if middle > target then compare to the first element and  middle -1

# [4,5,6,7,0,1,2]
class Solut:
    def search(self, nums: list[int],target: int) -> int:
        l, r = 0, len(nums)

        while l <= r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid

            # case 1
            if nums[l] <= nums[mid] :
                if target > nums[mid] or target < nums[l]:
                    left = mid+1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else: # target > mid ,but < right
                    l = mid+1
        return -1




















