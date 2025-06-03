"""
Linked List Implementation

This module provides comprehensive implementations of singly and doubly linked lists
with all essential operations including insertion, deletion, searching, and traversal.
"""

from typing import Optional, Any, Iterator


class ListNode:
    """
    Node class for singly linked list.
    
    Attributes:
        data: The data stored in the node
        next: Reference to the next node in the list
    """
    
    def __init__(self, data: Any) -> None:
        """Initialize a new node with given data."""
        self.data = data
        self.next: Optional['ListNode'] = None
    
    def __str__(self) -> str:
        """String representation of the node."""
        return str(self.data)


class SinglyLinkedList:
    """
    Singly Linked List implementation with comprehensive operations.
    
    Time Complexities:
    - Insert at head: O(1)
    - Insert at tail: O(1) with tail pointer, O(n) without
    - Insert at position: O(n)
    - Delete by value: O(n)
    - Delete at position: O(n)
    - Search: O(n)
    - Traverse: O(n)
    
    Space Complexity: O(n) where n is the number of elements
    """
    
    def __init__(self) -> None:
        """Initialize an empty linked list."""
        self.head: Optional[ListNode] = None
        self.tail: Optional[ListNode] = None
        self.size: int = 0
    
    def is_empty(self) -> bool:
        """Check if the list is empty."""
        return self.head is None
    
    def __len__(self) -> int:
        """Return the size of the list."""
        return self.size
    
    def insert_at_head(self, data: Any) -> None:
        """
        Insert a new node at the beginning of the list.
        
        Args:
            data: The data to insert
            
        Time Complexity: O(1)
        """
        new_node = ListNode(data)
        
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.size += 1
    
    def insert_at_tail(self, data: Any) -> None:
        """
        Insert a new node at the end of the list.
        
        Args:
            data: The data to insert
            
        Time Complexity: O(1)
        """
        new_node = ListNode(data)
        
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    
    def insert_at_position(self, position: int, data: Any) -> None:
        """
        Insert a new node at the specified position.
        
        Args:
            position: The position to insert at (0-indexed)
            data: The data to insert
            
        Raises:
            IndexError: If position is out of bounds
            
        Time Complexity: O(n)
        """
        if position < 0 or position > self.size:
            raise IndexError(f"Position {position} is out of bounds for list of size {self.size}")
        
        if position == 0:
            self.insert_at_head(data)
            return
        
        if position == self.size:
            self.insert_at_tail(data)
            return
        
        new_node = ListNode(data)
        current = self.head
        
        # Navigate to the position before the insertion point
        for _ in range(position - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self.size += 1
    
    def delete_by_value(self, data: Any) -> bool:
        """
        Delete the first occurrence of the specified value.
        
        Args:
            data: The value to delete
            
        Returns:
            bool: True if deletion was successful, False if value not found
            
        Time Complexity: O(n)
        """
        if self.is_empty():
            return False
        
        # If deleting the head node
        if self.head.data == data:
            if self.head == self.tail:  # Only one node
                self.head = self.tail = None
            else:
                self.head = self.head.next
            self.size -= 1
            return True
        
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        if current.next:  # Found the node to delete
            if current.next == self.tail:  # Deleting tail node
                self.tail = current
            current.next = current.next.next
            self.size -= 1
            return True
        
        return False
    
    def delete_at_position(self, position: int) -> Any:
        """
        Delete the node at the specified position.
        
        Args:
            position: The position to delete from (0-indexed)
            
        Returns:
            Any: The data from the deleted node
            
        Raises:
            IndexError: If position is out of bounds
            
        Time Complexity: O(n)
        """
        if position < 0 or position >= self.size:
            raise IndexError(f"Position {position} is out of bounds for list of size {self.size}")
        
        if position == 0:
            data = self.head.data
            if self.head == self.tail:  # Only one node
                self.head = self.tail = None
            else:
                self.head = self.head.next
            self.size -= 1
            return data
        
        current = self.head
        for _ in range(position - 1):
            current = current.next
        
        data = current.next.data
        if current.next == self.tail:  # Deleting tail node
            self.tail = current
        current.next = current.next.next
        self.size -= 1
        return data
    
    def search(self, data: Any) -> int:
        """
        Search for a value in the list.
        
        Args:
            data: The value to search for
            
        Returns:
            int: The index of the first occurrence, or -1 if not found
            
        Time Complexity: O(n)
        """
        current = self.head
        index = 0
        
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        
        return -1
    
    def get(self, position: int) -> Any:
        """
        Get the value at the specified position.
        
        Args:
            position: The position to get from (0-indexed)
            
        Returns:
            Any: The data at the specified position
            
        Raises:
            IndexError: If position is out of bounds
            
        Time Complexity: O(n)
        """
        if position < 0 or position >= self.size:
            raise IndexError(f"Position {position} is out of bounds for list of size {self.size}")
        
        current = self.head
        for _ in range(position):
            current = current.next
        
        return current.data
    
    def reverse(self) -> None:
        """
        Reverse the linked list in place.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if self.is_empty() or self.size == 1:
            return
        
        prev = None
        current = self.head
        self.tail = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev
    
    def to_list(self) -> list:
        """
        Convert the linked list to a Python list.
        
        Returns:
            list: A Python list containing all elements
            
        Time Complexity: O(n)
        """
        result = []
        current = self.head
        
        while current:
            result.append(current.data)
            current = current.next
        
        return result
    
    def __iter__(self) -> Iterator:
        """Make the linked list iterable."""
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def __str__(self) -> str:
        """String representation of the linked list."""
        if self.is_empty():
            return "[]"
        
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        
        return " -> ".join(elements)


class DoublyListNode:
    """
    Node class for doubly linked list.
    
    Attributes:
        data: The data stored in the node
        next: Reference to the next node
        prev: Reference to the previous node
    """
    
    def __init__(self, data: Any) -> None:
        """Initialize a new doubly linked list node."""
        self.data = data
        self.next: Optional['DoublyListNode'] = None
        self.prev: Optional['DoublyListNode'] = None
    
    def __str__(self) -> str:
        """String representation of the node."""
        return str(self.data)


class DoublyLinkedList:
    """
    Doubly Linked List implementation with comprehensive operations.
    
    Time Complexities:
    - Insert at head/tail: O(1)
    - Insert at position: O(n)
    - Delete by value: O(n)
    - Delete at position: O(n)
    - Search: O(n)
    - Traverse forward/backward: O(n)
    
    Space Complexity: O(n) where n is the number of elements
    """
    
    def __init__(self) -> None:
        """Initialize an empty doubly linked list."""
        self.head: Optional[DoublyListNode] = None
        self.tail: Optional[DoublyListNode] = None
        self.size: int = 0
    
    def is_empty(self) -> bool:
        """Check if the list is empty."""
        return self.head is None
    
    def __len__(self) -> int:
        """Return the size of the list."""
        return self.size
    
    def insert_at_head(self, data: Any) -> None:
        """
        Insert a new node at the beginning of the list.
        
        Args:
            data: The data to insert
            
        Time Complexity: O(1)
        """
        new_node = DoublyListNode(data)
        
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
    
    def insert_at_tail(self, data: Any) -> None:
        """
        Insert a new node at the end of the list.
        
        Args:
            data: The data to insert
            
        Time Complexity: O(1)
        """
        new_node = DoublyListNode(data)
        
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    
    def delete_by_value(self, data: Any) -> bool:
        """
        Delete the first occurrence of the specified value.
        
        Args:
            data: The value to delete
            
        Returns:
            bool: True if deletion was successful, False if value not found
            
        Time Complexity: O(n)
        """
        if self.is_empty():
            return False
        
        current = self.head
        while current and current.data != data:
            current = current.next
        
        if current:  # Found the node to delete
            if current.prev:
                current.prev.next = current.next
            else:  # Deleting head
                self.head = current.next
            
            if current.next:
                current.next.prev = current.prev
            else:  # Deleting tail
                self.tail = current.prev
            
            self.size -= 1
            return True
        
        return False
    
    def traverse_forward(self) -> list:
        """
        Traverse the list from head to tail.
        
        Returns:
            list: Elements in forward order
            
        Time Complexity: O(n)
        """
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def traverse_backward(self) -> list:
        """
        Traverse the list from tail to head.
        
        Returns:
            list: Elements in reverse order
            
        Time Complexity: O(n)
        """
        result = []
        current = self.tail
        while current:
            result.append(current.data)
            current = current.prev
        return result
    
    def __str__(self) -> str:
        """String representation of the doubly linked list."""
        if self.is_empty():
            return "[]"
        
        elements = self.traverse_forward()
        return " <-> ".join(map(str, elements))
