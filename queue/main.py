"""
Interactive Queue Demonstration

This module provides an interactive demonstration of queue operations,
allowing users to experiment with different queue implementations and
see real-world applications in action.
"""

from implementation import (
    ListQueue, LinkedQueue, CircularQueue, DequeQueue, 
    PriorityQueue, QueueEmptyError, QueueFullError
)


def display_main_menu():
    """Display the main menu options."""
    print("\n" + "="*60)
    print("QUEUE INTERACTIVE DEMO")
    print("="*60)
    print("1. Basic Queue Operations")
    print("2. Circular Queue Demo")
    print("3. Priority Queue Demo")
    print("4. Task Scheduling Simulation")
    print("5. Breadth-First Search Visualization")
    print("6. Printer Queue System")
    print("7. Performance Comparison")
    print("8. Queue vs Stack Comparison")
    print("9. Exit")
    print("="*60)


def basic_queue_demo():
    """Interactive demo for basic queue operations."""
    print("\n" + "="*50)
    print("BASIC QUEUE OPERATIONS DEMO")
    print("="*50)
    
    # Let user choose implementation
    print("Choose queue implementation:")
    print("1. ListQueue (Python list-based)")
    print("2. LinkedQueue (Linked list-based)")
    print("3. DequeQueue (Collections.deque-based)")
    
    try:
        choice = int(input("\nEnter choice (1-3): "))
        if choice == 1:
            queue = ListQueue()
            queue_name = "ListQueue"
        elif choice == 2:
            queue = LinkedQueue()
            queue_name = "LinkedQueue"
        elif choice == 3:
            queue = DequeQueue()
            queue_name = "DequeQueue"
        else:
            print("Invalid choice, using DequeQueue")
            queue = DequeQueue()
            queue_name = "DequeQueue"
    except ValueError:
        print("Invalid input, using DequeQueue")
        queue = DequeQueue()
        queue_name = "DequeQueue"
    
    print(f"\nUsing {queue_name}")
    
    while True:
        print(f"\nCurrent Queue: {queue}")
        print(f"Size: {queue.size()}, Empty: {queue.is_empty()}")
        
        print("\nOperations:")
        print("1. Enqueue element")
        print("2. Dequeue element")
        print("3. View front element")
        print("4. View rear element")
        print("5. Clear queue")
        print("6. Show as list")
        print("7. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-7): "))
            
            if choice == 1:
                element = input("Enter element to enqueue: ")
                queue.enqueue(element)
                print(f"Enqueued '{element}'")
                
            elif choice == 2:
                try:
                    dequeued = queue.dequeue()
                    print(f"Dequeued: '{dequeued}'")
                except QueueEmptyError as e:
                    print(f"Error: {e}")
                    
            elif choice == 3:
                try:
                    front = queue.front()
                    print(f"Front element: '{front}'")
                except QueueEmptyError as e:
                    print(f"Error: {e}")
                    
            elif choice == 4:
                try:
                    rear = queue.rear()
                    print(f"Rear element: '{rear}'")
                except QueueEmptyError as e:
                    print(f"Error: {e}")
                    
            elif choice == 5:
                queue.clear()
                print("Queue cleared")
                
            elif choice == 6:
                print(f"As list (front to rear): {queue.to_list()}")
                    
            elif choice == 7:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def circular_queue_demo():
    """Interactive demo for circular queue."""
    print("\n" + "="*50)
    print("CIRCULAR QUEUE DEMO")
    print("="*50)
    
    try:
        capacity = int(input("Enter queue capacity (3-10): "))
        if capacity < 3 or capacity > 10:
            capacity = 5
            print(f"Using default capacity: {capacity}")
    except ValueError:
        capacity = 5
        print(f"Invalid input, using default capacity: {capacity}")
    
    cq = CircularQueue(capacity)
    
    while True:
        print(f"\nCurrent Queue: {cq}")
        print(f"Size: {cq.size()}, Empty: {cq.is_empty()}, Full: {cq.is_full()}")
        
        print("\nOperations:")
        print("1. Enqueue element")
        print("2. Dequeue element")
        print("3. View front element")
        print("4. View rear element")
        print("5. Fill queue with sample data")
        print("6. Demonstrate circular behavior")
        print("7. Clear queue")
        print("8. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-8): "))
            
            if choice == 1:
                if cq.is_full():
                    print("Queue is full! Cannot enqueue.")
                else:
                    element = input("Enter element to enqueue: ")
                    cq.enqueue(element)
                    print(f"Enqueued '{element}'")
                    
            elif choice == 2:
                try:
                    dequeued = cq.dequeue()
                    print(f"Dequeued: '{dequeued}'")
                except QueueEmptyError as e:
                    print(f"Error: {e}")
                    
            elif choice == 3:
                try:
                    front = cq.front()
                    print(f"Front element: '{front}'")
                except QueueEmptyError as e:
                    print(f"Error: {e}")
                    
            elif choice == 4:
                try:
                    rear = cq.rear()
                    print(f"Rear element: '{rear}'")
                except QueueEmptyError as e:
                    print(f"Error: {e}")
                    
            elif choice == 5:
                cq.clear()
                print("Filling queue with sample data:")
                for i in range(cq.capacity()):
                    item = f"Item{i+1}"
                    cq.enqueue(item)
                    print(f"Enqueued {item}")
                    
            elif choice == 6:
                print("Demonstrating circular behavior:")
                print("1. Fill the queue")
                cq.clear()
                for i in range(cq.capacity()):
                    cq.enqueue(f"A{i+1}")
                print(f"Full queue: {cq}")
                
                print("2. Dequeue 2 items")
                for _ in range(2):
                    dequeued = cq.dequeue()
                    print(f"Dequeued: {dequeued}")
                
                print("3. Enqueue 2 new items")
                for i in range(2):
                    item = f"B{i+1}"
                    cq.enqueue(item)
                    print(f"Enqueued: {item}")
                
                print(f"Final queue: {cq}")
                print("Notice how the new items wrap around!")
                    
            elif choice == 7:
                cq.clear()
                print("Queue cleared")
                
            elif choice == 8:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def priority_queue_demo():
    """Interactive demo for priority queue."""
    print("\n" + "="*50)
    print("PRIORITY QUEUE DEMO")
    print("="*50)
    
    print("Choose priority order:")
    print("1. Min Priority (lower numbers = higher priority)")
    print("2. Max Priority (higher numbers = higher priority)")
    
    try:
        choice = int(input("\nEnter choice (1-2): "))
        reverse = (choice == 2)
        order_name = "Max" if reverse else "Min"
    except ValueError:
        reverse = False
        order_name = "Min"
        print("Invalid input, using Min Priority")
    
    pq = PriorityQueue(reverse=reverse)
    print(f"Using {order_name} Priority Queue")
    
    while True:
        print(f"\nCurrent Priority Queue: {pq}")
        print(f"Size: {pq.size()}, Empty: {pq.is_empty()}")
        
        print("\nOperations:")
        print("1. Enqueue element")
        print("2. Dequeue highest priority element")
        print("3. View highest priority element")
        print("4. Demo with sample priorities")
        print("5. Clear queue")
        print("6. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-6): "))
            
            if choice == 1:
                try:
                    priority = int(input("Enter priority (integer): "))
                    pq.enqueue(priority)
                    print(f"Enqueued priority {priority}")
                    if not pq.is_empty():
                        print(f"Current highest priority: {pq.front()}")
                except ValueError:
                    print("Please enter a valid integer")
                    
            elif choice == 2:
                try:
                    dequeued = pq.dequeue()
                    print(f"Dequeued highest priority: {dequeued}")
                    if not pq.is_empty():
                        print(f"New highest priority: {pq.front()}")
                except QueueEmptyError as e:
                    print(f"Error: {e}")
                    
            elif choice == 3:
                try:
                    highest = pq.front()
                    print(f"Highest priority element: {highest}")
                except QueueEmptyError as e:
                    print(f"Error: {e}")
                    
            elif choice == 4:
                pq.clear()
                sample_priorities = [30, 10, 40, 20, 50, 15]
                print(f"Adding sample priorities: {sample_priorities}")
                
                for priority in sample_priorities:
                    pq.enqueue(priority)
                    print(f"Added {priority}, Current highest: {pq.front()}")
                
                print(f"\nDequeuing all by priority:")
                while not pq.is_empty():
                    dequeued = pq.dequeue()
                    print(f"Dequeued: {dequeued}")
                    
            elif choice == 5:
                pq.clear()
                print("Priority queue cleared")
                
            elif choice == 6:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def task_scheduling_demo():
    """Interactive demo for task scheduling simulation."""
    print("\n" + "="*50)
    print("TASK SCHEDULING SIMULATION")
    print("="*50)
    
    class Task:
        def __init__(self, task_id, description, priority=0):
            self.task_id = task_id
            self.description = description
            self.priority = priority
        
        def __str__(self):
            return f"Task{self.task_id}: {self.description} (P:{self.priority})"
        
        def __lt__(self, other):
            return self.priority < other.priority
    
    normal_queue = DequeQueue()
    priority_queue = PriorityQueue()
    task_counter = 1
    
    def add_task(description, priority=None):
        nonlocal task_counter
        task = Task(task_counter, description, priority or 5)
        
        if priority is not None and priority <= 2:
            priority_queue.enqueue(task)
            print(f"Added to priority queue: {task}")
        else:
            normal_queue.enqueue(task)
            print(f"Added to normal queue: {task}")
        
        task_counter += 1
    
    def process_next_task():
        if not priority_queue.is_empty():
            task = priority_queue.dequeue()
            print(f"Processing PRIORITY task: {task}")
        elif not normal_queue.is_empty():
            task = normal_queue.dequeue()
            print(f"Processing NORMAL task: {task}")
        else:
            print("No tasks to process")
    
    def show_status():
        print(f"\nQueue Status:")
        print(f"  Priority tasks: {priority_queue.size()}")
        print(f"  Normal tasks: {normal_queue.size()}")
        print(f"  Total tasks: {priority_queue.size() + normal_queue.size()}")
    
    while True:
        show_status()
        
        print("\nTask Scheduler:")
        print("1. Add normal task")
        print("2. Add priority task")
        print("3. Process next task")
        print("4. Process all tasks")
        print("5. Add sample tasks")
        print("6. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-6): "))
            
            if choice == 1:
                description = input("Enter task description: ")
                add_task(description)
                
            elif choice == 2:
                description = input("Enter task description: ")
                try:
                    priority = int(input("Enter priority (0=highest, 1-2=high): "))
                    add_task(description, priority)
                except ValueError:
                    print("Invalid priority, using default")
                    add_task(description, 1)
                    
            elif choice == 3:
                process_next_task()
                
            elif choice == 4:
                print("Processing all tasks:")
                while (not priority_queue.is_empty() or 
                       not normal_queue.is_empty()):
                    process_next_task()
                    
            elif choice == 5:
                sample_tasks = [
                    ("Send email", 5),
                    ("Critical bug fix", 0),
                    ("Update documentation", 4),
                    ("Backup database", 1),
                    ("Team meeting", 3),
                ]
                
                print("Adding sample tasks:")
                for desc, pri in sample_tasks:
                    add_task(desc, pri)
                    
            elif choice == 6:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def bfs_demo():
    """Interactive demo for Breadth-First Search."""
    print("\n" + "="*50)
    print("BREADTH-FIRST SEARCH VISUALIZATION")
    print("="*50)
    
    class GraphNode:
        def __init__(self, value):
            self.value = value
            self.neighbors = []
        
        def add_neighbor(self, neighbor):
            self.neighbors.append(neighbor)
        
        def __str__(self):
            return str(self.value)
    
    def create_sample_graph():
        """Create a sample graph for BFS demonstration."""
        # Create nodes
        nodes = {}
        for i in range(1, 8):
            nodes[i] = GraphNode(i)
        
        # Add connections
        # Graph structure:
        #    1
        #   / \
        #  2   3
        # /|   |\
        #4 5   6 7
        
        nodes[1].add_neighbor(nodes[2])
        nodes[1].add_neighbor(nodes[3])
        nodes[2].add_neighbor(nodes[4])
        nodes[2].add_neighbor(nodes[5])
        nodes[3].add_neighbor(nodes[6])
        nodes[3].add_neighbor(nodes[7])
        
        return nodes
    
    def bfs_search(start_node, target):
        """Perform BFS with step-by-step visualization."""
        queue = DequeQueue()
        visited = set()
        queue.enqueue(start_node)
        
        print(f"Starting BFS from node {start_node.value}")
        print(f"Looking for: {target}")
        
        step = 1
        while not queue.is_empty():
            current = queue.dequeue()
            
            if current.value in visited:
                continue
            
            visited.add(current.value)
            print(f"Step {step}: Visiting node {current.value}")
            
            if current.value == target:
                print(f"✓ Found target {target}!")
                return True
            
            # Add neighbors to queue
            neighbors_added = []
            for neighbor in current.neighbors:
                if neighbor.value not in visited:
                    queue.enqueue(neighbor)
                    neighbors_added.append(neighbor.value)
            
            if neighbors_added:
                print(f"   Added to queue: {neighbors_added}")
            
            queue_contents = [node.value for node in queue.to_list()]
            print(f"   Queue now contains: {queue_contents}")
            print()
            
            step += 1
        
        print(f"✗ Target {target} not found")
        return False
    
    nodes = create_sample_graph()
    
    while True:
        print("\nSample Graph Structure:")
        print("    1")
        print("   / \\")
        print("  2   3")
        print(" /|   |\\")
        print("4 5   6 7")
        
        print("\nBFS Demonstration:")
        print("1. Search for a specific node")
        print("2. Show complete BFS traversal")
        print("3. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-3): "))
            
            if choice == 1:
                try:
                    target = int(input("Enter node to search for (1-7): "))
                    if 1 <= target <= 7:
                        bfs_search(nodes[1], target)
                    else:
                        print("Please enter a number between 1 and 7")
                except ValueError:
                    print("Please enter a valid number")
                    
            elif choice == 2:
                print("Complete BFS traversal from node 1:")
                queue = DequeQueue()
                visited = set()
                queue.enqueue(nodes[1])
                traversal_order = []
                
                while not queue.is_empty():
                    current = queue.dequeue()
                    
                    if current.value in visited:
                        continue
                    
                    visited.add(current.value)
                    traversal_order.append(current.value)
                    
                    for neighbor in current.neighbors:
                        if neighbor.value not in visited:
                            queue.enqueue(neighbor)
                
                print(f"BFS traversal order: {' -> '.join(map(str, traversal_order))}")
                    
            elif choice == 3:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def printer_queue_demo():
    """Interactive demo for printer queue system."""
    print("\n" + "="*50)
    print("PRINTER QUEUE SYSTEM")
    print("="*50)
    
    class PrintJob:
        def __init__(self, job_id, document, pages, user):
            self.job_id = job_id
            self.document = document
            self.pages = pages
            self.user = user
        
        def __str__(self):
            return f"Job{self.job_id}: {self.document} ({self.pages}p) - {self.user}"
    
    queue = DequeQueue()
    job_counter = 1
    
    def add_job(document, pages, user):
        nonlocal job_counter
        job = PrintJob(job_counter, document, pages, user)
        queue.enqueue(job)
        print(f"Added: {job}")
        job_counter += 1
    
    def process_job():
        if queue.is_empty():
            print("No jobs in queue")
            return
        
        job = queue.dequeue()
        print(f"Printing: {job}")
        print(f"Estimated time: {job.pages * 0.5:.1f} minutes")
    
    def show_queue():
        if queue.is_empty():
            print("Print queue is empty")
        else:
            print(f"\nJobs in queue ({queue.size()}):")
            jobs = queue.to_list()
            for i, job in enumerate(jobs, 1):
                print(f"  {i}. {job}")
    
    while True:
        show_queue()
        
        print("\nPrinter Queue Operations:")
        print("1. Add print job")
        print("2. Process next job")
        print("3. Process all jobs")
        print("4. Add sample jobs")
        print("5. Clear queue")
        print("6. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-6): "))
            
            if choice == 1:
                document = input("Enter document name: ")
                try:
                    pages = int(input("Enter number of pages: "))
                    user = input("Enter user name: ")
                    add_job(document, pages, user)
                except ValueError:
                    print("Invalid page number")
                    
            elif choice == 2:
                process_job()
                
            elif choice == 3:
                print("Processing all jobs:")
                while not queue.is_empty():
                    process_job()
                    print()
                    
            elif choice == 4:
                sample_jobs = [
                    ("Report.pdf", 10, "Alice"),
                    ("Presentation.pptx", 25, "Bob"),
                    ("Invoice.doc", 2, "Charlie"),
                    ("Manual.pdf", 50, "Diana"),
                ]
                
                print("Adding sample jobs:")
                for doc, pages, user in sample_jobs:
                    add_job(doc, pages, user)
                    
            elif choice == 5:
                queue.clear()
                print("Queue cleared")
                
            elif choice == 6:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def performance_comparison():
    """Compare performance of different queue implementations."""
    print("\n" + "="*50)
    print("PERFORMANCE COMPARISON")
    print("="*50)
    
    import time
    
    test_sizes = [1000, 5000, 10000]
    implementations = [
        ("ListQueue", ListQueue),
        ("LinkedQueue", LinkedQueue),
        ("DequeQueue", DequeQueue)
    ]
    
    for size in test_sizes:
        print(f"\nTesting with {size} operations:")
        print("-" * 40)
        
        for name, QueueClass in implementations:
            queue = QueueClass()
            
            # Test enqueue operations
            start_time = time.time()
            for i in range(size):
                queue.enqueue(i)
            enqueue_time = time.time() - start_time
            
            # Test dequeue operations
            start_time = time.time()
            for i in range(size):
                queue.dequeue()
            dequeue_time = time.time() - start_time
            
            total_time = enqueue_time + dequeue_time
            
            print(f"{name:12} - Enqueue: {enqueue_time:.6f}s, Dequeue: {dequeue_time:.6f}s, Total: {total_time:.6f}s")


def queue_vs_stack_comparison():
    """Compare queue with stack behavior."""
    print("\n" + "="*50)
    print("QUEUE VS STACK COMPARISON")
    print("="*50)
    
    print("Conceptual Comparison:")
    print("\nQueue (FIFO - First In, First Out):")
    print("- enqueue(item) -> add to rear")
    print("- dequeue()     -> remove from front")
    print("- front()       -> view front item")
    print("- Like a line of people waiting")
    
    print("\nStack (LIFO - Last In, First Out):")
    print("- push(item) -> add to top")
    print("- pop()      -> remove from top")
    print("- peek()     -> view top item")
    print("- Like a stack of plates")
    
    print("\nPractical Demo:")
    
    # Demo with same operations
    queue = DequeQueue()
    stack_simulation = []  # Using list to simulate stack
    
    operations = [10, 20, 30, 40, 50]
    
    print(f"\nAdding elements: {operations}")
    
    for item in operations:
        queue.enqueue(item)
        stack_simulation.append(item)  # Push equivalent
    
    print(f"Queue: {queue}")
    print(f"Stack: {stack_simulation}")
    
    print("\nRemoving elements:")
    print("Queue (FIFO):", end=" ")
    queue_result = []
    while not queue.is_empty():
        queue_result.append(queue.dequeue())
    print(" -> ".join(map(str, queue_result)))
    
    print("Stack (LIFO):", end=" ")
    stack_result = []
    while stack_simulation:
        stack_result.append(stack_simulation.pop())
    print(" -> ".join(map(str, stack_result)))
    
    print("\nKey Differences:")
    print("1. Queue maintains insertion order (FIFO)")
    print("2. Stack reverses insertion order (LIFO)")
    print("3. Queue: fair scheduling, breadth-first processing")
    print("4. Stack: undo operations, depth-first processing")


def main():
    """Main function to run the interactive demo."""
    print("Welcome to the Queue Interactive Learning Tool!")
    print("Explore different queue implementations and their real-world applications.")
    
    while True:
        display_main_menu()
        
        try:
            choice = int(input("\nEnter your choice (1-9): "))
            
            if choice == 1:
                basic_queue_demo()
            elif choice == 2:
                circular_queue_demo()
            elif choice == 3:
                priority_queue_demo()
            elif choice == 4:
                task_scheduling_demo()
            elif choice == 5:
                bfs_demo()
            elif choice == 6:
                printer_queue_demo()
            elif choice == 7:
                performance_comparison()
            elif choice == 8:
                queue_vs_stack_comparison()
            elif choice == 9:
                print("\nThank you for using the Queue Demo!")
                print("Remember: Queues ensure fairness and order! 📋")
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
