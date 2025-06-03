"""
Algorithms Implementation

This module provides comprehensive implementations of fundamental algorithms
including sorting, searching, graph algorithms, and dynamic programming.
"""

from typing import List, Tuple, Optional, Dict, Any, Callable
import heapq
from collections import defaultdict, deque
import math


# ==================== SORTING ALGORITHMS ====================

def bubble_sort(arr: List[Any]) -> List[Any]:
    """
    Bubble Sort implementation.
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    Stable: Yes
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr


def selection_sort(arr: List[Any]) -> List[Any]:
    """
    Selection Sort implementation.
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    Stable: No
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


def insertion_sort(arr: List[Any]) -> List[Any]:
    """
    Insertion Sort implementation.
    
    Time Complexity: O(n²)
    Space Complexity: O(1)
    Stable: Yes
    """
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    
    return arr


def merge_sort(arr: List[Any]) -> List[Any]:
    """
    Merge Sort implementation.
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    Stable: Yes
    """
    if len(arr) <= 1:
        return arr.copy()
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return _merge(left, right)


def _merge(left: List[Any], right: List[Any]) -> List[Any]:
    """Helper function for merge sort."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def quick_sort(arr: List[Any]) -> List[Any]:
    """
    Quick Sort implementation.
    
    Time Complexity: O(n log n) average, O(n²) worst
    Space Complexity: O(log n)
    Stable: No
    """
    arr = arr.copy()
    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr


def _quick_sort_helper(arr: List[Any], low: int, high: int) -> None:
    """Helper function for quick sort."""
    if low < high:
        pi = _partition(arr, low, high)
        _quick_sort_helper(arr, low, pi - 1)
        _quick_sort_helper(arr, pi + 1, high)


def _partition(arr: List[Any], low: int, high: int) -> int:
    """Partition function for quick sort."""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def heap_sort(arr: List[Any]) -> List[Any]:
    """
    Heap Sort implementation.
    
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    Stable: No
    """
    arr = arr.copy()
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(arr, i, 0)
    
    return arr


def _heapify(arr: List[Any], n: int, i: int) -> None:
    """Helper function for heap sort."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)


def counting_sort(arr: List[int], max_val: Optional[int] = None) -> List[int]:
    """
    Counting Sort implementation for integers.
    
    Time Complexity: O(n + k) where k is the range
    Space Complexity: O(k)
    Stable: Yes
    """
    if not arr:
        return []
    
    if max_val is None:
        max_val = max(arr)
    
    min_val = min(arr)
    range_val = max_val - min_val + 1
    
    count = [0] * range_val
    output = [0] * len(arr)
    
    # Count occurrences
    for num in arr:
        count[num - min_val] += 1
    
    # Calculate cumulative count
    for i in range(1, range_val):
        count[i] += count[i - 1]
    
    # Build output array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    
    return output


def radix_sort(arr: List[int]) -> List[int]:
    """
    Radix Sort implementation for non-negative integers.
    
    Time Complexity: O(d * (n + k)) where d is digits, k is radix
    Space Complexity: O(n + k)
    Stable: Yes
    """
    if not arr:
        return []
    
    max_num = max(arr)
    exp = 1
    
    while max_num // exp > 0:
        arr = _counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr


def _counting_sort_by_digit(arr: List[int], exp: int) -> List[int]:
    """Helper function for radix sort."""
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Count occurrences of each digit
    for num in arr:
        index = (num // exp) % 10
        count[index] += 1
    
    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
    
    return output


# ==================== SEARCHING ALGORITHMS ====================

def linear_search(arr: List[Any], target: Any) -> int:
    """
    Linear Search implementation.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1


def binary_search(arr: List[Any], target: Any) -> int:
    """
    Binary Search implementation (requires sorted array).
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr: List[Any], target: Any, left: int = 0, right: int = None) -> int:
    """
    Recursive Binary Search implementation.
    
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def jump_search(arr: List[Any], target: Any) -> int:
    """
    Jump Search implementation (requires sorted array).
    
    Time Complexity: O(√n)
    Space Complexity: O(1)
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    
    # Jump ahead
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    
    # Linear search in the block
    while arr[prev] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    
    if arr[prev] == target:
        return prev
    
    return -1


def interpolation_search(arr: List[int], target: int) -> int:
    """
    Interpolation Search implementation (requires sorted array with uniform distribution).
    
    Time Complexity: O(log log n) average, O(n) worst
    Space Complexity: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right and target >= arr[left] and target <= arr[right]:
        if left == right:
            if arr[left] == target:
                return left
            return -1
        
        # Interpolation formula
        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
        
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    
    return -1


# ==================== GRAPH ALGORITHMS ====================

def depth_first_search(graph: Dict[Any, List[Any]], start: Any, visited: Optional[set] = None) -> List[Any]:
    """
    Depth-First Search implementation.
    
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    if visited is None:
        visited = set()
    
    result = []
    
    def dfs_helper(node):
        visited.add(node)
        result.append(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_helper(neighbor)
    
    dfs_helper(start)
    return result


def breadth_first_search(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Breadth-First Search implementation.
    
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    visited = set()
    queue = deque([start])
    result = []
    visited.add(start)
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result


def dijkstra_shortest_path(graph: Dict[Any, List[Tuple[Any, int]]], start: Any) -> Dict[Any, int]:
    """
    Dijkstra's shortest path algorithm.
    
    Time Complexity: O((V + E) log V)
    Space Complexity: O(V)
    """
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        for neighbor, weight in graph.get(current_node, []):
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances


def bellman_ford(graph: Dict[Any, List[Tuple[Any, int]]], start: Any) -> Tuple[Dict[Any, int], bool]:
    """
    Bellman-Ford algorithm for shortest paths (handles negative weights).
    
    Time Complexity: O(VE)
    Space Complexity: O(V)
    
    Returns:
        Tuple of (distances, has_negative_cycle)
    """
    # Get all vertices
    vertices = set(graph.keys())
    for neighbors in graph.values():
        for neighbor, _ in neighbors:
            vertices.add(neighbor)
    
    distances = {vertex: float('infinity') for vertex in vertices}
    distances[start] = 0
    
    # Relax edges V-1 times
    for _ in range(len(vertices) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] != float('infinity'):
                    if distances[node] + weight < distances[neighbor]:
                        distances[neighbor] = distances[node] + weight
    
    # Check for negative cycles
    has_negative_cycle = False
    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] != float('infinity'):
                if distances[node] + weight < distances[neighbor]:
                    has_negative_cycle = True
                    break
        if has_negative_cycle:
            break
    
    return distances, has_negative_cycle


def floyd_warshall(graph: Dict[Any, Dict[Any, int]]) -> Dict[Any, Dict[Any, int]]:
    """
    Floyd-Warshall algorithm for all-pairs shortest paths.
    
    Time Complexity: O(V³)
    Space Complexity: O(V²)
    """
    vertices = list(graph.keys())
    n = len(vertices)
    
    # Initialize distance matrix
    dist = {}
    for i in vertices:
        dist[i] = {}
        for j in vertices:
            if i == j:
                dist[i][j] = 0
            elif j in graph[i]:
                dist[i][j] = graph[i][j]
            else:
                dist[i][j] = float('infinity')
    
    # Floyd-Warshall algorithm
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist


def topological_sort(graph: Dict[Any, List[Any]]) -> List[Any]:
    """
    Topological sort using DFS.
    
    Time Complexity: O(V + E)
    Space Complexity: O(V)
    """
    visited = set()
    stack = []
    
    def dfs_helper(node):
        visited.add(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_helper(neighbor)
        
        stack.append(node)
    
    # Visit all vertices
    for vertex in graph:
        if vertex not in visited:
            dfs_helper(vertex)
    
    return stack[::-1]


def kruskal_mst(edges: List[Tuple[Any, Any, int]]) -> List[Tuple[Any, Any, int]]:
    """
    Kruskal's algorithm for Minimum Spanning Tree.
    
    Time Complexity: O(E log E)
    Space Complexity: O(V)
    """
    # Union-Find data structure
    parent = {}
    rank = {}
    
    def find(x):
        if x not in parent:
            parent[x] = x
            rank[x] = 0
        
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False
        
        if rank[px] < rank[py]:
            parent[px] = py
        elif rank[px] > rank[py]:
            parent[py] = px
        else:
            parent[py] = px
            rank[px] += 1
        
        return True
    
    # Sort edges by weight
    edges_sorted = sorted(edges, key=lambda x: x[2])
    mst = []
    
    for u, v, weight in edges_sorted:
        if union(u, v):
            mst.append((u, v, weight))
    
    return mst


def prim_mst(graph: Dict[Any, List[Tuple[Any, int]]]) -> List[Tuple[Any, Any, int]]:
    """
    Prim's algorithm for Minimum Spanning Tree.
    
    Time Complexity: O((V + E) log V)
    Space Complexity: O(V)
    """
    if not graph:
        return []
    
    mst = []
    visited = set()
    
    # Start from arbitrary vertex
    start = next(iter(graph))
    visited.add(start)
    
    # Priority queue of edges (weight, from, to)
    edges = []
    for neighbor, weight in graph[start]:
        heapq.heappush(edges, (weight, start, neighbor))
    
    while edges and len(visited) < len(graph):
        weight, u, v = heapq.heappop(edges)
        
        if v in visited:
            continue
        
        visited.add(v)
        mst.append((u, v, weight))
        
        # Add new edges
        for neighbor, edge_weight in graph[v]:
            if neighbor not in visited:
                heapq.heappush(edges, (edge_weight, v, neighbor))
    
    return mst


# ==================== DYNAMIC PROGRAMMING ====================

def fibonacci_dp(n: int) -> int:
    """
    Fibonacci using dynamic programming.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    
    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1


def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Longest Common Subsequence using dynamic programming.
    
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    """
    0/1 Knapsack problem using dynamic programming.
    
    Time Complexity: O(n * W)
    Space Complexity: O(n * W)
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]


def edit_distance(word1: str, word2: str) -> int:
    """
    Edit distance (Levenshtein distance) using dynamic programming.
    
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # deletion
                    dp[i][j - 1],      # insertion
                    dp[i - 1][j - 1]   # substitution
                )
    
    return dp[m][n]


def coin_change(coins: List[int], amount: int) -> int:
    """
    Coin change problem using dynamic programming.
    
    Time Complexity: O(amount * len(coins))
    Space Complexity: O(amount)
    """
    dp = [float('infinity')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('infinity') else -1


def longest_increasing_subsequence(nums: List[int]) -> int:
    """
    Longest Increasing Subsequence using dynamic programming.
    
    Time Complexity: O(n²)
    Space Complexity: O(n)
    """
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


def maximum_subarray_sum(nums: List[int]) -> int:
    """
    Maximum subarray sum using Kadane's algorithm.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
    
    max_ending_here = max_so_far = nums[0]
    
    for i in range(1, len(nums)):
        max_ending_here = max(nums[i], max_ending_here + nums[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far


# ==================== STRING ALGORITHMS ====================

def kmp_search(text: str, pattern: str) -> List[int]:
    """
    Knuth-Morris-Pratt string matching algorithm.
    
    Time Complexity: O(n + m)
    Space Complexity: O(m)
    """
    def compute_lps(pattern):
        """Compute Longest Proper Prefix which is also Suffix array."""
        m = len(pattern)
        lps = [0] * m
        length = 0
        i = 1
        
        while i < m:
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps
    
    n, m = len(text), len(pattern)
    if m == 0:
        return []
    
    lps = compute_lps(pattern)
    matches = []
    
    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return matches


def rabin_karp_search(text: str, pattern: str) -> List[int]:
    """
    Rabin-Karp string matching algorithm using rolling hash.
    
    Time Complexity: O(n + m) average, O(nm) worst
    Space Complexity: O(1)
    """
    n, m = len(text), len(pattern)
    if m > n:
        return []
    
    base = 256
    prime = 101
    
    pattern_hash = 0
    text_hash = 0
    h = 1
    matches = []
    
    # Calculate h = pow(base, m-1) % prime
    for _ in range(m - 1):
        h = (h * base) % prime
    
    # Calculate hash for pattern and first window of text
    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime
    
    # Slide the pattern over text
    for i in range(n - m + 1):
        # Check if hash values match
        if pattern_hash == text_hash:
            # Check characters one by one
            if text[i:i + m] == pattern:
                matches.append(i)
        
        # Calculate hash for next window
        if i < n - m:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime
    
    return matches


# ==================== UTILITY FUNCTIONS ====================

def is_sorted(arr: List[Any], reverse: bool = False) -> bool:
    """Check if array is sorted."""
    if len(arr) <= 1:
        return True
    
    if reverse:
        return all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
    else:
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))


def get_algorithm_info() -> Dict[str, Dict[str, str]]:
    """Get information about all implemented algorithms."""
    return {
        "Sorting Algorithms": {
            "Bubble Sort": "O(n²) - Simple but inefficient",
            "Selection Sort": "O(n²) - Finds minimum each iteration",
            "Insertion Sort": "O(n²) - Good for small/nearly sorted arrays",
            "Merge Sort": "O(n log n) - Stable, divide and conquer",
            "Quick Sort": "O(n log n) avg - Fast in practice",
            "Heap Sort": "O(n log n) - In-place, not stable",
            "Counting Sort": "O(n + k) - For integers in range",
            "Radix Sort": "O(d(n + k)) - For integers"
        },
        "Searching Algorithms": {
            "Linear Search": "O(n) - Works on unsorted arrays",
            "Binary Search": "O(log n) - Requires sorted array",
            "Jump Search": "O(√n) - Block-based search",
            "Interpolation Search": "O(log log n) - For uniform data"
        },
        "Graph Algorithms": {
            "DFS": "O(V + E) - Depth-first traversal",
            "BFS": "O(V + E) - Breadth-first traversal",
            "Dijkstra": "O((V + E) log V) - Shortest path",
            "Bellman-Ford": "O(VE) - Handles negative weights",
            "Floyd-Warshall": "O(V³) - All pairs shortest path",
            "Kruskal MST": "O(E log E) - Minimum spanning tree",
            "Prim MST": "O((V + E) log V) - Minimum spanning tree"
        },
        "Dynamic Programming": {
            "Fibonacci": "O(n) - Classic DP example",
            "LCS": "O(mn) - Longest common subsequence",
            "Knapsack": "O(nW) - 0/1 knapsack problem",
            "Edit Distance": "O(mn) - String similarity",
            "Coin Change": "O(amount × coins) - Minimum coins",
            "LIS": "O(n²) - Longest increasing subsequence"
        },
        "String Algorithms": {
            "KMP": "O(n + m) - Pattern matching",
            "Rabin-Karp": "O(n + m) avg - Rolling hash search"
        }
    }