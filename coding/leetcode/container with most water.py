
# [1,7,2,3,2,6,8] these are y coordinates and  their indexes give x coordinates find the max area
# covered by a container with these coordinates ,and those coordinates

# BRUTE FORCE
class Solut:
    def maxarea(self,height: list[int]) -> int:
        res = 0
        for l in range(len(height)):
            for r in range(l+1,len(height)):
                area = (r-l) * min(height[l], height[r])
                res = max(res, area)

        return res

# linear time sol - two pointer

class Solut2:
    def maxarea(self,height: list[int]) -> int:
        res=0
        n = len(height)
        l,r = 0, n-1
        while l < r:
            area = (r-1) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
               l += 1
            else:
               r -= 1
        return res





