
# given an array of meeting intervals with start and end time, find the min no of rooms required(how many pairs overlap)
# 1-2, 2-3 is non overlapping
"""
1                           6                         -  room1
        3            5                                -  room2
              4                   7                   -  room3
                            6                   9     -  room1
required = 3
 if i.start < min(endlist)
    room += 1

endlist = endlist.append(i.end)
"""
class Interval(object):  # list f intervals as object(two member start and end)
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solut:

    def meeting(self,intervals):
        intervals.sort(key= lambda i: i.start)
        room = 0
        endlist = []

        for i in range(1,len(intervals)): # compare index 1 with prev index
            i1 = intervals[i-1] # prev
            i2 = intervals[i] # curr
            endlist = endlist.append(i1.end)

            if  i2.start < min(endlist):
                room += 1
            # if not go to next iter
        return room




print("============================================================")
class Interval2(object):  # list f intervals as object(two member start and end)
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solut2:

    def meeting2(self,intervals):
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)

        rooms, count = 0, 0 # max no of rooms and count
        s,e = 0,0

        while s < len(intervals):

            if start[s] < end[e]:
                s += 1
                count += 1 # for ist meet 1 room ,if again for next meet start time is lees than 1st meet end time it will require anather room
            else:
                e += 1
                count -= 1
            rooms = max(rooms,count)

        return rooms




inp=[[0,30], [5,10], [15,20]]
output = 3

