import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(graph):
    G = nx.DiGraph()

    for task in graph:
        G.add_node(task)

        for dependent in graph[task]:
            G.add_edge(task, dependent)

    fig, ax = plt.subplots(figsize=(10, 5))

    if nx.is_directed_acyclic_graph(G):
        for layer, nodes in enumerate(nx.topological_generations(G)):
            for node in nodes:
                G.nodes[node]["layer"] = layer

        pos = nx.multipartite_layout(
            G, subset_key="layer", align="horizontal"
        )

        pos = {
            node: (x, -y)
            for node, (x, y) in pos.items()
        }
    else:
        pos = nx.circular_layout(G)

    nx.draw(
        G,
        pos,
        ax=ax,
        with_labels=True,
        node_color="skyblue",
        node_size=3000,
        font_size=10,
        font_weight="bold",
        arrows=True,
        arrowsize=20,
        edge_color="gray"
    )

    ax.set_title("Project Dependency Graph")

    return fig