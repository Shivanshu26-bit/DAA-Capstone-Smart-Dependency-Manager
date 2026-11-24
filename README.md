# Smart Dependency and Project Execution Manager

## DAA Capstone Project – Project 10

### Introduction

This project is a Python-based application that manages project tasks and their dependencies using graph algorithms. It determines a valid execution sequence and detects circular dependencies.

### Objectives

- Represent project tasks using a directed graph.
- Implement Kahn's Algorithm using BFS.
- Implement DFS-based Topological Sorting.
- Detect circular dependencies.
- Visualize project dependencies.
- Compare algorithm execution times for different graph sizes.

### Technologies Used

- Python
- Streamlit
- NetworkX
- Matplotlib
- Pandas

### Algorithms Used

| Algorithm | Time Complexity | Auxiliary Space Complexity |
|---|---|---|
| Kahn's Algorithm | O(V + E) | O(V) |
| DFS Topological Sorting | O(V + E) | O(V) |

V represents the number of vertices and E represents the number of edges.

### Features

- Add project tasks.
- Create task dependencies.
- Generate valid execution sequences.
- Detect circular dependencies.
- Display directed dependency graphs.
- Compare algorithm performance using tables and charts.

### Installation

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python -m streamlit run app.py
```

### Project Structure

- app.py — Main Streamlit application
- algorithms.py — Algorithm implementations
- visualization.py — Graph visualization
- benchmark.py — Algorithm performance analysis
- requirements.txt — Required libraries
- README.md — Project documentation

### Conclusion

The project demonstrates how graph algorithms can solve real-world project scheduling and dependency management problems. Both Kahn's Algorithm and DFS-based Topological Sorting efficiently determine valid task execution sequences in directed acyclic graphs.

## Academic Information

| Details | Information |
|---|---|
| Submitted By | Shivanshu Shukla |
| Roll Number | 2501060131 |
| Course | BCA (AI & DS) |
| Semester | 3rd Semester |
| Section | B |
| Subject | Design and Analysis of Algorithms |
| Project Type | Capstone Project |
| Project Number | 10 |
| Academic Session | 2026-27 |