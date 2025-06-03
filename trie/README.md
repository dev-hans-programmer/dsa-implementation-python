# Trie (Prefix Tree) Implementation

A comprehensive implementation of trie data structure with autocomplete, spell checking, and pattern matching capabilities.

## Overview

A trie (pronounced "try") is a tree-like data structure that stores a dynamic set of strings, where keys are usually strings. It's particularly efficient for prefix-based operations and is commonly used in applications like autocomplete systems, spell checkers, and IP routing tables.

## Features

### Core Implementations
- **Basic Trie**: Standard prefix tree with insertion, search, and deletion
- **Compressed Trie**: Space-optimized radix tree implementation
- **Suffix Trie**: Pattern matching and substring search capabilities

### Advanced Operations
- Autocomplete with frequency-based suggestions
- Prefix counting and word frequency tracking
- Longest common prefix finding
- Pattern matching and occurrence finding

## Time Complexity

| Operation | Time Complexity | Description |
|-----------|----------------|-------------|
| Insert | O(m) | m = length of word |
| Search | O(m) | m = length of word |
| Delete | O(m) | m = length of word |
| Prefix Search | O(p + n) | p = prefix length, n = matches |
| Autocomplete | O(p + n log n) | Includes sorting by frequency |

## Space Complexity

- **Standard Trie**: O(ALPHABET_SIZE × N × M) where N is number of words, M is average length
- **Compressed Trie**: O(N × M) with better space efficiency for sparse data
- **Memory per node**: ~40-60 bytes including Python object overhead

## Real-World Applications

### 1. Autocomplete Systems
```python
# Search engine suggestions
trie = Trie()
trie.insert("python programming")
trie.insert("python tutorial")
suggestions = trie.autocomplete("pyth", 5)
# Returns: [("python programming", freq), ("python tutorial", freq)]
```

### 2. Spell Checkers
```python
# Dictionary-based spell checking
dictionary = Trie()
dictionary.insert("programming")
is_correct = dictionary.search("programing")  # False
suggestions = dictionary.autocomplete("program", 3)
```

### 3. IP Routing Tables
```python
# Longest prefix matching for network routing
routing_trie = Trie()
routing_trie.insert("192.168.1")  # Network prefix
# Find best matching route for IP address
```

### 4. Text Processing
```python
# Pattern matching in documents
suffix_trie = SuffixTrie("banana")
positions = suffix_trie.find_all_occurrences("an")  # [1, 3]
longest_repeat = suffix_trie.longest_repeated_substring()  # "ana"
```

## When to Use Tries

### Advantages
- **Prefix Operations**: Extremely efficient for prefix-based queries
- **Autocomplete**: Natural fit for suggestion systems
- **Memory Sharing**: Common prefixes share storage space
- **Predictable Performance**: No hash collisions like hash tables

### Best Use Cases
- Search engine autocomplete
- Spell checking and correction
- IP address routing (longest prefix matching)
- Phone directory lookups
- DNA sequence analysis
- Web browser URL suggestions

### When NOT to Use
- **Simple Lookups**: Hash tables are faster for exact matches
- **Large Alphabets**: Memory overhead becomes significant
- **Sparse Data**: When words share few common prefixes
- **Memory Constraints**: Each node has overhead

## Performance Comparison

### vs Hash Tables (Sets)
- **Trie Advantages**: Prefix operations, ordered traversal, autocomplete
- **Hash Table Advantages**: Faster exact lookups, less memory per word

### vs Binary Search Trees
- **Trie Advantages**: No key comparison needed, prefix operations
- **BST Advantages**: Works with any comparable data type

### Memory Usage
```
Example: 1000 English words (average 6 characters)
- Trie: ~80KB (with prefix sharing)
- Hash Set: ~50KB (no prefix sharing)
- List: ~40KB (linear search required)
```

## Advanced Features

### Frequency Tracking
- Track how often words are inserted
- Rank autocomplete suggestions by popularity
- Identify trending search terms

### Compressed Trie (Radix Tree)
- Merge nodes with single children
- Reduce memory usage for sparse data
- Maintain O(m) time complexity

### Suffix Trie Applications
- Pattern matching in bioinformatics
- Text indexing for search engines
- Longest common substring problems
- DNA sequence alignment

## Industry Usage

### Technology Companies
- **Google**: Search autocomplete and suggestions
- **Amazon**: Product search and recommendations
- **Microsoft**: Office spell checking and autocorrect
- **DNS Systems**: Domain name resolution with prefix matching

### Networking
- **Router Tables**: Longest prefix matching for packet forwarding
- **Firewalls**: URL filtering and pattern matching
- **CDNs**: Geographic routing based on IP prefixes

### Databases
- **Full-text Search**: Inverted indexes for document retrieval
- **Autocomplete**: User input suggestions in applications
- **Data Compression**: Dictionary-based compression algorithms

## Implementation Notes

### Memory Optimization
- Use character arrays instead of dictionaries for small alphabets
- Implement node pooling for memory reuse
- Consider compressed tries for sparse data

### Thread Safety
- Current implementation is not thread-safe
- Add locks for concurrent access
- Consider immutable trie variants

### Persistence
- Serialize trie structure for disk storage
- Implement lazy loading for large datasets
- Use memory-mapped files for huge dictionaries

## Educational Value

### Learning Outcomes
- Understanding tree data structures
- Prefix-based algorithm design
- String processing techniques
- Memory vs. time complexity trade-offs

### Related Concepts
- **Suffix Arrays**: Alternative for pattern matching
- **Ternary Search Trees**: Hybrid approach combining benefits
- **Bloom Filters**: Probabilistic membership testing
- **Finite Automata**: Theoretical foundation for pattern matching

## Files

- `implementation.py`: Core trie implementations with all variants
- `usage.py`: Comprehensive examples and real-world applications
- `main.py`: Interactive demonstration and learning tool
- `README.md`: Complete documentation and usage guide

## Getting Started

Run the interactive demo:
```bash
python main.py
```

Explore usage examples:
```bash
python usage.py
```

The trie implementation provides a powerful foundation for text processing, search systems, and any application requiring efficient prefix-based operations.