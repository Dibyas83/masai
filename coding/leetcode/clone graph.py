
# given a ref of a node in a connected undirected graph,return a deep copy of graph
# each node has a ref to its val and its neighbors
# so we have to go through each node

# hashmap - ceate old and new, create double directed edges
class Node:
    def __init__(self, val = 0,neighbors = None):
        self.val = val
        self.neighbors= neighbors


class Sole:
    def clonegraph(self, node: 'Node') -> 'Node':
        oldtonew = {} # mapping in dict

        def dfs(node):
            if node in oldtonew:
                return oldtonew[node]
            copy = Node(node.val) # create a copy using class Node
            oldtonew[node] = copy
            for neigh in node.neighbors: # this will find neighbors neighbor
                copy.neighbors.append(dfs(neigh))  # ref to neighbors created
            return copy

        return dfs(node) if node else None



