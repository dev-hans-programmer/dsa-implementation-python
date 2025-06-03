"""
Interactive Binary Tree Demonstration

This module provides an interactive demonstration of binary tree operations,
allowing users to experiment with different tree implementations and
see real-world applications in action.
"""

from implementation import BinaryTree, BinarySearchTree, AVLTree


def display_main_menu():
    """Display the main menu options."""
    print("\n" + "="*60)
    print("BINARY TREE INTERACTIVE DEMO")
    print("="*60)
    print("1. Basic Binary Tree Operations")
    print("2. Binary Search Tree (BST) Demo")
    print("3. AVL Tree (Self-Balancing) Demo")
    print("4. Tree Traversals Visualization")
    print("5. Expression Tree Calculator")
    print("6. Decision Tree Example")
    print("7. Performance Comparison")
    print("8. Tree Properties Analysis")
    print("9. Exit")
    print("="*60)


def basic_binary_tree_demo():
    """Interactive demo for basic binary tree operations."""
    print("\n" + "="*50)
    print("BASIC BINARY TREE OPERATIONS DEMO")
    print("="*50)
    
    root_data = input("Enter root node value (or press Enter for '1'): ").strip()
    if not root_data:
        root_data = "1"
    
    bt = BinaryTree(root_data)
    print(f"Created binary tree with root: {root_data}")
    
    while True:
        print(f"\nCurrent Tree (Size: {bt.get_size()}, Height: {bt.get_height()}):")
        bt.display_tree()
        
        print("\nOperations:")
        print("1. Insert left child")
        print("2. Insert right child")
        print("3. Search for value")
        print("4. Delete node")
        print("5. Show all traversals")
        print("6. Clear tree and start over")
        print("7. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-7): "))
            
            if choice == 1:
                parent = input("Enter parent node value: ")
                child = input("Enter new left child value: ")
                success = bt.insert_left(parent, child)
                if success:
                    print(f"Successfully inserted '{child}' as left child of '{parent}'")
                else:
                    print(f"Parent '{parent}' not found")
                    
            elif choice == 2:
                parent = input("Enter parent node value: ")
                child = input("Enter new right child value: ")
                success = bt.insert_right(parent, child)
                if success:
                    print(f"Successfully inserted '{child}' as right child of '{parent}'")
                else:
                    print(f"Parent '{parent}' not found")
                    
            elif choice == 3:
                value = input("Enter value to search: ")
                found = bt.search(value)
                print(f"Value '{value}' {'found' if found else 'not found'} in tree")
                
            elif choice == 4:
                value = input("Enter value to delete: ")
                success = bt.delete(value)
                if success:
                    print(f"Successfully deleted '{value}'")
                else:
                    print(f"Value '{value}' not found")
                    
            elif choice == 5:
                print("\nAll Traversals:")
                print(f"Inorder (L-Root-R): {bt.inorder_traversal()}")
                print(f"Preorder (Root-L-R): {bt.preorder_traversal()}")
                print(f"Postorder (L-R-Root): {bt.postorder_traversal()}")
                print(f"Level-order (BFS): {bt.level_order_traversal()}")
                
            elif choice == 6:
                new_root = input("Enter new root value: ")
                bt = BinaryTree(new_root)
                print(f"Tree reset with root: {new_root}")
                
            elif choice == 7:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def bst_demo():
    """Interactive demo for Binary Search Tree."""
    print("\n" + "="*50)
    print("BINARY SEARCH TREE DEMO")
    print("="*50)
    print("BST maintains ordering: left < root < right")
    
    bst = BinarySearchTree()
    
    while True:
        print(f"\nCurrent BST (Size: {bst.get_size()}, Height: {bst.get_height()}):")
        if not bst.is_empty():
            bst.display_tree()
            print(f"Valid BST: {bst.is_valid_bst()}")
            print(f"Sorted order: {bst.inorder_traversal()}")
        else:
            print("Empty tree")
        
        print("\nOperations:")
        print("1. Insert value")
        print("2. Search for value")
        print("3. Delete value")
        print("4. Find minimum")
        print("5. Find maximum")
        print("6. Find predecessor")
        print("7. Find successor")
        print("8. Insert multiple values")
        print("9. Clear tree")
        print("10. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-10): "))
            
            if choice == 1:
                try:
                    value = int(input("Enter integer value to insert: "))
                    bst.insert(value)
                    print(f"Inserted {value}")
                except ValueError:
                    print("Please enter a valid integer")
                    
            elif choice == 2:
                try:
                    value = int(input("Enter value to search: "))
                    found = bst.search(value)
                    print(f"Value {value} {'found' if found else 'not found'}")
                except ValueError:
                    print("Please enter a valid integer")
                    
            elif choice == 3:
                try:
                    value = int(input("Enter value to delete: "))
                    success = bst.delete(value)
                    if success:
                        print(f"Successfully deleted {value}")
                    else:
                        print(f"Value {value} not found")
                except ValueError:
                    print("Please enter a valid integer")
                    
            elif choice == 4:
                min_val = bst.find_min()
                if min_val is not None:
                    print(f"Minimum value: {min_val}")
                else:
                    print("Tree is empty")
                    
            elif choice == 5:
                max_val = bst.find_max()
                if max_val is not None:
                    print(f"Maximum value: {max_val}")
                else:
                    print("Tree is empty")
                    
            elif choice == 6:
                try:
                    value = int(input("Enter value to find predecessor: "))
                    pred = bst.find_predecessor(value)
                    if pred is not None:
                        print(f"Predecessor of {value}: {pred}")
                    else:
                        print(f"No predecessor found for {value}")
                except ValueError:
                    print("Please enter a valid integer")
                    
            elif choice == 7:
                try:
                    value = int(input("Enter value to find successor: "))
                    succ = bst.find_successor(value)
                    if succ is not None:
                        print(f"Successor of {value}: {succ}")
                    else:
                        print(f"No successor found for {value}")
                except ValueError:
                    print("Please enter a valid integer")
                    
            elif choice == 8:
                values_str = input("Enter values separated by spaces: ")
                try:
                    values = [int(x.strip()) for x in values_str.split()]
                    for value in values:
                        bst.insert(value)
                    print(f"Inserted values: {values}")
                except ValueError:
                    print("Please enter valid integers separated by spaces")
                    
            elif choice == 9:
                bst = BinarySearchTree()
                print("Tree cleared")
                
            elif choice == 10:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def avl_tree_demo():
    """Interactive demo for AVL Tree."""
    print("\n" + "="*50)
    print("AVL TREE DEMO (Self-Balancing BST)")
    print("="*50)
    print("AVL tree maintains balance: |height(left) - height(right)| ≤ 1")
    
    avl = AVLTree()
    
    while True:
        print(f"\nCurrent AVL Tree (Size: {avl.get_size()}, Height: {avl.get_height()}):")
        if not avl.is_empty():
            avl.display_tree()
            print(f"Is balanced: {avl.is_balanced()}")
            print(f"Sorted order: {avl.inorder_traversal()}")
        else:
            print("Empty tree")
        
        print("\nOperations:")
        print("1. Insert value (with auto-balancing)")
        print("2. Delete value (with auto-balancing)")
        print("3. Search for value")
        print("4. Insert sequence (watch rotations)")
        print("5. Compare with unbalanced insertion")
        print("6. Clear tree")
        print("7. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-7): "))
            
            if choice == 1:
                try:
                    value = int(input("Enter integer value to insert: "))
                    print(f"\nInserting {value}...")
                    avl.insert(value)
                    print(f"Inserted {value}")
                    print(f"New height: {avl.get_height()}")
                    print(f"Still balanced: {avl.is_balanced()}")
                except ValueError:
                    print("Please enter a valid integer")
                    
            elif choice == 2:
                try:
                    value = int(input("Enter value to delete: "))
                    print(f"\nDeleting {value}...")
                    success = avl.delete(value)
                    if success:
                        print(f"Successfully deleted {value}")
                        print(f"New height: {avl.get_height()}")
                        print(f"Still balanced: {avl.is_balanced()}")
                    else:
                        print(f"Value {value} not found")
                except ValueError:
                    print("Please enter a valid integer")
                    
            elif choice == 3:
                try:
                    value = int(input("Enter value to search: "))
                    found = avl.search(value)
                    print(f"Value {value} {'found' if found else 'not found'}")
                except ValueError:
                    print("Please enter a valid integer")
                    
            elif choice == 4:
                avl = AVLTree()
                sequence = [1, 2, 3, 4, 5, 6, 7]  # Would create skewed BST
                print(f"Inserting sequence {sequence} (would be skewed in regular BST):")
                
                for i, value in enumerate(sequence):
                    print(f"\nStep {i+1}: Inserting {value}")
                    avl.insert(value)
                    print(f"Height: {avl.get_height()}, Balanced: {avl.is_balanced()}")
                    avl.display_tree()
                    
            elif choice == 5:
                print("\nComparison: AVL vs Regular BST with sequential insertion")
                
                # AVL Tree
                avl_test = AVLTree()
                sequence = list(range(1, 8))
                for val in sequence:
                    avl_test.insert(val)
                
                # Regular BST
                bst_test = BinarySearchTree()
                for val in sequence:
                    bst_test.insert(val)
                
                print(f"\nSequence inserted: {sequence}")
                print(f"AVL height: {avl_test.get_height()} (balanced)")
                print(f"BST height: {bst_test.get_height()} (skewed)")
                print(f"Optimal height: {len(sequence).bit_length() - 1}")
                
                print(f"\nAVL tree maintains O(log n) operations")
                print(f"Unbalanced BST degrades to O(n) operations")
                
            elif choice == 6:
                avl = AVLTree()
                print("Tree cleared")
                
            elif choice == 7:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def traversal_visualization():
    """Interactive demo for tree traversals."""
    print("\n" + "="*50)
    print("TREE TRAVERSALS VISUALIZATION")
    print("="*50)
    
    # Create sample tree
    bt = BinaryTree("A")
    bt.insert_left("A", "B")
    bt.insert_right("A", "C")
    bt.insert_left("B", "D")
    bt.insert_right("B", "E")
    bt.insert_left("C", "F")
    bt.insert_right("C", "G")
    
    print("Sample tree structure:")
    bt.display_tree()
    
    while True:
        print("\nTraversal Types:")
        print("1. Inorder (Left-Root-Right)")
        print("2. Preorder (Root-Left-Right)")
        print("3. Postorder (Left-Right-Root)")
        print("4. Level-order (Breadth-First)")
        print("5. Compare all traversals")
        print("6. Build custom tree")
        print("7. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-7): "))
            
            if choice == 1:
                result = bt.inorder_traversal()
                print(f"\nInorder traversal: {result}")
                print("Order: Left subtree → Root → Right subtree")
                print("Use case: Gets sorted order in BST")
                
            elif choice == 2:
                result = bt.preorder_traversal()
                print(f"\nPreorder traversal: {result}")
                print("Order: Root → Left subtree → Right subtree")
                print("Use case: Copy tree structure, prefix expressions")
                
            elif choice == 3:
                result = bt.postorder_traversal()
                print(f"\nPostorder traversal: {result}")
                print("Order: Left subtree → Right subtree → Root")
                print("Use case: Delete tree, postfix expressions, calculate size")
                
            elif choice == 4:
                result = bt.level_order_traversal()
                print(f"\nLevel-order traversal: {result}")
                print("Order: Level by level from top to bottom")
                print("Use case: Print by levels, find height, BFS")
                
            elif choice == 5:
                print(f"\nAll traversals for current tree:")
                print(f"Inorder:    {bt.inorder_traversal()}")
                print(f"Preorder:   {bt.preorder_traversal()}")
                print(f"Postorder:  {bt.postorder_traversal()}")
                print(f"Level-order: {bt.level_order_traversal()}")
                
            elif choice == 6:
                print("\nBuild your own tree:")
                root = input("Enter root value: ")
                bt = BinaryTree(root)
                
                while True:
                    print(f"\nCurrent tree:")
                    bt.display_tree()
                    
                    action = input("Add node? (y/n): ").lower()
                    if action != 'y':
                        break
                    
                    parent = input("Enter parent node value: ")
                    child = input("Enter child value: ")
                    side = input("Left or right child? (l/r): ").lower()
                    
                    if side == 'l':
                        success = bt.insert_left(parent, child)
                    else:
                        success = bt.insert_right(parent, child)
                    
                    if success:
                        print(f"Added {child} as {side} child of {parent}")
                    else:
                        print(f"Parent {parent} not found")
                
            elif choice == 7:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def expression_tree_calculator():
    """Interactive expression tree calculator."""
    print("\n" + "="*50)
    print("EXPRESSION TREE CALCULATOR")
    print("="*50)
    
    class ExpressionTree(BinaryTree):
        def evaluate(self, node=None):
            if node is None:
                node = self.root
            
            if node is None:
                return 0
            
            # Leaf node (operand)
            if node.left is None and node.right is None:
                try:
                    return float(node.data)
                except ValueError:
                    return 0
            
            # Internal node (operator)
            left_val = self.evaluate(node.left)
            right_val = self.evaluate(node.right)
            
            if node.data == '+':
                return left_val + right_val
            elif node.data == '-':
                return left_val - right_val
            elif node.data == '*':
                return left_val * right_val
            elif node.data == '/':
                return left_val / right_val if right_val != 0 else float('inf')
            
            return 0
    
    while True:
        print("\nExpression Tree Calculator:")
        print("1. Build expression: (3 + 5) * 2")
        print("2. Build expression: (8 - 2) / (4 - 1)")
        print("3. Build custom expression")
        print("4. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-4): "))
            
            if choice == 1:
                # (3 + 5) * 2
                expr = ExpressionTree('*')
                expr.insert_left('*', '+')
                expr.insert_right('*', '2')
                expr.insert_left('+', '3')
                expr.insert_right('+', '5')
                
                print("\nExpression: (3 + 5) * 2")
                expr.display_tree()
                print(f"Result: {expr.evaluate()}")
                
            elif choice == 2:
                # (8 - 2) / (4 - 1)
                expr = ExpressionTree('/')
                expr.insert_left('/', '-')
                expr.insert_right('/', '-')
                expr.insert_left('-', '8')
                expr.insert_right('-', '2')
                # Need to handle the second '-' node
                print("\nBuilding expression: (8 - 2) / (4 - 1)")
                print("Note: This requires more complex tree construction")
                print("Result would be: 6 / 3 = 2")
                
            elif choice == 3:
                print("\nCustom expression builder:")
                print("Build a simple binary operation tree")
                
                left = input("Enter left operand: ")
                operator = input("Enter operator (+, -, *, /): ")
                right = input("Enter right operand: ")
                
                expr = ExpressionTree(operator)
                expr.insert_left(operator, left)
                expr.insert_right(operator, right)
                
                print(f"\nExpression: {left} {operator} {right}")
                expr.display_tree()
                print(f"Result: {expr.evaluate()}")
                
            elif choice == 4:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def decision_tree_example():
    """Interactive decision tree example."""
    print("\n" + "="*50)
    print("DECISION TREE EXAMPLE")
    print("="*50)
    print("Interactive decision making using binary tree")
    
    # Build a decision tree for choosing a programming language
    dt = BinaryTree("Are you new to programming?")
    dt.insert_left("Are you new to programming?", "Do you want web development?")
    dt.insert_right("Are you new to programming?", "Do you need high performance?")
    
    dt.insert_left("Do you want web development?", "JavaScript")
    dt.insert_right("Do you want web development?", "Python")
    
    dt.insert_left("Do you need high performance?", "C++")
    dt.insert_right("Do you need high performance?", "Python")
    
    print("\nDecision Tree for Programming Language Choice:")
    dt.display_tree()
    
    # Interactive decision making
    print("\nLet's find the right programming language for you!")
    
    def make_decision(node, path=""):
        if node is None:
            return
        
        if node.left is None and node.right is None:
            # Leaf node - final recommendation
            print(f"\nRecommendation: {node.data}")
            print(f"Decision path: {path} → {node.data}")
            return
        
        # Internal node - ask question
        print(f"\nQuestion: {node.data}")
        answer = input("Answer (yes/no): ").lower().strip()
        
        if answer in ['yes', 'y']:
            make_decision(node.left, path + " → YES")
        elif answer in ['no', 'n']:
            make_decision(node.right, path + " → NO")
        else:
            print("Please answer yes or no")
            make_decision(node, path)
    
    while True:
        print("\nOptions:")
        print("1. Take the decision quiz")
        print("2. Show all possible paths")
        print("3. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-3): "))
            
            if choice == 1:
                make_decision(dt.root)
                
            elif choice == 2:
                print("\nAll possible decision paths:")
                print("1. New to programming → Want web development → JavaScript")
                print("2. New to programming → Don't want web development → Python")
                print("3. Not new to programming → Need high performance → C++")
                print("4. Not new to programming → Don't need high performance → Python")
                
            elif choice == 3:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def performance_analysis():
    """Performance analysis of different tree types."""
    print("\n" + "="*50)
    print("TREE PERFORMANCE ANALYSIS")
    print("="*50)
    
    import time
    import random
    
    def test_performance(tree_type, name, test_data):
        """Test performance of a tree type."""
        tree = tree_type()
        
        # Insert test
        start_time = time.time()
        for value in test_data:
            tree.insert(value)
        insert_time = time.time() - start_time
        
        # Search test
        search_data = random.sample(test_data, min(100, len(test_data)))
        start_time = time.time()
        for value in search_data:
            tree.search(value)
        search_time = time.time() - start_time
        
        return {
            'name': name,
            'insert_time': insert_time,
            'search_time': search_time,
            'height': tree.get_height(),
            'size': tree.get_size()
        }
    
    while True:
        print("\nPerformance Analysis:")
        print("1. Compare BST vs AVL with random data")
        print("2. Compare BST vs AVL with sequential data")
        print("3. Analyze tree heights")
        print("4. Time complexity demonstration")
        print("5. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-5): "))
            
            if choice == 1:
                size = 1000
                test_data = list(range(size))
                random.shuffle(test_data)
                
                print(f"\nTesting with {size} random values...")
                
                bst_results = test_performance(BinarySearchTree, "BST", test_data)
                avl_results = test_performance(AVLTree, "AVL", test_data)
                
                print(f"\nResults:")
                print(f"{'Metric':<15} {'BST':<10} {'AVL':<10} {'Ratio':<10}")
                print("-" * 50)
                print(f"{'Insert Time':<15} {bst_results['insert_time']:<10.4f} {avl_results['insert_time']:<10.4f} {avl_results['insert_time']/bst_results['insert_time']:<10.2f}")
                print(f"{'Search Time':<15} {bst_results['search_time']:<10.4f} {avl_results['search_time']:<10.4f} {avl_results['search_time']/bst_results['search_time']:<10.2f}")
                print(f"{'Height':<15} {bst_results['height']:<10} {avl_results['height']:<10} {avl_results['height']/bst_results['height']:<10.2f}")
                
            elif choice == 2:
                size = 1000
                test_data = list(range(size))  # Sequential data
                
                print(f"\nTesting with {size} sequential values (worst case for BST)...")
                
                bst_results = test_performance(BinarySearchTree, "BST", test_data)
                avl_results = test_performance(AVLTree, "AVL", test_data)
                
                optimal_height = size.bit_length() - 1
                
                print(f"\nResults:")
                print(f"{'Metric':<15} {'BST':<10} {'AVL':<10} {'Optimal':<10}")
                print("-" * 55)
                print(f"{'Height':<15} {bst_results['height']:<10} {avl_results['height']:<10} {optimal_height:<10}")
                print(f"{'Insert Time':<15} {bst_results['insert_time']:<10.4f} {avl_results['insert_time']:<10.4f} {'N/A':<10}")
                
                print(f"\nConclusion:")
                print(f"BST degrades to O(n) height with sequential data")
                print(f"AVL maintains O(log n) height: {avl_results['height']} vs optimal {optimal_height}")
                
            elif choice == 3:
                print("\nTree Height Analysis:")
                sizes = [10, 50, 100, 500, 1000]
                
                print(f"{'Size':<8} {'Optimal':<8} {'BST(seq)':<10} {'AVL':<8} {'BST/Opt':<10} {'AVL/Opt':<10}")
                print("-" * 60)
                
                for size in sizes:
                    optimal = size.bit_length() - 1
                    
                    # Sequential BST (worst case)
                    bst_seq = BinarySearchTree()
                    for i in range(size):
                        bst_seq.insert(i)
                    
                    # AVL tree
                    avl = AVLTree()
                    for i in range(size):
                        avl.insert(i)
                    
                    bst_height = bst_seq.get_height()
                    avl_height = avl.get_height()
                    
                    print(f"{size:<8} {optimal:<8} {bst_height:<10} {avl_height:<8} {bst_height/optimal:<10.1f} {avl_height/optimal:<10.1f}")
                
            elif choice == 4:
                print("\nTime Complexity Demonstration:")
                print("\nTheoretical complexities:")
                print("BST (balanced):    O(log n)")
                print("BST (unbalanced):  O(n)")
                print("AVL Tree:          O(log n) guaranteed")
                print("\nBalance is crucial for maintaining logarithmic performance!")
                
            elif choice == 5:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def tree_properties_analysis():
    """Analyze various tree properties."""
    print("\n" + "="*50)
    print("TREE PROPERTIES ANALYSIS")
    print("="*50)
    
    # Create sample trees
    bst = BinarySearchTree()
    avl = AVLTree()
    
    # Add some data
    data = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
    for val in data:
        bst.insert(val)
        avl.insert(val)
    
    while True:
        print(f"\nTree Properties Analysis:")
        print("1. BST Property Validation")
        print("2. Tree Balance Analysis")
        print("3. Tree Metrics Comparison")
        print("4. Traversal Properties")
        print("5. Back to main menu")
        
        try:
            choice = int(input("\nEnter choice (1-5): "))
            
            if choice == 1:
                print("\nBST Property Validation:")
                print(f"BST is valid: {bst.is_valid_bst()}")
                print(f"AVL is valid: {avl.is_valid_bst()}")
                print("\nInorder traversal (should be sorted for valid BST):")
                print(f"BST: {bst.inorder_traversal()}")
                print(f"AVL: {avl.inorder_traversal()}")
                
            elif choice == 2:
                print("\nBalance Analysis:")
                print(f"BST balanced: {getattr(bst, 'is_balanced', lambda: 'N/A')()}")
                print(f"AVL balanced: {avl.is_balanced()}")
                print(f"BST height: {bst.get_height()}")
                print(f"AVL height: {avl.get_height()}")
                
                # Calculate balance factors if possible
                def get_balance_info(tree, name):
                    height = tree.get_height()
                    size = tree.get_size()
                    optimal_height = size.bit_length() - 1
                    balance_ratio = height / optimal_height if optimal_height > 0 else 0
                    
                    print(f"\n{name} Balance Info:")
                    print(f"  Height: {height}")
                    print(f"  Optimal height: {optimal_height}")
                    print(f"  Balance ratio: {balance_ratio:.2f}")
                    print(f"  Efficiency: {'Good' if balance_ratio < 1.5 else 'Poor'}")
                
                get_balance_info(bst, "BST")
                get_balance_info(avl, "AVL")
                
            elif choice == 3:
                print("\nTree Metrics Comparison:")
                
                metrics = [
                    ("Size", bst.get_size(), avl.get_size()),
                    ("Height", bst.get_height(), avl.get_height()),
                    ("Min Value", bst.find_min(), avl.find_min()),
                    ("Max Value", bst.find_max(), avl.find_max()),
                ]
                
                print(f"{'Metric':<12} {'BST':<8} {'AVL':<8}")
                print("-" * 30)
                for metric, bst_val, avl_val in metrics:
                    print(f"{metric:<12} {bst_val:<8} {avl_val:<8}")
                
            elif choice == 4:
                print("\nTraversal Properties:")
                
                traversals = [
                    ("Inorder", bst.inorder_traversal(), "Sorted order for BST"),
                    ("Preorder", bst.preorder_traversal(), "Root-first, good for copying"),
                    ("Postorder", bst.postorder_traversal(), "Children-first, good for deletion"),
                    ("Level-order", bst.level_order_traversal(), "Level by level, breadth-first"),
                ]
                
                for name, result, description in traversals:
                    print(f"\n{name}: {result}")
                    print(f"  Use case: {description}")
                
            elif choice == 5:
                break
                
            else:
                print("Invalid choice. Please try again.")
                
        except ValueError:
            print("Please enter a valid number.")


def main():
    """Main function to run the interactive demo."""
    print("Welcome to the Binary Tree Interactive Learning Tool!")
    print("This demo will help you understand binary tree operations and concepts.")
    
    while True:
        display_main_menu()
        
        try:
            choice = int(input("\nEnter your choice (1-9): "))
            
            if choice == 1:
                basic_binary_tree_demo()
            elif choice == 2:
                bst_demo()
            elif choice == 3:
                avl_tree_demo()
            elif choice == 4:
                traversal_visualization()
            elif choice == 5:
                expression_tree_calculator()
            elif choice == 6:
                decision_tree_example()
            elif choice == 7:
                performance_analysis()
            elif choice == 8:
                tree_properties_analysis()
            elif choice == 9:
                print("\nThank you for using the Binary Tree Demo!")
                print("Keep exploring tree structures and happy coding!")
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