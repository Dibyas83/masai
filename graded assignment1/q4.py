tank = 0
N=5
gas = [1,2,3,4,5]
cost =[3,4,5,1,2]
for i in range(0,N):
    if  tank + gas[i] >= cost[i] :
        tank =tank + gas[i] - cost[i]
        print(i)
        print(tank)











