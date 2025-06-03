"""
Binary Tree Implementation

This module provides comprehensive implementations of binary tree data structures
including Binary Tree, Binary Search Tree, and AVL Tree with all essential operations.
"""

from typing import Any, Optional, List, Callable
from collections import deque


class TreeNode:
    """
    Node class for binary tree structures.
    
    Attributes:
        data: The data stored in the node
        left: Reference to the left child
        right: Reference to the right child
        parent: Reference to the parent node (optional)
    """
    
    def __init__(self, data: Any) -> None:
        """Initialize a new tree node."""
        self.data = data
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None
        self.parent: Optional['TreeNode'] = None
    
    def __str__(self) -> str:
        """String representation of the node."""
        return str(self.data)


class BinaryTree:
    """
    Binary Tree implementation with traversal and basic operations.
    
    A binary tree is a tree data structure where each node has at most
    two children, referred to as left and right child.
    
    Time Complexities:
    - Search: O(n) worst case
    - Insert: O(n) worst case
    - Delete: O(n) worst case
    - Traversals: O(n)
    
    Space Complexity: O(n) for storage, O(h) for recursion where h is height
    """
    
    def __init__(self, root_data: Any = None) -> None:
        """Initialize binary tree with optional root data."""
        self.root: Optional[TreeNode] = TreeNode(root_data) if root_data is not None else None
        self.size: int = 1 if root_data is not None else 0
    
    def is_empty(self) -> bool:
        """Check if tree is empty."""
        return self.root is None
    
    def get_size(self) -> int:
        """Get the number of nodes in the tree."""
        return self.size
    
    def get_height(self, node: Optional[TreeNode] = None) -> int:
        """
        Get the height of the tree or subtree.
        
        Args:
            node: Root of subtree (uses tree root if None)
            
        Returns:
            int: Height of the tree/subtree
            
        Time Complexity: O(n)
        """
        if node is None:
            node = self.root
        
        if node is None:
            return -1
        
        if node.left is None and node.right is None:
            return 0
        
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        
        return max(left_height, right_height) + 1
    
    def insert_left(self, parent_data: Any, data: Any) -> bool:
        """
        Insert a new node as the left child of a parent node.
        
        Args:
            parent_data: Data of the parent node
            data: Data for the new node
            
        Returns:
            bool: True if insertion successful, False if parent not found
            
        Time Complexity: O(n)
        """
        parent_node = self._find_node(parent_data)
        if parent_node is None:
            return False
        
        if parent_node.left is not None:
            # If left child exists, make it the left child of new node
            new_node = TreeNode(data)
            new_node.left = parent_node.left
            parent_node.left.parent = new_node
            parent_node.left = new_node
            new_node.parent = parent_node
        else:
            parent_node.left = TreeNode(data)
            parent_node.left.parent = parent_node
        
        self.size += 1
        return True
    
    def insert_right(self, parent_data: Any, data: Any) -> bool:
        """
        Insert a new node as the right child of a parent node.
        
        Args:
            parent_data: Data of the parent node
            data: Data for the new node
            
        Returns:
            bool: True if insertion successful, False if parent not found
            
        Time Complexity: O(n)
        """
        parent_node = self._find_node(parent_data)
        if parent_node is None:
            return False
        
        if parent_node.right is not None:
            # If right child exists, make it the right child of new node
            new_node = TreeNode(data)
            new_node.right = parent_node.right
            parent_node.right.parent = new_node
            parent_node.right = new_node
            new_node.parent = parent_node
        else:
            parent_node.right = TreeNode(data)
            parent_node.right.parent = parent_node
        
        self.size += 1
        return True
    
    def _find_node(self, data: Any) -> Optional[TreeNode]:
        """
        Find a node with the given data using level-order traversal.
        
        Args:
            data: Data to search for
            
        Returns:
            TreeNode: Node with the data, or None if not found
            
        Time Complexity: O(n)
        """
        if self.root is None:
            return None
        
        queue = deque([self.root])
        
        while queue:
            current = queue.popleft()
            
            if current.data == data:
                return current
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return None
    
    def search(self, data: Any) -> bool:
        """
        Search for a value in the tree.
        
        Args:
            data: Value to search for
            
        Returns:
            bool: True if found, False otherwise
            
        Time Complexity: O(n)
        """
        return self._find_node(data) is not None
    
    def delete(self, data: Any) -> bool:
        """
        Delete a node with the given data.
        
        Args:
            data: Data of the node to delete
            
        Returns:
            bool: True if deletion successful, False if not found
            
        Time Complexity: O(n)
        """
        node_to_delete = self._find_node(data)
        if node_to_delete is None:
            return False
        
        # Case 1: Node is a leaf
        if node_to_delete.left is None and node_to_delete.right is None:
            if node_to_delete.parent:
                if node_to_delete.parent.left == node_to_delete:
                    node_to_delete.parent.left = None
                else:
                    node_to_delete.parent.right = None
            else:
                self.root = None
        
        # Case 2: Node has one child
        elif node_to_delete.left is None or node_to_delete.right is None:
            child = node_to_delete.left if node_to_delete.left else node_to_delete.right
            
            if node_to_delete.parent:
                if node_to_delete.parent.left == node_to_delete:
                    node_to_delete.parent.left = child
                else:
                    node_to_delete.parent.right = child
                child.parent = node_to_delete.parent
            else:
                self.root = child
                child.parent = None
        
        # Case 3: Node has two children
        else:
            # Find inorder successor (leftmost node in right subtree)
            successor = self._find_min_node(node_to_delete.right)
            
            # Replace node's data with successor's data
            node_to_delete.data = successor.data
            
            # Delete the successor (which has at most one child)
            if successor.parent.left == successor:
                successor.parent.left = successor.right
            else:
                successor.parent.right = successor.right
            
            if successor.right:
                successor.right.parent = successor.parent
        
        self.size -= 1
        return True
    
    def _find_min_node(self, node: TreeNode) -> TreeNode:
        """Find the node with minimum value in a subtree."""
        while node.left:
            node = node.left
        return node
    
    # Traversal Methods
    
    def inorder_traversal(self, node: Optional[TreeNode] = None) -> List[Any]:
        """
        Perform inorder traversal (Left, Root, Right).
        
        Args:
            node: Starting node (uses root if None)
            
        Returns:
            List[Any]: List of values in inorder
            
        Time Complexity: O(n)
        """
        if node is None:
            node = self.root
        
        result = []
        self._inorder_helper(node, result)
        return result
    
    def _inorder_helper(self, node: Optional[TreeNode], result: List[Any]) -> None:
        """Helper method for inorder traversal."""
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.data)
            self._inorder_helper(node.right, result)
    
    def preorder_traversal(self, node: Optional[TreeNode] = None) -> List[Any]:
        """
        Perform preorder traversal (Root, Left, Right).
        
        Args:
            node: Starting node (uses root if None)
            
        Returns:
            List[Any]: List of values in preorder
            
        Time Complexity: O(n)
        """
        if node is None:
            node = self.root
        
        result = []
        self._preorder_helper(node, result)
        return result
    
    def _preorder_helper(self, node: Optional[TreeNode], result: List[Any]) -> None:
        """Helper method for preorder traversal."""
        if node:
            result.append(node.data)
            self._preorder_helper(node.left, result)
            self._preorder_helper(node.right, result)
    
    def postorder_traversal(self, node: Optional[TreeNode] = None) -> List[Any]:
        """
        Perform postorder traversal (Left, Right, Root).
        
        Args:
            node: Starting node (uses root if None)
            
        Returns:
            List[Any]: List of values in postorder
            
        Time Complexity: O(n)
        """
        if node is None:
            node = self.root
        
        result = []
        self._postorder_helper(node, result)
        return result
    
    def _postorder_helper(self, node: Optional[TreeNode], result: List[Any]) -> None:
        """Helper method for postorder traversal."""
        if node:
            self._postorder_helper(node.left, result)
            self._postorder_helper(node.right, result)
            result.append(node.data)
    
    def level_order_traversal(self) -> List[Any]:
        """
        Perform level-order traversal (breadth-first).
        
        Returns:
            List[Any]: List of values in level order
            
        Time Complexity: O(n)
        """
        if self.root is None:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            current = queue.popleft()
            result.append(current.data)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return result
    
    def display_tree(self) -> None:
        """Display tree in a visual format."""
        if self.root is None:
            print("Empty tree")
            return
        
        lines, *_ = self._display_aux(self.root)
        for line in lines:
            print(line)
    
    def _display_aux(self, node: Optional[TreeNode]):
        """Auxiliary method for tree display."""
        if node is None:
            return [], 0, 0, 0
        
        if node.left is None and node.right is None:
            line = str(node.data)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle
        
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = str(node.data)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = str(node.data)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = str(node.data)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class BinarySearchTree(BinaryTree):
    """
    Binary Search Tree implementation extending Binary Tree.
    
    BST maintains the property that for any node:
    - All nodes in left subtree have values less than the node
    - All nodes in right subtree have values greater than the node
    
    Time Complexities (average case):
    - Search: O(log n)
    - Insert: O(log n)
    - Delete: O(log n)
    
    Time Complexities (worst case - unbalanced):
    - Search: O(n)
    - Insert: O(n)
    - Delete: O(n)
    """
    
    def __init__(self) -> None:
        """Initialize empty BST."""
        super().__init__()
    
    def insert(self, data: Any) -> None:
        """
        Insert a value into the BST maintaining BST property.
        
        Args:
            data: Value to insert
            
        Time Complexity: O(log n) average, O(n) worst case
        """
        if self.root is None:
            self.root = TreeNode(data)
            self.size = 1
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node: TreeNode, data: Any) -> TreeNode:
        """Recursive helper for insertion."""
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
                node.left.parent = node
                self.size += 1
            else:
                self._insert_recursive(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = TreeNode(data)
                node.right.parent = node
                self.size += 1
            else:
                self._insert_recursive(node.right, data)
        # If data == node.data, we don't insert (no duplicates)
        
        return node
    
    def search(self, data: Any) -> bool:
        """
        Search for a value in the BST.
        
        Args:
            data: Value to search for
            
        Returns:
            bool: True if found, False otherwise
            
        Time Complexity: O(log n) average, O(n) worst case
        """
        return self._search_recursive(self.root, data) is not None
    
    def _search_recursive(self, node: Optional[TreeNode], data: Any) -> Optional[TreeNode]:
        """Recursive helper for search."""
        if node is None or node.data == data:
            return node
        
        if data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
    
    def delete(self, data: Any) -> bool:
        """
        Delete a value from the BST.
        
        Args:
            data: Value to delete
            
        Returns:
            bool: True if deletion successful, False if not found
            
        Time Complexity: O(log n) average, O(n) worst case
        """
        if self.root is None:
            return False
        
        self.root = self._delete_recursive(self.root, data)
        return True
    
    def _delete_recursive(self, node: Optional[TreeNode], data: Any) -> Optional[TreeNode]:
        """Recursive helper for deletion."""
        if node is None:
            return node
        
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Node to be deleted found
            self.size -= 1
            
            # Case 1: Node has no children
            if node.left is None and node.right is None:
                return None
            
            # Case 2: Node has one child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Case 3: Node has two children
            else:
                # Find inorder successor (smallest in right subtree)
                successor = self._find_min_node(node.right)
                node.data = successor.data
                node.right = self._delete_recursive(node.right, successor.data)
        
        return node
    
    def find_min(self) -> Optional[Any]:
        """
        Find minimum value in the BST.
        
        Returns:
            Any: Minimum value, or None if tree is empty
            
        Time Complexity: O(log n) average, O(n) worst case
        """
        if self.root is None:
            return None
        
        return self._find_min_node(self.root).data
    
    def find_max(self) -> Optional[Any]:
        """
        Find maximum value in the BST.
        
        Returns:
            Any: Maximum value, or None if tree is empty
            
        Time Complexity: O(log n) average, O(n) worst case
        """
        if self.root is None:
            return None
        
        node = self.root
        while node.right:
            node = node.right
        return node.data
    
    def find_predecessor(self, data: Any) -> Optional[Any]:
        """
        Find the predecessor (largest value smaller than given value).
        
        Args:
            data: Value to find predecessor for
            
        Returns:
            Any: Predecessor value, or None if not found
        """
        node = self._search_recursive(self.root, data)
        if node is None:
            return None
        
        # If left subtree exists, predecessor is the max in left subtree
        if node.left:
            return self._find_max_in_subtree(node.left)
        
        # Otherwise, predecessor is the nearest ancestor whose right child
        # is also an ancestor of the current node
        ancestor = node.parent
        while ancestor and node == ancestor.left:
            node = ancestor
            ancestor = ancestor.parent
        
        return ancestor.data if ancestor else None
    
    def find_successor(self, data: Any) -> Optional[Any]:
        """
        Find the successor (smallest value larger than given value).
        
        Args:
            data: Value to find successor for
            
        Returns:
            Any: Successor value, or None if not found
        """
        node = self._search_recursive(self.root, data)
        if node is None:
            return None
        
        # If right subtree exists, successor is the min in right subtree
        if node.right:
            return self._find_min_node(node.right).data
        
        # Otherwise, successor is the nearest ancestor whose left child
        # is also an ancestor of the current node
        ancestor = node.parent
        while ancestor and node == ancestor.right:
            node = ancestor
            ancestor = ancestor.parent
        
        return ancestor.data if ancestor else None
    
    def _find_max_in_subtree(self, node: TreeNode) -> Any:
        """Find maximum value in a subtree."""
        while node.right:
            node = node.right
        return node.data
    
    def is_valid_bst(self) -> bool:
        """
        Check if the tree satisfies BST property.
        
        Returns:
            bool: True if valid BST, False otherwise
            
        Time Complexity: O(n)
        """
        return self._is_valid_bst_helper(self.root, float('-inf'), float('inf'))
    
    def _is_valid_bst_helper(self, node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
        """Helper method for BST validation."""
        if node is None:
            return True
        
        if node.data <= min_val or node.data >= max_val:
            return False
        
        return (self._is_valid_bst_helper(node.left, min_val, node.data) and
                self._is_valid_bst_helper(node.right, node.data, max_val))


class AVLNode(TreeNode):
    """Node class for AVL Tree with height information."""
    
    def __init__(self, data: Any) -> None:
        """Initialize AVL node with height."""
        super().__init__(data)
        self.height: int = 1


class AVLTree(BinarySearchTree):
    """
    AVL Tree implementation - self-balancing binary search tree.
    
    AVL tree maintains balance by ensuring that for every node,
    the heights of left and right subtrees differ by at most 1.
    
    Time Complexities (guaranteed):
    - Search: O(log n)
    - Insert: O(log n)
    - Delete: O(log n)
    
    Space Complexity: O(n)
    """
    
    def __init__(self) -> None:
        """Initialize empty AVL tree."""
        super().__init__()
    
    def _get_height(self, node: Optional[AVLNode]) -> int:
        """Get height of a node."""
        if node is None:
            return 0
        return node.height
    
    def _get_balance(self, node: Optional[AVLNode]) -> int:
        """Get balance factor of a node."""
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _update_height(self, node: AVLNode) -> None:
        """Update height of a node."""
        node.height = max(self._get_height(node.left), 
                         self._get_height(node.right)) + 1
    
    def _rotate_right(self, y: AVLNode) -> AVLNode:
        """Perform right rotation."""
        x = y.left
        T2 = x.right
        
        # Perform rotation
        x.right = y
        y.left = T2
        
        # Update heights
        self._update_height(y)
        self._update_height(x)
        
        # Return new root
        return x
    
    def _rotate_left(self, x: AVLNode) -> AVLNode:
        """Perform left rotation."""
        y = x.right
        T2 = y.left
        
        # Perform rotation
        y.left = x
        x.right = T2
        
        # Update heights
        self._update_height(x)
        self._update_height(y)
        
        # Return new root
        return y
    
    def insert(self, data: Any) -> None:
        """
        Insert a value into the AVL tree.
        
        Args:
            data: Value to insert
            
        Time Complexity: O(log n)
        """
        if self.root is None:
            self.root = AVLNode(data)
            self.size = 1
        else:
            self.root = self._insert_avl(self.root, data)
    
    def _insert_avl(self, node: Optional[AVLNode], data: Any) -> AVLNode:
        """Recursive helper for AVL insertion with balancing."""
        # Step 1: Perform normal BST insertion
        if node is None:
            self.size += 1
            return AVLNode(data)
        
        if data < node.data:
            node.left = self._insert_avl(node.left, data)
        elif data > node.data:
            node.right = self._insert_avl(node.right, data)
        else:
            # Duplicate values not allowed
            return node
        
        # Step 2: Update height of current node
        self._update_height(node)
        
        # Step 3: Get balance factor
        balance = self._get_balance(node)
        
        # Step 4: If unbalanced, perform rotations
        
        # Left Left Case
        if balance > 1 and data < node.left.data:
            return self._rotate_right(node)
        
        # Right Right Case
        if balance < -1 and data > node.right.data:
            return self._rotate_left(node)
        
        # Left Right Case
        if balance > 1 and data > node.left.data:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Right Left Case
        if balance < -1 and data < node.right.data:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        # Return unchanged node
        return node
    
    def delete(self, data: Any) -> bool:
        """
        Delete a value from the AVL tree.
        
        Args:
            data: Value to delete
            
        Returns:
            bool: True if deletion successful
            
        Time Complexity: O(log n)
        """
        if self.root is None:
            return False
        
        initial_size = self.size
        self.root = self._delete_avl(self.root, data)
        return self.size < initial_size
    
    def _delete_avl(self, node: Optional[AVLNode], data: Any) -> Optional[AVLNode]:
        """Recursive helper for AVL deletion with balancing."""
        # Step 1: Perform normal BST deletion
        if node is None:
            return node
        
        if data < node.data:
            node.left = self._delete_avl(node.left, data)
        elif data > node.data:
            node.right = self._delete_avl(node.right, data)
        else:
            # Node to be deleted
            self.size -= 1
            
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children
            successor = self._find_min_node(node.right)
            node.data = successor.data
            node.right = self._delete_avl(node.right, successor.data)
        
        # Step 2: Update height
        self._update_height(node)
        
        # Step 3: Get balance factor
        balance = self._get_balance(node)
        
        # Step 4: If unbalanced, perform rotations
        
        # Left Left Case
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)
        
        # Left Right Case
        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Right Right Case
        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)
        
        # Right Left Case
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def is_balanced(self) -> bool:
        """
        Check if the tree is balanced (satisfies AVL property).
        
        Returns:
            bool: True if balanced, False otherwise
        """
        return self._is_balanced_helper(self.root)
    
    def _is_balanced_helper(self, node: Optional[AVLNode]) -> bool:
        """Helper method for balance checking."""
        if node is None:
            return True
        
        balance = self._get_balance(node)
        
        return (abs(balance) <= 1 and 
                self._is_balanced_helper(node.left) and 
                self._is_balanced_helper(node.right))
