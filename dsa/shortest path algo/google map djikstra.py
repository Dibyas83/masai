graph = {
    'a': {'b': 2, 'c': 4},  # nodes as key and values(anather dict) as connected neighbors
    'b': {'a': 2, 'c': 3, 'd': 2},
    'c': {'a': 4, 'b': 3, 'e': 5, 'd': 2},
    'd': {'b': 8, 'c': 2, 'e': 11, 'f': 22},
    'e': {'c': 5, 'd': 11, 'f': 1},
    'f': {'d': 22, 'e': 1}
}

def dijsktra(graph, source, destination):
    shortest_distance = {}  # recods the cost to reach that node.keeps updating
    track_predecessor = {}  # keeps track of the previous node
    unvisited = graph  # all nodes are unvisited initially.shows if whole graph is covered
    infinity = float('inf')  # to assign infinite cost to vertices not visited
    path = []  # to store the path,traceback path

    for node in unvisited:
        shortest_distance[node] = infinity
    # Assigning the initial cost to the source node
    shortest_distance[source] = 0
    # Looping until all nodes are visited
    while unvisited:   # Finding the node having smallest distance
        min_distance_node = None
        for node in unvisited:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

        path_options = graph[min_distance_node].items()
        for child_node, weight in path_options:
            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node

        unvisited.pop(min_distance_node)
        """
       

            if neighbor in unvisited:
                new_distance = shortest_distance[min_distance_node] + weight
                if new_distance < shortest_distance[neighbor]:
                    shortest_distance[neighbor] = new_distance
                    predecessor[neighbor] = min_distance_node
        unvisited.pop(min_distance_node)
         """

    currnode = destination
    while currnode != source: # traceback path, keeping predecessor
        try:
            path.insert(0, currnode)
            currnode = track_predecessor[currnode]
        except KeyError:
            print('So sorry, but a connecting path doesn\'t exist between %s and %s' % (source, destination))
            break

    path.insert(0, source) # source doesnt have predecessor

    if shortest_distance[destination] != infinity:
        print('Shortest path: %s' % path)
        print('Shortest distance: %s' % shortest_distance[destination])
    else:
        print('So sorry, but a connecting path doesn\'t exist between %s and %s' % (source, destination))


dijsktra(graph, 'a', 'f')
















