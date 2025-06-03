"""
Trie Usage Examples

This module demonstrates practical usage of trie implementations
with real-world scenarios and comprehensive test cases.
"""

from implementation import Trie, CompressedTrie, SuffixTrie


def test_basic_trie_operations():
    """Test basic operations of trie implementation."""
    print("=== Testing Basic Trie Operations ===\n")
    
    # Create trie and insert words
    trie = Trie()
    words = ["apple", "app", "application", "apply", "banana", "band", "bandana"]
    
    print("Inserting words:")
    for word in words:
        trie.insert(word)
        print(f"Inserted '{word}'")
    
    print(f"\nTrie state: {trie}")
    print(f"Total unique words: {trie.size()}")
    
    # Test search operations
    print("\n--- Search Operations ---")
    search_words = ["app", "apple", "apply", "application", "orange", "ban"]
    for word in search_words:
        found = trie.search(word)
        print(f"Search '{word}': {'Found' if found else 'Not found'}")
    
    # Test prefix operations
    print("\n--- Prefix Operations ---")
    prefixes = ["app", "ban", "xyz", "a"]
    for prefix in prefixes:
        has_prefix = trie.starts_with(prefix)
        count = trie.count_words_with_prefix(prefix)
        print(f"Prefix '{prefix}': {'Exists' if has_prefix else 'Not found'}, Count: {count}")
    
    # Test getting all words
    print(f"\nAll words in trie: {trie.get_all_words()}")
    
    # Test deletion
    print("\n--- Deletion Operations ---")
    delete_words = ["app", "banana", "xyz"]
    for word in delete_words:
        deleted = trie.delete(word)
        print(f"Delete '{word}': {'Success' if deleted else 'Not found'}")
    
    print(f"Words after deletion: {trie.get_all_words()}")


def test_autocomplete_functionality():
    """Test autocomplete features of trie."""
    print("\n=== Testing Autocomplete Functionality ===\n")
    
    # Create trie with common words
    trie = Trie()
    
    # Insert words with frequencies (insert multiple times)
    word_frequencies = {
        "python": 10,
        "programming": 8,
        "program": 5,
        "programmer": 7,
        "project": 6,
        "problem": 4,
        "product": 3,
        "process": 2,
        "practice": 9,
        "print": 15
    }
    
    print("Building autocomplete dictionary:")
    for word, freq in word_frequencies.items():
        for _ in range(freq):
            trie.insert(word)
        print(f"'{word}': frequency {freq}")
    
    # Test autocomplete suggestions
    print("\n--- Autocomplete Suggestions ---")
    prefixes = ["pr", "pro", "prog", "python", "xyz"]
    
    for prefix in prefixes:
        suggestions = trie.autocomplete(prefix, max_suggestions=5)
        print(f"\nAutocomplete for '{prefix}':")
        if suggestions:
            for i, (word, freq) in enumerate(suggestions, 1):
                print(f"  {i}. {word} (used {freq} times)")
        else:
            print(f"  No suggestions found")
    
    # Test prefix-based word retrieval
    print(f"\n--- Words with Prefix 'pro' ---")
    pro_words = trie.get_words_with_prefix("pro")
    for word in pro_words:
        freq = trie.get_word_frequency(word)
        print(f"  {word} (frequency: {freq})")


def real_world_example_spell_checker():
    """
    Demonstrate trie usage in spell checking system.
    """
    print("\n=== Real-World Example: Spell Checker ===\n")
    
    class SpellChecker:
        """Simple spell checker using trie."""
        
        def __init__(self):
            self.dictionary = Trie()
            self.custom_words = Trie()
        
        def load_dictionary(self, words):
            """Load dictionary words into trie."""
            print("Loading dictionary...")
            for word in words:
                self.dictionary.insert(word.lower())
            print(f"Loaded {len(words)} words into dictionary")
        
        def add_custom_word(self, word):
            """Add custom word to personal dictionary."""
            self.custom_words.insert(word.lower())
            print(f"Added '{word}' to custom dictionary")
        
        def is_word_correct(self, word):
            """Check if word is spelled correctly."""
            word_lower = word.lower()
            return (self.dictionary.search(word_lower) or 
                   self.custom_words.search(word_lower))
        
        def get_suggestions(self, word, max_suggestions=5):
            """Get spelling suggestions for a word."""
            word_lower = word.lower()
            suggestions = []
            
            # Get suggestions from dictionary
            dict_suggestions = self.dictionary.autocomplete(word_lower, max_suggestions)
            suggestions.extend([word for word, _ in dict_suggestions])
            
            # Get suggestions from custom words
            custom_suggestions = self.custom_words.autocomplete(word_lower, max_suggestions)
            suggestions.extend([word for word, _ in custom_suggestions])
            
            # Remove duplicates and limit results
            return list(dict(fromkeys=suggestions)))[:max_suggestions]
        
        def check_text(self, text):
            """Check spelling of entire text."""
            words = text.lower().replace(',', '').replace('.', '').split()
            errors = []
            
            for word in words:
                if not self.is_word_correct(word):
                    suggestions = self.get_suggestions(word, 3)
                    errors.append((word, suggestions))
            
            return errors
    
    # Create spell checker and load dictionary
    spell_checker = SpellChecker()
    
    # Common English words dictionary
    dictionary_words = [
        "hello", "world", "python", "programming", "computer", "science",
        "algorithm", "data", "structure", "function", "variable", "string",
        "integer", "boolean", "list", "dictionary", "loop", "condition",
        "class", "object", "method", "import", "library", "module",
        "error", "debug", "test", "code", "software", "development"
    ]
    
    spell_checker.load_dictionary(dictionary_words)
    
    # Add some custom words
    custom_words = ["javascript", "frontend", "backend", "api"]
    for word in custom_words:
        spell_checker.add_custom_word(word)
    
    # Test spell checking
    test_texts = [
        "Hello wrold, this is a pythom program",
        "I am lerning programing and algoritms",
        "The javscript api is working wel"
    ]
    
    print(f"\n--- Spell Checking Results ---")
    for i, text in enumerate(test_texts, 1):
        print(f"\nText {i}: '{text}'")
        errors = spell_checker.check_text(text)
        
        if errors:
            print("Spelling errors found:")
            for word, suggestions in errors:
                if suggestions:
                    print(f"  '{word}' -> suggestions: {suggestions}")
                else:
                    print(f"  '{word}' -> no suggestions found")
        else:
            print("No spelling errors found!")


def real_world_example_autocomplete_search():
    """
    Demonstrate trie usage in search autocomplete system.
    """
    print("\n=== Real-World Example: Search Autocomplete ===\n")
    
    class SearchEngine:
        """Simple search engine with autocomplete."""
        
        def __init__(self):
            self.search_trie = Trie()
            self.search_history = {}
        
        def index_content(self, content_items):
            """Index content for search."""
            print("Indexing content...")
            for item in content_items:
                # Split into words and index each
                words = item.lower().replace(',', '').replace('.', '').split()
                for word in words:
                    if len(word) > 2:  # Index words longer than 2 characters
                        self.search_trie.insert(word)
            
            print(f"Indexed {self.search_trie.size()} unique search terms")
        
        def record_search(self, query):
            """Record a search query to improve suggestions."""
            query_lower = query.lower()
            self.search_history[query_lower] = self.search_history.get(query_lower, 0) + 1
            
            # Add to trie with frequency
            for _ in range(self.search_history[query_lower]):
                self.search_trie.insert(query_lower)
        
        def get_search_suggestions(self, partial_query, max_results=8):
            """Get autocomplete suggestions for partial search query."""
            suggestions = self.search_trie.autocomplete(partial_query.lower(), max_results)
            
            # Include search history boost
            enhanced_suggestions = []
            for word, freq in suggestions:
                history_boost = self.search_history.get(word, 0)
                total_score = freq + (history_boost * 2)  # Boost popular searches
                enhanced_suggestions.append((word, total_score))
            
            # Re-sort by enhanced score
            enhanced_suggestions.sort(key=lambda x: -x[1])
            
            return [(word, score) for word, score in enhanced_suggestions]
        
        def search(self, query):
            """Perform search and record query."""
            self.record_search(query)
            print(f"Searching for: '{query}'")
            return f"Search results for '{query}' (simulated)"
    
    # Create search engine and index content
    search_engine = SearchEngine()
    
    # Sample content to index
    content = [
        "Python programming tutorial for beginners",
        "Data structures and algorithms in Python",
        "Machine learning with Python and TensorFlow",
        "Web development using Django and Flask",
        "Python data analysis with pandas and numpy",
        "Artificial intelligence and deep learning",
        "Software engineering best practices",
        "Database design and optimization",
        "Cloud computing and AWS services",
        "Mobile app development with React Native"
    ]
    
    search_engine.index_content(content)
    
    # Simulate some popular searches
    popular_searches = [
        ("python", 15),
        ("machine learning", 12),
        ("web development", 8),
        ("data analysis", 10),
        ("programming", 20),
        ("artificial intelligence", 6)
    ]
    
    print(f"\nSimulating popular searches:")
    for query, times in popular_searches:
        for _ in range(times):
            search_engine.record_search(query)
        print(f"'{query}' searched {times} times")
    
    # Test autocomplete
    print(f"\n--- Autocomplete Testing ---")
    partial_queries = ["py", "prog", "mach", "web", "dat", "art"]
    
    for partial in partial_queries:
        suggestions = search_engine.get_search_suggestions(partial, 5)
        print(f"\nAutocomplete for '{partial}':")
        if suggestions:
            for i, (suggestion, score) in enumerate(suggestions, 1):
                print(f"  {i}. {suggestion} (score: {score})")
        else:
            print("  No suggestions found")


def real_world_example_ip_routing():
    """
    Demonstrate trie usage in IP address routing.
    """
    print("\n=== Real-World Example: IP Address Routing ===\n")
    
    class IPRoutingTable:
        """IP routing table using trie for longest prefix matching."""
        
        def __init__(self):
            self.routing_trie = Trie()
            self.route_info = {}
        
        def add_route(self, network_prefix, next_hop, interface):
            """Add a route to the routing table."""
            # Convert IP prefix to binary string for trie storage
            binary_prefix = self._ip_to_binary_prefix(network_prefix)
            self.routing_trie.insert(binary_prefix)
            self.route_info[binary_prefix] = {
                'next_hop': next_hop,
                'interface': interface,
                'network': network_prefix
            }
            print(f"Added route: {network_prefix} -> {next_hop} via {interface}")
        
        def _ip_to_binary_prefix(self, network_prefix):
            """Convert IP network prefix to binary string."""
            # Simplified implementation for demonstration
            if '/' in network_prefix:
                ip, prefix_len = network_prefix.split('/')
                prefix_len = int(prefix_len)
            else:
                ip = network_prefix
                prefix_len = 32
            
            # Convert IP to binary (simplified)
            octets = ip.split('.')
            binary = ''
            for octet in octets:
                binary += format(int(octet), '08b')
            
            return binary[:prefix_len]
        
        def lookup_route(self, destination_ip):
            """Find best matching route for destination IP."""
            binary_ip = self._ip_to_binary_prefix(destination_ip)
            
            # Find longest matching prefix
            best_match = ""
            for i in range(len(binary_ip), 0, -1):
                prefix = binary_ip[:i]
                if self.routing_trie.search(prefix):
                    best_match = prefix
                    break
            
            if best_match and best_match in self.route_info:
                route = self.route_info[best_match]
                return route
            
            return None
        
        def show_routing_table(self):
            """Display current routing table."""
            print("\nCurrent Routing Table:")
            print(f"{'Network':<18} {'Next Hop':<15} {'Interface':<10}")
            print("-" * 45)
            
            for binary_prefix, route in self.route_info.items():
                network = route['network']
                next_hop = route['next_hop']
                interface = route['interface']
                print(f"{network:<18} {next_hop:<15} {interface:<10}")
    
    # Create routing table and add routes
    router = IPRoutingTable()
    
    # Add sample routes
    routes = [
        ("192.168.1.0/24", "10.0.0.1", "eth0"),
        ("192.168.0.0/16", "10.0.0.2", "eth1"),
        ("10.0.0.0/8", "172.16.0.1", "eth2"),
        ("0.0.0.0/0", "8.8.8.8", "eth3"),  # Default route
        ("192.168.1.128/25", "10.0.0.3", "eth0")  # More specific route
    ]
    
    for network, next_hop, interface in routes:
        router.add_route(network, next_hop, interface)
    
    router.show_routing_table()
    
    # Test route lookups
    print(f"\n--- Route Lookup Tests ---")
    test_ips = [
        "192.168.1.10",
        "192.168.1.150",
        "192.168.2.1",
        "10.5.5.5",
        "8.8.8.8"
    ]
    
    for ip in test_ips:
        route = router.lookup_route(ip)
        if route:
            print(f"Route for {ip}: -> {route['next_hop']} via {route['interface']} ({route['network']})")
        else:
            print(f"No route found for {ip}")


def test_compressed_trie():
    """Test compressed trie implementation."""
    print("\n=== Testing Compressed Trie ===\n")
    
    # Create compressed trie
    compressed_trie = CompressedTrie()
    
    # Insert words with common prefixes
    words = ["car", "card", "care", "careful", "cars", "cat", "cats"]
    
    print("Inserting words into compressed trie:")
    for word in words:
        compressed_trie.insert(word)
        print(f"Inserted '{word}'")
    
    print(f"\nCompressed trie: {compressed_trie}")
    
    # Test search
    print("\n--- Search Tests ---")
    test_words = ["car", "card", "care", "careful", "dog", "ca"]
    for word in test_words:
        found = compressed_trie.search(word)
        print(f"Search '{word}': {'Found' if found else 'Not found'}")


def test_suffix_trie():
    """Test suffix trie for pattern matching."""
    print("\n=== Testing Suffix Trie ===\n")
    
    # Create suffix trie for a text
    text = "banana"
    suffix_trie = SuffixTrie(text)
    
    print(f"Created suffix trie for text: '{text}'")
    print(f"Suffix trie contains {suffix_trie.trie.size()} suffixes")
    
    # Test pattern matching
    print("\n--- Pattern Matching Tests ---")
    patterns = ["an", "ana", "nan", "ban", "xyz", "a"]
    
    for pattern in patterns:
        found = suffix_trie.contains_pattern(pattern)
        positions = suffix_trie.find_all_occurrences(pattern)
        print(f"Pattern '{pattern}': {'Found' if found else 'Not found'}")
        if positions:
            print(f"  Positions: {positions}")
    
    # Find longest repeated substring
    longest = suffix_trie.longest_repeated_substring()
    print(f"\nLongest repeated substring: '{longest}'")


def performance_comparison():
    """Compare performance of trie vs other data structures."""
    print("\n=== Performance Comparison ===\n")
    
    import time
    
    # Test data
    words = [
        "apple", "application", "apply", "appreciate", "approach",
        "banana", "band", "bandana", "basic", "battery",
        "cat", "car", "card", "care", "careful", "carry",
        "dog", "door", "down", "develop", "development"
    ]
    
    # Test trie performance
    print("Testing Trie performance:")
    
    trie = Trie()
    
    # Insert performance
    start_time = time.time()
    for word in words:
        trie.insert(word)
    insert_time = time.time() - start_time
    
    # Search performance
    start_time = time.time()
    for word in words:
        trie.search(word)
    search_time = time.time() - start_time
    
    # Prefix search performance
    start_time = time.time()
    for word in words:
        trie.get_words_with_prefix(word[:2])
    prefix_time = time.time() - start_time
    
    print(f"  Insert {len(words)} words: {insert_time:.6f} seconds")
    print(f"  Search {len(words)} words: {search_time:.6f} seconds")
    print(f"  Prefix search {len(words)} times: {prefix_time:.6f} seconds")
    
    # Compare with Python set/list
    print("\nTesting Python set performance:")
    
    word_set = set()
    
    # Insert performance
    start_time = time.time()
    for word in words:
        word_set.add(word)
    set_insert_time = time.time() - start_time
    
    # Search performance
    start_time = time.time()
    for word in words:
        word in word_set
    set_search_time = time.time() - start_time
    
    # Prefix search performance (inefficient for sets)
    start_time = time.time()
    for word in words:
        [w for w in word_set if w.startswith(word[:2])]
    set_prefix_time = time.time() - start_time
    
    print(f"  Insert {len(words)} words: {set_insert_time:.6f} seconds")
    print(f"  Search {len(words)} words: {set_search_time:.6f} seconds")
    print(f"  Prefix search {len(words)} times: {set_prefix_time:.6f} seconds")
    
    print("\n--- Performance Analysis ---")
    print(f"Trie is better for:")
    print(f"  - Prefix operations: {set_prefix_time/prefix_time:.1f}x faster")
    print(f"  - Autocomplete features")
    print(f"  - Memory efficiency with common prefixes")
    
    print(f"Set is better for:")
    print(f"  - Simple membership: {search_time/set_search_time:.1f}x faster")
    print(f"  - Memory usage for unrelated words")


if __name__ == "__main__":
    test_basic_trie_operations()
    test_autocomplete_functionality()
    real_world_example_spell_checker()
    real_world_example_autocomplete_search()
    real_world_example_ip_routing()
    test_compressed_trie()
    test_suffix_trie()
    performance_comparison()