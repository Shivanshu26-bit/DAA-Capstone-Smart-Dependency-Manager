import streamlit as st
import matplotlib.pyplot as plt

from algorithms import kahn_sort, dfs_sort
from visualization import draw_graph
from benchmark import compare_algorithms


st.set_page_config(
    page_title="Smart Dependency Manager",
    layout="wide"
)

st.title("Smart Dependency Manager")

st.caption(
    "Design and Analysis of Algorithms | Project 10"
)
st.markdown("""
**Submitted by:** Shivanshu Shukla  
**Roll No:** 2501060131  
**Course:** BCA (AI & DS)  
**Semester:** 3 | **Section:** B
""")

if "graph" not in st.session_state:
    st.session_state.graph = {
        "Planning": ["Design"],
        "Design": ["Frontend", "Backend"],
        "Frontend": ["Testing"],
        "Backend": ["Testing"],
        "Testing": ["Deployment"],
        "Deployment": []
    }

graph = st.session_state.graph

st.sidebar.header("Project Management")

task = st.sidebar.text_input("New task name")

if st.sidebar.button("Add Task"):
    task = task.strip()

    if not task:
        st.sidebar.warning("Enter a task name.")

    elif task in graph:
        st.sidebar.warning("Task already exists.")

    else:
        graph[task] = []
        st.sidebar.success("Task added!")

st.sidebar.subheader("Add Dependency")

if len(graph) >= 2:

    source = st.sidebar.selectbox(
        "Prerequisite Task",
        list(graph.keys())
    )

    target = st.sidebar.selectbox(
        "Dependent Task",
        list(graph.keys())
    )

    if st.sidebar.button("Add Dependency"):

        if source == target:
            st.sidebar.error(
                "A task cannot depend on itself."
            )

        elif target in graph[source]:
            st.sidebar.warning(
                "Dependency already exists."
            )

        else:
            graph[source].append(target)
            st.sidebar.success("Dependency added!")

if st.sidebar.button("Reset Project"):
    graph.clear()
    st.rerun()

kahn_result = kahn_sort(graph)
dfs_result = dfs_sort(graph)

col1, col2, col3 = st.columns(3)

col1.metric("Total Tasks", len(graph))

col2.metric(
    "Dependencies",
    sum(len(edges) for edges in graph.values())
)

col3.metric(
    "Graph Status",
    "Cycle Detected" if kahn_result is None
    else "Valid DAG"
)

st.divider()

if not graph:
    st.info("Add tasks using the sidebar.")

else:
    st.subheader("Dependency Graph")

    fig = draw_graph(graph)
    st.pyplot(fig)
    plt.close(fig)

    st.subheader("Execution Order")

    left, right = st.columns(2)

    with left:
        st.markdown("### Kahn's Algorithm")

        if kahn_result is None:
            st.error("Circular dependency detected!")

        else:
            for i, task in enumerate(kahn_result, 1):
                st.write(f"{i}. {task}")

    with right:
        st.markdown("### DFS Algorithm")

        if dfs_result is None:
            st.error("Circular dependency detected!")

        else:
            for i, task in enumerate(dfs_result, 1):
                st.write(f"{i}. {task}")

st.divider()

st.subheader("Algorithm Performance")

if st.button("Run Performance Analysis"):

    results = compare_algorithms()

    st.dataframe(results)

    st.line_chart(
        results.set_index("Tasks")
    )

st.divider()

st.markdown(
    "**Time Complexity:** O(V + E) for both algorithms."
)