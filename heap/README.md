# Heap Implementation

A comprehensive implementation of heap data structures in Python including min-heap, max-heap, priority queue, and specialized heap variants with detailed explanations and real-world applications.

## 📖 Table of Contents

- [Overview](#overview)
- [Theory](#theory)
- [Implementation Details](#implementation-details)
- [Time and Space Complexity](#time-and-space-complexity)
- [Real-World Applications](#real-world-applications)
- [Usage Examples](#usage-examples)
- [Running the Code](#running-the-code)

## Overview

A **Heap** is a specialized tree-based data structure that satisfies the heap property. It's a complete binary tree where parent nodes have a specific relationship with their children - either greater than (max-heap) or less than (min-heap) all child nodes.

### Types Implemented

1. **Min-Heap**: Parent nodes are smaller than their children (root contains minimum)
2. **Max-Heap**: Parent nodes are larger than their children (root contains maximum)
3. **Priority Queue**: Queue where elements are served based on priority, not arrival order
4. **Median Heap**: Efficiently maintains running median using two heaps

### Key Characteristics

- **Complete Binary Tree**: All levels filled except possibly the last, filled left to right
- **Heap Property**: Consistent parent-child relationship throughout the tree
- **Array Representation**: Efficiently stored in arrays without pointers
- **Efficient Operations**: Logarithmic time for insertion and extraction

## Theory

### Heap Structure

```
Min-Heap Example:
       1
     /   \
    3     2
   / \   / \
  7   8 4   5

Array: [1, 3, 2, 7, 8, 4, 5]
```

### Array-Based Representation

For any element at index `i`:
- **Parent**: `(i - 1) // 2`
- **Left Child**: `2 * i + 1`
- **Right Child**: `2 * i + 2`

This representation eliminates the need for pointers and provides excellent cache locality.

### Heap Property

#### Min-Heap Property
- For every node `i`: `heap[i] ≤ heap[2*i+1]` and `heap[i] ≤ heap[2*i+2]`
- Root contains the minimum element
- Used for ascending priority queues

#### Max-Heap Property
- For every node `i`: `heap[i] ≥ heap[2*i+1]` and `heap[i] ≥ heap[2*i+2]`
- Root contains the maximum element
- Used for descending priority queues

### Heap Operations

#### Heapify Up (Bubble Up)
Used after insertion to maintain heap property:
1. Compare inserted element with parent
2. Swap if heap property violated
3. Repeat until property satisfied or reach root

#### Heapify Down (Bubble Down)
Used after extraction to maintain heap property:
1. Compare root with children
2. Swap with appropriate child (min/max depending on heap type)
3. Repeat until property satisfied or reach leaf

## Implementation Details

### Core Classes

#### MinHeap
```python
class MinHeap:
    def __init__(self, initial_data=None)
    def insert(self, item)          # O(log n)
    def extract_min(self)           # O(log n)
    def peek_min(self)              # O(1)
    def heap_sort(self)             # O(n log n)
```

#### MaxHeap
```python
class MaxHeap:
    def __init__(self, initial_data=None)
    def insert(self, item)          # O(log n)
    def extract_max(self)           # O(log n)
    def peek_max(self)              # O(1)
    def heap_sort(self)             # O(n log n)
```

#### PriorityQueue
```python
class PriorityQueue:
    def __init__(self, is_max_priority=False)
    def enqueue(self, item, priority)    # O(log n)
    def dequeue(self)                    # O(log n)
    def peek(self)                       # O(1)
    def update_priority(self, item, new_priority)  # O(n)
```

#### MedianHeap
```python
class MedianHeap:
    def __init__(self)
    def add_number(self, num)       # O(log n)
    def find_median(self)           # O(1)
```

### Advanced Features

- **Heap Construction**: Build heap from array in O(n) time
- **Priority Queue**: Support for both min and max priority
- **Median Tracking**: Efficient running median calculation
- **Flexible Comparison**: Support for custom comparison functions

## Time and Space Complexity

### Time Complexity

| Operation | Min/Max Heap | Priority Queue | Median Heap |
|-----------|-------------|----------------|-------------|
| **Insert** | O(log n) | O(log n) | O(log n) |
| **Extract** | O(log n) | O(log n) | - |
| **Peek** | O(1) | O(1) | O(1) |
| **Build Heap** | O(n) | O(n) | - |
| **Heap Sort** | O(n log n) | O(n log n) | - |
| **Find Median** | - | - | O(1) |

### Space Complexity

- **Storage**: O(n) for n elements
- **Auxiliary Space**: O(1) for iterative operations, O(log n) for recursive
- **Memory Efficiency**: Excellent due to array-based storage

### Performance Characteristics

- **Cache Friendly**: Array storage provides good cache locality
- **Memory Efficient**: No pointer overhead
- **Predictable Performance**: Guaranteed logarithmic operations

## Real-World Applications

### 1. Operating System Task Scheduling
- **Process Priority**: Schedule tasks based on priority levels
- **Real-time Systems**: Ensure high-priority tasks execute first
- **Load Balancing**: Distribute tasks across CPU cores efficiently

### 2. Network Packet Routing
- **Quality of Service (QoS)**: Prioritize critical network traffic
- **Bandwidth Management**: Allocate resources based on service levels
- **Traffic Shaping**: Control data flow to prevent network congestion

### 3. Emergency Response Systems
- **Hospital Triage**: Prioritize patients based on medical urgency
- **Emergency Services**: Dispatch resources to highest priority incidents
- **Disaster Management**: Allocate rescue resources effectively

### 4. Graph Algorithms
- **Dijkstra's Algorithm**: Find shortest paths using min-heap
- **Prim's Algorithm**: Build minimum spanning trees
- **A* Search**: Pathfinding with heuristic prioritization

### 5. Data Stream Processing
- **Top-K Problems**: Efficiently find largest/smallest K elements
- **Running Statistics**: Maintain median, percentiles in real-time
- **Event Processing**: Handle events based on timestamps and priorities

### 6. Memory Management
- **Garbage Collection**: Prioritize memory cleanup operations
- **Cache Replacement**: Implement LRU and other replacement policies
- **Resource Allocation**: Manage system resources efficiently

### 7. Financial Systems
- **Order Matching**: Process trading orders by price and time priority
- **Risk Management**: Prioritize risk assessment tasks
- **Payment Processing**: Handle transactions based on priority levels

## Usage Examples

### Basic Min-Heap Operations

```python
from implementation import MinHeap

# Create and populate min-heap
min_heap = MinHeap()
elements = [15, 10, 20, 8, 25, 5, 12]

for element in elements:
    min_heap.insert(element)
    print(f"Inserted {element}, min: {min_heap.peek_min()}")

# Extract elements in sorted order
sorted_elements = []
while not min_heap.is_empty():
    sorted_elements.append(min_heap.extract_min())

print(f"Sorted: {sorted_elements}")  # [5, 8, 10, 12, 15, 20, 25]
```

### Priority Queue for Task Scheduling

```python
from implementation import PriorityQueue

# Create high-priority queue (higher numbers = higher priority)
task_queue = PriorityQueue(is_max_priority=True)

# Add tasks with priorities
tasks = [
    ("Send email", 3),
    ("Critical bug fix", 10),
    ("Update docs", 2),
    ("Deploy to prod", 9),
    ("Team meeting", 5)
]

for task, priority in tasks:
    task_queue.enqueue(task, priority)

# Process tasks by priority
print("Processing tasks by priority:")
while not task_queue.is_empty():
    task = task_queue.dequeue()
    print(f"Executing: {task}")
```

### Real-Time Median Tracking

```python
from implementation import MedianHeap

# Track running median of data stream
median_heap = MedianHeap()
data_stream = [5, 15, 1, 3, 8, 7, 9, 2, 6, 4]

print("Tracking running median:")
for value in data_stream:
    median_heap.add_number(value)
    median = median_heap.find_median()
    print(f"Added {value}, median: {median}")
```

### Emergency Room Triage System

```python
from implementation import PriorityQueue

# Min-priority queue (lower numbers = higher priority)
emergency_queue = PriorityQueue(is_max_priority=False)

# Add patients with severity levels (1=critical, 5=minor)
patients = [
    ("John Doe", 3),      # Moderate
    ("Jane Smith", 1),    # Critical
    ("Bob Wilson", 5),    # Minor
    ("Alice Brown", 2),   # Serious
    ("Charlie Davis", 1)  # Critical
]

for patient, severity in patients:
    emergency_queue.enqueue(patient, severity)

print("Treating patients by severity:")
while not emergency_queue.is_empty():
    patient = emergency_queue.dequeue()
    print(f"Now treating: {patient}")
```

### Heap Sort Implementation

```python
from implementation import MinHeap

def heap_sort(arr):
    """Sort array using heap sort algorithm."""
    heap = MinHeap(arr.copy())
    return heap.heap_sort()

# Example usage
unsorted = [64, 34, 25, 12, 22, 11, 90]
sorted_array = heap_sort(unsorted)
print(f"Original: {unsorted}")
print(f"Sorted:   {sorted_array}")
```

### Finding Top-K Elements

```python
from implementation import MinHeap, k_largest, k_smallest

# Large dataset
data = [23, 45, 12, 67, 89, 34, 56, 78, 90, 13, 25, 47]

# Find top 5 largest elements efficiently
top_5 = k_largest(5, data)
print(f"Top 5 largest: {top_5}")

# Find bottom 3 smallest elements
bottom_3 = k_smallest(3, data)
print(f"Bottom 3 smallest: {bottom_3}")

# Manual approach using heap
def find_top_k(arr, k):
    """Find top k elements using min-heap."""
    heap = MinHeap()
    
    for num in arr:
        if heap.size() < k:
            heap.insert(num)
        elif num > heap.peek_min():
            heap.extract_min()
            heap.insert(num)
    
    return heap.heap_sort()[::-1]  # Return in descending order

top_k = find_top_k(data, 5)
print(f"Top 5 (manual): {top_k}")
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
- Min-heap and max-heap operations
- Priority queue simulations
- Median heap demonstrations
- Heap sort visualization
- Task scheduling simulation
- Performance analysis

### Usage Examples

```bash
# Run comprehensive examples and tests
python usage.py
```

Includes:
- Basic heap operations
- Priority queue applications
- Real-world simulations
- Performance comparisons
- Stream processing examples

### File Structure

```
heap/
├── implementation.py  # Core heap implementations
├── usage.py          # Comprehensive examples and applications
├── main.py           # Interactive demonstration
└── README.md         # This documentation
```

### Learning Progression

1. **Basic Concepts**: Understand heap property and array representation
2. **Operations**: Learn insertion, extraction, and heap maintenance
3. **Priority Queues**: Explore priority-based processing
4. **Applications**: Study real-world use cases and algorithms
5. **Optimization**: Analyze performance characteristics and trade-offs

This implementation provides a comprehensive foundation for understanding heap data structures and their applications in solving priority-based problems efficiently.