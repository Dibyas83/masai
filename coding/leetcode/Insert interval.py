
# given a set of non overlapping intervals, insert or merge a new interval into the intrvals
# assume interval were sorted according to their start times.

class Solu:

    def insert(self,intervals: list[list[int]], new_interv: list[int]) -> list[list[int]]:
        res = []

        for i in range(len(intervals)):
            if new_interv[1] < intervals[i][0]: # no overlapping and less
                res.append(new_interv)
                return  res + intervals[i:]
            elif new_interv[0] > intervals[i][1]: # not overlapping and bigger
                res.append(intervals[i]) # add only the ith element of interval which is less
            else:
                new_interv = [min(new_interv[0],intervals[i][0]), max(new_interv[1],intervals[i][1])]

        res.append(new_interv)
        return res








interval  = [[2,4], [6, 9]]
new_int = [3,5]  # 1   3 and 2  5  overlap, take min and max of overlaping pair
# if new int was [0,1] -> [[0,1], [2,4], [6, 9]]
# if new int was [0,5] -> [[0,5], [6, 9]]