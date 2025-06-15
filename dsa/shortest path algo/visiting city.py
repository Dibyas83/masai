
import heapq

def min_distance(n,m,highway):
    g = [[] for _ in range(n+1)] # create adjacency list for the graph
    for x in highway:
        g[x[0]].append(x[1,x[2]]) # add edges to the graph,x[0] is src,x[1] is the cost or weight edge
    pq = [(0,1)] # priority que to store nodes ,starting from city 1 with distance 0
    vis = [-1]* n # list to store visited cities and their distances,initialize to -1

    while pq:
        cost,node = heapq.heappop(pq) # get the city with the smallest distance from priorty que
        if vis[node - 1] !=-1: # if the city already visited skip
            continue

        vis[node-1] = cost # mark the curr city as visited with the  curr distance
        # traverse the neighboring cities and update their distances
        for dest,weight in g[node]:
            if vis[dest-1] == -1 or vis[dest-1] > cost + weight: # curr calculated weight is less than previously calculated
                heapq.heappush(pq,(cost + weight , dest)) # add the  neighboring city to priorty que

    return vis # return list of distances from city 1 to all other cities

n,m = map(int,input().split(" "))
highway = []
for _ in range(m):
    highway.append(list(map(int,input().split(" "))))

# calculate min distance using dijkstra algorithm
ans = min_distance(n,m,highway)

#output the distance
print(" ".join(map(str,ans)))
















