# Binary Tree Implementation

A comprehensive implementation of binary tree data structures in Python including Binary Tree, Binary Search Tree (BST), and AVL Tree with detailed explanations and real-world applications.

## 📖 Table of Contents

- [Overview](#overview)
- [Theory](#theory)
- [Implementation Details](#implementation-details)
- [Time and Space Complexity](#time-and-space-complexity)
- [Real-World Applications](#real-world-applications)
- [Usage Examples](#usage-examples)
- [Running the Code](#running-the-code)

## Overview

A **Binary Tree** is a hierarchical data structure where each node has at most two children, referred to as the left child and right child. Binary trees form the foundation for more specialized trees like Binary Search Trees and AVL Trees.

### Types Implemented

1. **Binary Tree**: Basic tree structure with insertion and traversal operations
2. **Binary Search Tree (BST)**: Maintains ordering property for efficient searching
3. **AVL Tree**: Self-balancing BST that maintains optimal height

### Key Characteristics

- **Hierarchical Structure**: Nodes organized in parent-child relationships
- **Binary Property**: Each node has at most two children
- **Root Node**: Single entry point to the tree
- **Leaf Nodes**: Nodes with no children
- **Height**: Length of longest path from root to leaf

## Theory

### Binary Tree Structure

```
       Root
      /    \
   Left    Right
   /  \    /   \
  ...  ... ... ...
```

### Tree Terminology

- **Node**: Each element in the tree containing data and references to children
- **Edge**: Connection between parent and child nodes
- **Path**: Sequence of nodes connected by edges
- **Depth**: Distance from root to a specific node
- **Height**: Maximum depth of any node in the tree
- **Subtree**: Tree formed by a node and all its descendants

### Binary Search Tree Property

For every node in a BST:
- All values in the left subtree are less than the node's value
- All values in the right subtree are greater than the node's value
- Both left and right subtrees are also BSTs

### AVL Tree Balancing

AVL trees maintain balance through rotations:
- **Balance Factor**: Height difference between left and right subtrees
- **Balanced**: Balance factor is -1, 0, or 1 for every node
- **Rotations**: Single and double rotations restore balance after insertions/deletions

## Implementation Details

### TreeNode Class

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None  # Optional parent reference
```

### Binary Tree Operations

| Operation | Description | Use Case |
|-----------|-------------|----------|
| `insert_left(parent, data)` | Insert as left child | Manual tree construction |
| `insert_right(parent, data)` | Insert as right child | Manual tree construction |
| `delete(data)` | Remove node with given data | Tree maintenance |
| `search(data)` | Find node with specific value | Data retrieval |
| `get_height()` | Calculate tree height | Performance analysis |
| `get_size()` | Count total nodes | Memory usage |

### Tree Traversals

| Traversal | Order | Use Case |
|-----------|-------|----------|
| **Inorder** | Left → Root → Right | Get sorted order (BST) |
| **Preorder** | Root → Left → Right | Copy tree structure |
| **Postorder** | Left → Right → Root | Delete tree, calculate size |
| **Level-order** | Level by level | Print by levels, BFS |

### BST Specific Operations

| Operation | Description | Benefit |
|-----------|-------------|---------|
| `insert(data)` | Insert maintaining BST property | Keeps data sorted |
| `find_min()` | Find smallest value | Quick access to minimum |
| `find_max()` | Find largest value | Quick access to maximum |
| `find_predecessor(data)` | Find next smaller value | Range queries |
| `find_successor(data)` | Find next larger value | Range queries |

### AVL Tree Features

- **Automatic Balancing**: Self-adjusts after every insertion/deletion
- **Rotation Types**: Single (LL, RR) and Double (LR, RL) rotations
- **Height Guarantee**: Always maintains O(log n) height
- **Balance Factor Tracking**: Monitors tree balance continuously

## Time and Space Complexity

### Binary Tree (General)

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Search | O(n) worst case | O(h) for recursion |
| Insert | O(n) worst case | O(h) for recursion |
| Delete | O(n) worst case | O(h) for recursion |
| Traversal | O(n) | O(h) for recursion |

### Binary Search Tree

| Operation | Average Case | Worst Case | Best Case |
|-----------|-------------|------------|-----------|
| Search | O(log n) | O(n) | O(1) |
| Insert | O(log n) | O(n) | O(1) |
| Delete | O(log n) | O(n) | O(1) |
| Find Min/Max | O(log n) | O(n) | O(1) |

### AVL Tree

| Operation | Time Complexity | Notes |
|-----------|----------------|-------|
| Search | O(log n) guaranteed | Always balanced |
| Insert | O(log n) guaranteed | Includes rebalancing |
| Delete | O(log n) guaranteed | Includes rebalancing |
| Rotation | O(1) | Constant time operation |

**Space Complexity**: O(n) for storage, O(log n) for recursion in balanced trees

## Real-World Applications

### 1. File Systems
- **Directory Structure**: Hierarchical organization of files and folders
- **Path Navigation**: Efficient file lookup and directory traversal
- **Implementation**: Unix/Linux file systems, Windows directory structure

### 2. Database Indexing
- **B+ Trees**: Database indexes for fast data retrieval
- **Query Optimization**: Range queries and sorted access
- **Implementation**: MySQL, PostgreSQL, Oracle database indexes

### 3. Expression Parsing
- **Mathematical Expressions**: Parse and evaluate arithmetic expressions
- **Compiler Design**: Abstract syntax trees for code compilation
- **Implementation**: Calculators, programming language interpreters

### 4. Decision Trees
- **Machine Learning**: Classification and regression algorithms
- **Business Logic**: Rule-based decision making systems
- **Implementation**: AI systems, expert systems, game AI

### 5. Network Routing
- **Routing Tables**: Efficient packet routing in networks
- **IP Address Lookup**: Fast network address resolution
- **Implementation**: Internet routers, network switches

### 6. Memory Management
- **Heap Data Structure**: Binary heap for priority queues
- **Memory Allocation**: Efficient memory block management
- **Implementation**: Operating system memory managers

### 7. Graphics and Games
- **Spatial Partitioning**: 3D space organization for collision detection
- **Scene Graphs**: Hierarchical representation of 3D scenes
- **Implementation**: Game engines, 3D modeling software

## Usage Examples

### Basic Binary Tree

```python
from implementation import BinaryTree

# Create and build tree
tree = BinaryTree(1)
tree.insert_left(1, 2)
tree.insert_right(1, 3)
tree.insert_left(2, 4)
tree.insert_right(2, 5)

# Display tree structure
tree.display_tree()

# Perform traversals
print("Inorder:", tree.inorder_traversal())
print("Preorder:", tree.preorder_traversal())
print("Level-order:", tree.level_order_traversal())
```

### Binary Search Tree

```python
from implementation import BinarySearchTree

# Create BST and insert values
bst = BinarySearchTree()
values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    bst.insert(value)

# Search operations
print("Search 40:", bst.search(40))
print("Minimum:", bst.find_min())
print("Maximum:", bst.find_max())

# Get sorted order
print("Sorted:", bst.inorder_traversal())
```

### AVL Tree

```python
from implementation import AVLTree

# Create AVL tree with automatic balancing
avl = AVLTree()
sequence = [1, 2, 3, 4, 5, 6, 7]  # Would be skewed in regular BST

for value in sequence:
    avl.insert(value)
    print(f"Height after inserting {value}: {avl.get_height()}")

print("Balanced:", avl.is_balanced())
print("Final height:", avl.get_height())
```

### Expression Tree

```python
# Build expression tree for (3 + 5) * 2
expr_tree = BinaryTree('*')
expr_tree.insert_left('*', '+')
expr_tree.insert_right('*', '2')
expr_tree.insert_left('+', '3')
expr_tree.insert_right('+', '5')

# Evaluate expression using traversal
def evaluate(node):
    if node.left is None and node.right is None:
        return int(node.data)
    
    left_val = evaluate(node.left)
    right_val = evaluate(node.right)
    
    if node.data == '+':
        return left_val + right_val
    elif node.data == '*':
        return left_val * right_val

result = evaluate(expr_tree.root)
print("Result:", result)  # Output: 16
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

The interactive demo provides:
- Basic binary tree operations
- BST insertion, deletion, and searching
- AVL tree balancing demonstrations
- Tree traversal visualizations
- Expression tree calculator
- Decision tree examples
- Performance comparisons

### Usage Examples

```bash
# Run comprehensive usage examples
python usage.py
```

This includes:
- All tree operation tests
- Real-world application examples
- Performance benchmarking
- Algorithm demonstrations

### File Structure

```
binary-tree/
├── implementation.py  # Core tree implementations
├── usage.py          # Comprehensive examples and tests
├── main.py           # Interactive demonstration
└── README.md         # This documentation
```

### Key Features Demonstrated

1. **Tree Construction**: Build trees manually or automatically
2. **Traversal Methods**: All four traversal types with explanations
3. **Search Operations**: Efficient searching in BST and AVL trees
4. **Balancing**: AVL tree self-balancing with rotation visualization
5. **Real Applications**: File systems, expression parsing, decision trees
6. **Performance Analysis**: Compare different tree types and operations

### Learning Path

1. **Start with**: Basic binary tree operations (`main.py` → option 1)
2. **Progress to**: BST properties and operations (`main.py` → option 2)
3. **Advanced**: AVL tree balancing (`main.py` → option 3)
4. **Applications**: Real-world examples (`usage.py`)
5. **Optimization**: Performance analysis and comparisons

This implementation provides a complete learning environment for understanding binary trees from basic concepts to advanced self-balancing structures, with practical applications and performance insights.