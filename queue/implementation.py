"""
Queue Implementation

This module provides comprehensive implementations of queue data structure
using different underlying representations (list-based, linked list-based, and circular).
"""

from typing import Any, Optional, List
from collections import deque


class QueueEmptyError(Exception):
    """Custom exception for operations on empty queue."""
    pass


class QueueFullError(Exception):
    """Custom exception for operations on full queue."""
    pass


class ListQueue:
    """
    Queue implementation using Python list as underlying storage.
    
    This implementation uses list.pop(0) which is O(n), making it less efficient
    for large queues but simple to understand.
    
    Time Complexities:
    - Enqueue: O(1)
    - Dequeue: O(n) due to list.pop(0)
    - Front: O(1)
    - Size: O(1)
    - Is Empty: O(1)
    
    Space Complexity: O(n) where n is the number of elements
    """
    
    def __init__(self) -> None:
        """Initialize an empty queue."""
        self._items: List[Any] = []
    
    def enqueue(self, item: Any) -> None:
        """
        Add an item to the rear of queue.
        
        Args:
            item: The item to add to the queue
            
        Time Complexity: O(1)
        """
        self._items.append(item)
    
    def dequeue(self) -> Any:
        """
        Remove and return the front item from queue.
        
        Returns:
            Any: The front item from the queue
            
        Raises:
            QueueEmptyError: If queue is empty
            
        Time Complexity: O(n)
        """
        if self.is_empty():
            raise QueueEmptyError("Cannot dequeue from empty queue")
        return self._items.pop(0)
    
    def front(self) -> Any:
        """
        Return the front item without removing it.
        
        Returns:
            Any: The front item from the queue
            
        Raises:
            QueueEmptyError: If queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise QueueEmptyError("Cannot peek empty queue")
        return self._items[0]
    
    def rear(self) -> Any:
        """
        Return the rear item without removing it.
        
        Returns:
            Any: The rear item from the queue
            
        Raises:
            QueueEmptyError: If queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise QueueEmptyError("Cannot peek empty queue")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """
        Check if queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise
            
        Time Complexity: O(1)
        """
        return len(self._items) == 0
    
    def size(self) -> int:
        """
        Get the number of items in queue.
        
        Returns:
            int: Number of items in queue
            
        Time Complexity: O(1)
        """
        return len(self._items)
    
    def clear(self) -> None:
        """
        Remove all items from queue.
        
        Time Complexity: O(1)
        """
        self._items.clear()
    
    def to_list(self) -> List[Any]:
        """
        Convert queue to list (front to rear).
        
        Returns:
            List[Any]: List representation of queue
            
        Time Complexity: O(n)
        """
        return self._items.copy()
    
    def __len__(self) -> int:
        """Return size of queue."""
        return self.size()
    
    def __str__(self) -> str:
        """String representation of queue."""
        if self.is_empty():
            return "Queue: []"
        return f"Queue: [front] {' <- '.join(map(str, self._items))} [rear]"


class QueueNode:
    """Node class for linked list-based queue implementation."""
    
    def __init__(self, data: Any) -> None:
        """Initialize a new node."""
        self.data = data
        self.next: Optional['QueueNode'] = None


class LinkedQueue:
    """
    Queue implementation using linked list as underlying storage.
    
    This implementation provides O(1) operations for both enqueue and dequeue
    by maintaining pointers to both front and rear.
    
    Time Complexities:
    - Enqueue: O(1)
    - Dequeue: O(1)
    - Front: O(1)
    - Size: O(1)
    - Is Empty: O(1)
    
    Space Complexity: O(n) where n is the number of elements
    """
    
    def __init__(self) -> None:
        """Initialize an empty queue."""
        self._front: Optional[QueueNode] = None
        self._rear: Optional[QueueNode] = None
        self._size: int = 0
    
    def enqueue(self, item: Any) -> None:
        """
        Add an item to the rear of queue.
        
        Args:
            item: The item to add to the queue
            
        Time Complexity: O(1)
        """
        new_node = QueueNode(item)
        
        if self.is_empty():
            self._front = self._rear = new_node
        else:
            self._rear.next = new_node
            self._rear = new_node
        
        self._size += 1
    
    def dequeue(self) -> Any:
        """
        Remove and return the front item from queue.
        
        Returns:
            Any: The front item from the queue
            
        Raises:
            QueueEmptyError: If queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise QueueEmptyError("Cannot dequeue from empty queue")
        
        data = self._front.data
        self._front = self._front.next
        
        if self._front is None:  # Queue became empty
            self._rear = None
        
        self._size -= 1
        return data
    
    def front(self) -> Any:
        """
        Return the front item without removing it.
        
        Returns:
            Any: The front item from the queue
            
        Raises:
            QueueEmptyError: If queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise QueueEmptyError("Cannot peek empty queue")
        return self._front.data
    
    def rear(self) -> Any:
        """
        Return the rear item without removing it.
        
        Returns:
            Any: The rear item from the queue
            
        Raises:
            QueueEmptyError: If queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise QueueEmptyError("Cannot peek empty queue")
        return self._rear.data
    
    def is_empty(self) -> bool:
        """
        Check if queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise
            
        Time Complexity: O(1)
        """
        return self._front is None
    
    def size(self) -> int:
        """
        Get the number of items in queue.
        
        Returns:
            int: Number of items in queue
            
        Time Complexity: O(1)
        """
        return self._size
    
    def clear(self) -> None:
        """
        Remove all items from queue.
        
        Time Complexity: O(1)
        """
        self._front = self._rear = None
        self._size = 0
    
    def to_list(self) -> List[Any]:
        """
        Convert queue to list (front to rear).
        
        Returns:
            List[Any]: List representation of queue
            
        Time Complexity: O(n)
        """
        result = []
        current = self._front
        
        while current:
            result.append(current.data)
            current = current.next
        
        return result
    
    def __len__(self) -> int:
        """Return size of queue."""
        return self.size()
    
    def __str__(self) -> str:
        """String representation of queue."""
        if self.is_empty():
            return "Queue: []"
        
        items = self.to_list()
        return f"Queue: [front] {' <- '.join(map(str, items))} [rear]"


class CircularQueue:
    """
    Circular Queue implementation using fixed-size array.
    
    This implementation uses a circular buffer approach where the rear
    wraps around to the beginning when it reaches the end of the array.
    
    Time Complexities:
    - Enqueue: O(1)
    - Dequeue: O(1)
    - Front: O(1)
    - Is Empty/Full: O(1)
    
    Space Complexity: O(capacity)
    """
    
    def __init__(self, capacity: int) -> None:
        """
        Initialize a circular queue with given capacity.
        
        Args:
            capacity: Maximum number of items the queue can hold
            
        Raises:
            ValueError: If capacity is not positive
        """
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        
        self._capacity = capacity
        self._items = [None] * capacity
        self._front = 0
        self._rear = -1
        self._size = 0
    
    def enqueue(self, item: Any) -> None:
        """
        Add an item to the rear of queue.
        
        Args:
            item: The item to add to the queue
            
        Raises:
            QueueFullError: If queue is at capacity
            
        Time Complexity: O(1)
        """
        if self.is_full():
            raise QueueFullError("Cannot enqueue to full queue")
        
        self._rear = (self._rear + 1) % self._capacity
        self._items[self._rear] = item
        self._size += 1
    
    def dequeue(self) -> Any:
        """
        Remove and return the front item from queue.
        
        Returns:
            Any: The front item from the queue
            
        Raises:
            QueueEmptyError: If queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise QueueEmptyError("Cannot dequeue from empty queue")
        
        data = self._items[self._front]
        self._items[self._front] = None  # Optional: clear reference
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        
        return data
    
    def front(self) -> Any:
        """
        Return the front item without removing it.
        
        Returns:
            Any: The front item from the queue
            
        Raises:
            QueueEmptyError: If queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise QueueEmptyError("Cannot peek empty queue")
        return self._items[self._front]
    
    def rear(self) -> Any:
        """
        Return the rear item without removing it.
        
        Returns:
            Any: The rear item from the queue
            
        Raises:
            QueueEmptyError: If queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise QueueEmptyError("Cannot peek empty queue")
        return self._items[self._rear]
    
    def is_empty(self) -> bool:
        """
        Check if queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise
            
        Time Complexity: O(1)
        """
        return self._size == 0
    
    def is_full(self) -> bool:
        """
        Check if queue is full.
        
        Returns:
            bool: True if queue is full, False otherwise
            
        Time Complexity: O(1)
        """
        return self._size == self._capacity
    
    def size(self) -> int:
        """
        Get the number of items in queue.
        
        Returns:
            int: Number of items in queue
            
        Time Complexity: O(1)
        """
        return self._size
    
    def capacity(self) -> int:
        """
        Get the maximum capacity of the queue.
        
        Returns:
            int: Maximum capacity
        """
        return self._capacity
    
    def clear(self) -> None:
        """
        Remove all items from queue.
        
        Time Complexity: O(1)
        """
        self._items = [None] * self._capacity
        self._front = 0
        self._rear = -1
        self._size = 0
    
    def to_list(self) -> List[Any]:
        """
        Convert queue to list (front to rear).
        
        Returns:
            List[Any]: List representation of queue
            
        Time Complexity: O(n)
        """
        if self.is_empty():
            return []
        
        result = []
        index = self._front
        
        for _ in range(self._size):
            result.append(self._items[index])
            index = (index + 1) % self._capacity
        
        return result
    
    def __len__(self) -> int:
        """Return size of queue."""
        return self.size()
    
    def __str__(self) -> str:
        """String representation of queue."""
        if self.is_empty():
            return f"CircularQueue(capacity={self._capacity}): []"
        
        items = self.to_list()
        return f"CircularQueue(capacity={self._capacity}): [front] {' <- '.join(map(str, items))} [rear]"


class DequeQueue:
    """
    Queue implementation using collections.deque for optimal performance.
    
    Python's deque is implemented as a doubly-linked list and provides
    O(1) operations at both ends.
    
    Time Complexities:
    - Enqueue: O(1)
    - Dequeue: O(1)
    - Front/Rear: O(1)
    - Size: O(1)
    
    Space Complexity: O(n) where n is the number of elements
    """
    
    def __init__(self) -> None:
        """Initialize empty queue using deque."""
        self._items = deque()
    
    def enqueue(self, item: Any) -> None:
        """
        Add an item to the rear of queue.
        
        Args:
            item: The item to add to the queue
            
        Time Complexity: O(1)
        """
        self._items.append(item)
    
    def dequeue(self) -> Any:
        """
        Remove and return the front item from queue.
        
        Returns:
            Any: The front item from the queue
            
        Raises:
            QueueEmptyError: If queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise QueueEmptyError("Cannot dequeue from empty queue")
        return self._items.popleft()
    
    def front(self) -> Any:
        """
        Return the front item without removing it.
        
        Returns:
            Any: The front item from the queue
            
        Raises:
            QueueEmptyError: If queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise QueueEmptyError("Cannot peek empty queue")
        return self._items[0]
    
    def rear(self) -> Any:
        """
        Return the rear item without removing it.
        
        Returns:
            Any: The rear item from the queue
            
        Raises:
            QueueEmptyError: If queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise QueueEmptyError("Cannot peek empty queue")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """
        Check if queue is empty.
        
        Returns:
            bool: True if queue is empty, False otherwise
            
        Time Complexity: O(1)
        """
        return len(self._items) == 0
    
    def size(self) -> int:
        """
        Get the number of items in queue.
        
        Returns:
            int: Number of items in queue
            
        Time Complexity: O(1)
        """
        return len(self._items)
    
    def clear(self) -> None:
        """
        Remove all items from queue.
        
        Time Complexity: O(1)
        """
        self._items.clear()
    
    def to_list(self) -> List[Any]:
        """
        Convert queue to list (front to rear).
        
        Returns:
            List[Any]: List representation of queue
            
        Time Complexity: O(n)
        """
        return list(self._items)
    
    def __len__(self) -> int:
        """Return size of queue."""
        return self.size()
    
    def __str__(self) -> str:
        """String representation of queue."""
        if self.is_empty():
            return "DequeQueue: []"
        return f"DequeQueue: [front] {' <- '.join(map(str, self._items))} [rear]"


class PriorityQueue:
    """
    Priority Queue implementation using a binary heap.
    
    Elements are dequeued based on priority rather than insertion order.
    Lower values have higher priority by default.
    """
    
    def __init__(self, reverse: bool = False) -> None:
        """
        Initialize priority queue.
        
        Args:
            reverse: If True, higher values have higher priority
        """
        self._heap: List[Any] = []
        self._reverse = reverse
    
    def _parent(self, i: int) -> int:
        """Get parent index."""
        return (i - 1) // 2
    
    def _left_child(self, i: int) -> int:
        """Get left child index."""
        return 2 * i + 1
    
    def _right_child(self, i: int) -> int:
        """Get right child index."""
        return 2 * i + 2
    
    def _compare(self, a: Any, b: Any) -> bool:
        """Compare two elements based on priority order."""
        if self._reverse:
            return a > b
        return a < b
    
    def _heapify_up(self, i: int) -> None:
        """Maintain heap property upward from index i."""
        while i > 0:
            parent = self._parent(i)
            if not self._compare(self._heap[i], self._heap[parent]):
                break
            self._heap[i], self._heap[parent] = self._heap[parent], self._heap[i]
            i = parent
    
    def _heapify_down(self, i: int) -> None:
        """Maintain heap property downward from index i."""
        while True:
            min_idx = i
            left = self._left_child(i)
            right = self._right_child(i)
            
            if (left < len(self._heap) and 
                self._compare(self._heap[left], self._heap[min_idx])):
                min_idx = left
            
            if (right < len(self._heap) and 
                self._compare(self._heap[right], self._heap[min_idx])):
                min_idx = right
            
            if min_idx == i:
                break
            
            self._heap[i], self._heap[min_idx] = self._heap[min_idx], self._heap[i]
            i = min_idx
    
    def enqueue(self, item: Any) -> None:
        """
        Add an item to the priority queue.
        
        Args:
            item: The item to add
            
        Time Complexity: O(log n)
        """
        self._heap.append(item)
        self._heapify_up(len(self._heap) - 1)
    
    def dequeue(self) -> Any:
        """
        Remove and return the highest priority item.
        
        Returns:
            Any: The highest priority item
            
        Raises:
            QueueEmptyError: If queue is empty
            
        Time Complexity: O(log n)
        """
        if self.is_empty():
            raise QueueEmptyError("Cannot dequeue from empty priority queue")
        
        if len(self._heap) == 1:
            return self._heap.pop()
        
        root = self._heap[0]
        self._heap[0] = self._heap.pop()
        self._heapify_down(0)
        
        return root
    
    def front(self) -> Any:
        """
        Return the highest priority item without removing it.
        
        Returns:
            Any: The highest priority item
            
        Raises:
            QueueEmptyError: If queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise QueueEmptyError("Cannot peek empty priority queue")
        return self._heap[0]
    
    def is_empty(self) -> bool:
        """Check if priority queue is empty."""
        return len(self._heap) == 0
    
    def size(self) -> int:
        """Get size of priority queue."""
        return len(self._heap)
    
    def clear(self) -> None:
        """Clear all items from priority queue."""
        self._heap.clear()
    
    def __len__(self) -> int:
        """Return size of priority queue."""
        return self.size()
    
    def __str__(self) -> str:
        """String representation of priority queue."""
        if self.is_empty():
            return "PriorityQueue: []"
        return f"PriorityQueue: {self._heap}"


# Alias for the most commonly used implementation
Queue = DequeQueue
