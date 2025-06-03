"""
Heap Implementation

This module provides comprehensive implementations of heap data structures
including min-heap, max-heap, and priority queue with all essential operations.
"""

from typing import Any, List, Optional, Callable
import heapq


class MinHeap:
    """
    Min-Heap implementation where the smallest element is at the root.
    
    A heap is a complete binary tree that satisfies the heap property:
    - Min-heap: parent <= children
    - Max-heap: parent >= children
    
    Time Complexities:
    - Insert: O(log n)
    - Extract min: O(log n)
    - Peek min: O(1)
    - Build heap: O(n)
    
    Space Complexity: O(n)
    """
    
    def __init__(self, initial_data: List[Any] = None) -> None:
        """
        Initialize heap with optional initial data.
        
        Args:
            initial_data: List of initial elements to heapify
        """
        self._heap: List[Any] = []
        if initial_data:
            self._heap = initial_data.copy()
            self._build_heap()
    
    def _build_heap(self) -> None:
        """Build heap from existing data in O(n) time."""
        n = len(self._heap)
        # Start from last non-leaf node and heapify down
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i)
    
    def _parent(self, index: int) -> int:
        """Get parent index."""
        return (index - 1) // 2
    
    def _left_child(self, index: int) -> int:
        """Get left child index."""
        return 2 * index + 1
    
    def _right_child(self, index: int) -> int:
        """Get right child index."""
        return 2 * index + 2
    
    def _has_left_child(self, index: int) -> bool:
        """Check if node has left child."""
        return self._left_child(index) < len(self._heap)
    
    def _has_right_child(self, index: int) -> bool:
        """Check if node has right child."""
        return self._right_child(index) < len(self._heap)
    
    def _has_parent(self, index: int) -> bool:
        """Check if node has parent."""
        return self._parent(index) >= 0
    
    def _swap(self, i: int, j: int) -> None:
        """Swap elements at two indices."""
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
    
    def _heapify_up(self, index: int) -> None:
        """
        Restore heap property by moving element up.
        Used after insertion.
        """
        while (self._has_parent(index) and 
               self._heap[self._parent(index)] > self._heap[index]):
            parent_index = self._parent(index)
            self._swap(index, parent_index)
            index = parent_index
    
    def _heapify_down(self, index: int) -> None:
        """
        Restore heap property by moving element down.
        Used after extraction.
        """
        while self._has_left_child(index):
            smaller_child_index = self._left_child(index)
            
            # Find smaller of two children
            if (self._has_right_child(index) and 
                self._heap[self._right_child(index)] < self._heap[smaller_child_index]):
                smaller_child_index = self._right_child(index)
            
            # If heap property is satisfied, stop
            if self._heap[index] <= self._heap[smaller_child_index]:
                break
            
            self._swap(index, smaller_child_index)
            index = smaller_child_index
    
    def insert(self, item: Any) -> None:
        """
        Insert an item into the heap.
        
        Args:
            item: The item to insert
            
        Time Complexity: O(log n)
        """
        self._heap.append(item)
        self._heapify_up(len(self._heap) - 1)
    
    def extract_min(self) -> Any:
        """
        Remove and return the minimum element.
        
        Returns:
            Any: The minimum element
            
        Raises:
            IndexError: If heap is empty
            
        Time Complexity: O(log n)
        """
        if self.is_empty():
            raise IndexError("Cannot extract from empty heap")
        
        if len(self._heap) == 1:
            return self._heap.pop()
        
        # Store the minimum element
        min_item = self._heap[0]
        
        # Move last element to root and remove last
        self._heap[0] = self._heap.pop()
        
        # Restore heap property
        self._heapify_down(0)
        
        return min_item
    
    def peek_min(self) -> Any:
        """
        Return the minimum element without removing it.
        
        Returns:
            Any: The minimum element
            
        Raises:
            IndexError: If heap is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot peek empty heap")
        return self._heap[0]
    
    def size(self) -> int:
        """
        Get the number of elements in the heap.
        
        Returns:
            int: Number of elements
            
        Time Complexity: O(1)
        """
        return len(self._heap)
    
    def is_empty(self) -> bool:
        """
        Check if heap is empty.
        
        Returns:
            bool: True if empty, False otherwise
            
        Time Complexity: O(1)
        """
        return len(self._heap) == 0
    
    def clear(self) -> None:
        """
        Remove all elements from the heap.
        
        Time Complexity: O(1)
        """
        self._heap.clear()
    
    def to_list(self) -> List[Any]:
        """
        Convert heap to list (not sorted).
        
        Returns:
            List[Any]: List representation of heap
            
        Time Complexity: O(n)
        """
        return self._heap.copy()
    
    def heap_sort(self) -> List[Any]:
        """
        Return sorted list using heap sort algorithm.
        Note: This modifies the heap.
        
        Returns:
            List[Any]: Sorted list in ascending order
            
        Time Complexity: O(n log n)
        """
        sorted_list = []
        while not self.is_empty():
            sorted_list.append(self.extract_min())
        return sorted_list
    
    def __len__(self) -> int:
        """Return size of heap."""
        return self.size()
    
    def __str__(self) -> str:
        """String representation of heap."""
        if self.is_empty():
            return "MinHeap: []"
        return f"MinHeap: {self._heap}"


class MaxHeap:
    """
    Max-Heap implementation where the largest element is at the root.
    
    Similar to MinHeap but maintains max-heap property.
    """
    
    def __init__(self, initial_data: List[Any] = None) -> None:
        """Initialize max-heap with optional initial data."""
        self._heap: List[Any] = []
        if initial_data:
            self._heap = initial_data.copy()
            self._build_heap()
    
    def _build_heap(self) -> None:
        """Build heap from existing data in O(n) time."""
        n = len(self._heap)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify_down(i)
    
    def _parent(self, index: int) -> int:
        """Get parent index."""
        return (index - 1) // 2
    
    def _left_child(self, index: int) -> int:
        """Get left child index."""
        return 2 * index + 1
    
    def _right_child(self, index: int) -> int:
        """Get right child index."""
        return 2 * index + 2
    
    def _has_left_child(self, index: int) -> bool:
        """Check if node has left child."""
        return self._left_child(index) < len(self._heap)
    
    def _has_right_child(self, index: int) -> bool:
        """Check if node has right child."""
        return self._right_child(index) < len(self._heap)
    
    def _has_parent(self, index: int) -> bool:
        """Check if node has parent."""
        return self._parent(index) >= 0
    
    def _swap(self, i: int, j: int) -> None:
        """Swap elements at two indices."""
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
    
    def _heapify_up(self, index: int) -> None:
        """Restore heap property by moving element up."""
        while (self._has_parent(index) and 
               self._heap[self._parent(index)] < self._heap[index]):
            parent_index = self._parent(index)
            self._swap(index, parent_index)
            index = parent_index
    
    def _heapify_down(self, index: int) -> None:
        """Restore heap property by moving element down."""
        while self._has_left_child(index):
            larger_child_index = self._left_child(index)
            
            # Find larger of two children
            if (self._has_right_child(index) and 
                self._heap[self._right_child(index)] > self._heap[larger_child_index]):
                larger_child_index = self._right_child(index)
            
            # If heap property is satisfied, stop
            if self._heap[index] >= self._heap[larger_child_index]:
                break
            
            self._swap(index, larger_child_index)
            index = larger_child_index
    
    def insert(self, item: Any) -> None:
        """Insert an item into the heap."""
        self._heap.append(item)
        self._heapify_up(len(self._heap) - 1)
    
    def extract_max(self) -> Any:
        """Remove and return the maximum element."""
        if self.is_empty():
            raise IndexError("Cannot extract from empty heap")
        
        if len(self._heap) == 1:
            return self._heap.pop()
        
        max_item = self._heap[0]
        self._heap[0] = self._heap.pop()
        self._heapify_down(0)
        
        return max_item
    
    def peek_max(self) -> Any:
        """Return the maximum element without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek empty heap")
        return self._heap[0]
    
    def size(self) -> int:
        """Get the number of elements in the heap."""
        return len(self._heap)
    
    def is_empty(self) -> bool:
        """Check if heap is empty."""
        return len(self._heap) == 0
    
    def clear(self) -> None:
        """Remove all elements from the heap."""
        self._heap.clear()
    
    def to_list(self) -> List[Any]:
        """Convert heap to list (not sorted)."""
        return self._heap.copy()
    
    def heap_sort(self) -> List[Any]:
        """Return sorted list in descending order."""
        sorted_list = []
        while not self.is_empty():
            sorted_list.append(self.extract_max())
        return sorted_list
    
    def __len__(self) -> int:
        """Return size of heap."""
        return self.size()
    
    def __str__(self) -> str:
        """String representation of heap."""
        if self.is_empty():
            return "MaxHeap: []"
        return f"MaxHeap: {self._heap}"


class PriorityQueue:
    """
    Priority Queue implementation using heap.
    
    Items with higher priority are served first.
    Can be configured as min-priority or max-priority queue.
    """
    
    def __init__(self, is_max_priority: bool = False) -> None:
        """
        Initialize priority queue.
        
        Args:
            is_max_priority: If True, higher values have higher priority
                           If False, lower values have higher priority
        """
        self._is_max_priority = is_max_priority
        self._heap: List[tuple] = []
        self._entry_count = 0  # For handling equal priorities
    
    def enqueue(self, item: Any, priority: float) -> None:
        """
        Add an item with given priority.
        
        Args:
            item: The item to add
            priority: Priority value
            
        Time Complexity: O(log n)
        """
        # Use negative priority for max-priority queue (since heapq is min-heap)
        heap_priority = -priority if self._is_max_priority else priority
        
        # Include entry count to handle equal priorities (FIFO for equal priorities)
        entry = (heap_priority, self._entry_count, item)
        heapq.heappush(self._heap, entry)
        self._entry_count += 1
    
    def dequeue(self) -> Any:
        """
        Remove and return the highest priority item.
        
        Returns:
            Any: The highest priority item
            
        Raises:
            IndexError: If queue is empty
            
        Time Complexity: O(log n)
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from empty priority queue")
        
        _, _, item = heapq.heappop(self._heap)
        return item
    
    def peek(self) -> Any:
        """
        Return the highest priority item without removing it.
        
        Returns:
            Any: The highest priority item
            
        Raises:
            IndexError: If queue is empty
            
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot peek empty priority queue")
        
        _, _, item = self._heap[0]
        return item
    
    def peek_priority(self) -> float:
        """
        Return the priority of the highest priority item.
        
        Returns:
            float: The highest priority value
            
        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Cannot peek empty priority queue")
        
        priority, _, _ = self._heap[0]
        return -priority if self._is_max_priority else priority
    
    def size(self) -> int:
        """Get the number of items in the queue."""
        return len(self._heap)
    
    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return len(self._heap) == 0
    
    def clear(self) -> None:
        """Remove all items from the queue."""
        self._heap.clear()
        self._entry_count = 0
    
    def update_priority(self, item: Any, new_priority: float) -> bool:
        """
        Update priority of an existing item.
        Note: This is O(n) operation as it requires finding the item.
        
        Args:
            item: The item to update
            new_priority: New priority value
            
        Returns:
            bool: True if item was found and updated, False otherwise
        """
        # Find and remove the item
        for i, (priority, count, heap_item) in enumerate(self._heap):
            if heap_item == item:
                # Remove the item
                self._heap[i] = self._heap[-1]
                self._heap.pop()
                heapq.heapify(self._heap)
                
                # Re-add with new priority
                self.enqueue(item, new_priority)
                return True
        
        return False
    
    def __len__(self) -> int:
        """Return size of queue."""
        return self.size()
    
    def __str__(self) -> str:
        """String representation of priority queue."""
        if self.is_empty():
            return "PriorityQueue: []"
        
        items = []
        for priority, _, item in self._heap:
            actual_priority = -priority if self._is_max_priority else priority
            items.append(f"({item}, {actual_priority})")
        
        queue_type = "Max" if self._is_max_priority else "Min"
        return f"{queue_type}PriorityQueue: [{', '.join(items)}]"


class MedianHeap:
    """
    Data structure to efficiently find median using two heaps.
    
    Uses a max-heap for the smaller half and min-heap for the larger half.
    Maintains the property that the size difference is at most 1.
    """
    
    def __init__(self) -> None:
        """Initialize median heap with two internal heaps."""
        self._max_heap = MaxHeap()  # Smaller half
        self._min_heap = MinHeap()  # Larger half
    
    def add_number(self, num: float) -> None:
        """
        Add a number to the data structure.
        
        Args:
            num: Number to add
            
        Time Complexity: O(log n)
        """
        # If max_heap is empty or num is smaller than max of smaller half
        if self._max_heap.is_empty() or num <= self._max_heap.peek_max():
            self._max_heap.insert(num)
        else:
            self._min_heap.insert(num)
        
        # Balance the heaps
        self._balance_heaps()
    
    def _balance_heaps(self) -> None:
        """Balance the two heaps to maintain median property."""
        # If max_heap has more than one extra element
        if self._max_heap.size() > self._min_heap.size() + 1:
            self._min_heap.insert(self._max_heap.extract_max())
        
        # If min_heap has more elements than max_heap
        elif self._min_heap.size() > self._max_heap.size():
            self._max_heap.insert(self._min_heap.extract_min())
    
    def find_median(self) -> float:
        """
        Find the median of all numbers added so far.
        
        Returns:
            float: The median value
            
        Raises:
            ValueError: If no numbers have been added
            
        Time Complexity: O(1)
        """
        if self._max_heap.is_empty() and self._min_heap.is_empty():
            raise ValueError("No numbers added yet")
        
        # If odd number of elements, median is top of max_heap
        if self._max_heap.size() > self._min_heap.size():
            return self._max_heap.peek_max()
        
        # If even number of elements, median is average of both tops
        return (self._max_heap.peek_max() + self._min_heap.peek_min()) / 2
    
    def size(self) -> int:
        """Get total number of elements."""
        return self._max_heap.size() + self._min_heap.size()
    
    def is_empty(self) -> bool:
        """Check if no numbers have been added."""
        return self._max_heap.is_empty() and self._min_heap.is_empty()
    
    def __str__(self) -> str:
        """String representation of median heap."""
        if self.is_empty():
            return "MedianHeap: [] (median: N/A)"
        
        try:
            median = self.find_median()
            return f"MedianHeap: size={self.size()}, median={median}"
        except ValueError:
            return "MedianHeap: [] (median: N/A)"


# Utility functions using Python's heapq

def heap_merge(*iterables) -> List[Any]:
    """
    Merge multiple sorted iterables using heap.
    
    Args:
        *iterables: Multiple sorted iterables
        
    Returns:
        List[Any]: Merged sorted list
        
    Time Complexity: O(n log k) where n is total elements and k is number of iterables
    """
    return list(heapq.merge(*iterables))


def k_largest(k: int, iterable) -> List[Any]:
    """
    Find k largest elements from iterable.
    
    Args:
        k: Number of largest elements to find
        iterable: Input iterable
        
    Returns:
        List[Any]: k largest elements in descending order
        
    Time Complexity: O(n log k)
    """
    return heapq.nlargest(k, iterable)


def k_smallest(k: int, iterable) -> List[Any]:
    """
    Find k smallest elements from iterable.
    
    Args:
        k: Number of smallest elements to find
        iterable: Input iterable
        
    Returns:
        List[Any]: k smallest elements in ascending order
        
    Time Complexity: O(n log k)
    """
    return heapq.nsmallest(k, iterable)


# Aliases for common usage
Heap = MinHeap  # Default to min-heap