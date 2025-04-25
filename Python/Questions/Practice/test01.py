'''
def twoArrays(k, A, B):
    # Sort A in ascending order
    A.sort()
    # Sort B in descending order
    B.sort(reverse=True)
    
    # Check the condition for all indices
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"

# Example Usage
queries = [
    (10, [2, 1, 3], [7, 8, 9]),
    (5, [1, 2, 2, 1], [3, 3, 3, 4])
]

for k, A, B in queries:
    print(twoArrays(k, A, B))

    '''

import sys

def floyd_warshall(graph):
    """
    Implements the Floyd-Warshall algorithm to find all-pairs shortest paths in a weighted graph.

    Args:
        graph: A 2D list representing the adjacency matrix of the graph. 
               graph[i][j] represents the weight of the edge from node i to node j. 
               If there is no edge, graph[i][j] should be set to infinity.

    Returns:
        A 2D list representing the shortest distances between all pairs of nodes.
    """

    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))  # Initialize distance matrix

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example usage: 
graph = [
    [0, 3, float('inf'), 7],
    [8, 0, 2,float('inf')], 
    [5, float('inf'), 0,1],
    [2,float('inf'), float('inf'), 0]
]

shortest_paths = floyd_warshall(graph)

for row in shortest_paths:
    print(row)
pass