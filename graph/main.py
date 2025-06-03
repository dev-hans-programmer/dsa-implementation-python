"""
Interactive Graph Demonstration

This module provides an interactive demonstration of graph operations,
allowing users to experiment with different graph types and algorithms.
"""

from implementation import Graph


def display_main_menu():
    """Display the main menu options."""
    print("\n" + "="*60)
    print("GRAPH INTERACTIVE DEMO")
    print("="*60)
    print("1. Basic Graph Operations")
    print("2. Graph Traversals (DFS/BFS)")
    print("3. Shortest Path Finding")
    print("4. Social Network Simulation")
    print("5. Transportation Network")
    print("6. Web Page Link Analysis")
    print("7. Graph Properties Analysis")
    print("8. Performance Testing")
    print("9. Exit")
    print("="*60)


def basic_graph_demo():
    """Interactive demo for basic graph operations."""
    print("\n" + "="*50)
    print("BASIC GRAPH OPERATIONS DEMO")
    print("="*50)
    
    # Choose graph type
    print("Choose graph type:")
    print("1. Undirected Graph")
    print("2. Directed Graph")
    
    try:
        choice = int(input("\nEnter choice (1-2): "))
        directed = (choice == 2)
        graph_type = "Directed" if directed else "Undirected"
    except ValueError:
        print("Invalid input, using Undirected Graph")
        directed = False
        graph_type = "Undirected"
    
    graph = Graph(directed=directed)
    print(f"Created {graph_type} Graph")
    
    while True:
        print(f"\nCurrent Graph:")
        print(graph)
        
        print(f"\nOperations:")
        print("1. Add vertex")
        print("2. Add edge")
        print("3. Remove vertex")
        print("4. Remove edge")
        print("5. Check if vertex exists")
        print("6. Check if edge exists")
        print("7. Get neighbors")
        print("8. Show graph statistics")
        print("9. Clear graph")
        print("10. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-10): "))
            
            if choice == 1:
                vertex = input("Enter vertex name: ")
                success = graph.add_vertex(vertex)
                if success:
                    print(f"Added vertex: {vertex}")
                else:
                    print(f"Vertex {vertex} already exists")
                    
            elif choice == 2:
                from_vertex = input("Enter source vertex: ")
                to_vertex = input("Enter destination vertex: ")
                success = graph.add_edge(from_vertex, to_vertex)
                if success:
                    print(f"Added edge: {from_vertex} -> {to_vertex}")
                else:
                    print("One or both vertices don't exist")
                    
            elif choice == 3:
                vertex = input("Enter vertex to remove: ")
                success = graph.remove_vertex(vertex)
                if success:
                    print(f"Removed vertex: {vertex}")
                else:
                    print(f"Vertex {vertex} not found")
                    
            elif choice == 4:
                from_vertex = input("Enter source vertex: ")
                to_vertex = input("Enter destination vertex: ")
                success = graph.remove_edge(from_vertex, to_vertex)
                if success:
                    print(f"Removed edge: {from_vertex} -> {to_vertex}")
                else:
                    print("Edge not found")
                    
            elif choice == 5:
                vertex = input("Enter vertex to check: ")
                exists = graph.has_vertex(vertex)
                print(f"Vertex {vertex} {'exists' if exists else 'does not exist'}")
                
            elif choice == 6:
                from_vertex = input("Enter source vertex: ")
                to_vertex = input("Enter destination vertex: ")
                exists = graph.has_edge(from_vertex, to_vertex)
                print(f"Edge {from_vertex} -> {to_vertex} {'exists' if exists else 'does not exist'}")
                
            elif choice == 7:
                vertex = input("Enter vertex: ")
                neighbors = graph.get_neighbors(vertex)
                if neighbors:
                    print(f"Neighbors of {vertex}: {neighbors}")
                else:
                    print(f"No neighbors found for {vertex}")
                    
            elif choice == 8:
                print(f"Graph Statistics:")
                print(f"  Vertices: {graph.vertex_count()}")
                print(f"  Edges: {graph.edge_count()}")
                print(f"  Type: {graph_type}")
                print(f"  Empty: {graph.is_empty()}")
                
            elif choice == 9:
                graph.clear()
                print("Graph cleared")
                
            elif choice == 10:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def graph_traversal_demo():
    """Interactive demo for graph traversals."""
    print("\n" + "="*50)
    print("GRAPH TRAVERSALS DEMO")
    print("="*50)
    
    # Create sample graph or let user build one
    print("Choose option:")
    print("1. Use sample graph")
    print("2. Build custom graph")
    
    try:
        choice = int(input("\nEnter choice (1-2): "))
    except ValueError:
        choice = 1
    
    graph = Graph(directed=False)
    
    if choice == 1:
        # Create sample graph
        vertices = ['A', 'B', 'C', 'D', 'E', 'F']
        edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'F'), ('E', 'F')]
        
        for vertex in vertices:
            graph.add_vertex(vertex)
        
        for from_v, to_v in edges:
            graph.add_edge(from_v, to_v)
        
        print("Created sample graph with vertices A-F")
    
    else:
        # Let user build graph
        print("Build your graph (enter 'done' when finished):")
        
        while True:
            vertex = input("Enter vertex name (or 'done'): ").strip()
            if vertex.lower() == 'done':
                break
            graph.add_vertex(vertex)
        
        if graph.vertex_count() > 1:
            print("Add edges:")
            while True:
                from_v = input("Enter source vertex (or 'done'): ").strip()
                if from_v.lower() == 'done':
                    break
                to_v = input("Enter destination vertex: ").strip()
                graph.add_edge(from_v, to_v)
    
    while True:
        print(f"\nCurrent Graph:")
        print(graph)
        
        print(f"\nTraversal Operations:")
        print("1. Depth-First Search (DFS)")
        print("2. Breadth-First Search (BFS)")
        print("3. Compare DFS vs BFS")
        print("4. Find shortest path")
        print("5. Check connectivity")
        print("6. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-6): "))
            
            if choice == 1:
                if graph.is_empty():
                    print("Graph is empty")
                    continue
                
                start_vertex = input("Enter starting vertex: ")
                if graph.has_vertex(start_vertex):
                    result = graph.depth_first_search(start_vertex)
                    print(f"DFS from {start_vertex}: {' -> '.join(map(str, result))}")
                else:
                    print("Vertex not found")
                    
            elif choice == 2:
                if graph.is_empty():
                    print("Graph is empty")
                    continue
                
                start_vertex = input("Enter starting vertex: ")
                if graph.has_vertex(start_vertex):
                    result = graph.breadth_first_search(start_vertex)
                    print(f"BFS from {start_vertex}: {' -> '.join(map(str, result))}")
                else:
                    print("Vertex not found")
                    
            elif choice == 3:
                if graph.is_empty():
                    print("Graph is empty")
                    continue
                
                start_vertex = input("Enter starting vertex: ")
                if graph.has_vertex(start_vertex):
                    dfs_result = graph.depth_first_search(start_vertex)
                    bfs_result = graph.breadth_first_search(start_vertex)
                    
                    print(f"Comparison from {start_vertex}:")
                    print(f"DFS: {' -> '.join(map(str, dfs_result))}")
                    print(f"BFS: {' -> '.join(map(str, bfs_result))}")
                    print(f"\nDFS explores deeply before backtracking")
                    print(f"BFS explores all neighbors before going deeper")
                else:
                    print("Vertex not found")
                    
            elif choice == 4:
                if graph.vertex_count() < 2:
                    print("Need at least 2 vertices")
                    continue
                
                start_vertex = input("Enter start vertex: ")
                end_vertex = input("Enter end vertex: ")
                
                if graph.has_vertex(start_vertex) and graph.has_vertex(end_vertex):
                    path = graph.find_shortest_path(start_vertex, end_vertex)
                    if path:
                        print(f"Shortest path: {' -> '.join(map(str, path))}")
                        print(f"Path length: {len(path) - 1} edges")
                    else:
                        print("No path found between vertices")
                else:
                    print("One or both vertices not found")
                    
            elif choice == 5:
                if graph.is_empty():
                    print("Graph is empty")
                else:
                    # Check if all vertices are reachable from first vertex
                    start_vertex = list(graph.get_vertices())[0]
                    reachable = graph.depth_first_search(start_vertex)
                    total_vertices = graph.vertex_count()
                    
                    print(f"Connectivity Analysis:")
                    print(f"Total vertices: {total_vertices}")
                    print(f"Reachable from {start_vertex}: {len(reachable)}")
                    
                    if len(reachable) == total_vertices:
                        print("Graph is connected - all vertices reachable")
                    else:
                        unreachable = set(graph.get_vertices()) - set(reachable)
                        print(f"Graph is disconnected")
                        print(f"Unreachable vertices: {list(unreachable)}")
                    
            elif choice == 6:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def shortest_path_demo():
    """Interactive demo for shortest path algorithms."""
    print("\n" + "="*50)
    print("SHORTEST PATH DEMO")
    print("="*50)
    
    # Create a sample transportation network
    graph = Graph(directed=False)
    
    # Add cities
    cities = ['NYC', 'Boston', 'DC', 'Atlanta', 'Miami', 'Chicago', 'Detroit']
    for city in cities:
        graph.add_vertex(city)
    
    # Add connections
    connections = [
        ('NYC', 'Boston'), ('NYC', 'DC'), ('NYC', 'Chicago'),
        ('Boston', 'Detroit'), ('DC', 'Atlanta'), ('Atlanta', 'Miami'),
        ('Chicago', 'Detroit'), ('Detroit', 'Atlanta')
    ]
    
    for city1, city2 in connections:
        graph.add_edge(city1, city2)
    
    print("Sample Transportation Network:")
    print(graph)
    
    while True:
        print(f"\nShortest Path Operations:")
        print("1. Find shortest path between cities")
        print("2. Find all reachable cities from a starting city")
        print("3. Check if two cities are connected")
        print("4. Add new city connection")
        print("5. Show network analysis")
        print("6. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-6): "))
            
            if choice == 1:
                print(f"Available cities: {graph.get_vertices()}")
                start_city = input("Enter starting city: ").strip()
                end_city = input("Enter destination city: ").strip()
                
                if graph.has_vertex(start_city) and graph.has_vertex(end_city):
                    path = graph.find_shortest_path(start_city, end_city)
                    if path:
                        print(f"\nShortest route from {start_city} to {end_city}:")
                        print(f"Path: {' → '.join(path)}")
                        print(f"Stops: {len(path) - 1}")
                    else:
                        print(f"No route found between {start_city} and {end_city}")
                else:
                    print("One or both cities not found in network")
                    
            elif choice == 2:
                print(f"Available cities: {graph.get_vertices()}")
                start_city = input("Enter starting city: ").strip()
                
                if graph.has_vertex(start_city):
                    reachable = graph.breadth_first_search(start_city)
                    print(f"\nCities reachable from {start_city}:")
                    for i, city in enumerate(reachable):
                        if i == 0:
                            print(f"  {city} (starting point)")
                        else:
                            print(f"  {city}")
                else:
                    print("City not found in network")
                    
            elif choice == 3:
                print(f"Available cities: {graph.get_vertices()}")
                city1 = input("Enter first city: ").strip()
                city2 = input("Enter second city: ").strip()
                
                if graph.has_vertex(city1) and graph.has_vertex(city2):
                    path = graph.find_shortest_path(city1, city2)
                    if path:
                        print(f"{city1} and {city2} are connected")
                        print(f"Distance: {len(path) - 1} stops")
                    else:
                        print(f"{city1} and {city2} are not connected")
                else:
                    print("One or both cities not found")
                    
            elif choice == 4:
                city1 = input("Enter first city (new or existing): ").strip()
                city2 = input("Enter second city (new or existing): ").strip()
                
                # Add cities if they don't exist
                graph.add_vertex(city1)
                graph.add_vertex(city2)
                
                success = graph.add_edge(city1, city2)
                if success:
                    print(f"Added connection: {city1} ↔ {city2}")
                else:
                    print("Connection already exists")
                    
            elif choice == 5:
                print(f"\nNetwork Analysis:")
                print(f"Total cities: {graph.vertex_count()}")
                print(f"Total connections: {graph.edge_count()}")
                
                # Find most connected cities
                connectivity = {}
                for city in graph.get_vertices():
                    connectivity[city] = len(graph.get_neighbors(city))
                
                sorted_cities = sorted(connectivity.items(), key=lambda x: x[1], reverse=True)
                print(f"\nMost connected cities:")
                for city, connections in sorted_cities[:3]:
                    print(f"  {city}: {connections} connections")
                
                # Check overall connectivity
                if graph.vertex_count() > 0:
                    start_city = list(graph.get_vertices())[0]
                    reachable = graph.depth_first_search(start_city)
                    if len(reachable) == graph.vertex_count():
                        print(f"\nNetwork is fully connected")
                    else:
                        print(f"\nNetwork has disconnected components")
                        
            elif choice == 6:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def social_network_demo():
    """Interactive demo for social network analysis."""
    print("\n" + "="*50)
    print("SOCIAL NETWORK SIMULATION")
    print("="*50)
    
    social_graph = Graph(directed=False)
    user_profiles = {}
    
    # Add some initial users
    initial_users = [
        ("alice", "Alice Johnson"),
        ("bob", "Bob Smith"),
        ("charlie", "Charlie Brown"),
        ("diana", "Diana Prince")
    ]
    
    for username, full_name in initial_users:
        social_graph.add_vertex(username)
        user_profiles[username] = full_name
    
    # Add some initial friendships
    social_graph.add_edge("alice", "bob")
    social_graph.add_edge("alice", "charlie")
    social_graph.add_edge("bob", "diana")
    
    print("Initial social network created with sample users and friendships")
    
    while True:
        print(f"\nCurrent Network:")
        print(f"Users: {social_graph.vertex_count()}")
        print(f"Friendships: {social_graph.edge_count()}")
        
        print(f"\nSocial Network Operations:")
        print("1. Add new user")
        print("2. Add friendship")
        print("3. View user's friends")
        print("4. Find mutual friends")
        print("5. Find connection path between users")
        print("6. Suggest friends")
        print("7. Show network statistics")
        print("8. List all users")
        print("9. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-9): "))
            
            if choice == 1:
                username = input("Enter username: ").strip().lower()
                full_name = input("Enter full name: ").strip()
                
                success = social_graph.add_vertex(username)
                if success:
                    user_profiles[username] = full_name
                    print(f"Added user: {full_name} (@{username})")
                else:
                    print(f"Username @{username} already exists")
                    
            elif choice == 2:
                print(f"Available users: {list(user_profiles.keys())}")
                user1 = input("Enter first username: ").strip().lower()
                user2 = input("Enter second username: ").strip().lower()
                
                if social_graph.has_vertex(user1) and social_graph.has_vertex(user2):
                    if user1 != user2:
                        success = social_graph.add_edge(user1, user2)
                        if success:
                            print(f"{user_profiles[user1]} and {user_profiles[user2]} are now friends!")
                        else:
                            print("They are already friends")
                    else:
                        print("Users cannot be friends with themselves")
                else:
                    print("One or both users don't exist")
                    
            elif choice == 3:
                print(f"Available users: {list(user_profiles.keys())}")
                username = input("Enter username: ").strip().lower()
                
                if social_graph.has_vertex(username):
                    friends = social_graph.get_neighbors(username)
                    if friends:
                        print(f"\n{user_profiles[username]}'s friends:")
                        for friend in friends:
                            print(f"  {user_profiles[friend]} (@{friend})")
                    else:
                        print(f"{user_profiles[username]} has no friends yet")
                else:
                    print("User not found")
                    
            elif choice == 4:
                print(f"Available users: {list(user_profiles.keys())}")
                user1 = input("Enter first username: ").strip().lower()
                user2 = input("Enter second username: ").strip().lower()
                
                if social_graph.has_vertex(user1) and social_graph.has_vertex(user2):
                    friends1 = set(social_graph.get_neighbors(user1))
                    friends2 = set(social_graph.get_neighbors(user2))
                    mutual = friends1.intersection(friends2)
                    
                    if mutual:
                        print(f"\nMutual friends of {user_profiles[user1]} and {user_profiles[user2]}:")
                        for friend in mutual:
                            print(f"  {user_profiles[friend]} (@{friend})")
                    else:
                        print(f"No mutual friends found")
                else:
                    print("One or both users don't exist")
                    
            elif choice == 5:
                print(f"Available users: {list(user_profiles.keys())}")
                user1 = input("Enter first username: ").strip().lower()
                user2 = input("Enter second username: ").strip().lower()
                
                if social_graph.has_vertex(user1) and social_graph.has_vertex(user2):
                    path = social_graph.find_shortest_path(user1, user2)
                    if path:
                        print(f"\nConnection path:")
                        path_names = [f"{user_profiles[user]} (@{user})" for user in path]
                        print(" → ".join(path_names))
                        print(f"Degrees of separation: {len(path) - 1}")
                    else:
                        print("No connection found between users")
                else:
                    print("One or both users don't exist")
                    
            elif choice == 6:
                print(f"Available users: {list(user_profiles.keys())}")
                username = input("Enter username: ").strip().lower()
                
                if social_graph.has_vertex(username):
                    user_friends = set(social_graph.get_neighbors(username))
                    suggestions = set()
                    
                    # Find friends of friends
                    for friend in user_friends:
                        friend_friends = set(social_graph.get_neighbors(friend))
                        suggestions.update(friend_friends)
                    
                    # Remove user and existing friends
                    suggestions.discard(username)
                    suggestions -= user_friends
                    
                    if suggestions:
                        print(f"\nFriend suggestions for {user_profiles[username]}:")
                        for suggestion in suggestions:
                            print(f"  {user_profiles[suggestion]} (@{suggestion})")
                    else:
                        print("No friend suggestions available")
                else:
                    print("User not found")
                    
            elif choice == 7:
                if social_graph.vertex_count() > 0:
                    # Calculate network statistics
                    total_users = social_graph.vertex_count()
                    total_friendships = social_graph.edge_count()
                    avg_friends = (total_friendships * 2) / total_users if total_users > 0 else 0
                    
                    print(f"\nNetwork Statistics:")
                    print(f"Total users: {total_users}")
                    print(f"Total friendships: {total_friendships}")
                    print(f"Average friends per user: {avg_friends:.1f}")
                    
                    # Find most popular users
                    popularity = {}
                    for user in social_graph.get_vertices():
                        popularity[user] = len(social_graph.get_neighbors(user))
                    
                    if popularity:
                        sorted_users = sorted(popularity.items(), key=lambda x: x[1], reverse=True)
                        print(f"\nMost popular users:")
                        for user, friend_count in sorted_users[:3]:
                            print(f"  {user_profiles[user]}: {friend_count} friends")
                else:
                    print("Network is empty")
                    
            elif choice == 8:
                if user_profiles:
                    print(f"\nAll users in network:")
                    for username, full_name in user_profiles.items():
                        friend_count = len(social_graph.get_neighbors(username))
                        print(f"  {full_name} (@{username}) - {friend_count} friends")
                else:
                    print("No users in network")
                    
            elif choice == 9:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Main function to run the interactive demo."""
    print("Welcome to the Graph Interactive Learning Tool!")
    print("This demo will help you understand graph data structures and algorithms.")
    
    while True:
        display_main_menu()
        
        try:
            choice = int(input("\nEnter your choice (1-9): "))
            
            if choice == 1:
                basic_graph_demo()
            elif choice == 2:
                graph_traversal_demo()
            elif choice == 3:
                shortest_path_demo()
            elif choice == 4:
                social_network_demo()
            elif choice == 5:
                print("\nTransportation network demo - Feature in development")
                print("Try the shortest path demo for similar functionality")
            elif choice == 6:
                print("\nWeb page analysis demo - Feature in development")
                print("Check the usage.py file for web crawler examples")
            elif choice == 7:
                print("\nGraph properties analysis - Feature in development")
                print("Basic analysis available in other demos")
            elif choice == 8:
                print("\nPerformance testing - Feature in development")
                print("Check the usage.py file for performance comparisons")
            elif choice == 9:
                print("\nThank you for using the Graph Demo!")
                print("Keep exploring graph algorithms and happy coding!")
                break
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n\nExiting... Goodbye!")
            break


if __name__ == "__main__":
    main()