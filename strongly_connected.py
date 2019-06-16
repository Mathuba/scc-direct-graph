#Uses python3

import sys

sys.setrecursionlimit(200000)



def add_edge(graph, reverse_graph, vertex1, vertex2):
    """Build a directed graph as well as the reverse of the directed graph.

    The edges are reversed, so from input vertices, the neighbour vertex
    becomes the key vertex and key becomes neighbour.

    Parameters
    ----------
    graph, reverse_graph: dictionary
        Empty dictionaries to build directed graph and it's reverse.
    vertex1, vertex: int
        integer values representing key vey vertex and it's too neighbour.
    """
    
    rev_vert1, rev_vert2 = (vertex2, vertex1)
    if vertex1 in graph:
        if vertex2 not in graph[vertex1]:
            graph[vertex1].append(vertex2)
            reverse_graph[rev_vert1].append(rev_vert2)


def number_of_strongly_connected_components(adj):
    result = 0
    #write your code here
    return result

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    graph = {vertex: [] for vertex in range(1, n+1)}
    rev_graph = {vertex: [] for vertex in range(1, n+1)}
        
    for _ in range(m):
        vert1, vert2 = map(int, sys.stdin.readline().split())
        add_edge(graph, rev_graph, vert1, vert2)
        add_edge(graph, rev_graph, vert1, vert2)
    # print(number_of_strongly_connected_components(adj))
