"""
Binary Tree Usage Examples

This module demonstrates practical usage of binary tree implementations
with real-world scenarios and comprehensive test cases.
"""

from implementation import BinaryTree, BinarySearchTree, AVLTree


def test_binary_tree_operations():
    """Test basic operations of binary tree."""
    print("=== Testing Binary Tree Operations ===\n")
    
    # Create a binary tree
    bt = BinaryTree(1)
    print(f"Created binary tree with root: {bt.root.data}")
    print(f"Tree size: {bt.get_size()}")
    print(f"Tree height: {bt.get_height()}")
    print(f"Is empty: {bt.is_empty()}")
    
    # Insert nodes manually
    print("\n--- Manual Tree Construction ---")
    bt.insert_left(1, 2)
    bt.insert_right(1, 3)
    bt.insert_left(2, 4)
    bt.insert_right(2, 5)
    bt.insert_left(3, 6)
    bt.insert_right(3, 7)
    
    print(f"After insertions - Size: {bt.get_size()}, Height: {bt.get_height()}")
    
    # Display tree structure
    print("\nTree Structure:")
    bt.display_tree()
    
    # Test traversals
    print("\n--- Tree Traversals ---")
    print(f"Inorder (Left-Root-Right): {bt.inorder_traversal()}")
    print(f"Preorder (Root-Left-Right): {bt.preorder_traversal()}")
    print(f"Postorder (Left-Right-Root): {bt.postorder_traversal()}")
    print(f"Level-order (Breadth-first): {bt.level_order_traversal()}")
    
    # Test search
    print("\n--- Search Operations ---")
    print(f"Search for 5: {bt.search(5)}")
    print(f"Search for 10: {bt.search(10)}")
    
    # Test deletion
    print("\n--- Deletion Operations ---")
    print(f"Delete node 5: {bt.delete(5)}")
    print(f"Tree after deletion:")
    bt.display_tree()
    print(f"Size after deletion: {bt.get_size()}")


def test_binary_search_tree_operations():
    """Test operations of binary search tree."""
    print("\n=== Testing Binary Search Tree Operations ===\n")
    
    # Create BST and insert values
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
    
    print(f"Inserting values: {values}")
    for value in values:
        bst.insert(value)
    
    print(f"\nBST after insertions - Size: {bst.get_size()}, Height: {bst.get_height()}")
    
    # Display tree
    print("\nBST Structure:")
    bst.display_tree()
    
    # Test BST property
    print(f"\nIs valid BST: {bst.is_valid_bst()}")
    
    # Test traversals (inorder should be sorted for BST)
    print("\n--- BST Traversals ---")
    print(f"Inorder (should be sorted): {bst.inorder_traversal()}")
    print(f"Preorder: {bst.preorder_traversal()}")
    print(f"Level-order: {bst.level_order_traversal()}")
    
    # Test search operations
    print("\n--- Search Operations ---")
    search_values = [45, 25, 100, 10]
    for val in search_values:
        print(f"Search for {val}: {bst.search(val)}")
    
    # Test min/max operations
    print(f"\nMinimum value: {bst.find_min()}")
    print(f"Maximum value: {bst.find_max()}")
    
    # Test predecessor/successor
    print(f"Predecessor of 40: {bst.find_predecessor(40)}")
    print(f"Successor of 40: {bst.find_successor(40)}")
    
    # Test deletions
    print("\n--- Deletion Operations ---")
    delete_values = [10, 30, 50]  # leaf, one child, two children
    for val in delete_values:
        print(f"\nDeleting {val}:")
        success = bst.delete(val)
        print(f"Deletion successful: {success}")
        print(f"Inorder after deletion: {bst.inorder_traversal()}")
        print(f"Is still valid BST: {bst.is_valid_bst()}")


def test_avl_tree_operations():
    """Test operations of AVL tree."""
    print("\n=== Testing AVL Tree Operations ===\n")
    
    # Create AVL tree
    avl = AVLTree()
    values = [10, 20, 30, 40, 50, 25]  # This would cause imbalance in regular BST
    
    print(f"Inserting values (watch for rotations): {values}")
    for value in values:
        print(f"\nInserting {value}:")
        avl.insert(value)
        print(f"Tree height: {avl.get_height()}")
        print(f"Is balanced: {avl.is_balanced()}")
        avl.display_tree()
    
    print(f"\nFinal AVL Tree:")
    print(f"Size: {avl.get_size()}, Height: {avl.get_height()}")
    print(f"Is balanced: {avl.is_balanced()}")
    print(f"Inorder traversal: {avl.inorder_traversal()}")
    
    # Test deletions with rebalancing
    print("\n--- AVL Deletion with Rebalancing ---")
    delete_values = [40, 30]
    for val in delete_values:
        print(f"\nDeleting {val}:")
        success = avl.delete(val)
        print(f"Deletion successful: {success}")
        print(f"Height after deletion: {avl.get_height()}")
        print(f"Is balanced: {avl.is_balanced()}")
        avl.display_tree()


def real_world_example_file_system():
    """
    Demonstrate binary tree usage in file system representation.
    """
    print("\n=== Real-World Example: File System Structure ===\n")
    
    class FileSystemNode:
        """Represents a file or directory in the file system."""
        
        def __init__(self, name: str, is_directory: bool = False, size: int = 0):
            self.name = name
            self.is_directory = is_directory
            self.size = size
        
        def __str__(self):
            type_icon = "📁" if self.is_directory else "📄"
            size_info = f" ({self.size}KB)" if not self.is_directory else ""
            return f"{type_icon} {self.name}{size_info}"
    
    # Create file system tree
    fs_tree = BinaryTree(FileSystemNode("root", True))
    
    # Build directory structure
    # root/
    # ├── documents/
    # │   ├── report.pdf
    # │   └── presentation.pptx
    # └── projects/
    #     ├── code.py
    #     └── readme.txt
    
    print("Building file system structure:")
    fs_tree.insert_left("root", FileSystemNode("documents", True))
    fs_tree.insert_right("root", FileSystemNode("projects", True))
    fs_tree.insert_left("documents", FileSystemNode("report.pdf", False, 2500))
    fs_tree.insert_right("documents", FileSystemNode("presentation.pptx", False, 1800))
    fs_tree.insert_left("projects", FileSystemNode("code.py", False, 150))
    fs_tree.insert_right("projects", FileSystemNode("readme.txt", False, 50))
    
    print("\nFile System Tree Structure:")
    
    def display_file_system(traversal_order):
        """Display file system in different orders."""
        if traversal_order == "preorder":
            items = fs_tree.preorder_traversal()
            print("Directory listing (depth-first):")
        elif traversal_order == "level":
            items = fs_tree.level_order_traversal()
            print("Directory listing (breadth-first):")
        
        for item in items:
            print(f"  {item}")
    
    display_file_system("preorder")
    print()
    display_file_system("level")


def real_world_example_expression_tree():
    """
    Demonstrate binary tree usage in mathematical expression evaluation.
    """
    print("\n=== Real-World Example: Expression Tree ===\n")
    
    class ExpressionTree(BinaryTree):
        """Binary tree for mathematical expressions."""
        
        def __init__(self, expression_root=None):
            super().__init__(expression_root)
        
        def evaluate(self, node=None):
            """Evaluate the mathematical expression."""
            if node is None:
                node = self.root
            
            if node is None:
                return 0
            
            # If it's a number (leaf node)
            if node.left is None and node.right is None:
                try:
                    return float(node.data)
                except ValueError:
                    return 0
            
            # Evaluate left and right subtrees
            left_val = self.evaluate(node.left)
            right_val = self.evaluate(node.right)
            
            # Apply operator
            if node.data == '+':
                return left_val + right_val
            elif node.data == '-':
                return left_val - right_val
            elif node.data == '*':
                return left_val * right_val
            elif node.data == '/':
                return left_val / right_val if right_val != 0 else float('inf')
            
            return 0
        
        def to_infix(self, node=None):
            """Convert expression tree to infix notation."""
            if node is None:
                node = self.root
            
            if node is None:
                return ""
            
            # If it's a number (leaf node)
            if node.left is None and node.right is None:
                return str(node.data)
            
            # Build infix expression with parentheses
            left_expr = self.to_infix(node.left)
            right_expr = self.to_infix(node.right)
            
            return f"({left_expr} {node.data} {right_expr})"
    
    # Build expression tree for: (3 + 5) * (2 - 1)
    print("Building expression tree for: (3 + 5) * (2 - 1)")
    
    expr_tree = ExpressionTree('*')
    expr_tree.insert_left('*', '+')
    expr_tree.insert_right('*', '-')
    expr_tree.insert_left('+', '3')
    expr_tree.insert_right('+', '5')
    expr_tree.insert_left('-', '2')
    expr_tree.insert_right('-', '1')
    
    print("\nExpression Tree Structure:")
    expr_tree.display_tree()
    
    print(f"\nInfix notation: {expr_tree.to_infix()}")
    print(f"Evaluation result: {expr_tree.evaluate()}")
    
    # Show different traversals
    print(f"\nPreorder (prefix): {expr_tree.preorder_traversal()}")
    print(f"Inorder (infix components): {expr_tree.inorder_traversal()}")
    print(f"Postorder (postfix): {expr_tree.postorder_traversal()}")


def real_world_example_decision_tree():
    """
    Demonstrate binary tree usage in decision making.
    """
    print("\n=== Real-World Example: Decision Tree ===\n")
    
    class DecisionNode:
        """Node for decision tree."""
        
        def __init__(self, question: str, true_answer: str = None, false_answer: str = None):
            self.question = question
            self.true_answer = true_answer
            self.false_answer = false_answer
        
        def __str__(self):
            return self.question
        
        def is_leaf(self):
            return self.true_answer is not None and self.false_answer is not None
    
    # Build decision tree for weekend activity recommendation
    print("Building decision tree for weekend activity recommendation:")
    
    dt = BinaryTree(DecisionNode("Is it sunny outside?"))
    
    # Build decision tree structure
    dt.insert_left("Is it sunny outside?", DecisionNode("Do you like outdoor activities?"))
    dt.insert_right("Is it sunny outside?", DecisionNode("Do you enjoy reading?"))
    
    dt.insert_left("Do you like outdoor activities?", 
                   DecisionNode("Perfect weather!", "Go hiking or to the park!", "Try indoor rock climbing!"))
    dt.insert_right("Do you like outdoor activities?", 
                    DecisionNode("Rainy day activities", "Visit a museum or cafe!", "Watch movies at home!"))
    
    dt.insert_left("Do you enjoy reading?", 
                   DecisionNode("Cozy day!", "Read a book with tea!", "Try cooking a new recipe!"))
    dt.insert_right("Do you enjoy reading?", 
                    DecisionNode("Active indoor day", "Go to the gym or yoga!", "Learn something new online!"))
    
    print("\nDecision Tree Structure:")
    dt.display_tree()
    
    print("\nDecision paths (all possible outcomes):")
    
    def show_decision_paths(node, path="", indent=0):
        """Show all possible decision paths."""
        if node is None:
            return
        
        current_path = path + ("→ " if path else "") + str(node.data)
        print("  " * indent + current_path)
        
        if hasattr(node.data, 'is_leaf') and node.data.is_leaf():
            print("  " * (indent + 1) + f"✓ YES: {node.data.true_answer}")
            print("  " * (indent + 1) + f"✗ NO: {node.data.false_answer}")
        else:
            if node.left:
                print("  " * (indent + 1) + "YES:")
                show_decision_paths(node.left, current_path, indent + 2)
            if node.right:
                print("  " * (indent + 1) + "NO:")
                show_decision_paths(node.right, current_path, indent + 2)
    
    show_decision_paths(dt.root)


def performance_comparison():
    """Compare performance characteristics of different tree types."""
    print("\n=== Performance Comparison ===\n")
    
    import time
    import random
    
    # Generate test data
    test_size = 1000
    test_data = list(range(test_size))
    random.shuffle(test_data)
    search_data = random.sample(test_data, 100)
    
    print(f"Performance test with {test_size} elements:")
    
    # Test BST
    print("\n--- Binary Search Tree ---")
    bst = BinarySearchTree()
    
    start_time = time.time()
    for value in test_data:
        bst.insert(value)
    bst_insert_time = time.time() - start_time
    
    start_time = time.time()
    for value in search_data:
        bst.search(value)
    bst_search_time = time.time() - start_time
    
    print(f"Insert time: {bst_insert_time:.4f} seconds")
    print(f"Search time (100 queries): {bst_search_time:.4f} seconds")
    print(f"Final height: {bst.get_height()} (optimal: {int(test_size.bit_length()) - 1})")
    
    # Test AVL Tree
    print("\n--- AVL Tree ---")
    avl = AVLTree()
    
    start_time = time.time()
    for value in test_data:
        avl.insert(value)
    avl_insert_time = time.time() - start_time
    
    start_time = time.time()
    for value in search_data:
        avl.search(value)
    avl_search_time = time.time() - start_time
    
    print(f"Insert time: {avl_insert_time:.4f} seconds")
    print(f"Search time (100 queries): {avl_search_time:.4f} seconds")
    print(f"Final height: {avl.get_height()} (optimal: {int(test_size.bit_length()) - 1})")
    
    # Comparison
    print(f"\n--- Comparison ---")
    print(f"AVL insert is {avl_insert_time/bst_insert_time:.2f}x the time of BST")
    print(f"AVL search is {avl_search_time/bst_search_time:.2f}x the time of BST")
    print(f"AVL height is {avl.get_height()/bst.get_height():.2f}x BST height")
    
    print("\nNote: AVL trees maintain balance, ensuring O(log n) operations")
    print("while unbalanced BSTs can degrade to O(n) in worst case.")


if __name__ == "__main__":
    test_binary_tree_operations()
    test_binary_search_tree_operations()
    test_avl_tree_operations()
    real_world_example_file_system()
    real_world_example_expression_tree()
    real_world_example_decision_tree()
    performance_comparison()