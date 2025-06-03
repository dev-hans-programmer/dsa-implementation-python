"""
Stack Implementation

This module provides comprehensive implementations of stack data structure
using different underlying representations (list-based and linked list-based).
"""

from typing import Any, Optional, List
from collections import deque


class StackEmptyError(Exception):
    """Custom exception for operations on empty stack."""
    pass


class ListStack:
    """
    Stack implementation using Python list as underlying storage.
    
    This is the most common and efficient implementation in Python.
    
    Time Complexities:
    - Push: O(1) amortized
    - Pop: O(1)
    - Peek/Top: O(1)
    - Size: O(1)
    - Is Empty: O(1)
    
    Space Complexity: O(n) where n is the number of elements
    """
    
    def __init__(self) -> None:
        """Initialize an empty stack."""
        self._items: List[Any] = []
    
    def push(self, item: Any) -> None:
        """
        Add an item to the top of stack.
        
        Args:
            item: The item to push onto the stack
            
        Time Complexity: O(1) amortized
        """
        self._items.append(item)
    
    def pop(self) -> Any:
        """
        Remove and return the top item from stack.
        
        Returns:
            Any: The top item from the stack
            
        Raises:
            StackEmptyError: If stack is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise StackEmptyError("Cannot pop from empty stack")
        return self._items.pop()
    
    def peek(self) -> Any:
        """
        Return the top item without removing it.
        
        Returns:
            Any: The top item from the stack
            
        Raises:
            StackEmptyError: If stack is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise StackEmptyError("Cannot peek empty stack")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """
        Check if stack is empty.
        
        Returns:
            bool: True if stack is empty, False otherwise
            
        Time Complexity: O(1)
        """
        return len(self._items) == 0
    
    def size(self) -> int:
        """
        Get the number of items in stack.
        
        Returns:
            int: Number of items in stack
            
        Time Complexity: O(1)
        """
        return len(self._items)
    
    def clear(self) -> None:
        """
        Remove all items from stack.
        
        Time Complexity: O(1)
        """
        self._items.clear()
    
    def to_list(self) -> List[Any]:
        """
        Convert stack to list (bottom to top).
        
        Returns:
            List[Any]: List representation of stack
            
        Time Complexity: O(n)
        """
        return self._items.copy()
    
    def __len__(self) -> int:
        """Return size of stack."""
        return self.size()
    
    def __str__(self) -> str:
        """String representation of stack."""
        if self.is_empty():
            return "Stack: []"
        
        # Show stack vertically (top to bottom)
        items_str = []
        for i in range(len(self._items) - 1, -1, -1):
            if i == len(self._items) - 1:
                items_str.append(f"Top -> [{self._items[i]}]")
            else:
                items_str.append(f"       [{self._items[i]}]")
        
        return "Stack:\n" + "\n".join(items_str)


class StackNode:
    """Node class for linked list-based stack implementation."""
    
    def __init__(self, data: Any) -> None:
        """Initialize a new node."""
        self.data = data
        self.next: Optional['StackNode'] = None


class LinkedStack:
    """
    Stack implementation using linked list as underlying storage.
    
    This implementation is useful when you want to avoid the overhead
    of dynamic array resizing or when memory is fragmented.
    
    Time Complexities:
    - Push: O(1)
    - Pop: O(1)
    - Peek/Top: O(1)
    - Size: O(1)
    - Is Empty: O(1)
    
    Space Complexity: O(n) where n is the number of elements
    """
    
    def __init__(self) -> None:
        """Initialize an empty stack."""
        self._top: Optional[StackNode] = None
        self._size: int = 0
    
    def push(self, item: Any) -> None:
        """
        Add an item to the top of stack.
        
        Args:
            item: The item to push onto the stack
            
        Time Complexity: O(1)
        """
        new_node = StackNode(item)
        new_node.next = self._top
        self._top = new_node
        self._size += 1
    
    def pop(self) -> Any:
        """
        Remove and return the top item from stack.
        
        Returns:
            Any: The top item from the stack
            
        Raises:
            StackEmptyError: If stack is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise StackEmptyError("Cannot pop from empty stack")
        
        data = self._top.data
        self._top = self._top.next
        self._size -= 1
        return data
    
    def peek(self) -> Any:
        """
        Return the top item without removing it.
        
        Returns:
            Any: The top item from the stack
            
        Raises:
            StackEmptyError: If stack is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise StackEmptyError("Cannot peek empty stack")
        return self._top.data
    
    def is_empty(self) -> bool:
        """
        Check if stack is empty.
        
        Returns:
            bool: True if stack is empty, False otherwise
            
        Time Complexity: O(1)
        """
        return self._top is None
    
    def size(self) -> int:
        """
        Get the number of items in stack.
        
        Returns:
            int: Number of items in stack
            
        Time Complexity: O(1)
        """
        return self._size
    
    def clear(self) -> None:
        """
        Remove all items from stack.
        
        Time Complexity: O(1)
        """
        self._top = None
        self._size = 0
    
    def to_list(self) -> List[Any]:
        """
        Convert stack to list (bottom to top).
        
        Returns:
            List[Any]: List representation of stack
            
        Time Complexity: O(n)
        """
        result = []
        current = self._top
        
        # Collect items from top to bottom
        temp_list = []
        while current:
            temp_list.append(current.data)
            current = current.next
        
        # Reverse to get bottom to top order
        return temp_list[::-1]
    
    def __len__(self) -> int:
        """Return size of stack."""
        return self.size()
    
    def __str__(self) -> str:
        """String representation of stack."""
        if self.is_empty():
            return "Stack: []"
        
        items_str = []
        current = self._top
        is_top = True
        
        while current:
            if is_top:
                items_str.append(f"Top -> [{current.data}]")
                is_top = False
            else:
                items_str.append(f"       [{current.data}]")
            current = current.next
        
        return "Stack:\n" + "\n".join(items_str)


class MinStack:
    """
    Stack that supports getting minimum element in O(1) time.
    
    This is a special stack implementation that maintains the minimum
    element at each level, allowing constant-time minimum queries.
    """
    
    def __init__(self) -> None:
        """Initialize empty min stack."""
        self._stack: List[Any] = []
        self._min_stack: List[Any] = []
    
    def push(self, item: Any) -> None:
        """
        Push item onto stack and update minimum.
        
        Args:
            item: The item to push
            
        Time Complexity: O(1)
        """
        self._stack.append(item)
        
        # Update minimum stack
        if not self._min_stack or item <= self._min_stack[-1]:
            self._min_stack.append(item)
    
    def pop(self) -> Any:
        """
        Pop top item and update minimum.
        
        Returns:
            Any: The popped item
            
        Raises:
            StackEmptyError: If stack is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise StackEmptyError("Cannot pop from empty stack")
        
        item = self._stack.pop()
        
        # Update minimum stack
        if item == self._min_stack[-1]:
            self._min_stack.pop()
        
        return item
    
    def peek(self) -> Any:
        """Get top item without removing it."""
        if self.is_empty():
            raise StackEmptyError("Cannot peek empty stack")
        return self._stack[-1]
    
    def get_min(self) -> Any:
        """
        Get minimum element in stack.
        
        Returns:
            Any: The minimum element
            
        Raises:
            StackEmptyError: If stack is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise StackEmptyError("Cannot get min from empty stack")
        return self._min_stack[-1]
    
    def is_empty(self) -> bool:
        """Check if stack is empty."""
        return len(self._stack) == 0
    
    def size(self) -> int:
        """Get size of stack."""
        return len(self._stack)
    
    def __str__(self) -> str:
        """String representation showing stack and current minimum."""
        if self.is_empty():
            return "MinStack: []"
        
        return f"MinStack: {self._stack}, Min: {self.get_min()}"


class DequeStack:
    """
    Stack implementation using collections.deque for better performance.
    
    Python's deque is implemented as a doubly-linked list and provides
    O(1) operations at both ends.
    """
    
    def __init__(self) -> None:
        """Initialize empty stack using deque."""
        self._items = deque()
    
    def push(self, item: Any) -> None:
        """Push item onto stack."""
        self._items.append(item)
    
    def pop(self) -> Any:
        """Pop item from stack."""
        if self.is_empty():
            raise StackEmptyError("Cannot pop from empty stack")
        return self._items.pop()
    
    def peek(self) -> Any:
        """Peek at top item."""
        if self.is_empty():
            raise StackEmptyError("Cannot peek empty stack")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """Check if stack is empty."""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Get size of stack."""
        return len(self._items)
    
    def clear(self) -> None:
        """Clear all items."""
        self._items.clear()
    
    def __str__(self) -> str:
        """String representation."""
        return f"DequeStack: {list(self._items)}"


# Alias for the most commonly used implementation
Stack = ListStack
