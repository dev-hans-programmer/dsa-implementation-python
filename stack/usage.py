"""
Stack Usage Examples

This module demonstrates practical usage of stack implementations
with real-world scenarios and comprehensive test cases.
"""

from implementation import ListStack, LinkedStack, MinStack, DequeStack, StackEmptyError


def test_basic_stack_operations():
    """Test basic operations of different stack implementations."""
    print("=== Testing Basic Stack Operations ===\n")
    
    # Test different implementations
    implementations = [
        ("ListStack", ListStack()),
        ("LinkedStack", LinkedStack()),
        ("DequeStack", DequeStack())
    ]
    
    for name, stack in implementations:
        print(f"--- Testing {name} ---")
        
        # Test empty stack
        print(f"Is empty: {stack.is_empty()}")
        print(f"Size: {stack.size()}")
        
        # Test push operations
        for i in range(1, 6):
            stack.push(i * 10)
            print(f"Pushed {i * 10}")
        
        print(f"Stack after pushes: {stack}")
        print(f"Size: {stack.size()}")
        print(f"Top element: {stack.peek()}")
        
        # Test pop operations
        print("\nPopping elements:")
        while not stack.is_empty():
            popped = stack.pop()
            print(f"Popped: {popped}, Size: {stack.size()}")
        
        print(f"Final stack: {stack}")
        print()


def test_min_stack():
    """Test MinStack implementation."""
    print("=== Testing MinStack ===\n")
    
    min_stack = MinStack()
    
    # Test operations with minimum tracking
    operations = [30, 10, 20, 5, 15]
    
    print("Pushing elements and tracking minimum:")
    for num in operations:
        min_stack.push(num)
        print(f"Pushed {num}, Current min: {min_stack.get_min()}")
    
    print(f"\nCurrent stack: {min_stack}")
    
    print("\nPopping elements and tracking minimum:")
    while not min_stack.is_empty():
        popped = min_stack.pop()
        if not min_stack.is_empty():
            print(f"Popped {popped}, New min: {min_stack.get_min()}")
        else:
            print(f"Popped {popped}, Stack is empty")


def test_error_handling():
    """Test error handling for empty stack operations."""
    print("\n=== Testing Error Handling ===\n")
    
    stack = ListStack()
    
    operations = [
        ("pop", lambda: stack.pop()),
        ("peek", lambda: stack.peek())
    ]
    
    for op_name, operation in operations:
        try:
            result = operation()
            print(f"{op_name}: {result}")
        except StackEmptyError as e:
            print(f"{op_name} error: {e}")


def real_world_example_expression_validation():
    """
    Demonstrate stack usage in validating balanced parentheses.
    This is a classic application of stacks.
    """
    print("\n=== Real-World Example: Expression Validation ===\n")
    
    def is_balanced(expression: str) -> bool:
        """
        Check if parentheses, brackets, and braces are balanced.
        
        Args:
            expression: String containing brackets to validate
            
        Returns:
            bool: True if balanced, False otherwise
        """
        stack = ListStack()
        opening = {'(', '[', '{'}
        closing = {')', ']', '}'}
        pairs = {'(': ')', '[': ']', '{': '}'}
        
        for char in expression:
            if char in opening:
                stack.push(char)
            elif char in closing:
                if stack.is_empty():
                    return False
                
                top = stack.pop()
                if pairs[top] != char:
                    return False
        
        return stack.is_empty()
    
    # Test cases
    test_expressions = [
        "((()))",           # Balanced
        "([{}])",           # Balanced
        "({[]})",           # Balanced
        "((())",            # Unbalanced - missing closing
        "()))",             # Unbalanced - extra closing
        "([)]",             # Unbalanced - wrong order
        "{[()]}",           # Balanced
        "",                 # Empty - balanced
        "(((",              # Unbalanced - only opening
        ")))",              # Unbalanced - only closing
    ]
    
    print("Testing expression validation:")
    for expr in test_expressions:
        result = is_balanced(expr)
        status = "✓ Balanced" if result else "✗ Unbalanced"
        print(f"'{expr}' -> {status}")


def real_world_example_undo_functionality():
    """
    Demonstrate stack usage in implementing undo functionality.
    """
    print("\n=== Real-World Example: Undo Functionality ===\n")
    
    class TextEditor:
        """Simple text editor with undo functionality using stack."""
        
        def __init__(self):
            self.content = ""
            self.undo_stack = ListStack()
            self.max_undo = 10  # Limit undo history
        
        def type_text(self, text: str):
            """Add text and save state for undo."""
            # Save current state before modification
            self.undo_stack.push(self.content)
            
            # Limit undo history size
            if self.undo_stack.size() > self.max_undo:
                # Remove oldest state (bottom of stack)
                temp_stack = ListStack()
                for _ in range(self.max_undo):
                    if not self.undo_stack.is_empty():
                        temp_stack.push(self.undo_stack.pop())
                
                # Restore states except the oldest
                self.undo_stack.clear()
                for _ in range(self.max_undo - 1):
                    if not temp_stack.is_empty():
                        self.undo_stack.push(temp_stack.pop())
            
            self.content += text
            print(f"Typed: '{text}' -> Content: '{self.content}'")
        
        def delete_chars(self, count: int):
            """Delete characters and save state for undo."""
            self.undo_stack.push(self.content)
            
            if count <= len(self.content):
                deleted = self.content[-count:]
                self.content = self.content[:-count]
                print(f"Deleted: '{deleted}' -> Content: '{self.content}'")
            else:
                self.content = ""
                print(f"Deleted all content -> Content: '{self.content}'")
        
        def undo(self):
            """Undo the last operation."""
            if self.undo_stack.is_empty():
                print("Nothing to undo")
                return
            
            previous_state = self.undo_stack.pop()
            print(f"Undo: '{self.content}' -> '{previous_state}'")
            self.content = previous_state
        
        def get_content(self) -> str:
            """Get current content."""
            return self.content
        
        def undo_history_size(self) -> int:
            """Get size of undo history."""
            return self.undo_stack.size()
    
    # Simulate text editing with undo
    editor = TextEditor()
    
    # Perform operations
    editor.type_text("Hello")
    editor.type_text(" World")
    editor.type_text("!")
    editor.delete_chars(1)  # Remove "!"
    editor.type_text(" Python")
    
    print(f"\nFinal content: '{editor.get_content()}'")
    print(f"Undo history size: {editor.undo_history_size()}")
    
    # Perform undo operations
    print("\nUndoing operations:")
    for i in range(3):
        editor.undo()
    
    print(f"Content after undos: '{editor.get_content()}'")


def real_world_example_function_call_stack():
    """
    Demonstrate how stack works in function calls and recursion.
    """
    print("\n=== Real-World Example: Function Call Stack Simulation ===\n")
    
    class CallStack:
        """Simulate function call stack."""
        
        def __init__(self):
            self.stack = ListStack()
        
        def push_frame(self, function_name: str, params: dict):
            """Push a new function frame onto call stack."""
            frame = {
                'function': function_name,
                'parameters': params,
                'local_vars': {}
            }
            self.stack.push(frame)
            print(f"Called {function_name}({params})")
            self.show_stack()
        
        def pop_frame(self, return_value=None):
            """Pop function frame from call stack."""
            if not self.stack.is_empty():
                frame = self.stack.pop()
                print(f"Returning from {frame['function']} with value: {return_value}")
                self.show_stack()
                return return_value
        
        def show_stack(self):
            """Display current call stack."""
            if self.stack.is_empty():
                print("Call stack: Empty")
            else:
                print("Call stack:")
                temp_stack = ListStack()
                frames = []
                
                # Get all frames
                while not self.stack.is_empty():
                    frame = self.stack.pop()
                    frames.append(frame)
                    temp_stack.push(frame)
                
                # Restore stack and display
                while not temp_stack.is_empty():
                    self.stack.push(temp_stack.pop())
                
                for i, frame in enumerate(reversed(frames)):
                    indent = "  " * i
                    print(f"{indent}-> {frame['function']}({frame['parameters']})")
            print()
    
    def simulate_factorial(n: int, call_stack: CallStack):
        """Simulate factorial calculation with call stack tracking."""
        call_stack.push_frame("factorial", {"n": n})
        
        if n <= 1:
            result = 1
        else:
            result = n * simulate_factorial(n - 1, call_stack)
        
        return call_stack.pop_frame(result)
    
    # Simulate recursive factorial calculation
    print("Simulating factorial(4) calculation:")
    call_stack = CallStack()
    result = simulate_factorial(4, call_stack)
    print(f"Final result: {result}")


def real_world_example_browser_back_button():
    """
    Demonstrate stack usage in browser back button functionality.
    """
    print("\n=== Real-World Example: Browser Back Button ===\n")
    
    class SimpleBrowser:
        """Simple browser with back functionality using stack."""
        
        def __init__(self):
            self.history_stack = ListStack()
            self.current_page = None
        
        def visit_page(self, url: str):
            """Visit a new page."""
            if self.current_page:
                # Save current page to history before navigating
                self.history_stack.push(self.current_page)
            
            self.current_page = url
            print(f"Navigated to: {url}")
        
        def go_back(self):
            """Go back to previous page."""
            if self.history_stack.is_empty():
                print("No previous page to go back to")
                return
            
            previous_page = self.history_stack.pop()
            print(f"Going back from {self.current_page} to {previous_page}")
            self.current_page = previous_page
        
        def get_current_page(self) -> str:
            """Get current page URL."""
            return self.current_page or "No page loaded"
        
        def get_history_size(self) -> int:
            """Get size of browser history."""
            return self.history_stack.size()
    
    # Simulate browser usage
    browser = SimpleBrowser()
    
    # Visit some pages
    pages = [
        "https://www.google.com",
        "https://www.stackoverflow.com",
        "https://github.com",
        "https://www.python.org"
    ]
    
    for page in pages:
        browser.visit_page(page)
    
    print(f"\nCurrent page: {browser.get_current_page()}")
    print(f"History size: {browser.get_history_size()}")
    
    # Use back button
    print("\nUsing back button:")
    for _ in range(3):
        browser.go_back()
        print(f"Current page: {browser.get_current_page()}")
    
    # Try to go back when no history
    browser.go_back()


def performance_comparison():
    """Compare performance of different stack implementations."""
    print("\n=== Performance Comparison ===\n")
    
    import time
    
    implementations = [
        ("ListStack", ListStack),
        ("LinkedStack", LinkedStack),
        ("DequeStack", DequeStack)
    ]
    
    test_size = 10000
    
    print(f"Performance test with {test_size} operations:")
    
    for name, StackClass in implementations:
        stack = StackClass()
        
        # Test push operations
        start_time = time.time()
        for i in range(test_size):
            stack.push(i)
        push_time = time.time() - start_time
        
        # Test pop operations
        start_time = time.time()
        for i in range(test_size):
            stack.pop()
        pop_time = time.time() - start_time
        
        print(f"{name}:")
        print(f"  Push {test_size} items: {push_time:.6f} seconds")
        print(f"  Pop {test_size} items: {pop_time:.6f} seconds")
        print(f"  Total time: {push_time + pop_time:.6f} seconds")
        print()


if __name__ == "__main__":
    test_basic_stack_operations()
    test_min_stack()
    test_error_handling()
    real_world_example_expression_validation()
    real_world_example_undo_functionality()
    real_world_example_function_call_stack()
    real_world_example_browser_back_button()
    performance_comparison()
