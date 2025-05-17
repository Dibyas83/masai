
def max_gem(c,gems):
    gems.sort(key = lambda x: x[0] / x[1], revers = True) # sorted by ratio of val/weight in desc order
    total_value = 0.0
    curr_weight = 0
    for value,weight in gems:
        if curr_weight + weight <= c:
            total_value += value
            curr_weight += weight
        else:
            available_space = c - curr_weight
            total_value += value *(available_space/weight)
            break
    return
if __name__ == "__main__":
    c = int(input())
    n = int(input())
    values = list(map(int,input().split(" ")))
    weights = list(map(int,input().split(" ")))
    gems = [(values[i],weights[i]) for i in range(n)]
    res = max_gem(c,gems)
    print(res)





