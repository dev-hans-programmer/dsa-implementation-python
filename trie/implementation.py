"""
Trie Implementation

This module provides comprehensive implementations of trie (prefix tree) data structure
with all essential operations including insertion, search, prefix matching, and autocomplete.
"""

from typing import List, Dict, Optional, Set, Tuple
from collections import defaultdict, deque


class TrieNode:
    """
    Node class for trie structure.
    
    Attributes:
        children: Dictionary mapping characters to child nodes
        is_end_of_word: Boolean indicating if this node represents end of a word
        word_count: Number of times this word has been inserted (for frequency)
        prefix_count: Number of words that have this node as prefix
    """
    
    def __init__(self) -> None:
        """Initialize a new trie node."""
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_end_of_word: bool = False
        self.word_count: int = 0
        self.prefix_count: int = 0
    
    def __str__(self) -> str:
        """String representation of the node."""
        return f"TrieNode(children={len(self.children)}, end_word={self.is_end_of_word})"


class Trie:
    """
    Trie (Prefix Tree) implementation with comprehensive operations.
    
    A trie is a tree-like data structure used to store a dynamic set of strings
    where keys are usually strings. It's particularly efficient for prefix-based
    operations like autocomplete and spell checking.
    
    Time Complexities:
    - Insert: O(m) where m is the length of the word
    - Search: O(m) where m is the length of the word
    - Delete: O(m) where m is the length of the word
    - Prefix search: O(p + n) where p is prefix length and n is number of matches
    
    Space Complexity: O(ALPHABET_SIZE * N * M) where N is number of words and M is average length
    """
    
    def __init__(self) -> None:
        """Initialize an empty trie."""
        self.root = TrieNode()
        self.word_count = 0
        self.total_words = 0
    
    def insert(self, word: str) -> None:
        """
        Insert a word into the trie.
        
        Args:
            word: The word to insert
            
        Time Complexity: O(m) where m is the length of the word
        """
        if not word:
            return
        
        current = self.root
        
        # Traverse through each character
        for char in word.lower():
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            current.prefix_count += 1
        
        # Mark end of word
        if not current.is_end_of_word:
            current.is_end_of_word = True
            self.word_count += 1
        
        current.word_count += 1
        self.total_words += 1
    
    def search(self, word: str) -> bool:
        """
        Search for a word in the trie.
        
        Args:
            word: The word to search for
            
        Returns:
            bool: True if word exists, False otherwise
            
        Time Complexity: O(m) where m is the length of the word
        """
        node = self._find_node(word)
        return node is not None and node.is_end_of_word
    
    def starts_with(self, prefix: str) -> bool:
        """
        Check if any word in the trie starts with the given prefix.
        
        Args:
            prefix: The prefix to search for
            
        Returns:
            bool: True if prefix exists, False otherwise
            
        Time Complexity: O(p) where p is the length of the prefix
        """
        return self._find_node(prefix) is not None
    
    def _find_node(self, word: str) -> Optional[TrieNode]:
        """
        Find the node corresponding to a word/prefix.
        
        Args:
            word: The word or prefix to find
            
        Returns:
            TrieNode: The node if found, None otherwise
        """
        current = self.root
        
        for char in word.lower():
            if char not in current.children:
                return None
            current = current.children[char]
        
        return current
    
    def delete(self, word: str) -> bool:
        """
        Delete a word from the trie.
        
        Args:
            word: The word to delete
            
        Returns:
            bool: True if word was deleted, False if not found
            
        Time Complexity: O(m) where m is the length of the word
        """
        if not word or not self.search(word):
            return False
        
        def _delete_helper(node: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                # We've reached the end of the word
                if not node.is_end_of_word:
                    return False
                
                node.is_end_of_word = False
                node.word_count = 0
                
                # If node has no children, it can be deleted
                return len(node.children) == 0
            
            char = word[index].lower()
            child_node = node.children.get(char)
            
            if not child_node:
                return False
            
            should_delete_child = _delete_helper(child_node, word, index + 1)
            
            if should_delete_child:
                del node.children[char]
                # Delete current node if it's not end of word and has no children
                return not node.is_end_of_word and len(node.children) == 0
            
            return False
        
        deleted = _delete_helper(self.root, word, 0)
        if deleted or self.search(word) != True:  # Word was deleted
            self.word_count -= 1
            return True
        
        return False
    
    def get_all_words(self) -> List[str]:
        """
        Get all words stored in the trie.
        
        Returns:
            List[str]: List of all words in the trie
            
        Time Complexity: O(n) where n is total number of characters in all words
        """
        words = []
        
        def _dfs(node: TrieNode, current_word: str) -> None:
            if node.is_end_of_word:
                words.append(current_word)
            
            for char, child_node in node.children.items():
                _dfs(child_node, current_word + char)
        
        _dfs(self.root, "")
        return words
    
    def get_words_with_prefix(self, prefix: str) -> List[str]:
        """
        Get all words that start with the given prefix.
        
        Args:
            prefix: The prefix to search for
            
        Returns:
            List[str]: List of words starting with the prefix
            
        Time Complexity: O(p + n) where p is prefix length and n is number of matches
        """
        prefix_node = self._find_node(prefix)
        if not prefix_node:
            return []
        
        words = []
        
        def _dfs(node: TrieNode, current_word: str) -> None:
            if node.is_end_of_word:
                words.append(current_word)
            
            for char, child_node in node.children.items():
                _dfs(child_node, current_word + char)
        
        _dfs(prefix_node, prefix.lower())
        return words
    
    def autocomplete(self, prefix: str, max_suggestions: int = 10) -> List[Tuple[str, int]]:
        """
        Get autocomplete suggestions for a prefix, sorted by frequency.
        
        Args:
            prefix: The prefix to get suggestions for
            max_suggestions: Maximum number of suggestions to return
            
        Returns:
            List[Tuple[str, int]]: List of (word, frequency) tuples
            
        Time Complexity: O(p + n log n) where p is prefix length and n is number of matches
        """
        prefix_node = self._find_node(prefix)
        if not prefix_node:
            return []
        
        suggestions = []
        
        def _dfs(node: TrieNode, current_word: str) -> None:
            if node.is_end_of_word:
                suggestions.append((current_word, node.word_count))
            
            for char, child_node in node.children.items():
                _dfs(child_node, current_word + char)
        
        _dfs(prefix_node, prefix.lower())
        
        # Sort by frequency (descending) and then alphabetically
        suggestions.sort(key=lambda x: (-x[1], x[0]))
        
        return suggestions[:max_suggestions]
    
    def count_words_with_prefix(self, prefix: str) -> int:
        """
        Count the number of words that start with the given prefix.
        
        Args:
            prefix: The prefix to count
            
        Returns:
            int: Number of words with the prefix
            
        Time Complexity: O(p) where p is the length of the prefix
        """
        prefix_node = self._find_node(prefix)
        return prefix_node.prefix_count if prefix_node else 0
    
    def get_word_frequency(self, word: str) -> int:
        """
        Get the frequency of a specific word.
        
        Args:
            word: The word to get frequency for
            
        Returns:
            int: Frequency of the word (0 if not found)
        """
        node = self._find_node(word)
        return node.word_count if node and node.is_end_of_word else 0
    
    def longest_common_prefix(self, words: List[str]) -> str:
        """
        Find the longest common prefix among a list of words.
        
        Args:
            words: List of words to find common prefix for
            
        Returns:
            str: The longest common prefix
            
        Time Complexity: O(S) where S is sum of all word lengths
        """
        if not words:
            return ""
        
        # Insert all words into a temporary trie
        temp_trie = Trie()
        for word in words:
            temp_trie.insert(word)
        
        # Traverse from root while there's only one child and no end of word
        current = temp_trie.root
        prefix = ""
        
        while (len(current.children) == 1 and 
               not current.is_end_of_word and 
               current != temp_trie.root):
            char = next(iter(current.children.keys()))
            prefix += char
            current = current.children[char]
        
        # Handle case where we need to check the first character
        if current == temp_trie.root and len(current.children) == 1:
            char = next(iter(current.children.keys()))
            current = current.children[char]
            prefix += char
            
            while len(current.children) == 1 and not current.is_end_of_word:
                char = next(iter(current.children.keys()))
                prefix += char
                current = current.children[char]
        
        return prefix
    
    def is_empty(self) -> bool:
        """Check if trie is empty."""
        return self.word_count == 0
    
    def size(self) -> int:
        """Get number of unique words in trie."""
        return self.word_count
    
    def total_insertions(self) -> int:
        """Get total number of word insertions (including duplicates)."""
        return self.total_words
    
    def clear(self) -> None:
        """Remove all words from the trie."""
        self.root = TrieNode()
        self.word_count = 0
        self.total_words = 0
    
    def __len__(self) -> int:
        """Return number of unique words in trie."""
        return self.word_count
    
    def __contains__(self, word: str) -> bool:
        """Check if word is in trie."""
        return self.search(word)
    
    def __str__(self) -> str:
        """String representation of trie."""
        return f"Trie(words={self.word_count}, total_insertions={self.total_words})"


class CompressedTrie(Trie):
    """
    Compressed Trie (Radix Tree) implementation.
    
    A compressed trie stores strings more efficiently by merging nodes
    that have only one child, reducing space complexity.
    """
    
    class CompressedTrieNode:
        """Node for compressed trie with edge labels."""
        
        def __init__(self, edge_label: str = "") -> None:
            self.edge_label = edge_label
            self.children: Dict[str, 'CompressedTrie.CompressedTrieNode'] = {}
            self.is_end_of_word = False
            self.word_count = 0
        
        def __str__(self) -> str:
            return f"CompressedNode(label='{self.edge_label}', children={len(self.children)})"
    
    def __init__(self) -> None:
        """Initialize compressed trie."""
        self.root = self.CompressedTrieNode()
        self.word_count = 0
    
    def insert(self, word: str) -> None:
        """Insert word into compressed trie."""
        if not word:
            return
        
        word = word.lower()
        current = self.root
        i = 0
        
        while i < len(word):
            char = word[i]
            
            if char not in current.children:
                # Create new node with remaining suffix
                new_node = self.CompressedTrieNode(word[i:])
                new_node.is_end_of_word = True
                new_node.word_count = 1
                current.children[char] = new_node
                if new_node.is_end_of_word:
                    self.word_count += 1
                return
            
            child = current.children[char]
            edge_label = child.edge_label
            
            # Find common prefix between remaining word and edge label
            j = 0
            while (j < len(edge_label) and 
                   i + j < len(word) and 
                   edge_label[j] == word[i + j]):
                j += 1
            
            if j == len(edge_label):
                # Entire edge label matches, continue to child
                current = child
                i += j
            else:
                # Partial match, need to split the edge
                # Create new internal node
                split_node = self.CompressedTrieNode(edge_label[:j])
                
                # Update original child
                child.edge_label = edge_label[j:]
                split_node.children[edge_label[j]] = child
                
                # Create new child for remaining word
                if i + j < len(word):
                    new_child = self.CompressedTrieNode(word[i + j:])
                    new_child.is_end_of_word = True
                    new_child.word_count = 1
                    split_node.children[word[i + j]] = new_child
                else:
                    split_node.is_end_of_word = True
                    split_node.word_count = 1
                
                # Replace in parent
                current.children[char] = split_node
                
                if split_node.is_end_of_word or any(child.is_end_of_word 
                    for child in self._get_all_descendants(split_node) if child.is_end_of_word):
                    self.word_count += 1
                return
        
        # Reached end of word
        if not current.is_end_of_word:
            current.is_end_of_word = True
            self.word_count += 1
        current.word_count += 1
    
    def _get_all_descendants(self, node) -> List:
        """Get all descendant nodes."""
        descendants = []
        queue = deque([node])
        
        while queue:
            current = queue.popleft()
            descendants.append(current)
            queue.extend(current.children.values())
        
        return descendants
    
    def search(self, word: str) -> bool:
        """Search for word in compressed trie."""
        node = self._find_node(word)
        return node is not None and node.is_end_of_word
    
    def _find_node(self, word: str):
        """Find node for given word."""
        if not word:
            return self.root
        
        word = word.lower()
        current = self.root
        i = 0
        
        while i < len(word):
            char = word[i]
            
            if char not in current.children:
                return None
            
            child = current.children[char]
            edge_label = child.edge_label
            
            # Check if word matches edge label
            if i + len(edge_label) <= len(word):
                if word[i:i + len(edge_label)] == edge_label:
                    current = child
                    i += len(edge_label)
                else:
                    return None
            else:
                # Word is shorter than edge label
                return None
        
        return current


class SuffixTrie:
    """
    Suffix Trie implementation for pattern matching.
    
    A suffix trie contains all suffixes of a given string, useful for
    pattern matching and substring search operations.
    """
    
    def __init__(self, text: str) -> None:
        """
        Initialize suffix trie with a text.
        
        Args:
            text: The text to build suffix trie for
        """
        self.text = text
        self.trie = Trie()
        self._build_suffix_trie()
    
    def _build_suffix_trie(self) -> None:
        """Build suffix trie by inserting all suffixes."""
        for i in range(len(self.text)):
            suffix = self.text[i:] + "$"  # Add terminator
            self.trie.insert(suffix)
    
    def contains_pattern(self, pattern: str) -> bool:
        """
        Check if pattern exists in the original text.
        
        Args:
            pattern: Pattern to search for
            
        Returns:
            bool: True if pattern found, False otherwise
        """
        return self.trie.starts_with(pattern.lower())
    
    def find_all_occurrences(self, pattern: str) -> List[int]:
        """
        Find all starting positions of pattern in text.
        
        Args:
            pattern: Pattern to search for
            
        Returns:
            List[int]: List of starting positions
        """
        positions = []
        pattern = pattern.lower()
        
        for i in range(len(self.text) - len(pattern) + 1):
            if self.text[i:i + len(pattern)].lower() == pattern:
                positions.append(i)
        
        return positions
    
    def longest_repeated_substring(self) -> str:
        """
        Find the longest repeated substring in the text.
        
        Returns:
            str: The longest repeated substring
        """
        # This is a simplified implementation
        # A full implementation would traverse the trie to find deepest internal node
        max_length = 0
        longest_substring = ""
        
        for i in range(len(self.text)):
            for j in range(i + 1, len(self.text) + 1):
                substring = self.text[i:j]
                if len(substring) > max_length and self.text.count(substring) > 1:
                    max_length = len(substring)
                    longest_substring = substring
        
        return longest_substring