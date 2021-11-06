from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    """
        ## Fields:
        ```py
        value: any
        left: Node | None
        right: Node | None
        ```
    """
    
    value: any
    left: Node | None
    right: Node | None
    
    __slots__ = "value", "left", "right"
    
    def insert(self, value: any) -> None:
        """
            Inserts a new `Node` into the `Node`.
            
            ## Example:
            ```py
            node = Node(value=1, left=None, right=None)
            node.insert(value=2)
            node.insert(value=3)
            assert node.value == 1
            assert node.right.value == 2
            assert node.right.right.value == 3
            ```
        """
        
        current, parent = self, None
        
        while current:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right
        
        if value < parent.value:
            parent.left = Node(value=value, left=None, right=None)
        else:
            parent.right = Node(value=value, left=None, right=None)
    
    def remove(self, value: any, root: Node) -> None:
        """
            Removes a `Node` containing the specified `value` from the sub-tree.
            
            ## Parameters:
            ```py
            value: any # Value of the Node to remove.
            root: Node # Normally should be set to `self`, only a parameter for recurssion.
            ```
            
            ## Example:
            ```py
            node = Node(value=1, left=None, right=None)
            node.insert(value=2)
            node.insert(value=3)
            node.insert(value=4)
            node.insert(value=5)
            node.remove(value=3, root=node)
            assert node.value == 1
            assert node.right.value == 2
            assert node.right.right.value == 4
            ```
        """
        
        if not root:
            return root
        
        if value < root.value:
            root.left = self.remove(value=value, root=root.left)
        elif value > root.value:
            root.right = self.remove(value=value, root=root.right)
        else:
            if not root.left and not root.right:
                return None
            elif root.left and root.right:
                predecessor: Node = root.left
                while predecessor.right:
                    predecessor = predecessor.right

                root.value = predecessor.value
                root.left = self.remove(value=predecessor.value, root=root.left)
            else:
                child: Node = root.left if root.left else root.right
                root = child
        
        return root


class BinaryTree:
    """
        ## Fields:
        ```py
        root: Node | None
        ```
    """
    
    root: Node | None
    
    __slots__ = "root"
    
    def __init__(self, from_list: list[any] = [  ]) -> None:
        """
            ## Parameters:
            ```py
            from_list: list[any] = [  ] # List to create Tree from through insertion.
            ```
        """
        
        self.root = None
        
        if len(from_list) != 0:
            for x in from_list:
                self.insert(x)
    
    def clear(self) -> None:
        """
            Clears all `Node`s within the `BinaryTree`.
            
            ## Example:
            ```py
            tree = BinaryTree()
            tree.insert(value=1)
            tree.insert(value=2)
            tree.insert(value=3)
            tree.clear()
            assert tree.root == None
            ```
        """
        
        self.root = None
    
    def insert(self, value: any) -> None:
        """
            Inserts a new `Node` into the `BinaryTree`.
            
            ## Example:
            ```py
            tree = BinaryTree()
            tree.insert(value=1)
            tree.insert(value=2)
            tree.insert(value=3)
            assert tree.root.value == 1
            assert tree.root.right.value == 2
            assert tree.root.right.right.value == 3
            ```
        """
        
        if self.root == None:
            self.root = Node(value=value, left=None, right=None)
            return
        
        self.root.insert(value=value)
    
    def remove(self, value: any) -> None:
        """
            Removes a `Node` containing the specified `value` from the tree.
            
            ## Example:
            ```py
            tree = BinaryTree(from_list=[1, 2, 3, 4, 5])
            tree.remove(value=3)
            assert tree.root.value == 1
            assert tree.root.right.value == 2
            assert tree.root.right.right.value == 4
            ```
        """
        
        self.root.remove(value=value, root=self.root)