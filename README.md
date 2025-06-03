# Data Structures and Algorithms in Python

A comprehensive educational project implementing fundamental data structures and algorithms in Python with detailed documentation, practical examples, and interactive demonstrations.

## 📚 Project Structure

This project is organized into separate folders for each data structure and algorithm category:

### Implemented Data Structures

1. **[Linked Lists](./linked-list/)** - Singly and doubly linked lists with comprehensive operations
2. **[Stacks](./stack/)** - Multiple stack implementations including min-stack and applications
3. **[Queues](./queue/)** - Various queue types including circular, priority, and deque implementations
4. **[Binary Trees](./binary-tree/)** - Binary trees, BST, and AVL trees with traversals and operations
5. **[Graphs](./graph/)** - Directed and undirected graphs with traversal and pathfinding algorithms
6. **[Heaps](./heap/)** - Min-heap, max-heap, priority queues, and median heap implementations

## 🎯 Key Features

- **Complete Implementations**: Full-featured data structures with all essential operations
- **Interactive Demos**: Hands-on learning through interactive command-line interfaces
- **Real-World Examples**: Practical applications demonstrating usage scenarios
- **Performance Analysis**: Time and space complexity analysis with benchmarking
- **Educational Focus**: Clear explanations, comments, and step-by-step demonstrations
- **Comprehensive Testing**: Extensive test cases and usage examples

## 🚀 Quick Start

### Running Interactive Demos

Each data structure includes an interactive demonstration:

```bash
# Linked List Demo
cd linked-list && python main.py

# Stack Demo
cd stack && python main.py

# Queue Demo
cd queue && python main.py

# Binary Tree Demo
cd binary-tree && python main.py

# Graph Demo
cd graph && python main.py

# Heap Demo
cd heap && python main.py
```

### Running Usage Examples

Comprehensive examples and test cases:

```bash
# Run examples for any data structure
cd [data-structure-folder] && python usage.py
```

## 📖 Learning Path

### Beginner Level
1. **Linked Lists** - Understanding pointers and dynamic memory
2. **Stacks** - LIFO principle and recursive thinking
3. **Queues** - FIFO principle and buffering concepts

### Intermediate Level
4. **Binary Trees** - Hierarchical data and tree traversals
5. **Heaps** - Priority-based processing and heap properties

### Advanced Level
6. **Graphs** - Complex relationships and pathfinding algorithms

## 💡 Real-World Applications

### Linked Lists
- **Browser History**: Forward/backward navigation
- **Music Playlists**: Dynamic song management
- **Undo/Redo Systems**: Text editors and applications

### Stacks
- **Function Calls**: Programming language execution
- **Expression Evaluation**: Mathematical calculations
- **Browser Back Button**: Navigation state management

### Queues
- **Task Scheduling**: Operating system processes
- **Print Queues**: Document processing
- **Breadth-First Search**: Graph traversal algorithms

### Binary Trees
- **File Systems**: Directory hierarchies
- **Database Indexing**: Fast data retrieval
- **Expression Parsing**: Compiler design

### Graphs
- **Social Networks**: Friend connections and recommendations
- **Transportation**: Route planning and GPS navigation
- **Web Crawling**: Link analysis and page ranking

### Heaps
- **Priority Queues**: Emergency room triage systems
- **Task Scheduling**: Operating system job management
- **Data Streams**: Real-time median and top-K processing

## 🔧 Technical Specifications

### Requirements
- Python 3.7 or higher
- No external dependencies required
- Cross-platform compatibility

### Code Quality
- Type hints for better code documentation
- Comprehensive error handling
- Consistent coding style and conventions
- Extensive inline documentation

### Performance Characteristics

| Data Structure | Insert | Delete | Search | Space |
|----------------|--------|--------|--------|-------|
| Linked List | O(1) | O(n) | O(n) | O(n) |
| Stack | O(1) | O(1) | O(n) | O(n) |
| Queue | O(1) | O(1) | O(n) | O(n) |
| Binary Tree | O(log n)* | O(log n)* | O(log n)* | O(n) |
| Graph | O(1) | O(V+E) | O(V+E) | O(V+E) |
| Heap | O(log n) | O(log n) | O(n) | O(n) |

*Average case for balanced trees

## 🎓 Educational Goals

### Understanding Core Concepts
- **Time Complexity**: Big O notation and algorithm analysis
- **Space Complexity**: Memory usage optimization
- **Trade-offs**: Choosing appropriate data structures for specific problems

### Practical Skills
- **Implementation**: Building data structures from scratch
- **Problem Solving**: Applying structures to real-world scenarios
- **Optimization**: Performance tuning and efficiency improvements

### Programming Principles
- **Abstraction**: Clean interfaces and encapsulation
- **Modularity**: Reusable and maintainable code
- **Testing**: Comprehensive validation and edge case handling

