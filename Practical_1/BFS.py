def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=" ")  
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=" ")  
            
            
            for neighbor in reversed(graph[node]):  
                if neighbor not in visited:
                    stack.append(neighbor)


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


if __name__ == "__main__":
    print("Depth-First Search (DFS) Implementation")
    user_graph = get_graph_input()
    start_node = input("Enter the starting node: ")
    
    print("\nDFS Traversal (Recursive):")
    dfs_recursive(user_graph, start_node)
    
    print("\n\nDFS Traversal (Iterative):")
    dfs_iterative(user_graph, start_node)
