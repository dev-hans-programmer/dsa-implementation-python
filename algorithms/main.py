"""
Interactive Algorithms Demonstration

This module provides an interactive demonstration of fundamental algorithms,
allowing users to experiment with sorting, searching, graph algorithms, and dynamic programming.
"""

from implementation import *
import random
import time


def display_main_menu():
    """Display the main menu options."""
    print("\n" + "="*60)
    print("ALGORITHMS INTERACTIVE DEMO")
    print("="*60)
    print("1. Sorting Algorithms")
    print("2. Searching Algorithms")
    print("3. Graph Algorithms")
    print("4. Dynamic Programming")
    print("5. String Algorithms")
    print("6. Algorithm Performance Comparison")
    print("7. Algorithm Selection Guide")
    print("8. Exit")
    print("="*60)


def sorting_algorithms_demo():
    """Interactive demo for sorting algorithms."""
    print("\n" + "="*50)
    print("SORTING ALGORITHMS DEMO")
    print("="*50)
    
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Heap Sort", heap_sort),
        ("Counting Sort", counting_sort),
        ("Radix Sort", radix_sort)
    ]
    
    while True:
        print(f"\nSorting Algorithms:")
        print("1. Compare all algorithms")
        print("2. Test specific algorithm")
        print("3. Custom input sorting")
        print("4. Performance analysis")
        print("5. Algorithm characteristics")
        print("6. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-6): "))
            
            if choice == 1:
                # Generate test data
                test_data = [random.randint(1, 100) for _ in range(15)]
                print(f"\nOriginal array: {test_data}")
                print(f"Expected result: {sorted(test_data)}")
                print("\nAlgorithm Results:")
                print("-" * 50)
                
                for name, algorithm in algorithms[:6]:  # Skip specialized ones
                    start_time = time.time()
                    result = algorithm(test_data.copy())
                    end_time = time.time()
                    
                    execution_time = (end_time - start_time) * 1000
                    is_correct = result == sorted(test_data)
                    status = "✓" if is_correct else "✗"
                    
                    print(f"{name:<15}: {status} ({execution_time:.2f} ms)")
                    if not is_correct:
                        print(f"  Got: {result}")
                
            elif choice == 2:
                print(f"\nAvailable algorithms:")
                for i, (name, _) in enumerate(algorithms, 1):
                    print(f"  {i}. {name}")
                
                try:
                    alg_choice = int(input("Choose algorithm (1-8): "))
                    if 1 <= alg_choice <= len(algorithms):
                        name, algorithm = algorithms[alg_choice - 1]
                        
                        # Generate test data
                        size = int(input("Enter array size (1-50): ") or "10")
                        if name in ["Counting Sort", "Radix Sort"]:
                            test_data = [random.randint(0, 100) for _ in range(size)]
                        else:
                            test_data = [random.randint(-50, 50) for _ in range(size)]
                        
                        print(f"\nOriginal: {test_data}")
                        
                        start_time = time.time()
                        if name == "Counting Sort":
                            result = algorithm(test_data, max(test_data) if test_data else 0)
                        else:
                            result = algorithm(test_data)
                        end_time = time.time()
                        
                        print(f"Sorted:   {result}")
                        print(f"Time:     {(end_time - start_time) * 1000:.2f} ms")
                        print(f"Correct:  {'Yes' if result == sorted(test_data) else 'No'}")
                    else:
                        print("Invalid choice")
                except ValueError:
                    print("Please enter a valid number")
                    
            elif choice == 3:
                user_input = input("Enter numbers separated by spaces: ").strip()
                try:
                    numbers = [int(x) for x in user_input.split()]
                    if numbers:
                        print(f"\nYour array: {numbers}")
                        
                        # Choose algorithm
                        print("Choose sorting algorithm:")
                        for i, (name, _) in enumerate(algorithms[:6], 1):
                            print(f"  {i}. {name}")
                        
                        alg_choice = int(input("Algorithm choice (1-6): "))
                        if 1 <= alg_choice <= 6:
                            name, algorithm = algorithms[alg_choice - 1]
                            result = algorithm(numbers)
                            print(f"Sorted with {name}: {result}")
                        else:
                            print("Invalid choice")
                    else:
                        print("No valid numbers entered")
                except ValueError:
                    print("Please enter valid integers")
                    
            elif choice == 4:
                sizes = [10, 50, 100, 200]
                print(f"\nPerformance Analysis:")
                print(f"{'Algorithm':<15} {'Size':<6} {'Time (ms)':<12}")
                print("-" * 35)
                
                for size in sizes:
                    test_data = [random.randint(1, 1000) for _ in range(size)]
                    
                    for name, algorithm in algorithms[:6]:
                        if size > 100 and name in ["Bubble Sort", "Selection Sort"]:
                            continue  # Skip slow algorithms for large data
                        
                        start_time = time.time()
                        algorithm(test_data.copy())
                        end_time = time.time()
                        
                        execution_time = (end_time - start_time) * 1000
                        print(f"{name:<15} {size:<6} {execution_time:<12.2f}")
                        
            elif choice == 5:
                print(f"\nAlgorithm Characteristics:")
                characteristics = {
                    "Bubble Sort": "O(n²) - Simple, stable, in-place",
                    "Selection Sort": "O(n²) - Simple, not stable, in-place",
                    "Insertion Sort": "O(n²) - Good for small/sorted data, stable",
                    "Merge Sort": "O(n log n) - Stable, requires extra space",
                    "Quick Sort": "O(n log n) avg - Fast, in-place, not stable",
                    "Heap Sort": "O(n log n) - In-place, not stable",
                    "Counting Sort": "O(n+k) - For integers in range",
                    "Radix Sort": "O(d(n+k)) - For integers, stable"
                }
                
                for alg, desc in characteristics.items():
                    print(f"  {alg}: {desc}")
                    
            elif choice == 6:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def searching_algorithms_demo():
    """Interactive demo for searching algorithms."""
    print("\n" + "="*50)
    print("SEARCHING ALGORITHMS DEMO")
    print("="*50)
    
    algorithms = [
        ("Linear Search", linear_search),
        ("Binary Search", binary_search),
        ("Binary Search Recursive", binary_search_recursive),
        ("Jump Search", jump_search),
        ("Interpolation Search", interpolation_search)
    ]
    
    while True:
        print(f"\nSearching Algorithms:")
        print("1. Compare all algorithms")
        print("2. Test specific algorithm")
        print("3. Custom array search")
        print("4. Performance analysis")
        print("5. Algorithm requirements")
        print("6. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-6): "))
            
            if choice == 1:
                # Generate sorted test data
                size = 20
                sorted_array = sorted([random.randint(1, 100) for _ in range(size)])
                target = sorted_array[random.randint(0, size-1)]  # Ensure target exists
                
                print(f"\nSorted array: {sorted_array}")
                print(f"Searching for: {target}")
                print("\nSearch Results:")
                print("-" * 40)
                
                for name, algorithm in algorithms:
                    try:
                        start_time = time.time()
                        result = algorithm(sorted_array, target)
                        end_time = time.time()
                        
                        execution_time = (end_time - start_time) * 1000000  # microseconds
                        found = result != -1
                        
                        print(f"{name:<20}: {'Found' if found else 'Not found'} at index {result if found else 'N/A'} ({execution_time:.2f} μs)")
                    except Exception as e:
                        print(f"{name:<20}: Error - {e}")
                
            elif choice == 2:
                print(f"\nAvailable algorithms:")
                for i, (name, _) in enumerate(algorithms, 1):
                    print(f"  {i}. {name}")
                
                try:
                    alg_choice = int(input("Choose algorithm (1-5): "))
                    if 1 <= alg_choice <= len(algorithms):
                        name, algorithm = algorithms[alg_choice - 1]
                        
                        # Generate test data
                        size = int(input("Enter array size (5-30): ") or "15")
                        if name != "Linear Search":
                            array = sorted([random.randint(1, 100) for _ in range(size)])
                            print("Note: Array is sorted for binary/jump/interpolation search")
                        else:
                            array = [random.randint(1, 100) for _ in range(size)]
                        
                        target = int(input(f"Enter target to search (1-100): ") or str(array[size//2]))
                        
                        print(f"\nArray: {array}")
                        print(f"Target: {target}")
                        
                        start_time = time.time()
                        result = algorithm(array, target)
                        end_time = time.time()
                        
                        if result != -1:
                            print(f"Found at index {result}")
                            print(f"Value at index: {array[result]}")
                        else:
                            print("Not found")
                        
                        print(f"Time: {(end_time - start_time) * 1000000:.2f} μs")
                    else:
                        print("Invalid choice")
                except ValueError:
                    print("Please enter valid numbers")
                    
            elif choice == 3:
                user_input = input("Enter numbers separated by spaces: ").strip()
                try:
                    numbers = [int(x) for x in user_input.split()]
                    if numbers:
                        target = int(input("Enter target to search: "))
                        
                        print(f"\nYour array: {numbers}")
                        print(f"Target: {target}")
                        
                        # Test with unsorted (linear only) and sorted
                        print(f"\nLinear search on original:")
                        result = linear_search(numbers, target)
                        print(f"  Result: {'Found at index ' + str(result) if result != -1 else 'Not found'}")
                        
                        sorted_numbers = sorted(numbers)
                        print(f"\nSorted array: {sorted_numbers}")
                        print(f"Binary search on sorted:")
                        result = binary_search(sorted_numbers, target)
                        print(f"  Result: {'Found at index ' + str(result) if result != -1 else 'Not found'}")
                    else:
                        print("No valid numbers entered")
                except ValueError:
                    print("Please enter valid integers")
                    
            elif choice == 4:
                sizes = [100, 500, 1000, 2000]
                print(f"\nPerformance Analysis (searching for middle element):")
                print(f"{'Algorithm':<20} {'Size':<6} {'Time (μs)':<12}")
                print("-" * 40)
                
                for size in sizes:
                    sorted_array = sorted(range(1, size + 1))
                    target = sorted_array[size // 2]
                    
                    for name, algorithm in algorithms:
                        try:
                            start_time = time.time()
                            algorithm(sorted_array, target)
                            end_time = time.time()
                            
                            execution_time = (end_time - start_time) * 1000000
                            print(f"{name:<20} {size:<6} {execution_time:<12.2f}")
                        except:
                            print(f"{name:<20} {size:<6} {'Error':<12}")
                            
            elif choice == 5:
                print(f"\nAlgorithm Requirements and Characteristics:")
                requirements = {
                    "Linear Search": "No requirements - works on any array",
                    "Binary Search": "Requires sorted array - O(log n)",
                    "Binary Search Recursive": "Requires sorted array - O(log n) with recursion",
                    "Jump Search": "Requires sorted array - O(√n)",
                    "Interpolation Search": "Requires sorted array with uniform distribution"
                }
                
                for alg, req in requirements.items():
                    print(f"  {alg}: {req}")
                    
            elif choice == 6:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def graph_algorithms_demo():
    """Interactive demo for graph algorithms."""
    print("\n" + "="*50)
    print("GRAPH ALGORITHMS DEMO")
    print("="*50)
    
    # Sample graphs
    sample_graphs = {
        "Social Network": {
            'Alice': ['Bob', 'Charlie'],
            'Bob': ['Alice', 'David', 'Eve'],
            'Charlie': ['Alice', 'Frank'],
            'David': ['Bob'],
            'Eve': ['Bob', 'Frank'],
            'Frank': ['Charlie', 'Eve']
        },
        "City Roads": {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'D', 'E'],
            'D': ['B', 'C', 'E'],
            'E': ['C', 'D']
        }
    }
    
    weighted_graphs = {
        "Flight Routes": {
            'NYC': [('LA', 5), ('Chicago', 2)],
            'LA': [('NYC', 5), ('Vegas', 1)],
            'Chicago': [('NYC', 2), ('Denver', 3)],
            'Vegas': [('LA', 1), ('Denver', 2)],
            'Denver': [('Chicago', 3), ('Vegas', 2)]
        }
    }
    
    while True:
        print(f"\nGraph Algorithms:")
        print("1. Graph Traversals (DFS/BFS)")
        print("2. Shortest Path Algorithms")
        print("3. Minimum Spanning Tree")
        print("4. Custom graph operations")
        print("5. Graph visualization")
        print("6. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-6): "))
            
            if choice == 1:
                print(f"\nAvailable sample graphs:")
                graph_names = list(sample_graphs.keys())
                for i, name in enumerate(graph_names, 1):
                    print(f"  {i}. {name}")
                
                try:
                    graph_choice = int(input("Choose graph (1-2): "))
                    if 1 <= graph_choice <= len(graph_names):
                        graph_name = graph_names[graph_choice - 1]
                        graph = sample_graphs[graph_name]
                        
                        print(f"\n{graph_name} Graph:")
                        for node, neighbors in graph.items():
                            print(f"  {node}: {neighbors}")
                        
                        start_node = input(f"\nEnter starting node {list(graph.keys())}: ").strip()
                        if start_node in graph:
                            print(f"\nTraversal Results from '{start_node}':")
                            
                            dfs_result = depth_first_search(graph, start_node)
                            bfs_result = breadth_first_search(graph, start_node)
                            
                            print(f"DFS: {dfs_result}")
                            print(f"BFS: {bfs_result}")
                        else:
                            print("Invalid starting node")
                    else:
                        print("Invalid choice")
                except ValueError:
                    print("Please enter a valid number")
                    
            elif choice == 2:
                graph_name = "Flight Routes"
                graph = weighted_graphs[graph_name]
                
                print(f"\n{graph_name} (with distances):")
                for city, routes in graph.items():
                    print(f"  {city}: {routes}")
                
                start_city = input(f"\nEnter starting city {list(graph.keys())}: ").strip()
                if start_city in graph:
                    print(f"\nShortest paths from '{start_city}':")
                    
                    # Dijkstra's algorithm
                    distances = dijkstra_shortest_path(graph, start_city)
                    for city, distance in distances.items():
                        if distance == float('infinity'):
                            print(f"  To {city}: No path")
                        else:
                            print(f"  To {city}: {distance} hours")
                    
                    # Test with negative weights
                    print(f"\nTesting Bellman-Ford with potential negative weights:")
                    bellman_distances, has_cycle = bellman_ford(graph, start_city)
                    print(f"Has negative cycle: {has_cycle}")
                else:
                    print("Invalid starting city")
                    
            elif choice == 3:
                # Create edges for MST algorithms
                edges = [
                    ('A', 'B', 4), ('A', 'C', 2), ('B', 'D', 3),
                    ('C', 'D', 1), ('C', 'E', 5), ('D', 'E', 6)
                ]
                
                weighted_graph = {
                    'A': [('B', 4), ('C', 2)],
                    'B': [('A', 4), ('D', 3)],
                    'C': [('A', 2), ('D', 1), ('E', 5)],
                    'D': [('B', 3), ('C', 1), ('E', 6)],
                    'E': [('C', 5), ('D', 6)]
                }
                
                print(f"\nMinimum Spanning Tree Demo:")
                print(f"Graph edges: {edges}")
                
                print(f"\nKruskal's Algorithm:")
                kruskal_mst_result = kruskal_mst(edges)
                kruskal_weight = sum(weight for _, _, weight in kruskal_mst_result)
                print(f"  MST edges: {kruskal_mst_result}")
                print(f"  Total weight: {kruskal_weight}")
                
                print(f"\nPrim's Algorithm:")
                prim_mst_result = prim_mst(weighted_graph)
                prim_weight = sum(weight for _, _, weight in prim_mst_result)
                print(f"  MST edges: {prim_mst_result}")
                print(f"  Total weight: {prim_weight}")
                
            elif choice == 4:
                print(f"\nCustom Graph Operations:")
                print("Create your own graph by adding edges")
                
                custom_graph = {}
                print("Enter edges in format 'node1 node2' (empty line to finish):")
                
                while True:
                    edge_input = input("Edge: ").strip()
                    if not edge_input:
                        break
                    
                    try:
                        node1, node2 = edge_input.split()
                        if node1 not in custom_graph:
                            custom_graph[node1] = []
                        if node2 not in custom_graph:
                            custom_graph[node2] = []
                        
                        custom_graph[node1].append(node2)
                        custom_graph[node2].append(node1)  # Undirected
                        
                        print(f"Added edge: {node1} - {node2}")
                    except ValueError:
                        print("Invalid format. Use 'node1 node2'")
                
                if custom_graph:
                    print(f"\nYour graph:")
                    for node, neighbors in custom_graph.items():
                        print(f"  {node}: {neighbors}")
                    
                    start = input(f"Enter starting node for traversal: ").strip()
                    if start in custom_graph:
                        dfs_result = depth_first_search(custom_graph, start)
                        bfs_result = breadth_first_search(custom_graph, start)
                        print(f"DFS from {start}: {dfs_result}")
                        print(f"BFS from {start}: {bfs_result}")
                    else:
                        print("Invalid starting node")
                else:
                    print("No graph created")
                    
            elif choice == 5:
                print(f"\nGraph Visualization (Text-based):")
                graph = sample_graphs["Social Network"]
                
                print("Social Network Graph:")
                print("```")
                print("    Alice")
                print("   /     \\")
                print("  Bob --- Charlie")
                print("  / \\      |")
                print("David Eve -- Frank")
                print("```")
                
                print(f"\nAdjacency List Representation:")
                for node, neighbors in graph.items():
                    print(f"  {node}: {' -> '.join(neighbors)}")
                    
            elif choice == 6:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def dynamic_programming_demo():
    """Interactive demo for dynamic programming algorithms."""
    print("\n" + "="*50)
    print("DYNAMIC PROGRAMMING DEMO")
    print("="*50)
    
    while True:
        print(f"\nDynamic Programming Problems:")
        print("1. Fibonacci Sequence")
        print("2. Longest Common Subsequence")
        print("3. 0/1 Knapsack Problem")
        print("4. Edit Distance")
        print("5. Coin Change Problem")
        print("6. Maximum Subarray Sum")
        print("7. Custom problem solver")
        print("8. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-8): "))
            
            if choice == 1:
                try:
                    n = int(input("Enter n for Fibonacci(n): "))
                    if 0 <= n <= 50:
                        start_time = time.time()
                        result = fibonacci_dp(n)
                        end_time = time.time()
                        
                        print(f"Fibonacci({n}) = {result}")
                        print(f"Computed in {(end_time - start_time) * 1000:.2f} ms")
                        
                        # Show sequence
                        if n <= 20:
                            sequence = [fibonacci_dp(i) for i in range(n + 1)]
                            print(f"Sequence: {sequence}")
                    else:
                        print("Please enter a number between 0 and 50")
                except ValueError:
                    print("Please enter a valid number")
                    
            elif choice == 2:
                str1 = input("Enter first string: ").strip()
                str2 = input("Enter second string: ").strip()
                
                if str1 and str2:
                    start_time = time.time()
                    lcs_length = longest_common_subsequence(str1, str2)
                    end_time = time.time()
                    
                    print(f"\nStrings:")
                    print(f"  String 1: '{str1}'")
                    print(f"  String 2: '{str2}'")
                    print(f"LCS Length: {lcs_length}")
                    print(f"Computed in {(end_time - start_time) * 1000:.2f} ms")
                else:
                    print("Please enter valid strings")
                    
            elif choice == 3:
                print(f"\n0/1 Knapsack Problem:")
                try:
                    items_input = input("Enter item weights (space-separated): ").strip()
                    values_input = input("Enter item values (space-separated): ").strip()
                    capacity = int(input("Enter knapsack capacity: "))
                    
                    weights = [int(x) for x in items_input.split()]
                    values = [int(x) for x in values_input.split()]
                    
                    if len(weights) == len(values):
                        print(f"\nKnapsack Problem:")
                        print(f"Items (weight, value):")
                        for i, (w, v) in enumerate(zip(weights, values)):
                            print(f"  Item {i+1}: ({w}, {v})")
                        print(f"Capacity: {capacity}")
                        
                        start_time = time.time()
                        max_value = knapsack_01(weights, values, capacity)
                        end_time = time.time()
                        
                        print(f"\nMaximum value: {max_value}")
                        print(f"Computed in {(end_time - start_time) * 1000:.2f} ms")
                    else:
                        print("Number of weights and values must match")
                except ValueError:
                    print("Please enter valid numbers")
                    
            elif choice == 4:
                word1 = input("Enter first word: ").strip()
                word2 = input("Enter second word: ").strip()
                
                if word1 and word2:
                    start_time = time.time()
                    distance = edit_distance(word1, word2)
                    end_time = time.time()
                    
                    print(f"\nEdit Distance:")
                    print(f"  '{word1}' -> '{word2}'")
                    print(f"  Minimum operations: {distance}")
                    print(f"Computed in {(end_time - start_time) * 1000:.2f} ms")
                    
                    # Show what operations might be needed
                    if distance <= 5:
                        print(f"  Operations needed: insertions, deletions, substitutions")
                else:
                    print("Please enter valid words")
                    
            elif choice == 5:
                try:
                    coins_input = input("Enter coin denominations (space-separated): ").strip()
                    amount = int(input("Enter target amount: "))
                    
                    coins = [int(x) for x in coins_input.split()]
                    
                    print(f"\nCoin Change Problem:")
                    print(f"  Available coins: {coins}")
                    print(f"  Target amount: {amount}")
                    
                    start_time = time.time()
                    min_coins = coin_change(coins, amount)
                    end_time = time.time()
                    
                    if min_coins != -1:
                        print(f"  Minimum coins needed: {min_coins}")
                    else:
                        print(f"  Cannot make amount {amount} with given coins")
                    print(f"Computed in {(end_time - start_time) * 1000:.2f} ms")
                except ValueError:
                    print("Please enter valid numbers")
                    
            elif choice == 6:
                array_input = input("Enter array elements (space-separated): ").strip()
                try:
                    numbers = [int(x) for x in array_input.split()]
                    
                    if numbers:
                        print(f"\nMaximum Subarray Sum (Kadane's Algorithm):")
                        print(f"  Array: {numbers}")
                        
                        start_time = time.time()
                        max_sum = maximum_subarray_sum(numbers)
                        end_time = time.time()
                        
                        print(f"  Maximum subarray sum: {max_sum}")
                        print(f"Computed in {(end_time - start_time) * 1000:.2f} ms")
                    else:
                        print("Please enter valid numbers")
                except ValueError:
                    print("Please enter valid integers")
                    
            elif choice == 7:
                print(f"\nAvailable DP Problems:")
                print("  1. Longest Increasing Subsequence")
                print("  2. Custom Fibonacci with memoization")
                print("  3. Count paths in grid")
                
                try:
                    prob_choice = int(input("Choose problem (1-3): "))
                    
                    if prob_choice == 1:
                        array_input = input("Enter sequence (space-separated): ").strip()
                        numbers = [int(x) for x in array_input.split()]
                        
                        if numbers:
                            lis_length = longest_increasing_subsequence(numbers)
                            print(f"Array: {numbers}")
                            print(f"Longest Increasing Subsequence length: {lis_length}")
                        else:
                            print("Please enter valid numbers")
                            
                    elif prob_choice == 2:
                        n = int(input("Enter n for optimized Fibonacci(n): "))
                        if 0 <= n <= 100:
                            result = fibonacci_dp(n)
                            print(f"Fibonacci({n}) = {result}")
                        else:
                            print("Please enter a number between 0 and 100")
                            
                    elif prob_choice == 3:
                        print("Grid path counting not implemented in this demo")
                        print("Would count paths from top-left to bottom-right")
                        
                    else:
                        print("Invalid choice")
                except ValueError:
                    print("Please enter valid numbers")
                    
            elif choice == 8:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def string_algorithms_demo():
    """Interactive demo for string algorithms."""
    print("\n" + "="*50)
    print("STRING ALGORITHMS DEMO")
    print("="*50)
    
    while True:
        print(f"\nString Algorithms:")
        print("1. Pattern Matching (KMP)")
        print("2. Pattern Matching (Rabin-Karp)")
        print("3. Compare algorithms")
        print("4. Custom text search")
        print("5. Algorithm analysis")
        print("6. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-6): "))
            
            if choice == 1:
                text = input("Enter text: ").strip()
                pattern = input("Enter pattern to search: ").strip()
                
                if text and pattern:
                    print(f"\nKMP Pattern Matching:")
                    print(f"  Text: '{text}'")
                    print(f"  Pattern: '{pattern}'")
                    
                    start_time = time.time()
                    matches = kmp_search(text, pattern)
                    end_time = time.time()
                    
                    if matches:
                        print(f"  Found at positions: {matches}")
                        # Show context
                        for pos in matches[:5]:
                            start_pos = max(0, pos - 5)
                            end_pos = min(len(text), pos + len(pattern) + 5)
                            context = text[start_pos:end_pos]
                            highlighted = context.replace(pattern, f"[{pattern}]")
                            print(f"    Position {pos}: ...{highlighted}...")
                    else:
                        print(f"  Pattern not found")
                    
                    print(f"  Time: {(end_time - start_time) * 1000:.2f} ms")
                else:
                    print("Please enter valid text and pattern")
                    
            elif choice == 2:
                text = input("Enter text: ").strip()
                pattern = input("Enter pattern to search: ").strip()
                
                if text and pattern:
                    print(f"\nRabin-Karp Pattern Matching:")
                    print(f"  Text: '{text}'")
                    print(f"  Pattern: '{pattern}'")
                    
                    start_time = time.time()
                    matches = rabin_karp_search(text, pattern)
                    end_time = time.time()
                    
                    if matches:
                        print(f"  Found at positions: {matches}")
                    else:
                        print(f"  Pattern not found")
                    
                    print(f"  Time: {(end_time - start_time) * 1000:.2f} ms")
                else:
                    print("Please enter valid text and pattern")
                    
            elif choice == 3:
                # Sample data for comparison
                sample_texts = [
                    ("ABABDABACDABABCABCABCABC", "ABABCABC"),
                    ("The quick brown fox jumps over the lazy dog", "fox"),
                    ("GEEKS FOR GEEKS", "GEEK"),
                    ("mississippi", "issi")
                ]
                
                print(f"\nAlgorithm Comparison:")
                print(f"{'Text':<30} {'Pattern':<10} {'KMP (ms)':<10} {'R-K (ms)':<10} {'Matches'}")
                print("-" * 70)
                
                for text, pattern in sample_texts:
                    # KMP
                    start_time = time.time()
                    kmp_matches = kmp_search(text, pattern)
                    kmp_time = (time.time() - start_time) * 1000
                    
                    # Rabin-Karp
                    start_time = time.time()
                    rk_matches = rabin_karp_search(text, pattern)
                    rk_time = (time.time() - start_time) * 1000
                    
                    text_short = text[:25] + "..." if len(text) > 25 else text
                    print(f"{text_short:<30} {pattern:<10} {kmp_time:<10.3f} {rk_time:<10.3f} {len(kmp_matches)}")
                    
            elif choice == 4:
                print(f"\nCustom Text Search:")
                text = input("Enter your text: ").strip()
                
                if text:
                    print(f"Text loaded: {len(text)} characters")
                    
                    while True:
                        pattern = input("Enter pattern to search (or 'back'): ").strip()
                        if pattern.lower() == 'back':
                            break
                        
                        if pattern:
                            # Use both algorithms
                            kmp_matches = kmp_search(text, pattern)
                            rk_matches = rabin_karp_search(text, pattern)
                            
                            print(f"Pattern: '{pattern}'")
                            print(f"KMP found {len(kmp_matches)} matches: {kmp_matches}")
                            print(f"Rabin-Karp found {len(rk_matches)} matches: {rk_matches}")
                            
                            if kmp_matches == rk_matches:
                                print("✓ Both algorithms agree")
                            else:
                                print("✗ Algorithms disagree!")
                        else:
                            print("Please enter a pattern")
                else:
                    print("Please enter valid text")
                    
            elif choice == 5:
                print(f"\nString Algorithm Analysis:")
                print(f"\nKMP (Knuth-Morris-Pratt):")
                print(f"  Time Complexity: O(n + m)")
                print(f"  Space Complexity: O(m)")
                print(f"  Preprocessing: Builds failure function")
                print(f"  Best for: Guaranteed linear time")
                
                print(f"\nRabin-Karp:")
                print(f"  Time Complexity: O(n + m) average, O(nm) worst")
                print(f"  Space Complexity: O(1)")
                print(f"  Preprocessing: None")
                print(f"  Best for: Multiple pattern search, rolling hash")
                
                print(f"\nWhen to use:")
                print(f"  KMP: When you need guaranteed performance")
                print(f"  Rabin-Karp: When searching multiple patterns")
                print(f"  Both are better than naive O(nm) approach")
                
            elif choice == 6:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def performance_comparison():
    """Compare performance of different algorithm categories."""
    print("\n" + "="*50)
    print("ALGORITHM PERFORMANCE COMPARISON")
    print("="*50)
    
    import random
    
    while True:
        print(f"\nPerformance Analysis:")
        print("1. Sorting algorithm comparison")
        print("2. Searching algorithm comparison")
        print("3. Graph algorithm scalability")
        print("4. DP vs naive implementations")
        print("5. String matching comparison")
        print("6. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-6): "))
            
            if choice == 1:
                sizes = [100, 500, 1000]
                algorithms = [
                    ("Bubble Sort", bubble_sort),
                    ("Selection Sort", selection_sort),
                    ("Insertion Sort", insertion_sort),
                    ("Merge Sort", merge_sort),
                    ("Quick Sort", quick_sort),
                    ("Heap Sort", heap_sort)
                ]
                
                print(f"\nSorting Performance (ms):")
                header = f"{'Algorithm':<15} "
                for size in sizes:
                    header += f"{size}el".ljust(8)
                print(header)
                print("-" * 50)
                
                for name, algorithm in algorithms:
                    times = []
                    for size in sizes:
                        if size > 500 and name in ["Bubble Sort", "Selection Sort"]:
                            times.append("Too slow")
                            continue
                        
                        test_data = [random.randint(1, 1000) for _ in range(size)]
                        start_time = time.time()
                        algorithm(test_data)
                        end_time = time.time()
                        times.append(f"{(end_time - start_time) * 1000:.1f}")
                    
                    time_str = ' '.join(f'{t:<8}' for t in times)
                    print(f"{name:<15} {time_str}")
                    
            elif choice == 2:
                sizes = [1000, 5000, 10000]
                print(f"\nSearching Performance (μs, searching for middle element):")
                print(f"{'Algorithm':<20} {' '.join(f'{size}el':<10 for size in sizes)}")
                print("-" * 60)
                
                algorithms = [
                    ("Linear Search", linear_search),
                    ("Binary Search", binary_search),
                    ("Jump Search", jump_search)
                ]
                
                for name, algorithm in algorithms:
                    times = []
                    for size in sizes:
                        sorted_array = list(range(size))
                        target = size // 2
                        
                        start_time = time.time()
                        algorithm(sorted_array, target)
                        end_time = time.time()
                        
                        times.append(f"{(end_time - start_time) * 1000000:.1f}")
                    
                    time_str = ' '.join(f'{t:<10}' for t in times)
                    print(f"{name:<20} {time_str}")
                    
            elif choice == 3:
                print(f"\nGraph Algorithm Scalability:")
                
                # Create sample graphs of different sizes
                def create_graph(nodes):
                    graph = {}
                    for i in range(nodes):
                        graph[f'N{i}'] = []
                        # Connect to next few nodes (circular)
                        for j in range(1, min(4, nodes)):
                            neighbor = f'N{(i + j) % nodes}'
                            graph[f'N{i}'].append(neighbor)
                    return graph
                
                sizes = [10, 50, 100]
                print(f"{'Nodes':<8} {'DFS (ms)':<10} {'BFS (ms)':<10}")
                print("-" * 30)
                
                for size in sizes:
                    graph = create_graph(size)
                    start_node = 'N0'
                    
                    # DFS
                    start_time = time.time()
                    depth_first_search(graph, start_node)
                    dfs_time = (time.time() - start_time) * 1000
                    
                    # BFS
                    start_time = time.time()
                    breadth_first_search(graph, start_node)
                    bfs_time = (time.time() - start_time) * 1000
                    
                    print(f"{size:<8} {dfs_time:<10.2f} {bfs_time:<10.2f}")
                    
            elif choice == 4:
                print(f"\nDynamic Programming vs Naive:")
                
                def fibonacci_naive(n):
                    if n <= 1:
                        return n
                    return fibonacci_naive(n-1) + fibonacci_naive(n-2)
                
                test_values = [10, 15, 20, 25]
                print(f"{'N':<4} {'Naive (ms)':<12} {'DP (ms)':<10} {'Speedup':<10}")
                print("-" * 40)
                
                for n in test_values:
                    if n <= 20:  # Naive gets too slow
                        start_time = time.time()
                        fibonacci_naive(n)
                        naive_time = (time.time() - start_time) * 1000
                    else:
                        naive_time = float('inf')
                    
                    start_time = time.time()
                    fibonacci_dp(n)
                    dp_time = (time.time() - start_time) * 1000
                    
                    speedup = naive_time / dp_time if dp_time > 0 and naive_time != float('inf') else "∞"
                    naive_str = f"{naive_time:.1f}" if naive_time != float('inf') else "Too slow"
                    
                    print(f"{n:<4} {naive_str:<12} {dp_time:<10.3f} {speedup}")
                    
            elif choice == 5:
                texts = ["Short text", "A" * 1000, "ABAB" * 250]
                pattern = "ABAB"
                
                print(f"\nString Matching Performance:")
                print(f"{'Text Length':<12} {'KMP (ms)':<10} {'Rabin-Karp (ms)':<15}")
                print("-" * 40)
                
                for text in texts:
                    # KMP
                    start_time = time.time()
                    kmp_search(text, pattern)
                    kmp_time = (time.time() - start_time) * 1000
                    
                    # Rabin-Karp
                    start_time = time.time()
                    rabin_karp_search(text, pattern)
                    rk_time = (time.time() - start_time) * 1000
                    
                    print(f"{len(text):<12} {kmp_time:<10.3f} {rk_time:<15.3f}")
                    
            elif choice == 6:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def algorithm_selection_guide():
    """Provide guidance on algorithm selection."""
    print("\n" + "="*50)
    print("ALGORITHM SELECTION GUIDE")
    print("="*50)
    
    while True:
        print(f"\nAlgorithm Selection Topics:")
        print("1. Sorting algorithm selection")
        print("2. Searching algorithm selection")
        print("3. Graph algorithm selection")
        print("4. When to use Dynamic Programming")
        print("5. String algorithm selection")
        print("6. Performance vs Memory trade-offs")
        print("7. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-7): "))
            
            if choice == 1:
                print(f"\nSorting Algorithm Selection Guide:")
                scenarios = {
                    "Small datasets (< 50)": "Insertion Sort - Simple and efficient",
                    "Large datasets": "Merge Sort or Quick Sort - O(n log n)",
                    "Nearly sorted data": "Insertion Sort - O(n) for nearly sorted",
                    "Memory constrained": "Heap Sort - O(1) extra space",
                    "Stability required": "Merge Sort - Maintains relative order",
                    "Integer data in range": "Counting Sort - O(n + k) linear time",
                    "External sorting": "Merge Sort - Good for disk-based sorting"
                }
                
                for scenario, recommendation in scenarios.items():
                    print(f"  {scenario}: {recommendation}")
                    
            elif choice == 2:
                print(f"\nSearching Algorithm Selection Guide:")
                scenarios = {
                    "Unsorted data": "Linear Search - Only option O(n)",
                    "Sorted data (small)": "Binary Search - O(log n)",
                    "Sorted data (large)": "Binary Search - Most efficient",
                    "Uniform distribution": "Interpolation Search - O(log log n)",
                    "Block-based access": "Jump Search - O(√n), good for tapes",
                    "Multiple searches": "Build hash table first - O(1) per search"
                }
                
                for scenario, recommendation in scenarios.items():
                    print(f"  {scenario}: {recommendation}")
                    
            elif choice == 3:
                print(f"\nGraph Algorithm Selection Guide:")
                scenarios = {
                    "Find all reachable nodes": "DFS or BFS - both O(V + E)",
                    "Shortest path in unweighted": "BFS - O(V + E)",
                    "Shortest path (positive weights)": "Dijkstra - O((V + E) log V)",
                    "Shortest path (negative weights)": "Bellman-Ford - O(VE)",
                    "All pairs shortest paths": "Floyd-Warshall - O(V³)",
                    "Minimum spanning tree (sparse)": "Kruskal - O(E log E)",
                    "Minimum spanning tree (dense)": "Prim - O(V²) or O((V + E) log V)",
                    "Cycle detection": "DFS with color coding",
                    "Topological sorting": "DFS or Kahn's algorithm"
                }
                
                for scenario, recommendation in scenarios.items():
                    print(f"  {scenario}: {recommendation}")
                    
            elif choice == 4:
                print(f"\nWhen to Use Dynamic Programming:")
                criteria = [
                    "Optimal substructure - optimal solution contains optimal solutions to subproblems",
                    "Overlapping subproblems - same subproblems solved multiple times",
                    "Optimization problems - finding minimum/maximum value",
                    "Counting problems - number of ways to do something",
                    "Decision problems - can we achieve a certain goal"
                ]
                
                examples = {
                    "Classic DP Problems": [
                        "Fibonacci - overlapping subproblems",
                        "Knapsack - optimization with constraints",
                        "LCS - sequence alignment and comparison",
                        "Edit Distance - string similarity",
                        "Coin Change - minimum coins to make amount"
                    ],
                    "Signs you need DP": [
                        "Recursive solution with repeated calls",
                        "Problem asks for optimal value",
                        "Problem has multiple ways to reach solution",
                        "Time complexity is exponential without memoization"
                    ]
                }
                
                print(f"Criteria for DP:")
                for criterion in criteria:
                    print(f"  • {criterion}")
                
                for category, items in examples.items():
                    print(f"\n{category}:")
                    for item in items:
                        print(f"  • {item}")
                        
            elif choice == 5:
                print(f"\nString Algorithm Selection Guide:")
                scenarios = {
                    "Single pattern, multiple texts": "KMP - precompute pattern",
                    "Multiple patterns, single text": "Rabin-Karp with rolling hash",
                    "Very long patterns": "KMP - guaranteed O(n + m)",
                    "Short patterns": "Naive search might be sufficient",
                    "Approximate matching": "Edit distance algorithms",
                    "Wildcard patterns": "Regular expressions or specialized algorithms",
                    "Suffix-based operations": "Suffix trees or suffix arrays"
                }
                
                for scenario, recommendation in scenarios.items():
                    print(f"  {scenario}: {recommendation}")
                    
            elif choice == 6:
                print(f"\nPerformance vs Memory Trade-offs:")
                
                tradeoffs = {
                    "Sorting": {
                        "Time-optimized": "Quick Sort - O(n log n) avg, O(log n) space",
                        "Space-optimized": "Heap Sort - O(n log n), O(1) space",
                        "Balanced": "Merge Sort - O(n log n), O(n) space, stable"
                    },
                    "Searching": {
                        "Time-optimized": "Hash Table - O(1) search, O(n) space",
                        "Space-optimized": "Binary Search - O(log n) search, O(1) space",
                        "Balanced": "Balanced BST - O(log n) search, O(n) space"
                    },
                    "Graph Algorithms": {
                        "Time-optimized": "Adjacency Matrix - O(1) edge check, O(V²) space",
                        "Space-optimized": "Adjacency List - O(V) edge check, O(V + E) space",
                        "Balanced": "Depends on graph density"
                    }
                }
                
                for category, options in tradeoffs.items():
                    print(f"\n{category}:")
                    for option_type, description in options.items():
                        print(f"  {option_type}: {description}")
                        
            elif choice == 7:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Main function to run the interactive demo."""
    print("Welcome to the Algorithms Interactive Learning Tool!")
    print("This demo will help you understand fundamental algorithms and their applications.")
    
    while True:
        display_main_menu()
        
        try:
            choice = int(input("\nEnter your choice (1-8): "))
            
            if choice == 1:
                sorting_algorithms_demo()
            elif choice == 2:
                searching_algorithms_demo()
            elif choice == 3:
                graph_algorithms_demo()
            elif choice == 4:
                dynamic_programming_demo()
            elif choice == 5:
                string_algorithms_demo()
            elif choice == 6:
                performance_comparison()
            elif choice == 7:
                algorithm_selection_guide()
            elif choice == 8:
                print("\nThank you for using the Algorithms Demo!")
                print("Keep exploring algorithms and happy coding!")
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