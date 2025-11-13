
# there is a 5 roads for 5 cities  ,no loops, all connected
# we have to make sure all are connected to 0
"""
    ->    1   ->   3   <-  2
0

    <-     4     ->      5
"""
# strting from 0 see if its neighbor are connected to it ,if not make direction of road to it
# then check if 1 and 4 neighbor reach 1 & 4 , .......

class Solut:  # start at city 0,recursively check if its edges are outgoing,count outgoing edges
    def replace_withmax_ofrest(self,n: int, connections: list[list[int]]) -> int:
        edges = {(a,b) for a,b in connections}  # set comprehensions,if city a can reach city b a->b
        neighbors = {city:[] for city in range(n)}  # hash map using dictionary comprehension there may be list of neaighbors
        visit = set()
        changes = 0
        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        #write a function to traverse the graph recursively dfs
        def dfs(city):
            nonlocal edges, neighbors, visit, changes
            for neighbor in neighbors[city]: # starts from city 0 check if its neighbor reaches it
                if neighbor in visit:
                    continue
                # check if neighbor can reach city 0
                if (neighbor, city) not  in edges:  # if they are as a,b (neig->city) not b,a
                    changes += 1
                visit.add(neighbor)
                # to see if neighbors neighbor can reach city 0 ,for that its neighbor must reach itself
                dfs(neighbor)
            visit.add(0) # city 0 is the first city visited
            dfs(0)  # check by starting from city 0
            return  changes



