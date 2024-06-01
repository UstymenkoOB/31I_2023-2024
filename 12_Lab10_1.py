# Варіант 12
# 
# Написати програму для обходу графа за алгоритмом пошуку в глибину
# 
# Дзюба Владислав

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

graph = {
    1: {4, 6},
    2: {6},
    3: {8, 7},
    4: {5, 1},
    5: {4, 6, 8},
    6: {1, 2, 5},
    7: {3, 8},
    8: {7, 3, 5}
}

dfs(graph, 1)
