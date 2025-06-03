"""
Interactive Heap Demonstration

This module provides an interactive demonstration of heap operations,
allowing users to experiment with different heap types and priority queues.
"""

from implementation import MinHeap, MaxHeap, PriorityQueue, MedianHeap


def display_main_menu():
    """Display the main menu options."""
    print("\n" + "="*60)
    print("HEAP INTERACTIVE DEMO")
    print("="*60)
    print("1. Min-Heap Operations")
    print("2. Max-Heap Operations")
    print("3. Priority Queue Demo")
    print("4. Median Heap (Running Median)")
    print("5. Heap Sort Demonstration")
    print("6. Task Scheduler Simulation")
    print("7. Performance Analysis")
    print("8. Exit")
    print("="*60)


def min_heap_demo():
    """Interactive demo for min-heap operations."""
    print("\n" + "="*50)
    print("MIN-HEAP OPERATIONS DEMO")
    print("="*50)
    print("Min-heap maintains the smallest element at the root")
    
    min_heap = MinHeap()
    
    while True:
        print(f"\nCurrent Min-Heap: {min_heap}")
        print(f"Size: {min_heap.size()}, Empty: {min_heap.is_empty()}")
        
        if not min_heap.is_empty():
            print(f"Minimum element: {min_heap.peek_min()}")
        
        print("\nOperations:")
        print("1. Insert element")
        print("2. Extract minimum")
        print("3. Peek minimum")
        print("4. Insert multiple elements")
        print("5. Extract all (heap sort)")
        print("6. Clear heap")
        print("7. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-7): "))
            
            if choice == 1:
                try:
                    element = int(input("Enter integer to insert: "))
                    min_heap.insert(element)
                    print(f"Inserted {element}")
                except ValueError:
                    print("Please enter a valid integer")
                    
            elif choice == 2:
                try:
                    minimum = min_heap.extract_min()
                    print(f"Extracted minimum: {minimum}")
                except IndexError as e:
                    print(f"Error: {e}")
                    
            elif choice == 3:
                try:
                    minimum = min_heap.peek_min()
                    print(f"Minimum element: {minimum}")
                except IndexError as e:
                    print(f"Error: {e}")
                    
            elif choice == 4:
                elements_str = input("Enter integers separated by spaces: ")
                try:
                    elements = [int(x.strip()) for x in elements_str.split()]
                    for element in elements:
                        min_heap.insert(element)
                    print(f"Inserted elements: {elements}")
                except ValueError:
                    print("Please enter valid integers separated by spaces")
                    
            elif choice == 5:
                if min_heap.is_empty():
                    print("Heap is empty")
                else:
                    sorted_elements = []
                    print("Extracting all elements in sorted order:")
                    while not min_heap.is_empty():
                        element = min_heap.extract_min()
                        sorted_elements.append(element)
                        print(f"  Extracted: {element}")
                    print(f"Sorted order: {sorted_elements}")
                    
            elif choice == 6:
                min_heap.clear()
                print("Heap cleared")
                
            elif choice == 7:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def max_heap_demo():
    """Interactive demo for max-heap operations."""
    print("\n" + "="*50)
    print("MAX-HEAP OPERATIONS DEMO")
    print("="*50)
    print("Max-heap maintains the largest element at the root")
    
    max_heap = MaxHeap()
    
    while True:
        print(f"\nCurrent Max-Heap: {max_heap}")
        print(f"Size: {max_heap.size()}, Empty: {max_heap.is_empty()}")
        
        if not max_heap.is_empty():
            print(f"Maximum element: {max_heap.peek_max()}")
        
        print("\nOperations:")
        print("1. Insert element")
        print("2. Extract maximum")
        print("3. Peek maximum")
        print("4. Build heap from list")
        print("5. Extract top K elements")
        print("6. Clear heap")
        print("7. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-7): "))
            
            if choice == 1:
                try:
                    element = int(input("Enter integer to insert: "))
                    max_heap.insert(element)
                    print(f"Inserted {element}")
                except ValueError:
                    print("Please enter a valid integer")
                    
            elif choice == 2:
                try:
                    maximum = max_heap.extract_max()
                    print(f"Extracted maximum: {maximum}")
                except IndexError as e:
                    print(f"Error: {e}")
                    
            elif choice == 3:
                try:
                    maximum = max_heap.peek_max()
                    print(f"Maximum element: {maximum}")
                except IndexError as e:
                    print(f"Error: {e}")
                    
            elif choice == 4:
                elements_str = input("Enter integers separated by spaces: ")
                try:
                    elements = [int(x.strip()) for x in elements_str.split()]
                    max_heap = MaxHeap(elements)
                    print(f"Built heap from elements: {elements}")
                    print(f"Heap structure: {max_heap}")
                except ValueError:
                    print("Please enter valid integers separated by spaces")
                    
            elif choice == 5:
                if max_heap.is_empty():
                    print("Heap is empty")
                else:
                    try:
                        k = int(input(f"Enter number of top elements to extract (max {max_heap.size()}): "))
                        if k <= 0:
                            print("Please enter a positive number")
                            continue
                        
                        k = min(k, max_heap.size())
                        top_elements = []
                        
                        print(f"Extracting top {k} elements:")
                        for i in range(k):
                            element = max_heap.extract_max()
                            top_elements.append(element)
                            print(f"  #{i+1}: {element}")
                        
                        print(f"Top {k} elements: {top_elements}")
                    except ValueError:
                        print("Please enter a valid number")
                    
            elif choice == 6:
                max_heap.clear()
                print("Heap cleared")
                
            elif choice == 7:
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
    
    print("Choose priority queue type:")
    print("1. Min-Priority (lower numbers = higher priority)")
    print("2. Max-Priority (higher numbers = higher priority)")
    
    try:
        choice = int(input("\nEnter choice (1-2): "))
        is_max = (choice == 2)
        priority_type = "Max-Priority" if is_max else "Min-Priority"
    except ValueError:
        print("Invalid input, using Min-Priority")
        is_max = False
        priority_type = "Min-Priority"
    
    pq = PriorityQueue(is_max_priority=is_max)
    print(f"Created {priority_type} Queue")
    
    while True:
        print(f"\nCurrent Priority Queue: {pq}")
        print(f"Size: {pq.size()}, Empty: {pq.is_empty()}")
        
        if not pq.is_empty():
            print(f"Next item: {pq.peek()} (priority: {pq.peek_priority()})")
        
        print(f"\nOperations:")
        print("1. Enqueue item with priority")
        print("2. Dequeue highest priority item")
        print("3. Peek next item")
        print("4. Emergency room simulation")
        print("5. Job scheduler simulation")
        print("6. Clear queue")
        print("7. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-7): "))
            
            if choice == 1:
                item = input("Enter item description: ")
                try:
                    priority = float(input("Enter priority value: "))
                    pq.enqueue(item, priority)
                    print(f"Enqueued '{item}' with priority {priority}")
                except ValueError:
                    print("Please enter a valid priority number")
                    
            elif choice == 2:
                try:
                    item = pq.dequeue()
                    print(f"Dequeued: {item}")
                except IndexError as e:
                    print(f"Error: {e}")
                    
            elif choice == 3:
                try:
                    item = pq.peek()
                    priority = pq.peek_priority()
                    print(f"Next item: {item} (priority: {priority})")
                except IndexError as e:
                    print(f"Error: {e}")
                    
            elif choice == 4:
                # Emergency room simulation
                pq.clear()
                pq = PriorityQueue(is_max_priority=False)  # Lower number = higher priority
                
                patients = [
                    ("John Doe", 3),        # Moderate
                    ("Jane Smith", 1),      # Critical
                    ("Bob Johnson", 5),     # Minor
                    ("Alice Brown", 2),     # Serious
                    ("Charlie Wilson", 1),  # Critical
                ]
                
                print("\nEmergency Room Simulation (1=Critical, 5=Minor):")
                for patient, priority in patients:
                    pq.enqueue(patient, priority)
                    print(f"  Patient arrived: {patient} (severity: {priority})")
                
                print(f"\nProcessing patients by severity:")
                while not pq.is_empty():
                    patient = pq.dequeue()
                    print(f"  Treating: {patient}")
                    
            elif choice == 5:
                # Job scheduler simulation
                pq.clear()
                pq = PriorityQueue(is_max_priority=True)  # Higher number = higher priority
                
                jobs = [
                    ("Email notification", 3),
                    ("Database backup", 8),
                    ("System update", 9),
                    ("Log cleanup", 2),
                    ("Security scan", 7),
                ]
                
                print("\nJob Scheduler Simulation (higher number = higher priority):")
                for job, priority in jobs:
                    pq.enqueue(job, priority)
                    print(f"  Job queued: {job} (priority: {priority})")
                
                print(f"\nExecuting jobs by priority:")
                while not pq.is_empty():
                    job = pq.dequeue()
                    print(f"  Executing: {job}")
                    
            elif choice == 6:
                pq.clear()
                print("Priority queue cleared")
                
            elif choice == 7:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def median_heap_demo():
    """Interactive demo for median heap."""
    print("\n" + "="*50)
    print("MEDIAN HEAP DEMO")
    print("="*50)
    print("Efficiently maintains running median using two heaps")
    
    median_heap = MedianHeap()
    
    while True:
        print(f"\nCurrent state: {median_heap}")
        
        print(f"\nOperations:")
        print("1. Add number")
        print("2. Get current median")
        print("3. Add multiple numbers")
        print("4. Stream processing simulation")
        print("5. Clear all numbers")
        print("6. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-6): "))
            
            if choice == 1:
                try:
                    number = float(input("Enter number: "))
                    median_heap.add_number(number)
                    median = median_heap.find_median()
                    print(f"Added {number}, current median: {median}")
                except ValueError:
                    print("Please enter a valid number")
                    
            elif choice == 2:
                try:
                    median = median_heap.find_median()
                    print(f"Current median: {median}")
                except ValueError as e:
                    print(f"Error: {e}")
                    
            elif choice == 3:
                numbers_str = input("Enter numbers separated by spaces: ")
                try:
                    numbers = [float(x.strip()) for x in numbers_str.split()]
                    print("Adding numbers and tracking median:")
                    for number in numbers:
                        median_heap.add_number(number)
                        median = median_heap.find_median()
                        print(f"  Added {number}, median: {median}")
                except ValueError:
                    print("Please enter valid numbers separated by spaces")
                    
            elif choice == 4:
                # Stream processing simulation
                import random
                
                print("Simulating data stream (20 random numbers):")
                for i in range(20):
                    number = random.randint(1, 100)
                    median_heap.add_number(number)
                    median = median_heap.find_median()
                    
                    if i % 5 == 4:  # Print every 5th number
                        print(f"  After {i+1} numbers: median = {median}")
                
                final_median = median_heap.find_median()
                print(f"Final median after 20 numbers: {final_median}")
                
            elif choice == 5:
                median_heap = MedianHeap()
                print("All numbers cleared")
                
            elif choice == 6:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def heap_sort_demo():
    """Interactive demo for heap sort."""
    print("\n" + "="*50)
    print("HEAP SORT DEMONSTRATION")
    print("="*50)
    print("Heap sort: O(n log n) sorting algorithm using heap property")
    
    while True:
        print(f"\nHeap Sort Demo:")
        print("1. Sort user-provided numbers")
        print("2. Sort random numbers")
        print("3. Compare with other sorting")
        print("4. Step-by-step heap sort")
        print("5. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-5): "))
            
            if choice == 1:
                numbers_str = input("Enter numbers to sort (separated by spaces): ")
                try:
                    numbers = [int(x.strip()) for x in numbers_str.split()]
                    print(f"Original numbers: {numbers}")
                    
                    # Use min-heap for ascending sort
                    min_heap = MinHeap(numbers.copy())
                    sorted_asc = min_heap.heap_sort()
                    print(f"Sorted (ascending): {sorted_asc}")
                    
                    # Use max-heap for descending sort
                    max_heap = MaxHeap(numbers.copy())
                    sorted_desc = max_heap.heap_sort()
                    print(f"Sorted (descending): {sorted_desc}")
                    
                except ValueError:
                    print("Please enter valid integers")
                    
            elif choice == 2:
                import random
                size = 15
                numbers = [random.randint(1, 100) for _ in range(size)]
                print(f"Random numbers: {numbers}")
                
                heap = MinHeap(numbers.copy())
                sorted_numbers = heap.heap_sort()
                print(f"Heap sorted: {sorted_numbers}")
                
            elif choice == 3:
                import random
                import time
                
                size = 1000
                numbers = [random.randint(1, 10000) for _ in range(size)]
                
                print(f"Comparing sorting algorithms with {size} numbers:")
                
                # Heap sort
                heap = MinHeap(numbers.copy())
                start_time = time.time()
                heap_sorted = heap.heap_sort()
                heap_time = time.time() - start_time
                
                # Built-in sort
                start_time = time.time()
                builtin_sorted = sorted(numbers)
                builtin_time = time.time() - start_time
                
                print(f"Heap sort time: {heap_time:.6f} seconds")
                print(f"Built-in sort time: {builtin_time:.6f} seconds")
                print(f"Results match: {heap_sorted == builtin_sorted}")
                
            elif choice == 4:
                # Step-by-step heap sort
                numbers_str = input("Enter a small list of numbers (max 8): ")
                try:
                    numbers = [int(x.strip()) for x in numbers_str.split()]
                    if len(numbers) > 8:
                        numbers = numbers[:8]
                        print(f"Using first 8 numbers: {numbers}")
                    
                    print(f"\nStep-by-step heap sort:")
                    print(f"Original: {numbers}")
                    
                    heap = MinHeap()
                    print(f"\nBuilding heap:")
                    for i, num in enumerate(numbers):
                        heap.insert(num)
                        print(f"  Step {i+1}: Insert {num} -> {heap.to_list()}")
                    
                    print(f"\nExtracting in sorted order:")
                    sorted_result = []
                    step = 1
                    while not heap.is_empty():
                        min_val = heap.extract_min()
                        sorted_result.append(min_val)
                        remaining = heap.to_list()
                        print(f"  Step {step}: Extract {min_val} -> remaining: {remaining}")
                        step += 1
                    
                    print(f"\nFinal sorted result: {sorted_result}")
                    
                except ValueError:
                    print("Please enter valid integers")
                    
            elif choice == 5:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def task_scheduler_demo():
    """Interactive demo for task scheduling with priority queue."""
    print("\n" + "="*50)
    print("TASK SCHEDULER SIMULATION")
    print("="*50)
    
    task_queue = PriorityQueue(is_max_priority=True)
    completed_tasks = []
    
    while True:
        print(f"\nTask Scheduler Status:")
        print(f"Tasks in queue: {task_queue.size()}")
        print(f"Completed tasks: {len(completed_tasks)}")
        
        if not task_queue.is_empty():
            print(f"Next task: {task_queue.peek()} (priority: {task_queue.peek_priority()})")
        
        print(f"\nScheduler Operations:")
        print("1. Add new task")
        print("2. Execute next task")
        print("3. Execute all tasks")
        print("4. View queue status")
        print("5. Add sample tasks")
        print("6. Clear all tasks")
        print("7. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-7): "))
            
            if choice == 1:
                task_name = input("Enter task name: ")
                try:
                    priority = int(input("Enter priority (1-10, higher = more important): "))
                    if 1 <= priority <= 10:
                        task_queue.enqueue(task_name, priority)
                        print(f"Added task: {task_name} (priority: {priority})")
                    else:
                        print("Priority must be between 1 and 10")
                except ValueError:
                    print("Please enter a valid priority number")
                    
            elif choice == 2:
                try:
                    task = task_queue.dequeue()
                    completed_tasks.append(task)
                    print(f"Executed task: {task}")
                except IndexError:
                    print("No tasks in queue")
                    
            elif choice == 3:
                if task_queue.is_empty():
                    print("No tasks to execute")
                else:
                    print("Executing all tasks in priority order:")
                    execution_order = []
                    while not task_queue.is_empty():
                        task = task_queue.dequeue()
                        execution_order.append(task)
                        completed_tasks.append(task)
                        print(f"  Executed: {task}")
                    
                    print(f"Execution completed. Order: {execution_order}")
                    
            elif choice == 4:
                print(f"\nQueue details: {task_queue}")
                if completed_tasks:
                    print(f"Completed tasks: {completed_tasks}")
                    
            elif choice == 5:
                sample_tasks = [
                    ("Send weekly report", 6),
                    ("Fix critical bug", 10),
                    ("Update documentation", 3),
                    ("Review code", 7),
                    ("Deploy to production", 9),
                    ("Team meeting", 5),
                    ("Backup database", 8),
                ]
                
                print("Adding sample tasks:")
                for task, priority in sample_tasks:
                    task_queue.enqueue(task, priority)
                    print(f"  Added: {task} (priority: {priority})")
                    
            elif choice == 6:
                task_queue.clear()
                completed_tasks.clear()
                print("All tasks cleared")
                
            elif choice == 7:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def performance_analysis():
    """Performance analysis of heap operations."""
    print("\n" + "="*50)
    print("HEAP PERFORMANCE ANALYSIS")
    print("="*50)
    
    import time
    import random
    
    while True:
        print(f"\nPerformance Analysis:")
        print("1. Insert performance test")
        print("2. Extract performance test")
        print("3. Heap construction comparison")
        print("4. Priority queue vs sorting")
        print("5. Memory usage analysis")
        print("6. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-6): "))
            
            if choice == 1:
                sizes = [1000, 5000, 10000]
                print("\nInsert Performance Test:")
                print(f"{'Size':<8} {'MinHeap':<12} {'MaxHeap':<12} {'PriorityQ':<12}")
                print("-" * 50)
                
                for size in sizes:
                    data = [random.randint(1, 10000) for _ in range(size)]
                    
                    # MinHeap
                    min_heap = MinHeap()
                    start = time.time()
                    for val in data:
                        min_heap.insert(val)
                    min_time = time.time() - start
                    
                    # MaxHeap
                    max_heap = MaxHeap()
                    start = time.time()
                    for val in data:
                        max_heap.insert(val)
                    max_time = time.time() - start
                    
                    # PriorityQueue
                    pq = PriorityQueue()
                    start = time.time()
                    for i, val in enumerate(data):
                        pq.enqueue(f"item{i}", val)
                    pq_time = time.time() - start
                    
                    print(f"{size:<8} {min_time:<12.6f} {max_time:<12.6f} {pq_time:<12.6f}")
                    
            elif choice == 2:
                size = 5000
                data = [random.randint(1, 10000) for _ in range(size)]
                
                print(f"\nExtract Performance Test ({size} elements):")
                
                # Build heaps
                min_heap = MinHeap(data.copy())
                max_heap = MaxHeap(data.copy())
                
                # Test extraction
                start = time.time()
                while not min_heap.is_empty():
                    min_heap.extract_min()
                min_extract_time = time.time() - start
                
                start = time.time()
                while not max_heap.is_empty():
                    max_heap.extract_max()
                max_extract_time = time.time() - start
                
                print(f"MinHeap extract all: {min_extract_time:.6f} seconds")
                print(f"MaxHeap extract all: {max_extract_time:.6f} seconds")
                
            elif choice == 3:
                sizes = [1000, 5000, 10000]
                print("\nHeap Construction Comparison:")
                print(f"{'Size':<8} {'Insert One-by-One':<18} {'Build from Array':<18} {'Speedup':<10}")
                print("-" * 60)
                
                for size in sizes:
                    data = [random.randint(1, 10000) for _ in range(size)]
                    
                    # One-by-one insertion
                    start = time.time()
                    heap1 = MinHeap()
                    for val in data:
                        heap1.insert(val)
                    insert_time = time.time() - start
                    
                    # Build from array
                    start = time.time()
                    heap2 = MinHeap(data)
                    build_time = time.time() - start
                    
                    speedup = insert_time / build_time if build_time > 0 else 0
                    
                    print(f"{size:<8} {insert_time:<18.6f} {build_time:<18.6f} {speedup:<10.2f}x")
                
            elif choice == 4:
                print("\nPriority Queue vs Sorting for Top-K:")
                
                data_size = 10000
                k_values = [10, 50, 100]
                data = [random.randint(1, 100000) for _ in range(data_size)]
                
                print(f"Finding top-K from {data_size} elements:")
                print(f"{'K':<8} {'Heap Method':<15} {'Sort Method':<15} {'Speedup':<10}")
                print("-" * 50)
                
                for k in k_values:
                    # Heap method
                    start = time.time()
                    heap = MinHeap()
                    for val in data:
                        if heap.size() < k:
                            heap.insert(val)
                        elif val > heap.peek_min():
                            heap.extract_min()
                            heap.insert(val)
                    heap_time = time.time() - start
                    
                    # Sort method
                    start = time.time()
                    sorted_data = sorted(data, reverse=True)[:k]
                    sort_time = time.time() - start
                    
                    speedup = sort_time / heap_time if heap_time > 0 else 0
                    
                    print(f"{k:<8} {heap_time:<15.6f} {sort_time:<15.6f} {speedup:<10.2f}x")
                
            elif choice == 5:
                print("\nMemory Usage Analysis:")
                print("Heap implementations are memory efficient:")
                print("- Array-based storage: no pointer overhead")
                print("- Complete binary tree: optimal space utilization")
                print("- No balancing metadata needed")
                print("\nSpace complexity: O(n) for n elements")
                print("Additional space for operations: O(1)")
                
            elif choice == 6:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Main function to run the interactive demo."""
    print("Welcome to the Heap Interactive Learning Tool!")
    print("This demo will help you understand heap data structures and priority queues.")
    
    while True:
        display_main_menu()
        
        try:
            choice = int(input("\nEnter your choice (1-8): "))
            
            if choice == 1:
                min_heap_demo()
            elif choice == 2:
                max_heap_demo()
            elif choice == 3:
                priority_queue_demo()
            elif choice == 4:
                median_heap_demo()
            elif choice == 5:
                heap_sort_demo()
            elif choice == 6:
                task_scheduler_demo()
            elif choice == 7:
                performance_analysis()
            elif choice == 8:
                print("\nThank you for using the Heap Demo!")
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