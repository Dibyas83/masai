
"""

def all_construct(target, word_bank):
    if target == "":
        return [[]]

    total_ways = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank)
            target_ways = [[word] + way for way in suffix_ways] # first the word minused then from wordbank
            total_ways.extend(target_ways)

    return total_ways

print(all_construct("abcdef", ["ab", "abc", "cdef", "def", "cd", "ef"]))
"""
def ways2d(target,wordbank,count):
    if target == "":
        return  [[]]
    for word in wordbank:
        if target[0] == word[0]:
            suffix = target[len(word):]
            twodways = ways2d(suffix,wordbank,count)

    return count

print(ways2d("abcdef",["ab","abc","cdef","def","cd","ef"],0))
print(ways2d("abcdef",["ab","abc","cd","de","ef"],0))
# m (height)char in word and n or > m words to compare in  wordbank = n**m.space is m**2


"""
def mways(target,wordbank,memo):
    if target in memo:
        return memo[target]
    if target in wordbank:
        return [[]]
    total_ways = []
    for word in wordbank:
        if target[0] == word[0]:
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, wordbank)
            target_ways = [[word] + way for way in suffix_ways]  # first the word minused then from wordbank
            total_ways.extend(target_ways)

    memo[target] = total_ways
    return total_ways
#memo = {} # its storing true or false for other examples, which may return false values
# check in tutor
print(mways("abcdef",["ab","abc","cdef","def","cd","ef"],memo={}))
print(mways("abcdef",["ab","abc","cd","abcd"],memo={}))





s = "shfghgsh"
print(s[2:6])
"""
"""
/**
 * This topological sort implementation takes an adjacency list of an acyclic graph and returns an
 * array with the indexes of the nodes in a (non unique) topological order which tells you how to
 * process the nodes in the graph. More precisely from wiki: A topological ordering is a linear
 * ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes
 * before v in the ordering.
 *
 * <p>Time Complexity: O(V + E)
 *
 * @author William Fiset, william.alexandre.fiset@gmail.com
 */
"""

from collections import defaultdict
from typing import List, Dict, Optional

class Edge:
    def __init__(self, f: int, t: int, w: int):
        self.from_node = f
        self.to = t
        self.weight = w
"""
 // Helper method that performs a depth first search on the graph to give
  // us the topological ordering we want. Instead of maintaining a stack
  // of the nodes we see we simply place them inside the ordering array
  // in reverse order for simplicity.
"""
def dfs(i: int, at: int, visited: List[bool], ordering: List[int], graph: Dict[int, List[Edge]]) -> int:
    visited[at] = True
    edges = graph.get(at)

    if edges is not None:
        for edge in edges:
            if not visited[edge.to]:
                i = dfs(i, edge.to, visited, ordering, graph)

    ordering[i] = at
    return i - 1
"""
 // Finds a topological ordering of the nodes in a Directed Acyclic Graph (DAG)
  // The input to this function is an adjacency list for a graph and the number
  // of nodes in the graph.
  //
  // NOTE: 'numNodes' is not necessarily the number of nodes currently present
  // in the adjacency list since you can have singleton nodes with no edges which
  // wouldn't be present in the adjacency list but are still part of the graph!
  //
"""
def topological_sort(graph: Dict[int, List[Edge]], num_nodes: int) -> List[int]:
    ordering = [0] * num_nodes
    visited = [False] * num_nodes
    i = num_nodes - 1

    for at in range(num_nodes):
        if not visited[at]:
            i = dfs(i, at, visited, ordering, graph)

    return ordering
"""
 // A useful application of the topological sort is to find the shortest path
  // between two nodes in a Directed Acyclic Graph (DAG). Given an adjacency list
  // this method finds the shortest path to all nodes starting at 'start'
  //
  // NOTE: 'numNodes' is not necessarily the number of nodes currently present
  // in the adjacency list since you can have singleton nodes with no edges which
  // wouldn't be present in the adjacency list but are still part of the graph!
  //
"""
def dag_shortest_path(graph: Dict[int, List[Edge]], start: int, num_nodes: int) -> List[Optional[int]]:
    topsort = topological_sort(graph, num_nodes)
    dist = [None] * num_nodes
    dist[start] = 0

    for i in range(num_nodes):
        node_index = topsort[i]
        if dist[node_index] is not None:
            adjacent_edges = graph.get(node_index)
            if adjacent_edges is not None:
                for edge in adjacent_edges:
                    new_dist = dist[node_index] + edge.weight
                    if dist[edge.to] is None:
                        dist[edge.to] = new_dist
                    else:
                        dist[edge.to] = min(dist[edge.to], new_dist)

    return dist

# Example usage of topological sort
if __name__ == "__main__":
    # Graph setup
    N = 7
    graph = defaultdict(list)
    graph[0].append(Edge(0, 1, 3))
    graph[0].append(Edge(0, 2, 2))
    graph[0].append(Edge(0, 5, 3))
    graph[1].append(Edge(1, 3, 1))
    graph[1].append(Edge(1, 2, 6))
    graph[2].append(Edge(2, 3, 1))
    graph[2].append(Edge(2, 4, 10))
    graph[3].append(Edge(3, 4, 5))
    graph[5].append(Edge(5, 4, 7))

    ordering = topological_sort(graph, N)

    # Prints: [6, 0, 5, 1, 2, 3, 4]
    print(ordering)

    # Finds all the shortest paths starting at node 0
    dists = dag_shortest_path(graph, 0, N)

    # Find the shortest path from 0 to 4 which is 8.0
    print(dists[4])

    # Find the shortest path from 0 to 6 which
    # is None since 6 is not reachable!
    print(dists[6])


#-----------------

def is_even(number):
    """
    Checks if a number is even or odd.

    :param number: The number to check.
    :return: True if the number is even, False if odd.
    """
    # A number is even if it is divisible by 2 with no remainder
    return number % 2 == 0

def main():
    test_number = 5
    # Check if the number is even or odd
    if is_even(test_number):
        print(f"{test_number} is even.")
    else:
        print(f"{test_number} is odd.")

if __name__ == "__main__":
    main()


#------------------

def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

input_string = "racecar"  # Example input
print(f"Is '{input_string}' a palindrome? {is_palindrome(input_string)}")





