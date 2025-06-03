"""
Queue Usage Examples

This module demonstrates practical usage of queue implementations
with real-world scenarios and comprehensive test cases.
"""

from implementation import (
    ListQueue, LinkedQueue, CircularQueue, DequeQueue, 
    PriorityQueue, QueueEmptyError, QueueFullError
)


def test_basic_queue_operations():
    """Test basic operations of different queue implementations."""
    print("=== Testing Basic Queue Operations ===\n")
    
    # Test different implementations
    implementations = [
        ("ListQueue", ListQueue()),
        ("LinkedQueue", LinkedQueue()),
        ("DequeQueue", DequeQueue())
    ]
    
    for name, queue in implementations:
        print(f"--- Testing {name} ---")
        
        # Test empty queue
        print(f"Is empty: {queue.is_empty()}")
        print(f"Size: {queue.size()}")
        
        # Test enqueue operations
        for i in range(1, 6):
            queue.enqueue(i * 10)
            print(f"Enqueued {i * 10}")
        
        print(f"Queue after enqueues: {queue}")
        print(f"Size: {queue.size()}")
        print(f"Front element: {queue.front()}")
        print(f"Rear element: {queue.rear()}")
        
        # Test dequeue operations
        print("\nDequeuing elements:")
        while not queue.is_empty():
            dequeued = queue.dequeue()
            print(f"Dequeued: {dequeued}, Size: {queue.size()}")
        
        print(f"Final queue: {queue}")
        print()


def test_circular_queue():
    """Test circular queue implementation."""
    print("=== Testing Circular Queue ===\n")
    
    # Create a circular queue with capacity 5
    cq = CircularQueue(5)
    
    print(f"Created circular queue with capacity: {cq.capacity()}")
    print(f"Is empty: {cq.is_empty()}")
    print(f"Is full: {cq.is_full()}")
    
    # Fill the queue
    print("\nFilling the queue:")
    for i in range(5):
        cq.enqueue(f"Item{i+1}")
        print(f"Enqueued Item{i+1}, Size: {cq.size()}, Full: {cq.is_full()}")
    
    print(f"Full queue: {cq}")
    
    # Try to enqueue when full
    try:
        cq.enqueue("OverflowItem")
    except QueueFullError as e:
        print(f"Expected error: {e}")
    
    # Dequeue some items and enqueue new ones (circular behavior)
    print("\nDemonstrating circular behavior:")
    for i in range(3):
        dequeued = cq.dequeue()
        print(f"Dequeued: {dequeued}")
        
        new_item = f"NewItem{i+1}"
        cq.enqueue(new_item)
        print(f"Enqueued: {new_item}")
        print(f"Queue: {cq}")


def test_priority_queue():
    """Test priority queue implementation."""
    print("\n=== Testing Priority Queue ===\n")
    
    # Test min-heap (default)
    print("--- Min Priority Queue (lower values = higher priority) ---")
    pq_min = PriorityQueue()
    
    priorities = [30, 10, 40, 20, 50, 15]
    print(f"Enqueueing priorities: {priorities}")
    
    for priority in priorities:
        pq_min.enqueue(priority)
        print(f"Enqueued {priority}, Current highest priority: {pq_min.front()}")
    
    print(f"Priority queue: {pq_min}")
    
    print("\nDequeuing by priority:")
    while not pq_min.is_empty():
        dequeued = pq_min.dequeue()
        print(f"Dequeued: {dequeued}")
    
    # Test max-heap
    print("\n--- Max Priority Queue (higher values = higher priority) ---")
    pq_max = PriorityQueue(reverse=True)
    
    for priority in priorities:
        pq_max.enqueue(priority)
    
    print("Dequeuing by priority (highest first):")
    while not pq_max.is_empty():
        dequeued = pq_max.dequeue()
        print(f"Dequeued: {dequeued}")


def test_error_handling():
    """Test error handling for empty queue operations."""
    print("\n=== Testing Error Handling ===\n")
    
    queue = LinkedQueue()
    
    operations = [
        ("dequeue", lambda: queue.dequeue()),
        ("front", lambda: queue.front()),
        ("rear", lambda: queue.rear())
    ]
    
    for op_name, operation in operations:
        try:
            result = operation()
            print(f"{op_name}: {result}")
        except QueueEmptyError as e:
            print(f"{op_name} error: {e}")


def real_world_example_task_scheduling():
    """
    Demonstrate queue usage in task scheduling.
    This shows how queues can be used for job scheduling and processing.
    """
    print("\n=== Real-World Example: Task Scheduling ===\n")
    
    class Task:
        """Represents a task with ID and description."""
        
        def __init__(self, task_id: int, description: str, priority: int = 0):
            self.task_id = task_id
            self.description = description
            self.priority = priority
        
        def __str__(self):
            return f"Task{self.task_id}: {self.description}"
        
        def __lt__(self, other):
            # For priority queue - lower priority value = higher priority
            return self.priority < other.priority
    
    class TaskScheduler:
        """Simple task scheduler using queues."""
        
        def __init__(self):
            self.normal_queue = DequeQueue()
            self.priority_queue = PriorityQueue()
        
        def add_task(self, task: Task, is_priority: bool = False):
            """Add a task to appropriate queue."""
            if is_priority:
                self.priority_queue.enqueue(task)
                print(f"Added priority task: {task}")
            else:
                self.normal_queue.enqueue(task)
                print(f"Added normal task: {task}")
        
        def process_next_task(self):
            """Process the next task (priority first)."""
            if not self.priority_queue.is_empty():
                task = self.priority_queue.dequeue()
                print(f"Processing priority task: {task}")
                return task
            elif not self.normal_queue.is_empty():
                task = self.normal_queue.dequeue()
                print(f"Processing normal task: {task}")
                return task
            else:
                print("No tasks to process")
                return None
        
        def show_status(self):
            """Show current queue status."""
            print(f"Priority tasks: {self.priority_queue.size()}")
            print(f"Normal tasks: {self.normal_queue.size()}")
    
    # Simulate task scheduling
    scheduler = TaskScheduler()
    
    # Add various tasks
    tasks = [
        Task(1, "Send email to client", 5),
        Task(2, "Backup database", 1),  # High priority (low number)
        Task(3, "Update website", 3),
        Task(4, "Generate report", 4),
        Task(5, "Critical bug fix", 0),  # Highest priority
    ]
    
    # Add tasks to scheduler
    for task in tasks:
        is_priority = task.priority <= 2
        scheduler.add_task(task, is_priority)
    
    print(f"\nScheduler status:")
    scheduler.show_status()
    
    # Process all tasks
    print(f"\nProcessing all tasks:")
    while (not scheduler.priority_queue.is_empty() or 
           not scheduler.normal_queue.is_empty()):
        scheduler.process_next_task()


def real_world_example_breadth_first_search():
    """
    Demonstrate queue usage in Breadth-First Search algorithm.
    """
    print("\n=== Real-World Example: Breadth-First Search ===\n")
    
    class TreeNode:
        """Simple tree node for BFS demonstration."""
        
        def __init__(self, value):
            self.value = value
            self.children = []
        
        def add_child(self, child):
            self.children.append(child)
        
        def __str__(self):
            return str(self.value)
    
    def breadth_first_search(root: TreeNode, target) -> bool:
        """
        Perform BFS to find a target value in the tree.
        
        Args:
            root: Root node of the tree
            target: Value to search for
            
        Returns:
            bool: True if target found, False otherwise
        """
        if not root:
            return False
        
        queue = DequeQueue()
        queue.enqueue(root)
        visited = set()
        
        print(f"Searching for: {target}")
        
        while not queue.is_empty():
            current = queue.dequeue()
            
            if current.value in visited:
                continue
            
            visited.add(current.value)
            print(f"Visiting: {current.value}")
            
            if current.value == target:
                print(f"Found {target}!")
                return True
            
            # Add children to queue
            for child in current.children:
                if child.value not in visited:
                    queue.enqueue(child)
        
        print(f"{target} not found")
        return False
    
    # Create a sample tree
    #       1
    #     / | \
    #    2  3  4
    #   /|     |\
    #  5 6     7 8
    
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    
    root.add_child(node2)
    root.add_child(node3)
    root.add_child(node4)
    node2.add_child(node5)
    node2.add_child(node6)
    node4.add_child(node7)
    node4.add_child(node8)
    
    # Test BFS
    breadth_first_search(root, 7)
    print()
    breadth_first_search(root, 9)


def real_world_example_print_queue():
    """
    Demonstrate queue usage in a printer queue system.
    """
    print("\n=== Real-World Example: Printer Queue ===\n")
    
    class PrintJob:
        """Represents a print job."""
        
        def __init__(self, job_id: int, document: str, pages: int, user: str):
            self.job_id = job_id
            self.document = document
            self.pages = pages
            self.user = user
        
        def __str__(self):
            return f"Job{self.job_id}: {self.document} ({self.pages} pages) - {self.user}"
    
    class PrinterQueue:
        """Printer queue management system."""
        
        def __init__(self):
            self.queue = DequeQueue()
            self.job_counter = 1
        
        def add_print_job(self, document: str, pages: int, user: str):
            """Add a new print job to the queue."""
            job = PrintJob(self.job_counter, document, pages, user)
            self.queue.enqueue(job)
            print(f"Added to queue: {job}")
            self.job_counter += 1
        
        def process_next_job(self):
            """Process the next print job."""
            if self.queue.is_empty():
                print("No jobs in queue")
                return None
            
            job = self.queue.dequeue()
            print(f"Printing: {job}")
            print(f"Estimated time: {job.pages * 0.5:.1f} minutes")
            return job
        
        def show_queue_status(self):
            """Show current queue status."""
            if self.queue.is_empty():
                print("Print queue is empty")
            else:
                print(f"Jobs in queue: {self.queue.size()}")
                jobs = self.queue.to_list()
                for i, job in enumerate(jobs, 1):
                    print(f"  {i}. {job}")
        
        def cancel_job(self, job_id: int):
            """Cancel a specific job (simplified implementation)."""
            # This is a simplified version - in reality, you'd need
            # a more sophisticated data structure for efficient removal
            jobs = self.queue.to_list()
            self.queue.clear()
            
            cancelled = False
            for job in jobs:
                if job.job_id == job_id:
                    print(f"Cancelled: {job}")
                    cancelled = True
                else:
                    self.queue.enqueue(job)
            
            if not cancelled:
                print(f"Job {job_id} not found")
    
    # Simulate printer queue usage
    printer = PrinterQueue()
    
    # Add some print jobs
    jobs_to_add = [
        ("Report.pdf", 10, "Alice"),
        ("Presentation.pptx", 25, "Bob"),
        ("Invoice.doc", 2, "Charlie"),
        ("Manual.pdf", 50, "Diana"),
        ("Letter.txt", 1, "Eve")
    ]
    
    for document, pages, user in jobs_to_add:
        printer.add_print_job(document, pages, user)
    
    print(f"\nCurrent queue status:")
    printer.show_queue_status()
    
    # Process some jobs
    print(f"\nProcessing jobs:")
    for _ in range(3):
        printer.process_next_job()
        print()
    
    print(f"Queue status after processing:")
    printer.show_queue_status()
    
    # Cancel a job
    print(f"\nCancelling job 4:")
    printer.cancel_job(4)
    
    print(f"\nFinal queue status:")
    printer.show_queue_status()


def real_world_example_cpu_scheduling():
    """
    Demonstrate queue usage in CPU process scheduling.
    """
    print("\n=== Real-World Example: CPU Process Scheduling ===\n")
    
    class Process:
        """Represents a CPU process."""
        
        def __init__(self, pid: int, name: str, burst_time: int, priority: int = 0):
            self.pid = pid
            self.name = name
            self.burst_time = burst_time
            self.priority = priority
            self.remaining_time = burst_time
        
        def __str__(self):
            return f"P{self.pid}({self.name})"
        
        def __lt__(self, other):
            # For priority scheduling - lower number = higher priority
            return self.priority < other.priority
    
    class CPUScheduler:
        """Simple CPU scheduler using different queues."""
        
        def __init__(self):
            self.ready_queue = DequeQueue()  # FIFO scheduling
            self.priority_queue = PriorityQueue()  # Priority scheduling
            self.time = 0
        
        def add_process_fifo(self, process: Process):
            """Add process to FIFO ready queue."""
            self.ready_queue.enqueue(process)
            print(f"Added {process} to FIFO queue")
        
        def add_process_priority(self, process: Process):
            """Add process to priority queue."""
            self.priority_queue.enqueue(process)
            print(f"Added {process} to priority queue (priority: {process.priority})")
        
        def schedule_fifo(self):
            """Schedule next process using FIFO."""
            if self.ready_queue.is_empty():
                print("No processes in FIFO queue")
                return None
            
            process = self.ready_queue.dequeue()
            print(f"Scheduling {process} (FIFO) - Burst time: {process.burst_time}")
            self.time += process.burst_time
            return process
        
        def schedule_priority(self):
            """Schedule next process using priority."""
            if self.priority_queue.is_empty():
                print("No processes in priority queue")
                return None
            
            process = self.priority_queue.dequeue()
            print(f"Scheduling {process} (Priority) - Burst time: {process.burst_time}")
            self.time += process.burst_time
            return process
        
        def show_queues(self):
            """Show current queue status."""
            print(f"FIFO queue size: {self.ready_queue.size()}")
            print(f"Priority queue size: {self.priority_queue.size()}")
            print(f"Current time: {self.time}")
    
    # Simulate CPU scheduling
    scheduler = CPUScheduler()
    
    # Create some processes
    processes = [
        Process(1, "TextEditor", 5, 2),
        Process(2, "WebBrowser", 10, 3),
        Process(3, "SystemBackup", 20, 1),  # High priority
        Process(4, "VideoPlayer", 8, 4),
        Process(5, "FileManager", 3, 2),
    ]
    
    # Add processes to both queues for demonstration
    print("Adding processes to queues:")
    for process in processes:
        scheduler.add_process_fifo(Process(process.pid, process.name, process.burst_time, process.priority))
        scheduler.add_process_priority(process)
    
    print(f"\nQueue status:")
    scheduler.show_queues()
    
    # Schedule using FIFO
    print(f"\n--- FIFO Scheduling ---")
    while not scheduler.ready_queue.is_empty():
        scheduler.schedule_fifo()
    
    # Reset time and schedule using priority
    scheduler.time = 0
    print(f"\n--- Priority Scheduling ---")
    while not scheduler.priority_queue.is_empty():
        scheduler.schedule_priority()


def performance_comparison():
    """Compare performance of different queue implementations."""
    print("\n=== Performance Comparison ===\n")
    
    import time
    
    implementations = [
        ("ListQueue", ListQueue),
        ("LinkedQueue", LinkedQueue),
        ("DequeQueue", DequeQueue)
    ]
    
    test_size = 5000
    
    print(f"Performance test with {test_size} operations:")
    
    for name, QueueClass in implementations:
        queue = QueueClass()
        
        # Test enqueue operations
        start_time = time.time()
        for i in range(test_size):
            queue.enqueue(i)
        enqueue_time = time.time() - start_time
        
        # Test dequeue operations
        start_time = time.time()
        for i in range(test_size):
            queue.dequeue()
        dequeue_time = time.time() - start_time
        
        print(f"{name}:")
        print(f"  Enqueue {test_size} items: {enqueue_time:.6f} seconds")
        print(f"  Dequeue {test_size} items: {dequeue_time:.6f} seconds")
        print(f"  Total time: {enqueue_time + dequeue_time:.6f} seconds")
        print()


if __name__ == "__main__":
    test_basic_queue_operations()
    test_circular_queue()
    test_priority_queue()
    test_error_handling()
    real_world_example_task_scheduling()
    real_world_example_breadth_first_search()
    real_world_example_print_queue()
    real_world_example_cpu_scheduling()
    performance_comparison()
