class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_list = {i: [] for i in range(num_vertices)}

    def add_edge(self, src, dest):
        self.adjacency_list[src].append(dest)
        # For an undirected graph, also add the reverse edge
        self.adjacency_list[dest].append(src)

    def depth_first_search(self, start_vertex):
        visited = [False] * self.num_vertices
        self._dfs_util(start_vertex, visited)
        
        return visited

    def _dfs_util(self, vertex, visited):
        # Mark the current node as visited and print it
        visited[vertex] = True
        print(vertex, end=' ')

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.adjacency_list[vertex]:
            if not visited[neighbor]:
                self._dfs_util(neighbor, visited)

# Example usage:
if __name__ == "__main__":
    g = Graph(5)  # Create a graph with 5 vertices
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)

    print("Depth-First Traversal (starting from vertex 0):")
    visited = g.depth_first_search(0)
