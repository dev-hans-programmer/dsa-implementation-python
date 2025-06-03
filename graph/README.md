# Graph Implementation

A comprehensive implementation of graph data structures in Python with various algorithms for traversal, shortest path finding, and network analysis.

## 📖 Table of Contents

- [Overview](#overview)
- [Theory](#theory)
- [Implementation Details](#implementation-details)
- [Time and Space Complexity](#time-and-space-complexity)
- [Real-World Applications](#real-world-applications)
- [Usage Examples](#usage-examples)
- [Running the Code](#running-the-code)

## Overview

A **Graph** is a non-linear data structure consisting of vertices (nodes) connected by edges. Graphs are used to model relationships between objects and are fundamental in computer science for solving connectivity, pathfinding, and network analysis problems.

### Key Characteristics

- **Vertices (Nodes)**: Individual data points in the graph
- **Edges**: Connections between vertices
- **Directed vs Undirected**: Edges can have direction or be bidirectional
- **Weighted vs Unweighted**: Edges can have associated costs/distances
- **Connected vs Disconnected**: All vertices reachable vs separate components

## Theory

### Graph Types

#### Undirected Graph
```
A --- B
|     |
|     |
C --- D
```
- Edges have no direction
- If A connects to B, then B connects to A
- Used for: Social networks, road networks, electrical circuits

#### Directed Graph (Digraph)
```
A --> B
|     |
v     v
C --> D
```
- Edges have direction (one-way connections)
- A → B doesn't imply B → A
- Used for: Web links, task dependencies, state machines

### Graph Representations

#### Adjacency List (Our Implementation)
```python
{
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```
- Space efficient for sparse graphs: O(V + E)
- Fast neighbor lookup: O(1)
- Edge existence check: O(degree)

#### Adjacency Matrix
```python
    A  B  C  D
A [ 0  1  1  0 ]
B [ 1  0  0  1 ]
C [ 1  0  0  1 ]
D [ 0  1  1  0 ]
```
- Space: O(V²)
- Fast edge lookup: O(1)
- Better for dense graphs

### Graph Traversal Algorithms

#### Depth-First Search (DFS)
- Explores as deep as possible before backtracking
- Uses stack (recursive or explicit)
- Applications: Cycle detection, topological sorting, pathfinding

#### Breadth-First Search (BFS)
- Explores all neighbors before going deeper
- Uses queue
- Applications: Shortest path (unweighted), level-order traversal

## Implementation Details

### GraphNode Class

```python
class GraphNode:
    def __init__(self, data):
        self.data = data
        self.neighbors = set()
        self.visited = False
```

### Graph Operations

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Add vertex | O(1) | O(1) |
| Add edge | O(1) | O(1) |
| Remove vertex | O(V + E) | O(1) |
| Remove edge | O(1) | O(1) |
| DFS/BFS | O(V + E) | O(V) |
| Shortest path | O(V + E) | O(V) |

### Core Methods

#### Graph Construction
```python
graph = Graph(directed=False)
graph.add_vertex("A")
graph.add_edge("A", "B", weight=5.0)
```

#### Traversal
```python
dfs_order = graph.depth_first_search("A")
bfs_order = graph.breadth_first_search("A")
```

#### Path Finding
```python
path = graph.find_shortest_path("A", "Z")
```

## Time and Space Complexity

### Space Complexity
- **Adjacency List**: O(V + E)
  - V vertices + E edges storage
  - Optimal for sparse graphs
- **Auxiliary Space**: O(V) for traversal algorithms
  - Visited set and queue/stack

### Time Complexity by Operation

| Algorithm | Time Complexity | Use Case |
|-----------|----------------|----------|
| **Add Vertex** | O(1) | Graph construction |
| **Add Edge** | O(1) | Graph construction |
| **DFS** | O(V + E) | Connectivity, cycles |
| **BFS** | O(V + E) | Shortest path |
| **Shortest Path** | O(V + E) | Unweighted graphs |
| **Dijkstra** | O((V + E) log V) | Weighted graphs |

### Performance Characteristics

- **Dense Graphs** (E ≈ V²): Adjacency matrix preferred
- **Sparse Graphs** (E ≈ V): Adjacency list preferred
- **Memory Usage**: Linear in vertices and edges
- **Cache Performance**: Good locality for adjacency list

## Real-World Applications

### 1. Social Networks
- **Friend Connections**: Model relationships between users
- **Mutual Friends**: Find common connections
- **Friend Suggestions**: Recommend connections through mutual friends
- **Six Degrees of Separation**: Calculate connection distances

### 2. Transportation Networks
- **Route Planning**: Find shortest paths between locations
- **Traffic Analysis**: Model road networks and congestion
- **Public Transit**: Optimize bus/train routes
- **Flight Networks**: Model airline connections

### 3. Web and Internet
- **Web Page Links**: Model hyperlink relationships
- **PageRank Algorithm**: Rank web pages by importance
- **Social Media**: Model followers, likes, and shares
- **Network Topology**: Design and analyze network infrastructure

### 4. Computer Networks
- **Network Routing**: Find optimal data transmission paths
- **Topology Design**: Plan network infrastructure
- **Load Balancing**: Distribute traffic across network nodes
- **Fault Tolerance**: Design redundant network paths

### 5. Dependencies and Scheduling
- **Task Dependencies**: Model project task relationships
- **Package Management**: Resolve software dependencies
- **Build Systems**: Determine compilation order
- **Project Planning**: Schedule tasks with prerequisites

### 6. Biology and Chemistry
- **Molecular Structures**: Model chemical bonds
- **Protein Folding**: Analyze protein structures
- **Genetic Networks**: Model gene interactions
- **Evolutionary Trees**: Represent species relationships

### 7. Game Development
- **Game Maps**: Model game world connections
- **AI Pathfinding**: Find optimal movement paths
- **State Machines**: Model game state transitions
- **Quest Dependencies**: Track quest prerequisites

## Usage Examples

### Basic Graph Operations

```python
from implementation import Graph

# Create undirected graph
graph = Graph(directed=False)

# Add vertices
cities = ['NYC', 'Boston', 'DC', 'Atlanta']
for city in cities:
    graph.add_vertex(city)

# Add edges (connections)
graph.add_edge('NYC', 'Boston')
graph.add_edge('NYC', 'DC')
graph.add_edge('DC', 'Atlanta')

print(graph)  # Display graph structure
```

### Graph Traversal

```python
# Depth-First Search
dfs_order = graph.depth_first_search('NYC')
print(f"DFS: {dfs_order}")

# Breadth-First Search
bfs_order = graph.breadth_first_search('NYC')
print(f"BFS: {bfs_order}")

# Check connectivity
print(f"Connected: {len(dfs_order) == graph.vertex_count()}")
```

### Shortest Path Finding

```python
# Find shortest path
path = graph.find_shortest_path('NYC', 'Atlanta')
if path:
    print(f"Route: {' → '.join(path)}")
    print(f"Stops: {len(path) - 1}")
else:
    print("No path found")
```

### Social Network Example

```python
# Create social network
social = Graph(directed=False)

# Add users
users = ['Alice', 'Bob', 'Charlie', 'Diana']
for user in users:
    social.add_vertex(user)

# Add friendships
friendships = [('Alice', 'Bob'), ('Bob', 'Charlie'), ('Charlie', 'Diana')]
for user1, user2 in friendships:
    social.add_edge(user1, user2)

# Find mutual friends
alice_friends = set(social.get_neighbors('Alice'))
diana_friends = set(social.get_neighbors('Diana'))
mutual = alice_friends.intersection(diana_friends)
print(f"Mutual friends: {list(mutual)}")

# Find connection path
path = social.find_shortest_path('Alice', 'Diana')
print(f"Connection: {' → '.join(path)}")
print(f"Degrees of separation: {len(path) - 1}")
```

### Transportation Network

```python
# Create transportation network
transport = Graph(directed=False)

# Add stations
stations = ['Central', 'Airport', 'University', 'Mall', 'Hospital']
for station in stations:
    transport.add_vertex(station)

# Add routes
routes = [
    ('Central', 'Airport'),
    ('Central', 'University'),
    ('University', 'Mall'),
    ('Mall', 'Hospital'),
    ('Airport', 'Hospital')
]

for station1, station2 in routes:
    transport.add_edge(station1, station2)

# Find route
route = transport.find_shortest_path('Central', 'Hospital')
print(f"Route to Hospital: {' → '.join(route)}")

# Analyze connectivity
for station in stations:
    reachable = transport.breadth_first_search(station)
    print(f"From {station}: {len(reachable)} reachable stations")
```

### Directed Graph (Web Links)

```python
# Create web link graph
web = Graph(directed=True)

# Add pages
pages = ['home.html', 'about.html', 'products.html', 'contact.html']
for page in pages:
    web.add_vertex(page)

# Add links (directed)
links = [
    ('home.html', 'about.html'),
    ('home.html', 'products.html'),
    ('about.html', 'contact.html'),
    ('products.html', 'contact.html')
]

for from_page, to_page in links:
    web.add_edge(from_page, to_page)

# Find all pages reachable from home
reachable = web.depth_first_search('home.html')
print(f"Pages reachable from home: {reachable}")

# Find pages with no incoming links (entry points)
all_pages = set(web.get_vertices())
linked_pages = set()
for page in all_pages:
    for linked in web.get_neighbors(page):
        linked_pages.add(linked)

entry_points = all_pages - linked_pages
print(f"Entry points: {list(entry_points)}")
```

## Running the Code

### Prerequisites

- Python 3.7 or higher
- No external dependencies required

### Interactive Demo

```bash
# Run the main interactive demonstration
python main.py
```

Features include:
- Basic graph operations (add/remove vertices and edges)
- Graph traversal algorithms (DFS/BFS)
- Shortest path finding
- Social network simulation
- Transportation network analysis

### Usage Examples

```bash
# Run comprehensive examples and tests
python usage.py
```

Includes:
- Basic graph operations testing
- Real-world application examples
- Social network analysis
- Web crawling simulation
- Transportation routing
- Performance comparisons

### File Structure

```
graph/
├── implementation.py  # Core graph implementation
├── usage.py          # Comprehensive examples and applications
├── main.py           # Interactive demonstration
└── README.md         # This documentation
```

### Learning Progression

1. **Basic Concepts**: Understand vertices, edges, and graph types
2. **Construction**: Learn to build and modify graphs
3. **Traversal**: Master DFS and BFS algorithms
4. **Pathfinding**: Implement shortest path algorithms
5. **Applications**: Explore real-world use cases
6. **Optimization**: Analyze performance characteristics

This implementation provides a solid foundation for understanding graph theory and algorithms, with practical examples that demonstrate the power and versatility of graph data structures in solving real-world problems.