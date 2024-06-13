from collections import deque

def bfs(graph, start):
    visited = set()  # To keep track of visited nodes
    queue = deque([start])  # Start with the initial node in the queue

    visited.add(start)
    print(f"Starting BFS from node {start}")

    while queue:
        vertex = queue.popleft()  # Remove and return the leftmost element
        print(f"Visiting node {vertex}")
        # Process all adjacent nodes, enqueue any that have not been visited
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                print(f"Queueing {neighbor}")

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Run BFS starting from node 'A'
bfs(graph, 'A')
