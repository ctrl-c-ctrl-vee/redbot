from collections import deque

def bfs(graph, start):
    """
    Perform Breadth-First Search on a graph starting from the given node.
    
    :param graph: Dictionary representing the graph as an adjacency list
    :param start: The starting node for BFS
    """
    # Initialize visited set to keep track of visited nodes
    visited = set()
    # Queue for BFS traversal
    queue = deque([start])
    
    while queue:
        # Dequeue a vertex from queue and print it
        vertex = queue.popleft()
        print(vertex, end=" ")
        
        # Get all adjacent vertices of the dequeued vertex.
        # If an adjacent has not been visited, then mark it visited and enqueue it
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS traversal starting from node A:")
bfs(graph, 'A')
