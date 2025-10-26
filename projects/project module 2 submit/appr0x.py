
import random

import networkx as nx
import matplotlib.pyplot as plt

def gen_graph(num_nodes,weight_range= (1,100)):
    G = nx.complete_graph(num_nodes)
    """
    G = nx.Graph()
   
    for i in range(nodes):
        G.add_node(i)
        edges = []
        for j in range(i+1 , nodes):
            edges.append((i,j,random.randint(weight_range[0],weight_range[1])))
            G.add_weighted_edges_from(edges)
    return G
     """
    for u,v in G.edges():
        G.edges[u,v]['weight'] = random.randint(*weight_range)
    return G

print(gen_graph(5).edges())

def plot_steps(G,tour,current_node,pos):
    """
    tour =[1,2,3,4,5]
    list(zip(tour,tour[1:]))

    :param G:
    :param tour:
    :param current_node:
    :param pos:
    :return:
    """
    nx.draw(G,pos, with_labels=True, node_color = 'lightblue',node_size=500)
    path_edges = list(zip(tour,tour[1:]))
    nx.draw_networkx_edges(G,pos, edgelist=path_edges, edge_color='red',width=2)
    nx.draw_networkx_nodes(G,pos, nodelist=[current_node], node_color='green',node_size=500)
    edge_labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos, edge_labels=edge_labels)
    plt.pause(0.5)

def cal_tour_cost(G,tour):
    return  sum(G[tour[i]][tour[i+1]]['weight'] for i in range(len(tour)-1))

def nearest_neighbor_tap(G,start_node = None):
    if start_node is None:
        start_node = random.choice(list(G.nodes))

    pos = nx.spring_layout(G)
    plt.ion()
    plt.show()

    unvisited = set(G.nodes)
    unvisited.remove(start_node)
    tour = [start_node]
    cur_node = start_node

    plot_steps(G,tour,cur_node,pos)

    while unvisited:
        next_node = min(unvisited, key= lambda node: G[cur_node][node]['weight'])
        unvisited.remove(next_node)
        tour.append(next_node)
        cur_node = next_node
        plot_steps(G,tour,cur_node,pos)

    tour.append(start_node)
    plot_steps(G,tour,cur_node,pos)
    print(tour)
    tour_cost = cal_tour_cost(G,tour)
    print(f'Contruction heuristic tour cost: {tour_cost}')

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    G = gen_graph(5)
    nearest_neighbor_tap(G,start_node=0)




















