"""
Algorithms Usage Examples

This module demonstrates practical usage of algorithm implementations
with real-world scenarios and comprehensive test cases.
"""

from implementation import *
import time
import random


def test_sorting_algorithms():
    """Test and compare different sorting algorithms."""
    print("=== Testing Sorting Algorithms ===\n")
    
    # Test data of different sizes and types
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [],
        [3, 3, 3, 3],
        [9, 8, 7, 6, 5, 4, 3, 2, 1]  # Reverse sorted
    ]
    
    sorting_algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort)
    ]
    
    for i, test_case in enumerate(test_cases):
        print(f"Test Case {i + 1}: {test_case}")
        print(f"Expected Result: {sorted(test_case)}")
        
        for name, algorithm in sorting_algorithms:
            result = algorithm(test_case)
            status = "✓" if result == sorted(test_case) else "✗"
            print(f"  {name}: {result} {status}")
        
        print()
    
    # Test specialized sorting algorithms
    print("--- Specialized Sorting Algorithms ---")
    integer_array = [170, 45, 75, 90, 2, 802, 24, 66]
    print(f"Integer array: {integer_array}")
    
    counting_result = counting_sort(integer_array)
    radix_result = radix_sort(integer_array)
    
    print(f"Counting Sort: {counting_result}")
    print(f"Radix Sort: {radix_result}")
    print(f"Expected: {sorted(integer_array)}")


def test_searching_algorithms():
    """Test different searching algorithms."""
    print("\n=== Testing Searching Algorithms ===\n")
    
    # Test data
    sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
    unsorted_array = [23, 1, 15, 7, 21, 9, 13, 3, 17, 11, 25, 5, 19]
    
    test_values = [1, 7, 15, 25, 100, -5]
    
    print(f"Sorted array: {sorted_array}")
    print(f"Unsorted array: {unsorted_array}")
    
    searching_algorithms = [
        ("Linear Search (sorted)", linear_search, sorted_array),
        ("Linear Search (unsorted)", linear_search, unsorted_array),
        ("Binary Search", binary_search, sorted_array),
        ("Binary Search Recursive", binary_search_recursive, sorted_array),
        ("Jump Search", jump_search, sorted_array),
        ("Interpolation Search", interpolation_search, sorted_array)
    ]
    
    print(f"\n--- Search Results ---")
    for target in test_values:
        print(f"\nSearching for {target}:")
        
        for name, algorithm, array in searching_algorithms:
            try:
                result = algorithm(array, target)
                found = "Found" if result != -1 else "Not found"
                index_info = f" at index {result}" if result != -1 else ""
                print(f"  {name}: {found}{index_info}")
            except Exception as e:
                print(f"  {name}: Error - {e}")


def test_graph_algorithms():
    """Test graph algorithms with sample graphs."""
    print("\n=== Testing Graph Algorithms ===\n")
    
    # Sample graph for traversal
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    print("Sample Graph (adjacency list):")
    for node, neighbors in graph.items():
        print(f"  {node}: {neighbors}")
    
    # Test traversals
    print(f"\n--- Graph Traversals ---")
    dfs_result = depth_first_search(graph, 'A')
    bfs_result = breadth_first_search(graph, 'A')
    
    print(f"DFS from A: {dfs_result}")
    print(f"BFS from A: {bfs_result}")
    
    # Weighted graph for shortest path algorithms
    weighted_graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('D', 3), ('E', 1)],
        'C': [('A', 2), ('F', 5)],
        'D': [('B', 3), ('E', 2)],
        'E': [('B', 1), ('D', 2), ('F', 1)],
        'F': [('C', 5), ('E', 1)]
    }
    
    print(f"\n--- Shortest Path Algorithms ---")
    print("Weighted Graph:")
    for node, neighbors in weighted_graph.items():
        print(f"  {node}: {neighbors}")
    
    dijkstra_result = dijkstra_shortest_path(weighted_graph, 'A')
    print(f"\nDijkstra from A: {dijkstra_result}")
    
    # Test with negative weights
    graph_with_negative = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', -3), ('D', 2)],
        'C': [('D', 3)],
        'D': []
    }
    
    bellman_result, has_cycle = bellman_ford(graph_with_negative, 'A')
    print(f"\nBellman-Ford from A: {bellman_result}")
    print(f"Has negative cycle: {has_cycle}")
    
    # Test MST algorithms
    print(f"\n--- Minimum Spanning Tree ---")
    edges = [
        ('A', 'B', 4), ('A', 'C', 2), ('B', 'D', 3),
        ('B', 'E', 1), ('C', 'F', 5), ('D', 'E', 2),
        ('E', 'F', 1)
    ]
    
    print(f"Edges: {edges}")
    
    kruskal_result = kruskal_mst(edges)
    prim_result = prim_mst(weighted_graph)
    
    print(f"Kruskal MST: {kruskal_result}")
    print(f"Prim MST: {prim_result}")


def test_dynamic_programming():
    """Test dynamic programming algorithms."""
    print("\n=== Testing Dynamic Programming Algorithms ===\n")
    
    # Fibonacci
    print("--- Fibonacci Sequence ---")
    for n in range(10):
        fib_result = fibonacci_dp(n)
        print(f"F({n}) = {fib_result}")
    
    # Longest Common Subsequence
    print(f"\n--- Longest Common Subsequence ---")
    test_strings = [
        ("ABCDGH", "AEDFHR"),
        ("programming", "program"),
        ("AGGTAB", "GXTXAYB")
    ]
    
    for str1, str2 in test_strings:
        lcs_length = longest_common_subsequence(str1, str2)
        print(f"LCS('{str1}', '{str2}') = {lcs_length}")
    
    # Knapsack Problem
    print(f"\n--- 0/1 Knapsack Problem ---")
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    
    knapsack_result = knapsack_01(weights, values, capacity)
    print(f"Weights: {weights}")
    print(f"Values: {values}")
    print(f"Capacity: {capacity}")
    print(f"Maximum value: {knapsack_result}")
    
    # Edit Distance
    print(f"\n--- Edit Distance ---")
    word_pairs = [
        ("kitten", "sitting"),
        ("saturday", "sunday"),
        ("intention", "execution")
    ]
    
    for word1, word2 in word_pairs:
        distance = edit_distance(word1, word2)
        print(f"Edit distance('{word1}', '{word2}') = {distance}")
    
    # Coin Change
    print(f"\n--- Coin Change Problem ---")
    coins = [1, 3, 4]
    amounts = [6, 8, 11, 15]
    
    print(f"Available coins: {coins}")
    for amount in amounts:
        min_coins = coin_change(coins, amount)
        print(f"Amount {amount}: {min_coins} coins")
    
    # Longest Increasing Subsequence
    print(f"\n--- Longest Increasing Subsequence ---")
    sequences = [
        [10, 9, 2, 5, 3, 7, 101, 18],
        [0, 1, 0, 3, 2, 3],
        [7, 7, 7, 7, 7, 7, 7]
    ]
    
    for seq in sequences:
        lis_length = longest_increasing_subsequence(seq)
        print(f"LIS({seq}) = {lis_length}")
    
    # Maximum Subarray Sum
    print(f"\n--- Maximum Subarray Sum (Kadane's Algorithm) ---")
    arrays = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1, 2, 3, 4, 5],
        [-1, -2, -3, -4, -5]
    ]
    
    for arr in arrays:
        max_sum = maximum_subarray_sum(arr)
        print(f"Max subarray sum({arr}) = {max_sum}")


def test_string_algorithms():
    """Test string matching algorithms."""
    print("\n=== Testing String Algorithms ===\n")
    
    # Test cases for string matching
    test_cases = [
        ("ABABDABACDABABCABCABCABC", "ABABCABC"),
        ("GEEKS FOR GEEKS", "GEEK"),
        ("ABAAABCDABC", "ABC"),
        ("hello world", "world"),
        ("no match here", "xyz")
    ]
    
    print("--- String Matching Algorithms ---")
    for text, pattern in test_cases:
        print(f"\nText: '{text}'")
        print(f"Pattern: '{pattern}'")
        
        kmp_matches = kmp_search(text, pattern)
        rk_matches = rabin_karp_search(text, pattern)
        
        print(f"KMP matches at positions: {kmp_matches}")
        print(f"Rabin-Karp matches at positions: {rk_matches}")
        
        # Verify results
        if kmp_matches == rk_matches:
            print("✓ Both algorithms agree")
        else:
            print("✗ Algorithms disagree!")


def real_world_example_recommendation_system():
    """Demonstrate algorithms in a recommendation system."""
    print("\n=== Real-World Example: Movie Recommendation System ===\n")
    
    class MovieRecommendationSystem:
        """Simple movie recommendation using various algorithms."""
        
        def __init__(self):
            self.movies = []
            self.user_ratings = {}
            self.movie_features = {}
        
        def add_movie(self, movie_id, title, genres, year, rating):
            """Add a movie to the system."""
            self.movies.append({
                'id': movie_id,
                'title': title,
                'genres': genres,
                'year': year,
                'rating': rating
            })
            
            # Create feature vector for similarity calculations
            self.movie_features[movie_id] = {
                'year': year,
                'rating': rating,
                'genre_count': len(genres)
            }
        
        def add_user_rating(self, user_id, movie_id, rating):
            """Add user rating for a movie."""
            if user_id not in self.user_ratings:
                self.user_ratings[user_id] = {}
            self.user_ratings[user_id][movie_id] = rating
        
        def get_top_rated_movies(self, n=5):
            """Get top N rated movies using heap sort."""
            movie_ratings = [(movie['rating'], movie['title']) for movie in self.movies]
            
            # Sort by rating (descending)
            sorted_movies = sorted(movie_ratings, reverse=True)
            
            return sorted_movies[:n]
        
        def search_movies_by_title(self, query):
            """Search movies using string matching."""
            matches = []
            
            for movie in self.movies:
                title = movie['title'].lower()
                query_lower = query.lower()
                
                # Use KMP for exact substring matching
                kmp_matches = kmp_search(title, query_lower)
                
                if kmp_matches:
                    matches.append((movie['title'], movie['rating']))
            
            return sorted(matches, key=lambda x: x[1], reverse=True)
        
        def recommend_similar_movies(self, movie_id, n=3):
            """Recommend similar movies using feature similarity."""
            if movie_id not in self.movie_features:
                return []
            
            target_features = self.movie_features[movie_id]
            similarities = []
            
            for other_id, features in self.movie_features.items():
                if other_id != movie_id:
                    # Simple similarity calculation
                    year_diff = abs(target_features['year'] - features['year'])
                    rating_diff = abs(target_features['rating'] - features['rating'])
                    
                    similarity = 1 / (1 + year_diff * 0.01 + rating_diff)
                    similarities.append((similarity, other_id))
            
            # Sort by similarity (descending) and return top N
            similarities.sort(reverse=True)
            
            recommendations = []
            for _, movie_id in similarities[:n]:
                movie = next(m for m in self.movies if m['id'] == movie_id)
                recommendations.append((movie['title'], movie['rating']))
            
            return recommendations
        
        def get_user_recommendations(self, user_id, n=5):
            """Get personalized recommendations using collaborative filtering."""
            if user_id not in self.user_ratings:
                return self.get_top_rated_movies(n)
            
            user_ratings = self.user_ratings[user_id]
            
            # Find movies not rated by user
            unrated_movies = []
            for movie in self.movies:
                if movie['id'] not in user_ratings:
                    unrated_movies.append((movie['rating'], movie['title']))
            
            # Sort by global rating and return top N
            unrated_movies.sort(reverse=True)
            return unrated_movies[:n]
    
    # Create recommendation system and add sample data
    recommender = MovieRecommendationSystem()
    
    # Add sample movies
    movies_data = [
        (1, "The Shawshank Redemption", ["Drama"], 1994, 9.3),
        (2, "The Godfather", ["Crime", "Drama"], 1972, 9.2),
        (3, "The Dark Knight", ["Action", "Crime", "Drama"], 2008, 9.0),
        (4, "Pulp Fiction", ["Crime", "Drama"], 1994, 8.9),
        (5, "Forrest Gump", ["Drama", "Romance"], 1994, 8.8),
        (6, "Inception", ["Action", "Sci-Fi", "Thriller"], 2010, 8.8),
        (7, "The Matrix", ["Action", "Sci-Fi"], 1999, 8.7),
        (8, "Goodfellas", ["Crime", "Drama"], 1990, 8.7),
        (9, "The Lord of the Rings", ["Adventure", "Drama", "Fantasy"], 2001, 8.8),
        (10, "Interstellar", ["Adventure", "Drama", "Sci-Fi"], 2014, 8.6)
    ]
    
    for movie_data in movies_data:
        recommender.add_movie(*movie_data)
    
    # Add sample user ratings
    user_ratings = [
        (1, 1, 5), (1, 2, 4), (1, 3, 5), (1, 7, 4),
        (2, 1, 3), (2, 4, 5), (2, 5, 4), (2, 8, 5),
        (3, 3, 5), (3, 6, 5), (3, 7, 4), (3, 10, 4)
    ]
    
    for user_id, movie_id, rating in user_ratings:
        recommender.add_user_rating(user_id, movie_id, rating)
    
    print("Movie recommendation system initialized with sample data")
    
    # Test different recommendation features
    print(f"\n--- Top Rated Movies ---")
    top_movies = recommender.get_top_rated_movies(5)
    for i, (rating, title) in enumerate(top_movies, 1):
        print(f"{i}. {title} (Rating: {rating})")
    
    print(f"\n--- Movie Search ---")
    search_queries = ["god", "dark", "lord"]
    for query in search_queries:
        results = recommender.search_movies_by_title(query)
        print(f"Search '{query}': {results}")
    
    print(f"\n--- Similar Movie Recommendations ---")
    similar_to_matrix = recommender.recommend_similar_movies(7, 3)  # The Matrix
    print(f"Movies similar to 'The Matrix': {similar_to_matrix}")
    
    print(f"\n--- User Recommendations ---")
    for user_id in [1, 2, 3]:
        user_recs = recommender.get_user_recommendations(user_id, 3)
        print(f"Recommendations for User {user_id}: {user_recs}")


def performance_comparison():
    """Compare performance of different algorithms."""
    print("\n=== Algorithm Performance Comparison ===\n")
    
    # Generate test data
    sizes = [100, 1000, 5000]
    
    print("--- Sorting Algorithm Performance ---")
    print(f"{'Algorithm':<20} {'Size':<8} {'Time (ms)':<12} {'Sorted':<8}")
    print("-" * 50)
    
    for size in sizes:
        # Generate random data
        test_data = [random.randint(1, 1000) for _ in range(size)]
        
        # Test different sorting algorithms
        algorithms = [
            ("Bubble Sort", bubble_sort),
            ("Selection Sort", selection_sort),
            ("Insertion Sort", insertion_sort),
            ("Merge Sort", merge_sort),
            ("Quick Sort", quick_sort),
            ("Heap Sort", heap_sort)
        ]
        
        for name, algorithm in algorithms:
            if size > 1000 and name in ["Bubble Sort", "Selection Sort"]:
                continue  # Skip slow algorithms for large datasets
            
            start_time = time.time()
            result = algorithm(test_data.copy())
            end_time = time.time()
            
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            is_sorted_check = is_sorted(result)
            
            print(f"{name:<20} {size:<8} {execution_time:<12.2f} {'✓' if is_sorted_check else '✗':<8}")
    
    print(f"\n--- Searching Algorithm Performance ---")
    print(f"{'Algorithm':<25} {'Size':<8} {'Time (μs)':<12} {'Found':<8}")
    print("-" * 55)
    
    for size in sizes:
        # Generate sorted data for searching
        sorted_data = sorted([random.randint(1, 1000) for _ in range(size)])
        target = sorted_data[size // 2]  # Target in middle
        
        search_algorithms = [
            ("Linear Search", linear_search),
            ("Binary Search", binary_search),
            ("Jump Search", jump_search)
        ]
        
        for name, algorithm in search_algorithms:
            start_time = time.time()
            result = algorithm(sorted_data, target)
            end_time = time.time()
            
            execution_time = (end_time - start_time) * 1000000  # Convert to microseconds
            found = result != -1
            
            print(f"{name:<25} {size:<8} {execution_time:<12.2f} {'✓' if found else '✗':<8}")
    
    print(f"\n--- Algorithm Complexity Summary ---")
    complexity_info = get_algorithm_info()
    
    for category, algorithms in complexity_info.items():
        print(f"\n{category}:")
        for alg_name, complexity in algorithms.items():
            print(f"  {alg_name}: {complexity}")


def algorithm_selection_guide():
    """Provide guidance on when to use different algorithms."""
    print("\n=== Algorithm Selection Guide ===\n")
    
    scenarios = {
        "Small datasets (< 50 elements)": {
            "Sorting": "Insertion Sort - Simple and efficient for small data",
            "Searching": "Linear Search - No preprocessing needed"
        },
        "Large datasets (> 10,000 elements)": {
            "Sorting": "Merge Sort or Quick Sort - O(n log n) performance",
            "Searching": "Binary Search - Requires sorted data, O(log n)"
        },
        "Nearly sorted data": {
            "Sorting": "Insertion Sort - O(n) for nearly sorted arrays",
            "Searching": "Linear Search with early termination"
        },
        "Memory constrained": {
            "Sorting": "Heap Sort - O(1) extra space",
            "Searching": "Binary Search - No extra space needed"
        },
        "Stability required": {
            "Sorting": "Merge Sort - Maintains relative order of equal elements",
            "Searching": "Linear Search - Returns first occurrence"
        },
        "Integer data with known range": {
            "Sorting": "Counting Sort or Radix Sort - O(n) performance",
            "Searching": "Direct indexing if range is small"
        },
        "String pattern matching": {
            "Exact match": "KMP Algorithm - O(n + m) guaranteed",
            "Multiple patterns": "Rabin-Karp - Good for rolling hash"
        },
        "Graph problems": {
            "Shortest path": "Dijkstra (positive weights) or Bellman-Ford (negative)",
            "Connectivity": "DFS or BFS depending on requirements",
            "Minimum spanning tree": "Kruskal (sparse) or Prim (dense)"
        },
        "Dynamic programming": {
            "Optimization problems": "Break into subproblems with overlapping solutions",
            "String problems": "LCS, Edit Distance for similarity",
            "Combinatorial": "Knapsack, Coin Change for counting/optimization"
        }
    }
    
    for scenario, recommendations in scenarios.items():
        print(f"--- {scenario} ---")
        for problem_type, recommendation in recommendations.items():
            print(f"  {problem_type}: {recommendation}")
        print()


if __name__ == "__main__":
    test_sorting_algorithms()
    test_searching_algorithms()
    test_graph_algorithms()
    test_dynamic_programming()
    test_string_algorithms()
    real_world_example_recommendation_system()
    performance_comparison()
    algorithm_selection_guide()