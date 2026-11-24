import time
import random
import pandas as pd

from algorithms import kahn_sort, dfs_sort


def generate_graph(n):
    graph = {i: [] for i in range(n)}

    for i in range(n):
        for j in range(i + 1, min(i + 5, n)):
            if random.random() < 0.5:
                graph[i].append(j)

    return graph


def compare_algorithms():
    results = []

    random.seed(42)

    for size in [10, 50, 100, 250, 500]:
        graph = generate_graph(size)

        start = time.perf_counter()

        for _ in range(100):
            kahn_sort(graph)

        kahn_time = (time.perf_counter() - start) * 10

        start = time.perf_counter()

        for _ in range(100):
            dfs_sort(graph)

        dfs_time = (time.perf_counter() - start) * 10

        results.append({
            "Tasks": size,
            "Kahn (ms)": kahn_time,
            "DFS (ms)": dfs_time
        })

    return pd.DataFrame(results)