"""

Problem Statement
The Graph Coloring Problem is about assigning colors to the
vertices of a graph such that no two adjacent vertices have the
same color, using at most m colors.each vertex can only have one color.
Real-World Analogy:
Think of a map where each region (vertex) is connected to other regions (adjacent vertices). The taskis
 to color the map such that no two neighboring regions have the same color. This is similar toscheduling
 tasks where adjacent tasks should not occur at the same time.

Backtracking Approach
1 Start with the first vertex and assign it a color.
2 Move to the next vertex and assign it the first valid color that
doesn’t conflict with its neighbors.
3 If no valid color is found, backtrack to the previous vertex and
try a different color.
4 Repeat until all vertices are colored or backtracking fails.

Example for Graph Coloring:
For a graph with 4 vertices (A, B, C, D) and edges (A-B, B-C, C-D), we want to color the graph using
the minimum number of colors such that adjacent vertices do not share the same color.

"""
# if col is right
def is_safe(graph,colors,node,color):
    for neighbor in graph[node]:
        if colors[neighbor] == color:
            return False
    return True
# usin backtack to solve
def graph_coloring(graph,m,colors,node):
    if node == len(graph): # if all vertices are colored,final node
        return True

# try coloring with every color
    for color in range(1,m+1):
        if is_safe(graph,colors, node, color):
            colors[node] = color # assign the color
            if graph_coloring(graph, m, colors, node+1): # recurence for next vertex
                return True
            colors[node] = 0 # backtrack if no valid color is found
    return False # if no valid color is possible
# function to print the colors of vertices
def print_colors(colors):
    for i ,color in enumerate(colors):
        print(f"vertex{i}:Color {color}")

# driver code to solve the vertex coloring problem
graph = {
    0:[1,2], #vertex 0 is connected to vertices 1 and 2
    1:[0,2,3],
    2:[0,1],
    3:[1]
}
m = 3 # maximum no of col
colors = [0]*len(graph) # initialize all vertices with color 0-no color

if graph_coloring(graph,m,colors,0): # start coloring from the firstveertex
    print_colors(colors) # print the colored vertices
else:
    print("no sol")




















