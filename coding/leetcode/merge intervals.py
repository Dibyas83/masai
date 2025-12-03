
# given a set  intervals,  merge all overlapping interval and return an array of nonoverlapping that
# cover all the intrvals in the input
# sort by first value of pairs

class solut:

    def mergeoverlapping(self,inp_interval: list[list[int]]) -> list[list[int]]:
        inp_interval.sort(key = lambda i: i[0])
        output = [inp_interval[0]]

        for start,end in inp_interval[1:]:
            lastend = output[-1][1] # endvalue of recently added or last element

            if start <= lastend: # if first ele of current pair is less than max of pair in output pairs
                output[-1][1] = max(lastend, end)
            else:
                output.append([start, end])
        return output



interval  = [[1,3], [2,6], [7, 9], [12,14]]
output_interval  = [[1,6], [7, 9], [12,14]]








