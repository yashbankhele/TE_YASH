# Define the graph
graph = {
    '6': ['3', '7'],
    '3': ['2', '4'],
    '7': ['9'],
    '2': [],
    '4': ['9'],
    '9': []
}

# -----------------------------
# Breadth-First Search (BFS)
# -----------------------------
from collections import deque

visited_bfs = []  # List for visited nodes
queue = deque()   # Initialize a queue using deque for efficiency

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.popleft()  # Use popleft() for queue behavior
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Following is the Breadth-First Search:")
bfs(visited_bfs, graph, '6')
print()  # for newline

# -----------------------------
# Depth-First Search (DFS)
# -----------------------------
visited_dfs = set()  # Set to keep track of visited nodes

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

print("Following is the Depth-First Search:")
dfs(visited_dfs, graph, '6')
print()
