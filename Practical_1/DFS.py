def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=" ")  # Process the current node
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Get graph input from the user
def get_graph_input():
    graph = {}
    n = int(input("Enter the number of nodes in the graph: "))
    print("Enter each node and its neighbors as space-separated values (e.g., A B C):")
    for _ in range(n):
        line = input().split()
        node = line[0]
        neighbors = line[1:]
        graph[node] = neighbors
    return graph

# Example usage
if __name__ == "__main__":
    user_graph = get_graph_input()
    start_node = input("Enter the starting node: ")
    print("DFS Traversal:")
    dfs_recursive(user_graph, start_node)
