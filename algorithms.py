from collections import deque


def kahn_sort(graph):
    indegree = {node: 0 for node in graph}

    for node in graph:
        for neighbour in graph[node]:
            indegree[neighbour] += 1

    queue = deque(
        node for node in graph if indegree[node] == 0
    )

    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbour in graph[node]:
            indegree[neighbour] -= 1

            if indegree[neighbour] == 0:
                queue.append(neighbour)

    if len(order) != len(graph):
        return None

    return order


def dfs_sort(graph):
    visited = set()
    visiting = set()
    order = []

    def dfs(node):
        if node in visiting:
            return False

        if node in visited:
            return True

        visiting.add(node)

        for neighbour in graph[node]:
            if not dfs(neighbour):
                return False

        visiting.remove(node)
        visited.add(node)
        order.append(node)

        return True

    for node in graph:
        if not dfs(node):
            return None

    return order[::-1]