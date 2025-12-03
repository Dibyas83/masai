
#given graph of n nodes with array of edges edges[i] = [a,b] indicating there is edge between a & b
# 0 - 1 - 2    3 - 4 are two components
# keep dooing dfs on nodes which are not visited
# if dfs = true, comp += 1
#-------------------
# anather algorithm is Union find
# par[0,1,2,3,4] par[0,0,0,3,3] rank[1,1,1,1,1]  rank[3,1,1,2,1] noof times it is a parent

class Solu:

    def countcomp(self,n:int,edges: list[list[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1): # find its root parent
            res = n1

            while res != par[res]: # where node itself is its parent or not connected
                par[res] = par[par[res]]
                res = par[res]  # update its curent pointer
            return res

        def unin( n1, n2): #  union their components
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0

            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
        res = n
        for n1, n2 in edges: # going through every edges

            res -= unin(n1, n2)
        return res



n= 5
edges = [[0,1],[1,2],[3,4]]