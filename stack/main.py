"""
Interactive Stack Demonstration

This module provides an interactive demonstration of stack operations,
allowing users to experiment with different stack implementations and
see real-world applications in action.
"""

from implementation import ListStack, LinkedStack, MinStack, DequeStack, StackEmptyError


def display_main_menu():
    """Display the main menu options."""
    print("\n" + "="*60)
    print("STACK INTERACTIVE DEMO")
    print("="*60)
    print("1. Basic Stack Operations")
    print("2. MinStack Demo (Stack with O(1) minimum)")
    print("3. Expression Validator (Balanced Parentheses)")
    print("4. Text Editor with Undo")
    print("5. Browser Back Button Simulation")
    print("6. Function Call Stack Visualization")
    print("7. Performance Comparison")
    print("8. Stack vs List Comparison")
    print("9. Exit")
    print("="*60)


def basic_stack_demo():
    """Interactive demo for basic stack operations."""
    print("\n" + "="*50)
    print("BASIC STACK OPERATIONS DEMO")
    print("="*50)
    
    # Let user choose implementation
    print("Choose stack implementation:")
    print("1. ListStack (Python list-based)")
    print("2. LinkedStack (Linked list-based)")
    print("3. DequeStack (Collections.deque-based)")
    
    try:
        choice = int(input("\nEnter choice (1-3): "))
        if choice == 1:
            stack = ListStack()
            stack_name = "ListStack"
        elif choice == 2:
            stack = LinkedStack()
            stack_name = "LinkedStack"
        elif choice == 3:
            stack = DequeStack()
            stack_name = "DequeStack"
        else:
            print("Invalid choice, using ListStack")
            stack = ListStack()
            stack_name = "ListStack"
    except ValueError:
        print("Invalid input, using ListStack")
        stack = ListStack()
        stack_name = "ListStack"
    
    print(f"\nUsing {stack_name}")
    
    while True:
        print(f"\nCurrent Stack: {stack}")
        print(f"Size: {stack.size()}, Empty: {stack.is_empty()}")
        
        print("\nOperations:")
        print("1. Push element")
        print("2. Pop element")
        print("3. Peek top element")
        print("4. Clear stack")
        print("5. Show as list")
        print("6. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-6): "))
            
            if choice == 1:
                element = input("Enter element to push: ")
                stack.push(element)
                print(f"Pushed '{element}'")
                
            elif choice == 2:
                try:
                    popped = stack.pop()
                    print(f"Popped: '{popped}'")
                except StackEmptyError as e:
                    print(f"Error: {e}")
                    
            elif choice == 3:
                try:
                    top = stack.peek()
                    print(f"Top element: '{top}'")
                except StackEmptyError as e:
                    print(f"Error: {e}")
                    
            elif choice == 4:
                stack.clear()
                print("Stack cleared")
                
            elif choice == 5:
                if hasattr(stack, 'to_list'):
                    print(f"As list (bottom to top): {stack.to_list()}")
                else:
                    print("to_list() not available for this implementation")
                    
            elif choice == 6:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def min_stack_demo():
    """Interactive demo for MinStack."""
    print("\n" + "="*50)
    print("MINSTACK DEMO")
    print("="*50)
    print("MinStack supports O(1) minimum element retrieval")
    
    min_stack = MinStack()
    
    while True:
        print(f"\nCurrent Stack: {min_stack}")
        
        print("\nOperations:")
        print("1. Push element")
        print("2. Pop element")
        print("3. Peek top element")
        print("4. Get minimum element")
        print("5. Demo with sample data")
        print("6. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-6): "))
            
            if choice == 1:
                try:
                    element = int(input("Enter number to push: "))
                    min_stack.push(element)
                    print(f"Pushed {element}")
                    if not min_stack.is_empty():
                        print(f"Current minimum: {min_stack.get_min()}")
                except ValueError:
                    print("Please enter a valid number")
                    
            elif choice == 2:
                try:
                    popped = min_stack.pop()
                    print(f"Popped: {popped}")
                    if not min_stack.is_empty():
                        print(f"New minimum: {min_stack.get_min()}")
                except StackEmptyError as e:
                    print(f"Error: {e}")
                    
            elif choice == 3:
                try:
                    top = min_stack.peek()
                    print(f"Top element: {top}")
                except StackEmptyError as e:
                    print(f"Error: {e}")
                    
            elif choice == 4:
                try:
                    minimum = min_stack.get_min()
                    print(f"Minimum element: {minimum}")
                except StackEmptyError as e:
                    print(f"Error: {e}")
                    
            elif choice == 5:
                # Demo with sample data
                sample_data = [30, 10, 20, 5, 15, 25]
                print(f"Pushing sample data: {sample_data}")
                
                for num in sample_data:
                    min_stack.push(num)
                    print(f"Pushed {num}, Min: {min_stack.get_min()}")
                
                print("\nPopping all elements:")
                while not min_stack.is_empty():
                    popped = min_stack.pop()
                    min_str = f", Min: {min_stack.get_min()}" if not min_stack.is_empty() else ""
                    print(f"Popped {popped}{min_str}")
                    
            elif choice == 6:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def expression_validator_demo():
    """Interactive demo for expression validation."""
    print("\n" + "="*50)
    print("EXPRESSION VALIDATOR DEMO")
    print("="*50)
    print("Check if parentheses, brackets, and braces are balanced")
    
    def is_balanced(expression: str) -> tuple:
        """
        Check if expression has balanced brackets.
        Returns (is_balanced, details)
        """
        stack = ListStack()
        opening = {'(', '[', '{'}
        closing = {')', ']', '}'}
        pairs = {'(': ')', '[': ']', '{': '}'}
        
        for i, char in enumerate(expression):
            if char in opening:
                stack.push((char, i))
            elif char in closing:
                if stack.is_empty():
                    return False, f"Unmatched closing '{char}' at position {i}"
                
                open_char, open_pos = stack.pop()
                if pairs[open_char] != char:
                    return False, f"Mismatched pair: '{open_char}' at {open_pos} and '{char}' at {i}"
        
        if not stack.is_empty():
            open_char, open_pos = stack.peek()
            return False, f"Unmatched opening '{open_char}' at position {open_pos}"
        
        return True, "All brackets are balanced"
    
    # Predefined test cases
    test_cases = [
        "((()))",
        "([{}])",
        "({[]})",
        "((())",
        "()))",
        "([)]",
        "{[()]}",
        "",
        "(((",
        ")))",
        "Hello (world [test {example}])",
        "if (x > 0) { print('positive'); }",
        "arr[i] = func(a, b[c[d]])",
    ]
    
    while True:
        print("\nExpression Validator:")
        print("1. Enter custom expression")
        print("2. Test predefined examples")
        print("3. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-3): "))
            
            if choice == 1:
                expression = input("Enter expression to validate: ")
                is_valid, details = is_balanced(expression)
                status = "✓ BALANCED" if is_valid else "✗ UNBALANCED"
                print(f"\nExpression: '{expression}'")
                print(f"Result: {status}")
                print(f"Details: {details}")
                
            elif choice == 2:
                print("\nTesting predefined examples:")
                for expr in test_cases:
                    is_valid, details = is_balanced(expr)
                    status = "✓" if is_valid else "✗"
                    print(f"{status} '{expr}' - {details}")
                    
            elif choice == 3:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def text_editor_demo():
    """Interactive demo for text editor with undo functionality."""
    print("\n" + "="*50)
    print("TEXT EDITOR WITH UNDO DEMO")
    print("="*50)
    
    class SimpleTextEditor:
        def __init__(self):
            self.content = ""
            self.undo_stack = ListStack()
        
        def type_text(self, text: str):
            self.undo_stack.push(self.content)
            self.content += text
        
        def delete_chars(self, count: int):
            self.undo_stack.push(self.content)
            self.content = self.content[:-count] if count <= len(self.content) else ""
        
        def undo(self):
            if not self.undo_stack.is_empty():
                self.content = self.undo_stack.pop()
                return True
            return False
        
        def get_content(self):
            return self.content
        
        def undo_available(self):
            return not self.undo_stack.is_empty()
    
    editor = SimpleTextEditor()
    
    while True:
        print(f"\nCurrent Text: '{editor.get_content()}'")
        print(f"Undo Available: {editor.undo_available()}")
        
        print("\nText Editor Operations:")
        print("1. Type text")
        print("2. Delete characters")
        print("3. Undo last operation")
        print("4. Demo sequence")
        print("5. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-5): "))
            
            if choice == 1:
                text = input("Enter text to type: ")
                editor.type_text(text)
                print(f"Added: '{text}'")
                
            elif choice == 2:
                try:
                    count = int(input("Enter number of characters to delete: "))
                    if count > 0:
                        editor.delete_chars(count)
                        print(f"Deleted {count} characters")
                    else:
                        print("Please enter a positive number")
                except ValueError:
                    print("Please enter a valid number")
                    
            elif choice == 3:
                if editor.undo():
                    print("Undo successful")
                else:
                    print("Nothing to undo")
                    
            elif choice == 4:
                # Demo sequence
                operations = [
                    ("type", "Hello"),
                    ("type", " World"),
                    ("type", "!"),
                    ("delete", 1),
                    ("type", " Python"),
                ]
                
                print("Executing demo sequence:")
                for op_type, op_value in operations:
                    if op_type == "type":
                        editor.type_text(op_value)
                        print(f"Typed: '{op_value}' -> '{editor.get_content()}'")
                    elif op_type == "delete":
                        editor.delete_chars(op_value)
                        print(f"Deleted {op_value} chars -> '{editor.get_content()}'")
                
                print(f"\nFinal text: '{editor.get_content()}'")
                print("You can now use undo to reverse these operations")
                
            elif choice == 5:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def browser_demo():
    """Interactive demo for browser back button simulation."""
    print("\n" + "="*50)
    print("BROWSER BACK BUTTON DEMO")
    print("="*50)
    
    class SimpleBrowser:
        def __init__(self):
            self.history_stack = ListStack()
            self.current_page = None
        
        def visit_page(self, url: str):
            if self.current_page:
                self.history_stack.push(self.current_page)
            self.current_page = url
        
        def go_back(self):
            if not self.history_stack.is_empty():
                previous_page = self.history_stack.pop()
                self.current_page = previous_page
                return True
            return False
        
        def get_current_page(self):
            return self.current_page or "No page loaded"
        
        def can_go_back(self):
            return not self.history_stack.is_empty()
        
        def get_history_size(self):
            return self.history_stack.size()
    
    browser = SimpleBrowser()
    
    while True:
        print(f"\nCurrent Page: {browser.get_current_page()}")
        print(f"Can Go Back: {browser.can_go_back()}")
        print(f"History Size: {browser.get_history_size()}")
        
        print("\nBrowser Operations:")
        print("1. Visit new page")
        print("2. Go back")
        print("3. Visit sample sites")
        print("4. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-4): "))
            
            if choice == 1:
                url = input("Enter URL to visit: ")
                browser.visit_page(url)
                print(f"Navigated to: {url}")
                
            elif choice == 2:
                if browser.go_back():
                    print(f"Went back to: {browser.get_current_page()}")
                else:
                    print("Cannot go back - no previous page")
                    
            elif choice == 3:
                sample_sites = [
                    "https://www.google.com",
                    "https://www.github.com",
                    "https://www.stackoverflow.com",
                    "https://www.python.org"
                ]
                
                print("Visiting sample sites:")
                for site in sample_sites:
                    browser.visit_page(site)
                    print(f"Visited: {site}")
                
                print("You can now use the back button to navigate")
                
            elif choice == 4:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def call_stack_demo():
    """Demo showing function call stack visualization."""
    print("\n" + "="*50)
    print("FUNCTION CALL STACK DEMO")
    print("="*50)
    print("Visualizing how function calls work with a stack")
    
    def factorial_demo(n: int, depth: int = 0):
        """Recursive factorial with call stack visualization."""
        indent = "  " * depth
        print(f"{indent}-> Calling factorial({n})")
        
        if n <= 1:
            print(f"{indent}   Base case reached: factorial({n}) = 1")
            print(f"{indent}<- Returning 1 from factorial({n})")
            return 1
        else:
            print(f"{indent}   Need to calculate factorial({n-1}) first")
            result = n * factorial_demo(n - 1, depth + 1)
            print(f"{indent}   factorial({n-1}) returned, calculating {n} * {result // n} = {result}")
            print(f"{indent}<- Returning {result} from factorial({n})")
            return result
    
    def fibonacci_demo(n: int, depth: int = 0):
        """Recursive Fibonacci with call stack visualization."""
        indent = "  " * depth
        print(f"{indent}-> Calling fibonacci({n})")
        
        if n <= 1:
            print(f"{indent}   Base case: fibonacci({n}) = {n}")
            print(f"{indent}<- Returning {n} from fibonacci({n})")
            return n
        else:
            print(f"{indent}   Need fibonacci({n-1}) and fibonacci({n-2})")
            fib1 = fibonacci_demo(n - 1, depth + 1)
            fib2 = fibonacci_demo(n - 2, depth + 1)
            result = fib1 + fib2
            print(f"{indent}   Got fib({n-1})={fib1} and fib({n-2})={fib2}, returning {result}")
            print(f"{indent}<- Returning {result} from fibonacci({n})")
            return result
    
    while True:
        print("\nFunction Call Stack Visualization:")
        print("1. Factorial calculation")
        print("2. Fibonacci calculation")
        print("3. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-3): "))
            
            if choice == 1:
                try:
                    n = int(input("Enter number for factorial (1-6 recommended): "))
                    if 1 <= n <= 10:
                        print(f"\nCalculating factorial({n}):")
                        result = factorial_demo(n)
                        print(f"\nFinal result: factorial({n}) = {result}")
                    else:
                        print("Please enter a number between 1 and 10")
                except ValueError:
                    print("Please enter a valid number")
                    
            elif choice == 2:
                try:
                    n = int(input("Enter number for fibonacci (1-5 recommended): "))
                    if 1 <= n <= 8:
                        print(f"\nCalculating fibonacci({n}):")
                        result = fibonacci_demo(n)
                        print(f"\nFinal result: fibonacci({n}) = {result}")
                    else:
                        print("Please enter a number between 1 and 8")
                except ValueError:
                    print("Please enter a valid number")
                    
            elif choice == 3:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def performance_comparison():
    """Compare performance of different stack implementations."""
    print("\n" + "="*50)
    print("PERFORMANCE COMPARISON")
    print("="*50)
    
    import time
    
    test_sizes = [1000, 5000, 10000]
    implementations = [
        ("ListStack", ListStack),
        ("LinkedStack", LinkedStack),
        ("DequeStack", DequeStack)
    ]
    
    for size in test_sizes:
        print(f"\nTesting with {size} operations:")
        print("-" * 40)
        
        for name, StackClass in implementations:
            stack = StackClass()
            
            # Test push operations
            start_time = time.time()
            for i in range(size):
                stack.push(i)
            push_time = time.time() - start_time
            
            # Test pop operations
            start_time = time.time()
            for i in range(size):
                stack.pop()
            pop_time = time.time() - start_time
            
            total_time = push_time + pop_time
            
            print(f"{name:12} - Push: {push_time:.6f}s, Pop: {pop_time:.6f}s, Total: {total_time:.6f}s")


def stack_vs_list_comparison():
    """Compare stack operations with Python list operations."""
    print("\n" + "="*50)
    print("STACK VS PYTHON LIST COMPARISON")
    print("="*50)
    
    print("Conceptual Comparison:")
    print("\nStack (LIFO - Last In, First Out):")
    print("- push(item)  -> add to top")
    print("- pop()       -> remove from top") 
    print("- peek()      -> view top item")
    print("- Limited access (only top element)")
    
    print("\nPython List:")
    print("- append(item) -> add to end")
    print("- pop()        -> remove from end")
    print("- list[-1]     -> view last item")
    print("- Random access (any index)")
    
    print("\nPractical Demo:")
    
    # Demo with same operations
    stack = ListStack()
    py_list = []
    
    operations = [10, 20, 30, 40, 50]
    
    print(f"\nAdding elements: {operations}")
    
    for item in operations:
        stack.push(item)
        py_list.append(item)
    
    print(f"Stack: {stack}")
    print(f"List:  {py_list}")
    
    print("\nRemoving elements:")
    
    while not stack.is_empty():
        stack_popped = stack.pop()
        list_popped = py_list.pop()
        print(f"Stack popped: {stack_popped}, List popped: {list_popped}")
    
    print("\nKey Differences:")
    print("1. Stack enforces LIFO discipline")
    print("2. List allows random access and insertion anywhere")
    print("3. Stack prevents accidental access to middle elements")
    print("4. List is more flexible but less controlled")


def main():
    """Main function to run the interactive demo."""
    print("Welcome to the Stack Interactive Learning Tool!")
    print("This demo will help you understand stack operations and applications.")
    
    while True:
        display_main_menu()
        
        try:
            choice = int(input("\nEnter your choice (1-9): "))
            
            if choice == 1:
                basic_stack_demo()
            elif choice == 2:
                min_stack_demo()
            elif choice == 3:
                expression_validator_demo()
            elif choice == 4:
                text_editor_demo()
            elif choice == 5:
                browser_demo()
            elif choice == 6:
                call_stack_demo()
            elif choice == 7:
                performance_comparison()
            elif choice == 8:
                stack_vs_list_comparison()
            elif choice == 9:
                print("\nThank you for using the Stack Demo!")
                print("Remember: Stacks are everywhere in computing! 📚")
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
