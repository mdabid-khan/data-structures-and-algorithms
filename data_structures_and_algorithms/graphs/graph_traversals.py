from collections import deque

# ==============================
# Graph (Adjacency List)
# ==============================

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": []
}


# ==============================
# BFS (Breadth First Search)
# ==============================

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    visited.add(start_node)

    print("BFS Order:", end=" ")

    while queue:
        current = queue.popleft()
        print(current, end=" ")

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    print()


# ==============================
# DFS (Depth First Search)
# ==============================

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# ==============================
# Run
# ==============================

if __name__ == "__main__":
    bfs(graph, "A")

    print("DFS Order:", end=" ")
    dfs(graph, "A")

