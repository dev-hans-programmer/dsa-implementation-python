"""
Interactive Trie Demonstration

This module provides an interactive demonstration of trie operations,
allowing users to experiment with prefix trees and autocomplete functionality.
"""

from implementation import Trie, CompressedTrie, SuffixTrie


def display_main_menu():
    """Display the main menu options."""
    print("\n" + "="*60)
    print("TRIE INTERACTIVE DEMO")
    print("="*60)
    print("1. Basic Trie Operations")
    print("2. Autocomplete System")
    print("3. Spell Checker Demo")
    print("4. Search Engine Suggestions")
    print("5. Compressed Trie Demo")
    print("6. Suffix Trie Pattern Matching")
    print("7. Performance Analysis")
    print("8. Exit")
    print("="*60)


def basic_trie_demo():
    """Interactive demo for basic trie operations."""
    print("\n" + "="*50)
    print("BASIC TRIE OPERATIONS DEMO")
    print("="*50)
    print("Trie (prefix tree) for efficient string operations")
    
    trie = Trie()
    
    while True:
        print(f"\nCurrent Trie: {trie}")
        
        print("\nOperations:")
        print("1. Insert word")
        print("2. Search word")
        print("3. Check prefix")
        print("4. Delete word")
        print("5. Get all words")
        print("6. Get words with prefix")
        print("7. Count words with prefix")
        print("8. Clear trie")
        print("9. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-9): "))
            
            if choice == 1:
                word = input("Enter word to insert: ").strip()
                if word:
                    trie.insert(word)
                    print(f"Inserted '{word}'")
                else:
                    print("Please enter a valid word")
                    
            elif choice == 2:
                word = input("Enter word to search: ").strip()
                if word:
                    found = trie.search(word)
                    print(f"Word '{word}': {'Found' if found else 'Not found'}")
                else:
                    print("Please enter a valid word")
                    
            elif choice == 3:
                prefix = input("Enter prefix to check: ").strip()
                if prefix:
                    exists = trie.starts_with(prefix)
                    count = trie.count_words_with_prefix(prefix)
                    print(f"Prefix '{prefix}': {'Exists' if exists else 'Not found'}")
                    print(f"Words with this prefix: {count}")
                else:
                    print("Please enter a valid prefix")
                    
            elif choice == 4:
                word = input("Enter word to delete: ").strip()
                if word:
                    deleted = trie.delete(word)
                    print(f"Delete '{word}': {'Success' if deleted else 'Not found'}")
                else:
                    print("Please enter a valid word")
                    
            elif choice == 5:
                words = trie.get_all_words()
                if words:
                    print(f"All words in trie ({len(words)}):")
                    for word in sorted(words):
                        frequency = trie.get_word_frequency(word)
                        print(f"  {word} (frequency: {frequency})")
                else:
                    print("Trie is empty")
                    
            elif choice == 6:
                prefix = input("Enter prefix: ").strip()
                if prefix:
                    words = trie.get_words_with_prefix(prefix)
                    if words:
                        print(f"Words starting with '{prefix}':")
                        for word in sorted(words):
                            frequency = trie.get_word_frequency(word)
                            print(f"  {word} (frequency: {frequency})")
                    else:
                        print(f"No words found with prefix '{prefix}'")
                else:
                    print("Please enter a valid prefix")
                    
            elif choice == 7:
                prefix = input("Enter prefix to count: ").strip()
                if prefix:
                    count = trie.count_words_with_prefix(prefix)
                    print(f"Number of words with prefix '{prefix}': {count}")
                else:
                    print("Please enter a valid prefix")
                    
            elif choice == 8:
                trie.clear()
                print("Trie cleared")
                
            elif choice == 9:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def autocomplete_demo():
    """Interactive demo for autocomplete functionality."""
    print("\n" + "="*50)
    print("AUTOCOMPLETE SYSTEM DEMO")
    print("="*50)
    print("Type partial words to see autocomplete suggestions")
    
    trie = Trie()
    
    # Add sample dictionary
    sample_words = [
        "apple", "application", "apply", "appreciate", "approach",
        "banana", "band", "bandana", "basic", "battery",
        "cat", "car", "card", "care", "careful", "carry",
        "dog", "door", "down", "develop", "development",
        "elephant", "energy", "engine", "example", "exercise"
    ]
    
    print("Loading sample dictionary...")
    for word in sample_words:
        trie.insert(word)
        # Insert multiple times to simulate frequency
        for _ in range(abs(hash(word)) % 5):
            trie.insert(word)
    
    print(f"Loaded {len(sample_words)} words")
    
    while True:
        print(f"\nAutocomplete System:")
        print("1. Get autocomplete suggestions")
        print("2. Add word to dictionary")
        print("3. Search word in dictionary")
        print("4. Show all words")
        print("5. Simulate typing session")
        print("6. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-6): "))
            
            if choice == 1:
                prefix = input("Enter partial word: ").strip()
                if prefix:
                    suggestions = trie.autocomplete(prefix, max_suggestions=8)
                    if suggestions:
                        print(f"\nAutocomplete suggestions for '{prefix}':")
                        for i, (word, freq) in enumerate(suggestions, 1):
                            print(f"  {i}. {word} (used {freq} times)")
                    else:
                        print(f"No suggestions found for '{prefix}'")
                else:
                    print("Please enter a partial word")
                    
            elif choice == 2:
                word = input("Enter word to add: ").strip()
                if word:
                    trie.insert(word)
                    print(f"Added '{word}' to dictionary")
                else:
                    print("Please enter a valid word")
                    
            elif choice == 3:
                word = input("Enter word to search: ").strip()
                if word:
                    found = trie.search(word)
                    frequency = trie.get_word_frequency(word)
                    if found:
                        print(f"Found '{word}' (used {frequency} times)")
                    else:
                        print(f"'{word}' not found in dictionary")
                else:
                    print("Please enter a valid word")
                    
            elif choice == 4:
                words = trie.get_all_words()
                print(f"\nDictionary contains {len(words)} unique words:")
                for word in sorted(words)[:20]:  # Show first 20
                    frequency = trie.get_word_frequency(word)
                    print(f"  {word} (frequency: {frequency})")
                if len(words) > 20:
                    print(f"  ... and {len(words) - 20} more")
                    
            elif choice == 5:
                print("\nSimulating typing session (type 'quit' to stop):")
                while True:
                    partial = input("Type: ").strip()
                    if partial.lower() == 'quit':
                        break
                    if partial:
                        suggestions = trie.autocomplete(partial, 5)
                        if suggestions:
                            print("  Suggestions:", [word for word, _ in suggestions])
                        else:
                            print("  No suggestions")
                    
            elif choice == 6:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def spell_checker_demo():
    """Interactive spell checker demonstration."""
    print("\n" + "="*50)
    print("SPELL CHECKER DEMO")
    print("="*50)
    
    dictionary = Trie()
    custom_words = Trie()
    
    # Load basic dictionary
    basic_words = [
        "hello", "world", "python", "programming", "computer", "science",
        "algorithm", "data", "structure", "function", "variable", "string",
        "integer", "boolean", "list", "dictionary", "loop", "condition",
        "class", "object", "method", "import", "library", "module",
        "error", "debug", "test", "code", "software", "development",
        "application", "system", "network", "database", "server", "client"
    ]
    
    for word in basic_words:
        dictionary.insert(word)
    
    print(f"Loaded {len(basic_words)} words into dictionary")
    
    while True:
        print(f"\nSpell Checker:")
        print("1. Check single word")
        print("2. Check sentence")
        print("3. Add word to custom dictionary")
        print("4. Show suggestions for word")
        print("5. Show dictionary statistics")
        print("6. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-6): "))
            
            if choice == 1:
                word = input("Enter word to check: ").strip().lower()
                if word:
                    in_dict = dictionary.search(word)
                    in_custom = custom_words.search(word)
                    
                    if in_dict or in_custom:
                        print(f"✓ '{word}' is spelled correctly")
                    else:
                        print(f"✗ '{word}' may be misspelled")
                        
                        # Get suggestions
                        suggestions = []
                        for prefix_len in range(1, min(len(word) + 1, 4)):
                            prefix = word[:prefix_len]
                            dict_suggestions = dictionary.autocomplete(prefix, 3)
                            suggestions.extend([w for w, _ in dict_suggestions])
                        
                        if suggestions:
                            unique_suggestions = list(set(suggestions))[:5]
                            print(f"  Suggestions: {unique_suggestions}")
                        else:
                            print("  No suggestions found")
                else:
                    print("Please enter a word")
                    
            elif choice == 2:
                sentence = input("Enter sentence to check: ").strip()
                if sentence:
                    words = sentence.lower().replace('.', '').replace(',', '').split()
                    errors = []
                    
                    for word in words:
                        if not (dictionary.search(word) or custom_words.search(word)):
                            errors.append(word)
                    
                    if errors:
                        print(f"Potential spelling errors: {errors}")
                        for error in errors:
                            suggestions = dictionary.autocomplete(error[:2], 3)
                            if suggestions:
                                print(f"  '{error}' -> suggestions: {[w for w, _ in suggestions]}")
                    else:
                        print("✓ No spelling errors found")
                else:
                    print("Please enter a sentence")
                    
            elif choice == 3:
                word = input("Enter word to add to custom dictionary: ").strip().lower()
                if word:
                    custom_words.insert(word)
                    print(f"Added '{word}' to custom dictionary")
                else:
                    print("Please enter a word")
                    
            elif choice == 4:
                word = input("Enter word to get suggestions for: ").strip().lower()
                if word:
                    suggestions = dictionary.autocomplete(word, 8)
                    if suggestions:
                        print(f"Suggestions for '{word}':")
                        for i, (suggestion, freq) in enumerate(suggestions, 1):
                            print(f"  {i}. {suggestion}")
                    else:
                        print(f"No suggestions found for '{word}'")
                else:
                    print("Please enter a word")
                    
            elif choice == 5:
                dict_size = dictionary.size()
                custom_size = custom_words.size()
                print(f"\nDictionary Statistics:")
                print(f"  Main dictionary: {dict_size} words")
                print(f"  Custom dictionary: {custom_size} words")
                print(f"  Total vocabulary: {dict_size + custom_size} words")
                
            elif choice == 6:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def search_engine_demo():
    """Interactive search engine suggestions demo."""
    print("\n" + "="*50)
    print("SEARCH ENGINE SUGGESTIONS DEMO")
    print("="*50)
    
    search_trie = Trie()
    search_history = {}
    
    # Popular search terms
    popular_searches = [
        ("python programming", 50),
        ("machine learning", 45),
        ("web development", 40),
        ("data science", 35),
        ("artificial intelligence", 30),
        ("javascript tutorial", 25),
        ("react framework", 20),
        ("database design", 18),
        ("cloud computing", 15),
        ("cybersecurity", 12)
    ]
    
    print("Initializing with popular search terms...")
    for term, frequency in popular_searches:
        search_history[term] = frequency
        for _ in range(frequency):
            search_trie.insert(term)
    
    while True:
        print(f"\nSearch Engine:")
        print("1. Get search suggestions")
        print("2. Perform search (records in history)")
        print("3. View search history")
        print("4. Popular searches")
        print("5. Clear search history")
        print("6. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-6): "))
            
            if choice == 1:
                query = input("Enter partial search query: ").strip().lower()
                if query:
                    suggestions = search_trie.autocomplete(query, 8)
                    if suggestions:
                        print(f"\nSearch suggestions for '{query}':")
                        for i, (suggestion, freq) in enumerate(suggestions, 1):
                            print(f"  {i}. {suggestion} ({freq} searches)")
                    else:
                        print(f"No suggestions found for '{query}'")
                else:
                    print("Please enter a search query")
                    
            elif choice == 2:
                query = input("Enter search query: ").strip().lower()
                if query:
                    # Record search
                    search_history[query] = search_history.get(query, 0) + 1
                    search_trie.insert(query)
                    
                    print(f"Searching for: '{query}'")
                    print(f"Search recorded (searched {search_history[query]} times)")
                    
                    # Show related suggestions
                    related = search_trie.get_words_with_prefix(query[:3])
                    if len(related) > 1:
                        other_related = [w for w in related if w != query][:3]
                        if other_related:
                            print(f"Related searches: {other_related}")
                else:
                    print("Please enter a search query")
                    
            elif choice == 3:
                if search_history:
                    print(f"\nSearch History:")
                    sorted_history = sorted(search_history.items(), 
                                          key=lambda x: x[1], reverse=True)
                    for i, (query, count) in enumerate(sorted_history[:15], 1):
                        print(f"  {i}. {query} ({count} times)")
                else:
                    print("No search history")
                    
            elif choice == 4:
                popular = search_trie.autocomplete("", 10)
                if popular:
                    print(f"\nMost Popular Searches:")
                    for i, (query, freq) in enumerate(popular, 1):
                        print(f"  {i}. {query} ({freq} searches)")
                else:
                    print("No search data available")
                    
            elif choice == 5:
                search_trie.clear()
                search_history.clear()
                print("Search history cleared")
                
            elif choice == 6:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def suffix_trie_demo():
    """Interactive suffix trie pattern matching demo."""
    print("\n" + "="*50)
    print("SUFFIX TRIE PATTERN MATCHING DEMO")
    print("="*50)
    
    text = ""
    suffix_trie = None
    
    while True:
        if text:
            print(f"\nCurrent text: '{text}'")
            print(f"Suffix trie: {suffix_trie.trie.size()} suffixes")
        else:
            print("\nNo text loaded")
        
        print("\nOperations:")
        print("1. Load text")
        print("2. Search pattern")
        print("3. Find all occurrences")
        print("4. Find longest repeated substring")
        print("5. Load sample text")
        print("6. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-6): "))
            
            if choice == 1:
                new_text = input("Enter text: ").strip()
                if new_text:
                    text = new_text
                    suffix_trie = SuffixTrie(text)
                    print(f"Loaded text with {len(text)} characters")
                    print(f"Created suffix trie with {suffix_trie.trie.size()} suffixes")
                else:
                    print("Please enter valid text")
                    
            elif choice == 2:
                if not text:
                    print("Please load text first")
                    continue
                    
                pattern = input("Enter pattern to search: ").strip()
                if pattern:
                    found = suffix_trie.contains_pattern(pattern)
                    print(f"Pattern '{pattern}': {'Found' if found else 'Not found'}")
                else:
                    print("Please enter a pattern")
                    
            elif choice == 3:
                if not text:
                    print("Please load text first")
                    continue
                    
                pattern = input("Enter pattern to find all occurrences: ").strip()
                if pattern:
                    positions = suffix_trie.find_all_occurrences(pattern)
                    if positions:
                        print(f"Pattern '{pattern}' found at positions: {positions}")
                        # Show context
                        for pos in positions[:5]:  # Show first 5 occurrences
                            start = max(0, pos - 5)
                            end = min(len(text), pos + len(pattern) + 5)
                            context = text[start:end]
                            highlight = context.replace(pattern, f"[{pattern}]")
                            print(f"  Position {pos}: ...{highlight}...")
                    else:
                        print(f"Pattern '{pattern}' not found")
                else:
                    print("Please enter a pattern")
                    
            elif choice == 4:
                if not text:
                    print("Please load text first")
                    continue
                    
                longest = suffix_trie.longest_repeated_substring()
                if longest:
                    print(f"Longest repeated substring: '{longest}'")
                    positions = suffix_trie.find_all_occurrences(longest)
                    print(f"Occurs at positions: {positions}")
                else:
                    print("No repeated substrings found")
                    
            elif choice == 5:
                sample_texts = [
                    "banana",
                    "abracadabra",
                    "mississippi",
                    "the quick brown fox jumps over the lazy dog"
                ]
                
                print("\nSample texts:")
                for i, sample in enumerate(sample_texts, 1):
                    print(f"  {i}. {sample}")
                
                try:
                    sample_choice = int(input("Choose sample (1-4): "))
                    if 1 <= sample_choice <= len(sample_texts):
                        text = sample_texts[sample_choice - 1]
                        suffix_trie = SuffixTrie(text)
                        print(f"Loaded sample text: '{text}'")
                    else:
                        print("Invalid choice")
                except ValueError:
                    print("Please enter a valid number")
                    
            elif choice == 6:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def performance_analysis():
    """Performance analysis of trie operations."""
    print("\n" + "="*50)
    print("TRIE PERFORMANCE ANALYSIS")
    print("="*50)
    
    import time
    import random
    import string
    
    def generate_random_words(count, min_length=3, max_length=10):
        """Generate random words for testing."""
        words = []
        for _ in range(count):
            length = random.randint(min_length, max_length)
            word = ''.join(random.choices(string.ascii_lowercase, k=length))
            words.append(word)
        return words
    
    while True:
        print(f"\nPerformance Analysis:")
        print("1. Insert performance test")
        print("2. Search performance test")
        print("3. Prefix search comparison")
        print("4. Memory usage analysis")
        print("5. Autocomplete performance")
        print("6. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-6): "))
            
            if choice == 1:
                sizes = [100, 500, 1000, 2000]
                print("\nInsert Performance Test:")
                print(f"{'Size':<8} {'Trie (ms)':<12} {'Set (ms)':<12} {'Speedup':<10}")
                print("-" * 45)
                
                for size in sizes:
                    words = generate_random_words(size)
                    
                    # Test Trie
                    trie = Trie()
                    start = time.time()
                    for word in words:
                        trie.insert(word)
                    trie_time = (time.time() - start) * 1000
                    
                    # Test Set
                    word_set = set()
                    start = time.time()
                    for word in words:
                        word_set.add(word)
                    set_time = (time.time() - start) * 1000
                    
                    speedup = set_time / trie_time if trie_time > 0 else 0
                    print(f"{size:<8} {trie_time:<12.2f} {set_time:<12.2f} {speedup:<10.2f}x")
                    
            elif choice == 2:
                size = 1000
                words = generate_random_words(size)
                search_words = random.sample(words, 100)
                
                # Build structures
                trie = Trie()
                word_set = set()
                
                for word in words:
                    trie.insert(word)
                    word_set.add(word)
                
                print(f"\nSearch Performance Test ({size} words, 100 searches):")
                
                # Test Trie search
                start = time.time()
                for word in search_words:
                    trie.search(word)
                trie_search_time = (time.time() - start) * 1000
                
                # Test Set search
                start = time.time()
                for word in search_words:
                    word in word_set
                set_search_time = (time.time() - start) * 1000
                
                print(f"Trie search: {trie_search_time:.2f} ms")
                print(f"Set search: {set_search_time:.2f} ms")
                print(f"Set is {trie_search_time/set_search_time:.1f}x faster")
                
            elif choice == 3:
                size = 1000
                words = generate_random_words(size)
                prefixes = [word[:2] for word in random.sample(words, 50)]
                
                # Build structures
                trie = Trie()
                word_list = []
                
                for word in words:
                    trie.insert(word)
                    word_list.append(word)
                
                print(f"\nPrefix Search Comparison ({size} words, 50 prefixes):")
                
                # Test Trie prefix search
                start = time.time()
                for prefix in prefixes:
                    trie.get_words_with_prefix(prefix)
                trie_prefix_time = (time.time() - start) * 1000
                
                # Test List prefix search
                start = time.time()
                for prefix in prefixes:
                    [word for word in word_list if word.startswith(prefix)]
                list_prefix_time = (time.time() - start) * 1000
                
                print(f"Trie prefix search: {trie_prefix_time:.2f} ms")
                print(f"List prefix search: {list_prefix_time:.2f} ms")
                print(f"Trie is {list_prefix_time/trie_prefix_time:.1f}x faster for prefix operations")
                
            elif choice == 4:
                print(f"\nMemory Usage Analysis:")
                print("Trie Memory Characteristics:")
                print("- Node overhead: ~40-60 bytes per node")
                print("- Shared prefixes: Significant memory savings")
                print("- Sparse children: Dictionary overhead per node")
                print("\nSet Memory Characteristics:")
                print("- Hash table: ~24 bytes per string + string storage")
                print("- No prefix sharing: Full string storage for each word")
                print("- Better for exact lookups, worse for prefix operations")
                
            elif choice == 5:
                size = 1000
                words = generate_random_words(size)
                
                # Build trie with frequencies
                trie = Trie()
                for word in words:
                    # Insert with random frequency
                    freq = random.randint(1, 10)
                    for _ in range(freq):
                        trie.insert(word)
                
                prefixes = [word[:3] for word in random.sample(words, 20)]
                
                print(f"\nAutocomplete Performance Test:")
                
                start = time.time()
                for prefix in prefixes:
                    trie.autocomplete(prefix, 5)
                autocomplete_time = (time.time() - start) * 1000
                
                print(f"Autocomplete (20 queries, top 5): {autocomplete_time:.2f} ms")
                print(f"Average per query: {autocomplete_time/20:.2f} ms")
                
            elif choice == 6:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Main function to run the interactive demo."""
    print("Welcome to the Trie Interactive Learning Tool!")
    print("This demo will help you understand prefix trees and their applications.")
    
    while True:
        display_main_menu()
        
        try:
            choice = int(input("\nEnter your choice (1-8): "))
            
            if choice == 1:
                basic_trie_demo()
            elif choice == 2:
                autocomplete_demo()
            elif choice == 3:
                spell_checker_demo()
            elif choice == 4:
                search_engine_demo()
            elif choice == 5:
                print("\nCompressed Trie Demo - Feature in development")
                print("Basic functionality available in usage.py")
            elif choice == 6:
                suffix_trie_demo()
            elif choice == 7:
                performance_analysis()
            elif choice == 8:
                print("\nThank you for using the Trie Demo!")
                print("Keep exploring data structures and happy coding!")
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