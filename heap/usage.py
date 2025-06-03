"""
Heap Usage Examples

This module demonstrates practical usage of heap implementations
with real-world scenarios and comprehensive test cases.
"""

from implementation import MinHeap, MaxHeap, PriorityQueue, MedianHeap, k_largest, k_smallest


def test_min_heap_operations():
    """Test basic operations of min-heap."""
    print("=== Testing Min-Heap Operations ===\n")
    
    # Create min-heap
    min_heap = MinHeap()
    print(f"Created empty min-heap: {min_heap}")
    print(f"Is empty: {min_heap.is_empty()}")
    
    # Insert elements
    elements = [15, 10, 20, 8, 25, 5, 12]
    print(f"\nInserting elements: {elements}")
    
    for element in elements:
        min_heap.insert(element)
        print(f"Inserted {element}, min is now: {min_heap.peek_min()}")
    
    print(f"\nHeap after insertions: {min_heap}")
    print(f"Size: {min_heap.size()}")
    
    # Extract minimum elements
    print(f"\nExtracting elements in sorted order:")
    extracted = []
    while not min_heap.is_empty():
        min_element = min_heap.extract_min()
        extracted.append(min_element)
        remaining = min_heap.size()
        next_min = min_heap.peek_min() if not min_heap.is_empty() else "N/A"
        print(f"Extracted: {min_element}, remaining: {remaining}, next min: {next_min}")
    
    print(f"Extracted in order: {extracted}")
    print(f"Original unsorted: {elements}")
    print(f"Heap sort result: {sorted(elements)}")


def test_max_heap_operations():
    """Test basic operations of max-heap."""
    print("\n=== Testing Max-Heap Operations ===\n")
    
    # Create max-heap with initial data
    initial_data = [15, 10, 20, 8, 25, 5, 12]
    max_heap = MaxHeap(initial_data)
    print(f"Created max-heap with initial data: {initial_data}")
    print(f"Max-heap: {max_heap}")
    print(f"Maximum element: {max_heap.peek_max()}")
    
    # Insert more elements
    new_elements = [30, 3, 18]
    print(f"\nInserting additional elements: {new_elements}")
    
    for element in new_elements:
        max_heap.insert(element)
        print(f"Inserted {element}, max is now: {max_heap.peek_max()}")
    
    # Extract maximum elements
    print(f"\nExtracting top 5 largest elements:")
    for i in range(5):
        if not max_heap.is_empty():
            max_element = max_heap.extract_max()
            print(f"#{i+1} largest: {max_element}")
    
    print(f"\nRemaining heap: {max_heap}")


def test_priority_queue_operations():
    """Test priority queue with different priority schemes."""
    print("\n=== Testing Priority Queue Operations ===\n")
    
    # Test min-priority queue (lower number = higher priority)
    print("--- Min-Priority Queue (Emergency Room Triage) ---")
    emergency_queue = PriorityQueue(is_max_priority=False)
    
    # Add patients with priority levels (1=critical, 5=minor)
    patients = [
        ("Alice", 3),      # Moderate
        ("Bob", 1),        # Critical
        ("Charlie", 5),    # Minor
        ("Diana", 2),      # Serious
        ("Eve", 1),        # Critical
        ("Frank", 4)       # Low priority
    ]
    
    print("Adding patients to emergency queue:")
    for patient, priority in patients:
        emergency_queue.enqueue(patient, priority)
        print(f"Added {patient} (priority {priority})")
    
    print(f"\nQueue state: {emergency_queue}")
    print(f"Next patient: {emergency_queue.peek()} (priority: {emergency_queue.peek_priority()})")
    
    print(f"\nProcessing patients in priority order:")
    while not emergency_queue.is_empty():
        patient = emergency_queue.dequeue()
        print(f"Treating: {patient}")
    
    # Test max-priority queue (higher number = higher priority)
    print("\n--- Max-Priority Queue (Job Scheduling) ---")
    job_queue = PriorityQueue(is_max_priority=True)
    
    jobs = [
        ("Backup Database", 7),
        ("Send Email", 3),
        ("Critical Bug Fix", 10),
        ("Update Documentation", 2),
        ("Security Patch", 9),
        ("UI Enhancement", 4)
    ]
    
    print("Adding jobs to scheduler:")
    for job, priority in jobs:
        job_queue.enqueue(job, priority)
        print(f"Added '{job}' (priority {priority})")
    
    print(f"\nProcessing jobs by priority:")
    while not job_queue.is_empty():
        job = job_queue.dequeue()
        print(f"Executing: {job}")


def test_median_heap():
    """Test median finding using dual heap approach."""
    print("\n=== Testing Median Heap ===\n")
    
    median_heap = MedianHeap()
    
    # Stream of numbers
    numbers = [5, 15, 1, 3, 8, 7, 9, 2, 6, 4]
    
    print("Adding numbers and tracking median:")
    for num in numbers:
        median_heap.add_number(num)
        median = median_heap.find_median()
        print(f"Added {num}, current median: {median}")
    
    print(f"\nFinal state: {median_heap}")
    
    # Test with larger dataset
    print(f"\nTesting with larger dataset:")
    large_median_heap = MedianHeap()
    import random
    
    large_numbers = [random.randint(1, 100) for _ in range(20)]
    for i, num in enumerate(large_numbers):
        large_median_heap.add_number(num)
        if i % 5 == 4:  # Print every 5th addition
            median = large_median_heap.find_median()
            print(f"After {i+1} numbers, median: {median}")
    
    # Verify with sorted approach
    sorted_numbers = sorted(large_numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        expected_median = sorted_numbers[n // 2]
    else:
        expected_median = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    
    actual_median = large_median_heap.find_median()
    print(f"Expected median: {expected_median}")
    print(f"Calculated median: {actual_median}")
    print(f"Median calculation correct: {abs(expected_median - actual_median) < 1e-10}")


def real_world_example_task_scheduler():
    """
    Demonstrate heap usage in operating system task scheduling.
    """
    print("\n=== Real-World Example: OS Task Scheduler ===\n")
    
    class Task:
        """Represents a system task with various properties."""
        
        def __init__(self, name: str, cpu_time: int, priority: int, arrival_time: int):
            self.name = name
            self.cpu_time = cpu_time
            self.priority = priority
            self.arrival_time = arrival_time
            self.remaining_time = cpu_time
        
        def __str__(self):
            return f"{self.name}(CPU:{self.cpu_time}, P:{self.priority})"
    
    class TaskScheduler:
        """Priority-based task scheduler using heap."""
        
        def __init__(self):
            self.ready_queue = PriorityQueue(is_max_priority=True)
            self.completed_tasks = []
            self.current_time = 0
        
        def add_task(self, task: Task):
            """Add task to ready queue."""
            self.ready_queue.enqueue(task, task.priority)
            print(f"Added task: {task}")
        
        def execute_next_task(self, time_slice: int = 5):
            """Execute the highest priority task for given time slice."""
            if self.ready_queue.is_empty():
                print("No tasks in queue")
                return None
            
            task = self.ready_queue.dequeue()
            execution_time = min(time_slice, task.remaining_time)
            
            print(f"Executing {task.name} for {execution_time} time units")
            
            task.remaining_time -= execution_time
            self.current_time += execution_time
            
            if task.remaining_time > 0:
                # Task not completed, put back in queue
                self.ready_queue.enqueue(task, task.priority)
                print(f"  {task.name} preempted, {task.remaining_time} time units remaining")
            else:
                # Task completed
                self.completed_tasks.append(task)
                print(f"  {task.name} completed!")
            
            return task
        
        def run_scheduler(self):
            """Run scheduler until all tasks complete."""
            print(f"\nRunning scheduler (round-robin with priority):")
            
            while not self.ready_queue.is_empty():
                self.execute_next_task()
            
            print(f"\nAll tasks completed at time {self.current_time}")
            print(f"Completion order: {[task.name for task in self.completed_tasks]}")
    
    # Create scheduler and add tasks
    scheduler = TaskScheduler()
    
    tasks = [
        Task("System Update", 15, 8, 0),
        Task("User Program", 10, 5, 1),
        Task("Background Sync", 20, 3, 2),
        Task("Critical Process", 8, 10, 3),
        Task("Maintenance", 12, 2, 4)
    ]
    
    for task in tasks:
        scheduler.add_task(task)
    
    scheduler.run_scheduler()


def real_world_example_network_routing():
    """
    Demonstrate heap usage in network packet routing with QoS.
    """
    print("\n=== Real-World Example: Network Packet Routing ===\n")
    
    class Packet:
        """Represents a network packet with QoS properties."""
        
        def __init__(self, packet_id: str, source: str, destination: str, 
                     packet_type: str, size: int, qos_priority: int):
            self.packet_id = packet_id
            self.source = source
            self.destination = destination
            self.packet_type = packet_type
            self.size = size
            self.qos_priority = qos_priority
            self.timestamp = None
        
        def __str__(self):
            return f"Packet({self.packet_id}, {self.packet_type}, QoS:{self.qos_priority})"
    
    class NetworkRouter:
        """Network router with QoS-based packet prioritization."""
        
        def __init__(self, router_name: str):
            self.router_name = router_name
            self.packet_queue = PriorityQueue(is_max_priority=True)
            self.bandwidth_limit = 1000  # packets per second
            self.processed_packets = []
        
        def receive_packet(self, packet: Packet):
            """Receive and queue packet based on QoS priority."""
            self.packet_queue.enqueue(packet, packet.qos_priority)
            print(f"{self.router_name} received: {packet}")
        
        def process_packets(self, duration: int):
            """Process packets for given duration."""
            print(f"\n{self.router_name} processing packets for {duration} seconds:")
            
            packets_processed = 0
            max_packets = self.bandwidth_limit * duration
            
            while not self.packet_queue.is_empty() and packets_processed < max_packets:
                packet = self.packet_queue.dequeue()
                self.processed_packets.append(packet)
                packets_processed += 1
                print(f"  Forwarded: {packet}")
            
            print(f"Processed {packets_processed} packets")
            
            if not self.packet_queue.is_empty():
                remaining = self.packet_queue.size()
                next_priority = self.packet_queue.peek_priority()
                print(f"Queue: {remaining} packets remaining, next priority: {next_priority}")
        
        def get_queue_stats(self):
            """Get queue statistics by priority."""
            if self.packet_queue.is_empty():
                return "Queue is empty"
            
            # This is a simplified view - in practice you'd maintain separate counters
            return f"Packets in queue: {self.packet_queue.size()}"
    
    # Simulate network traffic
    router = NetworkRouter("Router-A")
    
    # Different types of network traffic with QoS priorities
    packets = [
        # Voice/Video calls (highest priority: 7-8)
        Packet("P001", "192.168.1.10", "192.168.2.20", "VoIP", 160, 8),
        Packet("P002", "192.168.1.11", "192.168.2.21", "Video", 1500, 7),
        
        # Business applications (medium-high priority: 5-6)
        Packet("P003", "192.168.1.12", "192.168.2.22", "Database", 1024, 6),
        Packet("P004", "192.168.1.13", "192.168.2.23", "Email", 512, 5),
        
        # Web browsing (medium priority: 3-4)
        Packet("P005", "192.168.1.14", "192.168.2.24", "HTTP", 1024, 4),
        Packet("P006", "192.168.1.15", "192.168.2.25", "HTTPS", 1024, 4),
        
        # File transfers (low priority: 1-2)
        Packet("P007", "192.168.1.16", "192.168.2.26", "FTP", 4096, 2),
        Packet("P008", "192.168.1.17", "192.168.2.27", "Backup", 8192, 1),
        
        # More real-time traffic
        Packet("P009", "192.168.1.18", "192.168.2.28", "VoIP", 160, 8),
        Packet("P010", "192.168.1.19", "192.168.2.29", "Gaming", 64, 6),
    ]
    
    # Receive packets in mixed order
    import random
    shuffled_packets = packets.copy()
    random.shuffle(shuffled_packets)
    
    print("Receiving packets in random order:")
    for packet in shuffled_packets:
        router.receive_packet(packet)
    
    print(f"\n{router.get_queue_stats()}")
    
    # Process packets - note how high priority packets go first
    router.process_packets(1)


def real_world_example_data_stream_processing():
    """
    Demonstrate heap usage in processing streaming data.
    """
    print("\n=== Real-World Example: Real-Time Data Processing ===\n")
    
    class DataStreamProcessor:
        """Process streaming data with different analysis requirements."""
        
        def __init__(self):
            self.top_values_heap = MaxHeap()  # Track top N values
            self.bottom_values_heap = MinHeap()  # Track bottom N values
            self.median_tracker = MedianHeap()  # Track running median
            self.data_count = 0
            self.top_n = 5
        
        def process_data_point(self, value: float, source: str):
            """Process a single data point from stream."""
            self.data_count += 1
            
            # Update median tracker
            self.median_tracker.add_number(value)
            
            # Update top N values (keep only top N)
            self.top_values_heap.insert(value)
            if self.top_values_heap.size() > self.top_n:
                # Remove smallest from top N
                temp_values = []
                while self.top_values_heap.size() > 0:
                    temp_values.append(self.top_values_heap.extract_max())
                
                # Keep only top N
                for val in temp_values[:self.top_n]:
                    self.top_values_heap.insert(val)
            
            # Update bottom N values (keep only bottom N)
            self.bottom_values_heap.insert(value)
            if self.bottom_values_heap.size() > self.top_n:
                # Remove largest from bottom N
                temp_values = []
                while self.bottom_values_heap.size() > 0:
                    temp_values.append(self.bottom_values_heap.extract_min())
                
                # Keep only bottom N
                for val in temp_values[:self.top_n]:
                    self.bottom_values_heap.insert(val)
            
            # Print periodic updates
            if self.data_count % 10 == 0:
                self.print_analysis()
        
        def print_analysis(self):
            """Print current analysis of the data stream."""
            print(f"\n--- Stream Analysis (after {self.data_count} data points) ---")
            
            # Current median
            median = self.median_tracker.find_median()
            print(f"Current median: {median:.2f}")
            
            # Top values
            top_values = self.top_values_heap.heap_sort()[::-1]  # Descending order
            self.top_values_heap = MaxHeap(top_values)  # Rebuild heap
            print(f"Top {len(top_values)} values: {top_values}")
            
            # Bottom values
            bottom_values = self.bottom_values_heap.heap_sort()
            self.bottom_values_heap = MinHeap(bottom_values)  # Rebuild heap
            print(f"Bottom {len(bottom_values)} values: {bottom_values}")
    
    # Simulate data stream processing
    processor = DataStreamProcessor()
    
    # Simulate sensor data from different sources
    import random
    import time
    
    sources = ["Temperature", "Humidity", "Pressure", "Light"]
    
    print("Processing streaming sensor data...")
    
    for i in range(50):
        # Generate random sensor reading
        if random.choice(sources) == "Temperature":
            value = random.uniform(15, 35)  # Temperature in Celsius
        elif random.choice(sources) == "Humidity":
            value = random.uniform(30, 90)  # Humidity percentage
        elif random.choice(sources) == "Pressure":
            value = random.uniform(980, 1020)  # Pressure in hPa
        else:  # Light
            value = random.uniform(0, 1000)  # Light in lux
        
        source = random.choice(sources)
        processor.process_data_point(value, source)
        
        # Small delay to simulate real-time processing
        if i % 20 == 19:
            time.sleep(0.1)
    
    # Final analysis
    processor.print_analysis()


def performance_comparison():
    """Compare performance of heap operations."""
    print("\n=== Performance Comparison ===\n")
    
    import time
    import random
    
    # Test different heap sizes
    sizes = [1000, 5000, 10000]
    
    for size in sizes:
        print(f"Testing with {size} elements:")
        
        # Generate random data
        data = [random.randint(1, 10000) for _ in range(size)]
        
        # Test MinHeap
        min_heap = MinHeap()
        start_time = time.time()
        for value in data:
            min_heap.insert(value)
        insert_time = time.time() - start_time
        
        start_time = time.time()
        sorted_data = []
        while not min_heap.is_empty():
            sorted_data.append(min_heap.extract_min())
        extract_time = time.time() - start_time
        
        print(f"  MinHeap - Insert: {insert_time:.4f}s, Extract all: {extract_time:.4f}s")
        
        # Test PriorityQueue
        pq = PriorityQueue()
        start_time = time.time()
        for i, value in enumerate(data):
            pq.enqueue(f"item_{i}", value)
        pq_insert_time = time.time() - start_time
        
        start_time = time.time()
        while not pq.is_empty():
            pq.dequeue()
        pq_extract_time = time.time() - start_time
        
        print(f"  PriorityQueue - Insert: {pq_insert_time:.4f}s, Extract all: {pq_extract_time:.4f}s")
        
        # Test k_largest and k_smallest
        k = min(10, size // 10)
        start_time = time.time()
        largest = k_largest(k, data)
        k_large_time = time.time() - start_time
        
        start_time = time.time()
        smallest = k_smallest(k, data)
        k_small_time = time.time() - start_time
        
        print(f"  k_largest({k}): {k_large_time:.4f}s, k_smallest({k}): {k_small_time:.4f}s")
        print()
    
    print("Performance Notes:")
    print("- Heap operations are O(log n) for insert/extract")
    print("- Building heap from array is O(n)")
    print("- k_largest/k_smallest are O(n log k), efficient for small k")
    print("- PriorityQueue has slight overhead due to tuple management")


if __name__ == "__main__":
    test_min_heap_operations()
    test_max_heap_operations()
    test_priority_queue_operations()
    test_median_heap()
    real_world_example_task_scheduler()
    real_world_example_network_routing()
    real_world_example_data_stream_processing()
    performance_comparison()