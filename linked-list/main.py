"""
Interactive Linked List Demonstration

This module provides an interactive demonstration of linked list operations,
allowing users to experiment with different functionalities.
"""

from implementation import SinglyLinkedList, DoublyLinkedList


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("LINKED LIST INTERACTIVE DEMO")
    print("="*50)
    print("1. Singly Linked List Demo")
    print("2. Doubly Linked List Demo")
    print("3. Performance Comparison")
    print("4. Real-World Examples")
    print("5. Exit")
    print("="*50)


def singly_linked_list_demo():
    """Interactive demo for singly linked list."""
    sll = SinglyLinkedList()
    
    while True:
        print(f"\nCurrent List: {sll}")
        print(f"Size: {len(sll)}")
        print("\nSingly Linked List Operations:")
        print("1. Insert at head")
        print("2. Insert at tail") 
        print("3. Insert at position")
        print("4. Delete by value")
        print("5. Delete at position")
        print("6. Search for value")
        print("7. Get value at position")
        print("8. Reverse list")
        print("9. Show as Python list")
        print("10. Back to main menu")
        
        try:
            choice = int(input("\nEnter your choice (1-10): "))
            
            if choice == 1:
                value = input("Enter value to insert at head: ")
                sll.insert_at_head(value)
                print(f"Inserted '{value}' at head")
                
            elif choice == 2:
                value = input("Enter value to insert at tail: ")
                sll.insert_at_tail(value)
                print(f"Inserted '{value}' at tail")
                
            elif choice == 3:
                position = int(input("Enter position: "))
                value = input("Enter value: ")
                sll.insert_at_position(position, value)
                print(f"Inserted '{value}' at position {position}")
                
            elif choice == 4:
                value = input("Enter value to delete: ")
                success = sll.delete_by_value(value)
                if success:
                    print(f"Deleted '{value}'")
                else:
                    print(f"Value '{value}' not found")
                    
            elif choice == 5:
                position = int(input("Enter position to delete: "))
                deleted = sll.delete_at_position(position)
                print(f"Deleted '{deleted}' from position {position}")
                
            elif choice == 6:
                value = input("Enter value to search: ")
                index = sll.search(value)
                if index != -1:
                    print(f"Found '{value}' at index {index}")
                else:
                    print(f"Value '{value}' not found")
                    
            elif choice == 7:
                position = int(input("Enter position: "))
                value = sll.get(position)
                print(f"Value at position {position}: '{value}'")
                
            elif choice == 8:
                sll.reverse()
                print("List reversed")
                
            elif choice == 9:
                print(f"As Python list: {sll.to_list()}")
                
            elif choice == 10:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except (ValueError, IndexError) as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")


def doubly_linked_list_demo():
    """Interactive demo for doubly linked list."""
    dll = DoublyLinkedList()
    
    while True:
        print(f"\nCurrent List: {dll}")
        print(f"Size: {len(dll)}")
        print("\nDoubly Linked List Operations:")
        print("1. Insert at head")
        print("2. Insert at tail")
        print("3. Delete by value")
        print("4. Traverse forward")
        print("5. Traverse backward")
        print("6. Back to main menu")
        
        try:
            choice = int(input("\nEnter your choice (1-6): "))
            
            if choice == 1:
                value = input("Enter value to insert at head: ")
                dll.insert_at_head(value)
                print(f"Inserted '{value}' at head")
                
            elif choice == 2:
                value = input("Enter value to insert at tail: ")
                dll.insert_at_tail(value)
                print(f"Inserted '{value}' at tail")
                
            elif choice == 3:
                value = input("Enter value to delete: ")
                success = dll.delete_by_value(value)
                if success:
                    print(f"Deleted '{value}'")
                else:
                    print(f"Value '{value}' not found")
                    
            elif choice == 4:
                forward = dll.traverse_forward()
                print(f"Forward traversal: {forward}")
                
            elif choice == 5:
                backward = dll.traverse_backward()
                print(f"Backward traversal: {backward}")
                
            elif choice == 6:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nOperation cancelled.")


def performance_demo():
    """Demonstrate performance characteristics."""
    print("\n" + "="*50)
    print("PERFORMANCE DEMONSTRATION")
    print("="*50)
    
    import time
    
    sizes = [100, 500, 1000]
    
    for size in sizes:
        print(f"\nTesting with {size} elements:")
        
        # Test insertion at head
        sll = SinglyLinkedList()
        start = time.time()
        for i in range(size):
            sll.insert_at_head(i)
        ll_time = time.time() - start
        
        py_list = []
        start = time.time()
        for i in range(size):
            py_list.insert(0, i)
        py_time = time.time() - start
        
        print(f"  Head insertion - Linked List: {ll_time:.6f}s, Python List: {py_time:.6f}s")
        if py_time > 0:
            print(f"  Linked List is {py_time/ll_time:.2f}x faster")
        
        # Test search
        search_value = size // 2
        
        start = time.time()
        sll.search(search_value)
        ll_search_time = time.time() - start
        
        start = time.time()
        try:
            py_list.index(search_value)
        except ValueError:
            pass
        py_search_time = time.time() - start
        
        print(f"  Search - Linked List: {ll_search_time:.6f}s, Python List: {py_search_time:.6f}s")


def real_world_examples():
    """Show real-world applications."""
    print("\n" + "="*50)
    print("REAL-WORLD APPLICATIONS")
    print("="*50)
    
    print("\n1. Music Playlist (Doubly Linked List)")
    print("   - Navigate forward/backward through songs")
    print("   - Easy insertion/deletion of songs")
    print("   - No need to know total number of songs")
    
    print("\n2. Browser History (Doubly Linked List)")
    print("   - Back/Forward navigation")
    print("   - Dynamic history size")
    print("   - Easy to add new pages")
    
    print("\n3. Undo/Redo Operations (Singly Linked List)")
    print("   - Stack-like behavior for recent actions")
    print("   - Memory efficient for large action histories")
    print("   - Easy to implement with head insertion")
    
    print("\n4. Image Viewer (Doubly Linked List)")
    print("   - Navigate between images")
    print("   - Add/remove images dynamically")
    print("   - Previous/Next functionality")
    
    print("\n5. Text Editor Gap Buffer (Modified Linked List)")
    print("   - Efficient cursor movement")
    print("   - Fast insertion/deletion at cursor")
    print("   - Memory efficient for large documents")
    
    # Simple playlist demo
    print("\n" + "-"*30)
    print("Simple Playlist Demo:")
    playlist = DoublyLinkedList()
    
    songs = ["Song A", "Song B", "Song C", "Song D"]
    for song in songs:
        playlist.insert_at_tail(song)
    
    print(f"Playlist: {playlist}")
    print(f"Forward play order: {playlist.traverse_forward()}")
    print(f"Shuffle (reverse): {playlist.traverse_backward()}")


def main():
    """Main function to run the interactive demo."""
    print("Welcome to the Linked List Interactive Learning Tool!")
    print("This demo will help you understand linked list operations through hands-on experience.")
    
    while True:
        display_menu()
        
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            
            if choice == 1:
                singly_linked_list_demo()
            elif choice == 2:
                doubly_linked_list_demo()
            elif choice == 3:
                performance_demo()
            elif choice == 4:
                real_world_examples()
            elif choice == 5:
                print("\nThank you for using the Linked List Demo!")
                print("Keep practicing and happy coding! 🚀")
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
