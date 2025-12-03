
# given an array of meeting intervals with start and end time, determine if a person can attend all meetings,
# only possible if nonoverlapping
# 1-2, 2-3 is non overlapping
class Interval(object):  # list f intervals as object(two member start and end)
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solut:

    def meeting(self,intervals):
        intervals.sort(key= lambda i: i.start)

        for i in range(1,len(intervals)): # compare index 1 with prev index
            i1 = intervals[i-1] # prev
            i2 = intervals[i] # curr

            if i1.end > i2.start:
                return False
            # if not go to next iter
        return True






inp=[[0,30], [5,10], [15,20]]
output = False

