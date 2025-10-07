def twosum(target,list1):
    num_dict = {}

    for i, num in enumerate(list1):
        comp = target - num
        print(i,num)

        if comp in num_dict:
            return [num_dict[comp],i] # when the comp of 5 came ,comp of 7 ie 5 is already there in dict is found and i  is the index of 7
        num_dict[num] = i
        print("num_dict",num_dict)

    return [] # if not found


list1 =[4,5,6,7]
targ = 12
print(twosum(targ,list1))
