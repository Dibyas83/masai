N= 6
no_of_gas_station = N
cost_gas = gas = 5
init = 0
listgasavailable=[1,2,3,4,5,6] # on each station serially
listofgasreqtonextstation =[2,4,5,1,2,8]
# so only in 4th station enough gas is available to go to next station
start = [0]
gas_in_tank = 0
for i in range(6):

    if listgasavailable[i] > listofgasreqtonextstation[i]:
        print(i)
        init = i
        print(init)
        break
for i in range(init,N):
    gas_in_tank = gas_in_tank - listofgasreqtonextstation[i] + listgasavailable[i]
    if gas_in_tank >= 0:
        print(i)

    else:
        break
for i in range(0,(N-init+1)):

    gas_in_tank = gas_in_tank - listofgasreqtonextstation[i] + listgasavailable[i]
    if gas_in_tank > 0:
        print(i)
    else:
        break





















