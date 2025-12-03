
#  give n input nodes 0 to (n-1) and list of unidirected edges(in both directions)

"""
        o                   o                               o
      /   \              /     \                          /
    o      0            o ----- o not tree               o      o not tree every node needs to connected and no loop
"""
# using edges we create adjacency list or a tree.
# using dfs we recursively visit neighbors,if visited = nodes given it is tree,if visited is again a 0 we stop

# starting from 0(added to visit set) we move to neighbor which is not in visited sed,we add link of prev=0 at 1
# and got to 4 where prev = 1 and 1 and 4 added to visited ,4 has no neighbor except prev so return to 0.
# at start 0 will have prev of -1.
# memory will have nodes + edges =O(e + nodes)
# empty is a tree

class Sol:

    def validtree(self,n,edges):
        if not n:
            return  True

        adj = { i:[] for i in range(n)} # paired list to form tree
        for n1, n2 in edges:   # bidirectional
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):  # detecting loop or cycle
            if i in visit:
                return False
            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue

                if not dfs(j, i): # i is the prev, checks future
                    return False # if dfs(j,i) does not return false and stop
            print(adj)
            print(visit)
            return  True

        return dfs(0, -1) and n == len(visit) # checks if all nodes are connected

edges = [[0,1],[0,2],[0,3],[1,4],[2,3]]
n=6
d=Sol()
print(d.validtree(n, edges))











