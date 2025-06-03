"""
Graph Implementation

This module provides comprehensive implementations of graph data structures
including directed and undirected graphs with various algorithms.
"""

from typing import Any, List, Dict, Set, Optional, Tuple
from collections import deque, defaultdict
import heapq


class GraphNode:
    """
    Node class for graph structures.
    
    Attributes:
        data: The data stored in the node
        neighbors: Set of connected nodes
    """
    
    def __init__(self, data: Any) -> None:
        """Initialize a new graph node."""
        self.data = data
        self.neighbors: Set['GraphNode'] = set()
        self.visited = False  # For traversal algorithms
    
    def add_neighbor(self, neighbor: 'GraphNode') -> None:
        """Add a neighbor to this node."""
        self.neighbors.add(neighbor)
    
    def remove_neighbor(self, neighbor: 'GraphNode') -> None:
        """Remove a neighbor from this node."""
        self.neighbors.discard(neighbor)
    
    def get_neighbors(self) -> Set['GraphNode']:
        """Get all neighbors of this node."""
        return self.neighbors
    
    def __str__(self) -> str:
        """String representation of the node."""
        return str(self.data)
    
    def __hash__(self) -> int:
        """Hash function for use in sets and dictionaries."""
        return hash(self.data)
    
    def __eq__(self, other) -> bool:
        """Equality comparison based on data."""
        if isinstance(other, GraphNode):
            return self.data == other.data
        return False


class Graph:
    """
    Graph implementation using adjacency list representation.
    
    Supports both directed and undirected graphs with weighted edges.
    
    Time Complexities:
    - Add vertex: O(1)
    - Add edge: O(1)
    - Remove vertex: O(V + E)
    - Remove edge: O(1)
    - DFS/BFS: O(V + E)
    
    Space Complexity: O(V + E) where V is vertices and E is edges
    """
    
    def __init__(self, directed: bool = False) -> None:
        """
        Initialize graph.
        
        Args:
            directed: Whether the graph is directed (default: False)
        """
        self.vertices: Dict[Any, GraphNode] = {}
        self.edges: Dict[Tuple[Any, Any], float] = {}  # For weighted edges
        self.directed = directed
    
    def add_vertex(self, data: Any) -> bool:
        """
        Add a vertex to the graph.
        
        Args:
            data: Data for the new vertex
            
        Returns:
            bool: True if vertex was added, False if already exists
            
        Time Complexity: O(1)
        """
        if data in self.vertices:
            return False
        
        self.vertices[data] = GraphNode(data)
        return True
    
    def add_edge(self, from_vertex: Any, to_vertex: Any, weight: float = 1.0) -> bool:
        """
        Add an edge between two vertices.
        
        Args:
            from_vertex: Source vertex data
            to_vertex: Destination vertex data
            weight: Edge weight (default: 1.0)
            
        Returns:
            bool: True if edge was added, False if vertices don't exist
            
        Time Complexity: O(1)
        """
        if from_vertex not in self.vertices or to_vertex not in self.vertices:
            return False
        
        from_node = self.vertices[from_vertex]
        to_node = self.vertices[to_vertex]
        
        from_node.add_neighbor(to_node)
        self.edges[(from_vertex, to_vertex)] = weight
        
        # For undirected graphs, add edge in both directions
        if not self.directed:
            to_node.add_neighbor(from_node)
            self.edges[(to_vertex, from_vertex)] = weight
        
        return True
    
    def remove_vertex(self, data: Any) -> bool:
        """
        Remove a vertex and all its edges.
        
        Args:
            data: Data of vertex to remove
            
        Returns:
            bool: True if vertex was removed, False if not found
            
        Time Complexity: O(V + E)
        """
        if data not in self.vertices:
            return False
        
        vertex = self.vertices[data]
        
        # Remove all edges involving this vertex
        edges_to_remove = []
        for edge in self.edges:
            if data in edge:
                edges_to_remove.append(edge)
        
        for edge in edges_to_remove:
            del self.edges[edge]
        
        # Remove from neighbors' neighbor lists
        for neighbor in vertex.neighbors:
            neighbor.remove_neighbor(vertex)
        
        # Remove references from other vertices
        for other_vertex in self.vertices.values():
            other_vertex.remove_neighbor(vertex)
        
        del self.vertices[data]
        return True
    
    def get_vertices(self) -> List[Any]:
        """Get all vertices in the graph."""
        return list(self.vertices.keys())
    
    def get_neighbors(self, vertex: Any) -> List[Any]:
        """Get neighbors of a vertex."""
        if vertex not in self.vertices:
            return []
        
        return [neighbor.data for neighbor in self.vertices[vertex].neighbors]
    
    def has_vertex(self, data: Any) -> bool:
        """Check if vertex exists in graph."""
        return data in self.vertices
    
    def has_edge(self, from_vertex: Any, to_vertex: Any) -> bool:
        """Check if edge exists between two vertices."""
        return (from_vertex, to_vertex) in self.edges
    
    def vertex_count(self) -> int:
        """Get number of vertices."""
        return len(self.vertices)
    
    def edge_count(self) -> int:
        """Get number of edges."""
        if self.directed:
            return len(self.edges)
        else:
            return len(self.edges) // 2
    
    def is_empty(self) -> bool:
        """Check if graph is empty."""
        return len(self.vertices) == 0
    
    def remove_edge(self, from_vertex: Any, to_vertex: Any) -> bool:
        """
        Remove an edge between two vertices.
        
        Args:
            from_vertex: Source vertex data
            to_vertex: Destination vertex data
            
        Returns:
            bool: True if edge was removed, False if not found
            
        Time Complexity: O(1)
        """
        if (from_vertex, to_vertex) not in self.edges:
            return False
        
        from_node = self.vertices[from_vertex]
        to_node = self.vertices[to_vertex]
        
        from_node.remove_neighbor(to_node)
        del self.edges[(from_vertex, to_vertex)]
        
        # For undirected graphs, remove edge in both directions
        if not self.directed:
            to_node.remove_neighbor(from_node)
            if (to_vertex, from_vertex) in self.edges:
                del self.edges[(to_vertex, from_vertex)]
        
        return True
    
    def clear(self) -> None:
        """Remove all vertices and edges."""
        self.vertices.clear()
        self.edges.clear()
    
    def _reset_visited(self) -> None:
        """Reset visited flags for all vertices."""
        for vertex in self.vertices.values():
            vertex.visited = False
    
    def depth_first_search(self, start_vertex: Any) -> List[Any]:
        """
        Perform depth-first search starting from given vertex.
        
        Time Complexity: O(V + E)
        """
        if start_vertex not in self.vertices:
            return []
        
        self._reset_visited()
        result = []
        
        def dfs_recursive(vertex_data: Any) -> None:
            vertex = self.vertices[vertex_data]
            vertex.visited = True
            result.append(vertex_data)
            
            for neighbor in vertex.neighbors:
                if not neighbor.visited:
                    dfs_recursive(neighbor.data)
        
        dfs_recursive(start_vertex)
        return result
    
    def breadth_first_search(self, start_vertex: Any) -> List[Any]:
        """
        Perform breadth-first search starting from given vertex.
        
        Time Complexity: O(V + E)
        """
        if start_vertex not in self.vertices:
            return []
        
        self._reset_visited()
        result = []
        queue = deque([start_vertex])
        self.vertices[start_vertex].visited = True
        
        while queue:
            current = queue.popleft()
            result.append(current)
            
            for neighbor in self.vertices[current].neighbors:
                if not neighbor.visited:
                    neighbor.visited = True
                    queue.append(neighbor.data)
        
        return result
    
    def find_shortest_path(self, start_vertex: Any, end_vertex: Any) -> List[Any]:
        """Find shortest path between two vertices using BFS."""
        if start_vertex not in self.vertices or end_vertex not in self.vertices:
            return []
        
        if start_vertex == end_vertex:
            return [start_vertex]
        
        parent = {start_vertex: None}
        queue = deque([start_vertex])
        
        while queue:
            current = queue.popleft()
            
            for neighbor in self.vertices[current].neighbors:
                if neighbor.data not in parent:
                    parent[neighbor.data] = current
                    queue.append(neighbor.data)
                    
                    if neighbor.data == end_vertex:
                        # Reconstruct path
                        path = []
                        node = end_vertex
                        while node is not None:
                            path.append(node)
                            node = parent[node]
                        return path[::-1]
        
        return []
    
    def __str__(self) -> str:
        """String representation of the graph."""
        if self.is_empty():
            return "Empty Graph"
        
        result = []
        result.append(f"Graph ({'Directed' if self.directed else 'Undirected'}):")
        result.append(f"Vertices: {self.vertex_count()}, Edges: {self.edge_count()}")
        result.append("Adjacency List:")
        
        for vertex_data, vertex in self.vertices.items():
            neighbors = [str(neighbor.data) for neighbor in vertex.neighbors]
            result.append(f"  {vertex_data} -> {neighbors}")
        
        return "\n".join(result)