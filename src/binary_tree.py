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


class BinaryTree:
    """
        ## Fields:
        ```py
        root: Node | None
        ```
    """
    
    root: Node | None
    
    __slots__ = "root"
    
    def __init__(self) -> None:
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