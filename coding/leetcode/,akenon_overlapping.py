
# given a set  intervals,  remove min intervals to return an array of nonoverlapping that
# make them sorted
# if last of one pair = first of next non overlapping
"""
1             ---           3
             2   -    -     3
1   -- --    2              3      -     4


"""
class solut:

    def remove_overlapping(self,intervals: list[list[int]]) -> int:
        intervals.sort()
        res = 0 # no of removals
        prev_end = intervals[0][1]  # starting pairs 2nd element
        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end # update prev for next matching
            else: # if overlapped
                res += 1
                prev_end = min(end,prev_end)
        return  res



interval  = [[1,2], [2,6], [3,4], [1,3]]
output_interval  = 1









