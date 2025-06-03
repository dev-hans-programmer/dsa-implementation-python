"""
Graph Usage Examples

This module demonstrates practical usage of graph implementations
with real-world scenarios and comprehensive test cases.
"""

from implementation import Graph


def test_basic_graph_operations():
    """Test basic operations of graph implementation."""
    print("=== Testing Basic Graph Operations ===\n")
    
    # Test undirected graph
    print("--- Undirected Graph ---")
    graph = Graph(directed=False)
    
    # Add vertices
    vertices = ['A', 'B', 'C', 'D', 'E']
    for vertex in vertices:
        graph.add_vertex(vertex)
    
    print(f"Added vertices: {vertices}")
    print(f"Vertex count: {graph.vertex_count()}")
    
    # Add edges
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
    for from_v, to_v in edges:
        graph.add_edge(from_v, to_v)
    
    print(f"Added edges: {edges}")
    print(f"Edge count: {graph.edge_count()}")
    print(f"Graph structure:\n{graph}")
    
    # Test neighbors
    print(f"\nNeighbors of B: {graph.get_neighbors('B')}")
    print(f"Has edge A-B: {graph.has_edge('A', 'B')}")
    print(f"Has edge A-E: {graph.has_edge('A', 'E')}")
    
    # Test directed graph
    print("\n--- Directed Graph ---")
    directed_graph = Graph(directed=True)
    
    for vertex in ['X', 'Y', 'Z']:
        directed_graph.add_vertex(vertex)
    
    directed_graph.add_edge('X', 'Y')
    directed_graph.add_edge('Y', 'Z')
    directed_graph.add_edge('Z', 'X')
    
    print(f"Directed graph:\n{directed_graph}")


def test_graph_traversals():
    """Test graph traversal algorithms."""
    print("\n=== Testing Graph Traversals ===\n")
    
    # Create sample graph
    graph = Graph(directed=False)
    vertices = [1, 2, 3, 4, 5, 6]
    for vertex in vertices:
        graph.add_vertex(vertex)
    
    # Create connected graph
    edges = [(1, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 6)]
    for from_v, to_v in edges:
        graph.add_edge(from_v, to_v)
    
    print("Graph structure:")
    print(graph)
    
    # Test DFS
    print(f"\nDepth-First Search from vertex 1:")
    dfs_result = graph.depth_first_search(1)
    print(f"DFS order: {dfs_result}")
    
    # Test BFS
    print(f"\nBreadth-First Search from vertex 1:")
    bfs_result = graph.breadth_first_search(1)
    print(f"BFS order: {bfs_result}")
    
    # Test shortest path
    print(f"\nShortest path from 1 to 6:")
    path = graph.find_shortest_path(1, 6)
    print(f"Path: {' -> '.join(map(str, path))}")
    
    # Test with disconnected vertex
    graph.add_vertex(7)
    print(f"\nShortest path from 1 to 7 (disconnected):")
    path = graph.find_shortest_path(1, 7)
    print(f"Path: {path if path else 'No path exists'}")


def real_world_example_social_network():
    """
    Demonstrate graph usage in social network representation.
    """
    print("\n=== Real-World Example: Social Network ===\n")
    
    class SocialNetwork:
        """Social network using graph structure."""
        
        def __init__(self):
            self.network = Graph(directed=False)  # Friendship is mutual
            self.user_info = {}  # Store additional user information
        
        def add_user(self, username: str, name: str, age: int):
            """Add a new user to the network."""
            success = self.network.add_vertex(username)
            if success:
                self.user_info[username] = {'name': name, 'age': age}
                print(f"Added user: {name} (@{username})")
            else:
                print(f"User @{username} already exists")
        
        def add_friendship(self, user1: str, user2: str):
            """Create friendship between two users."""
            if self.network.has_vertex(user1) and self.network.has_vertex(user2):
                success = self.network.add_edge(user1, user2)
                if success:
                    print(f"@{user1} and @{user2} are now friends!")
                else:
                    print(f"@{user1} and @{user2} are already friends")
            else:
                print("One or both users don't exist")
        
        def get_friends(self, username: str):
            """Get list of user's friends."""
            friends = self.network.get_neighbors(username)
            return [f"@{friend} ({self.user_info[friend]['name']})" for friend in friends]
        
        def find_mutual_friends(self, user1: str, user2: str):
            """Find mutual friends between two users."""
            if not (self.network.has_vertex(user1) and self.network.has_vertex(user2)):
                return []
            
            friends1 = set(self.network.get_neighbors(user1))
            friends2 = set(self.network.get_neighbors(user2))
            mutual = friends1.intersection(friends2)
            
            return [f"@{friend} ({self.user_info[friend]['name']})" for friend in mutual]
        
        def suggest_friends(self, username: str):
            """Suggest friends based on mutual connections."""
            if not self.network.has_vertex(username):
                return []
            
            user_friends = set(self.network.get_neighbors(username))
            suggestions = set()
            
            # Find friends of friends
            for friend in user_friends:
                friend_friends = set(self.network.get_neighbors(friend))
                suggestions.update(friend_friends)
            
            # Remove user themselves and existing friends
            suggestions.discard(username)
            suggestions -= user_friends
            
            return [f"@{friend} ({self.user_info[friend]['name']})" for friend in suggestions]
        
        def find_connection_path(self, user1: str, user2: str):
            """Find connection path between two users."""
            path = self.network.find_shortest_path(user1, user2)
            if path:
                return " -> ".join([f"@{user} ({self.user_info[user]['name']})" for user in path])
            return "No connection found"
        
        def get_network_stats(self):
            """Get network statistics."""
            return {
                'total_users': self.network.vertex_count(),
                'total_friendships': self.network.edge_count(),
                'avg_friends_per_user': self.network.edge_count() * 2 / self.network.vertex_count() if self.network.vertex_count() > 0 else 0
            }
    
    # Create social network
    social = SocialNetwork()
    
    # Add users
    users = [
        ("alice", "Alice Smith", 25),
        ("bob", "Bob Johnson", 28),
        ("charlie", "Charlie Brown", 22),
        ("diana", "Diana Prince", 30),
        ("eve", "Eve Wilson", 26),
        ("frank", "Frank Miller", 24)
    ]
    
    for username, name, age in users:
        social.add_user(username, name, age)
    
    # Add friendships
    friendships = [
        ("alice", "bob"),
        ("alice", "charlie"),
        ("bob", "diana"),
        ("charlie", "eve"),
        ("diana", "eve"),
        ("eve", "frank"),
        ("diana", "frank")
    ]
    
    print(f"\nCreating friendships:")
    for user1, user2 in friendships:
        social.add_friendship(user1, user2)
    
    # Test social network features
    print(f"\nAlice's friends: {social.get_friends('alice')}")
    print(f"Mutual friends of Alice and Diana: {social.find_mutual_friends('alice', 'diana')}")
    print(f"Friend suggestions for Alice: {social.suggest_friends('alice')}")
    print(f"Connection from Alice to Frank: {social.find_connection_path('alice', 'frank')}")
    
    stats = social.get_network_stats()
    print(f"\nNetwork Statistics:")
    print(f"Total users: {stats['total_users']}")
    print(f"Total friendships: {stats['total_friendships']}")
    print(f"Average friends per user: {stats['avg_friends_per_user']:.1f}")


def real_world_example_web_crawler():
    """
    Demonstrate graph usage in web page crawling.
    """
    print("\n=== Real-World Example: Web Page Dependencies ===\n")
    
    class WebCrawler:
        """Web page dependency tracker using directed graph."""
        
        def __init__(self):
            self.web_graph = Graph(directed=True)
            self.page_info = {}
        
        def add_page(self, url: str, title: str, load_time: float):
            """Add a web page to the graph."""
            success = self.web_graph.add_vertex(url)
            if success:
                self.page_info[url] = {'title': title, 'load_time': load_time}
                print(f"Added page: {title} ({url})")
        
        def add_link(self, from_url: str, to_url: str):
            """Add a link from one page to another."""
            success = self.web_graph.add_edge(from_url, to_url)
            if success:
                print(f"Link: {from_url} -> {to_url}")
        
        def find_all_reachable_pages(self, start_url: str):
            """Find all pages reachable from a starting page."""
            reachable = self.web_graph.depth_first_search(start_url)
            return [(url, self.page_info[url]['title']) for url in reachable]
        
        def find_entry_points(self):
            """Find pages with no incoming links (entry points)."""
            all_pages = set(self.web_graph.get_vertices())
            linked_pages = set()
            
            for page in all_pages:
                for linked_page in self.web_graph.get_neighbors(page):
                    linked_pages.add(linked_page)
            
            entry_points = all_pages - linked_pages
            return [(url, self.page_info[url]['title']) for url in entry_points]
        
        def find_dead_ends(self):
            """Find pages with no outgoing links (dead ends)."""
            dead_ends = []
            for page in self.web_graph.get_vertices():
                if not self.web_graph.get_neighbors(page):
                    dead_ends.append((page, self.page_info[page]['title']))
            return dead_ends
        
        def calculate_page_rank_simple(self):
            """Simple page rank based on incoming links."""
            page_rank = {}
            for page in self.web_graph.get_vertices():
                incoming_count = 0
                for other_page in self.web_graph.get_vertices():
                    if self.web_graph.has_edge(other_page, page):
                        incoming_count += 1
                page_rank[page] = incoming_count
            
            return sorted(page_rank.items(), key=lambda x: x[1], reverse=True)
    
    # Create web crawler
    crawler = WebCrawler()
    
    # Add web pages
    pages = [
        ("index.html", "Home Page", 0.5),
        ("about.html", "About Us", 0.3),
        ("products.html", "Our Products", 0.8),
        ("contact.html", "Contact Us", 0.4),
        ("blog.html", "Blog", 0.6),
        ("privacy.html", "Privacy Policy", 0.2)
    ]
    
    for url, title, load_time in pages:
        crawler.add_page(url, title, load_time)
    
    # Add links between pages
    links = [
        ("index.html", "about.html"),
        ("index.html", "products.html"),
        ("index.html", "blog.html"),
        ("about.html", "contact.html"),
        ("products.html", "contact.html"),
        ("blog.html", "index.html"),
        ("contact.html", "privacy.html"),
        ("products.html", "privacy.html")
    ]
    
    print(f"\nCreating page links:")
    for from_page, to_page in links:
        crawler.add_link(from_page, to_page)
    
    # Analyze web structure
    print(f"\nReachable from index.html:")
    reachable = crawler.find_all_reachable_pages("index.html")
    for url, title in reachable:
        print(f"  {title} ({url})")
    
    print(f"\nEntry points (no incoming links):")
    entry_points = crawler.find_entry_points()
    for url, title in entry_points:
        print(f"  {title} ({url})")
    
    print(f"\nDead ends (no outgoing links):")
    dead_ends = crawler.find_dead_ends()
    for url, title in dead_ends:
        print(f"  {title} ({url})")
    
    print(f"\nSimple page rank (by incoming links):")
    page_rank = crawler.calculate_page_rank_simple()
    for url, rank in page_rank[:3]:
        print(f"  {crawler.page_info[url]['title']}: {rank} incoming links")


def real_world_example_transportation_network():
    """
    Demonstrate graph usage in transportation routing.
    """
    print("\n=== Real-World Example: Transportation Network ===\n")
    
    class TransportationNetwork:
        """Transportation network with weighted edges for distances."""
        
        def __init__(self):
            self.network = Graph(directed=False)
            self.distances = {}  # Store distances between stations
            self.station_info = {}
        
        def add_station(self, station_id: str, name: str, station_type: str):
            """Add a transportation station."""
            success = self.network.add_vertex(station_id)
            if success:
                self.station_info[station_id] = {
                    'name': name,
                    'type': station_type
                }
                print(f"Added {station_type}: {name} ({station_id})")
        
        def add_route(self, station1: str, station2: str, distance: float, travel_time: int):
            """Add a route between two stations."""
            success = self.network.add_edge(station1, station2)
            if success:
                self.distances[(station1, station2)] = distance
                self.distances[(station2, station1)] = distance  # Bidirectional
                name1 = self.station_info[station1]['name']
                name2 = self.station_info[station2]['name']
                print(f"Route: {name1} ↔ {name2} ({distance}km, {travel_time}min)")
        
        def find_route(self, start_station: str, end_station: str):
            """Find route between two stations."""
            path = self.network.find_shortest_path(start_station, end_station)
            if not path:
                return None, 0, []
            
            total_distance = 0
            route_details = []
            
            for i in range(len(path) - 1):
                current = path[i]
                next_station = path[i + 1]
                distance = self.distances.get((current, next_station), 0)
                total_distance += distance
                
                current_name = self.station_info[current]['name']
                next_name = self.station_info[next_station]['name']
                route_details.append(f"{current_name} → {next_name} ({distance}km)")
            
            return path, total_distance, route_details
        
        def find_nearby_stations(self, station_id: str):
            """Find directly connected stations."""
            if not self.network.has_vertex(station_id):
                return []
            
            neighbors = self.network.get_neighbors(station_id)
            nearby = []
            
            for neighbor in neighbors:
                distance = self.distances.get((station_id, neighbor), 0)
                neighbor_info = self.station_info[neighbor]
                nearby.append((neighbor_info['name'], neighbor_info['type'], distance))
            
            return sorted(nearby, key=lambda x: x[2])  # Sort by distance
        
        def get_network_coverage(self):
            """Get network statistics."""
            total_distance = sum(self.distances.values()) / 2  # Each route counted twice
            station_types = {}
            
            for station_info in self.station_info.values():
                station_type = station_info['type']
                station_types[station_type] = station_types.get(station_type, 0) + 1
            
            return {
                'total_stations': self.network.vertex_count(),
                'total_routes': self.network.edge_count(),
                'total_distance': total_distance,
                'station_types': station_types
            }
    
    # Create transportation network
    transport = TransportationNetwork()
    
    # Add stations
    stations = [
        ("ST001", "Central Station", "Train"),
        ("ST002", "Airport Terminal", "Airport"),
        ("ST003", "University Campus", "Bus"),
        ("ST004", "Shopping Mall", "Bus"),
        ("ST005", "Hospital", "Bus"),
        ("ST006", "Beach Resort", "Train"),
        ("ST007", "Mountain View", "Train")
    ]
    
    for station_id, name, station_type in stations:
        transport.add_station(station_id, name, station_type)
    
    # Add routes with distances and travel times
    routes = [
        ("ST001", "ST002", 25.5, 35),  # Central to Airport
        ("ST001", "ST003", 8.2, 15),   # Central to University
        ("ST003", "ST004", 5.1, 10),   # University to Mall
        ("ST004", "ST005", 3.8, 8),    # Mall to Hospital
        ("ST001", "ST006", 45.0, 60),  # Central to Beach
        ("ST006", "ST007", 32.4, 45),  # Beach to Mountain
        ("ST002", "ST006", 38.7, 50),  # Airport to Beach
    ]
    
    print(f"\nCreating transportation routes:")
    for station1, station2, distance, time in routes:
        transport.add_route(station1, station2, distance, time)
    
    # Test route finding
    print(f"\nFinding route from Central Station to Hospital:")
    path, distance, details = transport.find_route("ST001", "ST005")
    if path:
        print(f"Route found (Total: {distance}km):")
        for detail in details:
            print(f"  {detail}")
    
    print(f"\nStations near University Campus:")
    nearby = transport.find_nearby_stations("ST003")
    for name, station_type, distance in nearby:
        print(f"  {name} ({station_type}) - {distance}km")
    
    # Network statistics
    stats = transport.get_network_coverage()
    print(f"\nTransportation Network Statistics:")
    print(f"Total stations: {stats['total_stations']}")
    print(f"Total routes: {stats['total_routes']}")
    print(f"Total network distance: {stats['total_distance']}km")
    print(f"Station types: {stats['station_types']}")


def performance_comparison():
    """Compare performance characteristics of graph operations."""
    print("\n=== Performance Comparison ===\n")
    
    import time
    import random
    
    def test_graph_performance(vertex_count: int, edge_ratio: float):
        """Test graph performance with given parameters."""
        graph = Graph(directed=False)
        
        # Add vertices
        vertices = list(range(vertex_count))
        start_time = time.time()
        for vertex in vertices:
            graph.add_vertex(vertex)
        vertex_time = time.time() - start_time
        
        # Add edges
        max_edges = vertex_count * (vertex_count - 1) // 2
        edge_count = int(max_edges * edge_ratio)
        edges_added = 0
        
        start_time = time.time()
        while edges_added < edge_count:
            v1, v2 = random.sample(vertices, 2)
            if not graph.has_edge(v1, v2):
                graph.add_edge(v1, v2)
                edges_added += 1
        edge_time = time.time() - start_time
        
        # Test traversal
        start_vertex = random.choice(vertices)
        start_time = time.time()
        dfs_result = graph.depth_first_search(start_vertex)
        dfs_time = time.time() - start_time
        
        start_time = time.time()
        bfs_result = graph.breadth_first_search(start_vertex)
        bfs_time = time.time() - start_time
        
        return {
            'vertices': vertex_count,
            'edges': edges_added,
            'vertex_time': vertex_time,
            'edge_time': edge_time,
            'dfs_time': dfs_time,
            'bfs_time': bfs_time,
            'dfs_coverage': len(dfs_result),
            'bfs_coverage': len(bfs_result)
        }
    
    # Test different graph sizes
    test_cases = [
        (100, 0.1),   # Sparse graph
        (100, 0.5),   # Medium density
        (100, 0.9),   # Dense graph
        (500, 0.1),   # Larger sparse graph
    ]
    
    print("Graph Performance Analysis:")
    print(f"{'Size':<8} {'Density':<8} {'Edges':<8} {'Add V':<10} {'Add E':<10} {'DFS':<10} {'BFS':<10}")
    print("-" * 70)
    
    for vertex_count, density in test_cases:
        result = test_graph_performance(vertex_count, density)
        print(f"{result['vertices']:<8} {density:<8.1f} {result['edges']:<8} "
              f"{result['vertex_time']:<10.4f} {result['edge_time']:<10.4f} "
              f"{result['dfs_time']:<10.4f} {result['bfs_time']:<10.4f}")
    
    print(f"\nObservations:")
    print(f"- Vertex addition: O(1) - constant time regardless of graph size")
    print(f"- Edge addition: O(1) - constant time per edge")
    print(f"- DFS/BFS: O(V + E) - linear in vertices and edges")
    print(f"- Dense graphs have more edges to traverse, increasing traversal time")


if __name__ == "__main__":
    test_basic_graph_operations()
    test_graph_traversals()
    real_world_example_social_network()
    real_world_example_web_crawler()
    real_world_example_transportation_network()
    performance_comparison()