"""
Linked List Usage Examples

This module demonstrates practical usage of linked list implementations
with real-world scenarios and comprehensive test cases.
"""

from implementation import SinglyLinkedList, DoublyLinkedList


def test_singly_linked_list():
    """Test all operations of the singly linked list."""
    print("=== Testing Singly Linked List ===\n")
    
    # Create a new list
    sll = SinglyLinkedList()
    print(f"Created empty list: {sll}")
    print(f"Is empty: {sll.is_empty()}")
    print(f"Size: {len(sll)}\n")
    
    # Test insertions
    print("--- Testing Insertions ---")
    sll.insert_at_head(10)
    print(f"After insert_at_head(10): {sll}")
    
    sll.insert_at_tail(20)
    print(f"After insert_at_tail(20): {sll}")
    
    sll.insert_at_tail(30)
    print(f"After insert_at_tail(30): {sll}")
    
    sll.insert_at_head(5)
    print(f"After insert_at_head(5): {sll}")
    
    sll.insert_at_position(2, 15)
    print(f"After insert_at_position(2, 15): {sll}")
    print(f"Size: {len(sll)}\n")
    
    # Test searching
    print("--- Testing Search ---")
    print(f"Search for 15: index {sll.search(15)}")
    print(f"Search for 100: index {sll.search(100)}")
    print(f"Get element at position 1: {sll.get(1)}\n")
    
    # Test deletions
    print("--- Testing Deletions ---")
    print(f"Delete value 15: {sll.delete_by_value(15)}")
    print(f"After deletion: {sll}")
    
    deleted = sll.delete_at_position(0)
    print(f"Deleted element at position 0: {deleted}")
    print(f"After deletion: {sll}\n")
    
    # Test iteration
    print("--- Testing Iteration ---")
    print("Elements via iteration:", end=" ")
    for element in sll:
        print(element, end=" ")
    print()
    
    # Test conversion to list
    print(f"As Python list: {sll.to_list()}")
    
    # Test reverse
    print(f"Before reverse: {sll}")
    sll.reverse()
    print(f"After reverse: {sll}\n")
    
    # Test edge cases
    print("--- Testing Edge Cases ---")
    try:
        sll.get(100)
    except IndexError as e:
        print(f"IndexError caught: {e}")
    
    try:
        sll.insert_at_position(-1, 999)
    except IndexError as e:
        print(f"IndexError caught: {e}")


def test_doubly_linked_list():
    """Test all operations of the doubly linked list."""
    print("\n=== Testing Doubly Linked List ===\n")
    
    # Create a new list
    dll = DoublyLinkedList()
    print(f"Created empty list: {dll}")
    print(f"Is empty: {dll.is_empty()}")
    print(f"Size: {len(dll)}\n")
    
    # Test insertions
    print("--- Testing Insertions ---")
    dll.insert_at_head(10)
    print(f"After insert_at_head(10): {dll}")
    
    dll.insert_at_tail(20)
    print(f"After insert_at_tail(20): {dll}")
    
    dll.insert_at_tail(30)
    print(f"After insert_at_tail(30): {dll}")
    
    dll.insert_at_head(5)
    print(f"After insert_at_head(5): {dll}")
    print(f"Size: {len(dll)}\n")
    
    # Test traversals
    print("--- Testing Traversals ---")
    print(f"Forward traversal: {dll.traverse_forward()}")
    print(f"Backward traversal: {dll.traverse_backward()}\n")
    
    # Test deletions
    print("--- Testing Deletions ---")
    print(f"Delete value 20: {dll.delete_by_value(20)}")
    print(f"After deletion: {dll}")
    print(f"Forward: {dll.traverse_forward()}")
    print(f"Backward: {dll.traverse_backward()}")


def real_world_example_browser_history():
    """
    Demonstrate linked list usage in browser history implementation.
    This shows how doubly linked lists can be used for navigation.
    """
    print("\n=== Real-World Example: Browser History ===\n")
    
    class BrowserHistory:
        """Simple browser history using doubly linked list concept."""
        
        def __init__(self):
            self.history = DoublyLinkedList()
            self.current_position = -1
        
        def visit_page(self, url: str):
            """Visit a new page."""
            self.history.insert_at_tail(url)
            self.current_position = len(self.history) - 1
            print(f"Visited: {url}")
        
        def get_history(self) -> list:
            """Get browsing history."""
            return self.history.traverse_forward()
        
        def get_current_page(self) -> str:
            """Get current page."""
            if self.current_position >= 0:
                return self.get_history()[self.current_position]
            return "No page loaded"
    
    # Simulate browser usage
    browser = BrowserHistory()
    
    # Visit some pages
    browser.visit_page("https://google.com")
    browser.visit_page("https://stackoverflow.com")
    browser.visit_page("https://github.com")
    browser.visit_page("https://python.org")
    
    print(f"\nBrowsing History: {browser.get_history()}")
    print(f"Current Page: {browser.get_current_page()}")


def real_world_example_undo_redo():
    """
    Demonstrate linked list usage in undo/redo functionality.
    """
    print("\n=== Real-World Example: Text Editor Undo/Redo ===\n")
    
    class TextEditor:
        """Simple text editor with undo functionality using linked list."""
        
        def __init__(self):
            self.actions = SinglyLinkedList()
            self.text = ""
        
        def type_text(self, text: str):
            """Type text and record action."""
            self.actions.insert_at_head(("type", text))
            self.text += text
            print(f"Typed: '{text}' -> Current text: '{self.text}'")
        
        def delete_chars(self, count: int):
            """Delete characters and record action."""
            deleted = self.text[-count:] if count <= len(self.text) else self.text
            self.actions.insert_at_head(("delete", deleted))
            self.text = self.text[:-count] if count <= len(self.text) else ""
            print(f"Deleted: '{deleted}' -> Current text: '{self.text}'")
        
        def undo(self):
            """Undo the last action."""
            if self.actions.is_empty():
                print("Nothing to undo")
                return
            
            action_type, data = self.actions.delete_at_position(0)
            
            if action_type == "type":
                # Undo typing by removing the typed text
                self.text = self.text[:-len(data)]
                print(f"Undid typing '{data}' -> Current text: '{self.text}'")
            elif action_type == "delete":
                # Undo deletion by adding back the deleted text
                self.text += data
                print(f"Undid deletion '{data}' -> Current text: '{self.text}'")
        
        def get_text(self) -> str:
            """Get current text."""
            return self.text
    
    # Simulate text editing
    editor = TextEditor()
    
    editor.type_text("Hello")
    editor.type_text(" World")
    editor.delete_chars(5)  # Delete "World"
    editor.type_text(" Python")
    
    print(f"\nFinal text: '{editor.get_text()}'")
    
    # Undo operations
    print("\nUndoing operations:")
    editor.undo()  # Undo typing " Python"
    editor.undo()  # Undo deleting "World"
    editor.undo()  # Undo typing " World"
    
    print(f"After undos: '{editor.get_text()}'")


def performance_comparison():
    """Compare performance characteristics of linked list vs Python list."""
    print("\n=== Performance Comparison ===\n")
    
    import time
    
    # Test insertion at the beginning
    print("Insertion at beginning (1000 elements):")
    
    # Linked List
    sll = SinglyLinkedList()
    start_time = time.time()
    for i in range(1000):
        sll.insert_at_head(i)
    ll_time = time.time() - start_time
    print(f"Linked List: {ll_time:.6f} seconds")
    
    # Python List
    py_list = []
    start_time = time.time()
    for i in range(1000):
        py_list.insert(0, i)
    py_time = time.time() - start_time
    print(f"Python List: {py_time:.6f} seconds")
    
    print(f"Linked List is {py_time/ll_time:.2f}x faster for head insertion\n")
    
    # Test memory usage comparison
    print("Memory Usage Characteristics:")
    print("Linked List:")
    print("  - Each node: ~28 bytes (data + pointer + overhead)")
    print("  - No pre-allocated memory")
    print("  - Memory scattered across heap")
    
    print("Python List:")
    print("  - Contiguous memory allocation")
    print("  - Over-allocation for growth")
    print("  - Better cache locality")


if __name__ == "__main__":
    test_singly_linked_list()
    test_doubly_linked_list()
    real_world_example_browser_history()
    real_world_example_undo_redo()
    performance_comparison()
