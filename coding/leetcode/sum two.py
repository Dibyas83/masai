def twosum(target,list1):
    num_dict = {}

    for i, num in enumerate(list1): # values were enumerated or indexed i changes as index
        comp = target - num
        print(i,num)

        if comp in num_dict:
            return [num_dict[comp],i] # when the comp of 5 came 7 was not in dict yet ,when finding comp of 7 ie 5 is already there in dict is found and i  is the index of 7
        num_dict[num] = i
        print("num_dict",num_dict)

    return [] # if not found


list1 =[4,5,6,7]
targ = 12
print(twosum(targ,list1))

class sollu:
    def t2sum(self, l: list[int],targ: int) -> list[int]: # eliminating from end right pointer moves left
        # to dec or movw left pointer to right to inc(not right pointer to right-limit cross )
        i,n1 = 0,len(l)
        while i < n1:
            currsum = l[i] + l[n1]
            if currsum > targ:
                n1 -= 1
            elif currsum < targ:
                i += 1
            else:
                return [i+1,n1+1]
        return []



