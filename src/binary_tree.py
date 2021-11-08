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
    
    @staticmethod
    def remove(value: any, root: Node) -> None:
        """
            Removes a `Node` containing the specified `value` from the sub-tree.
            
            ## Parameters:
            ```py
            value: any # Value of the Node to remove.
            root: Node # Root Node of the sub-tree containg the Node you want to remove.
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
            root.left = Node.remove(value=value, root=root.left)
        elif value > root.value:
            root.right = Node.remove(value=value, root=root.right)
        else:
            if not root.left and not root.right:
                return None
            elif root.left and root.right:
                predecessor: Node = root.left
                while predecessor.right:
                    predecessor = predecessor.right

                root.value = predecessor.value
                root.left = Node.remove(value=predecessor.value, root=root.left)
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
    
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return_string = "["
        
        current: Node = self.root
        queue: list[Node] = [  ]
        
        while True:
            if current:
                queue.append(current)
                current = current.left
            elif queue:
                current = queue.pop(0)
                return_string += f"{current.value}, "
                current = current.right
            else:
                break
        
        return_string = return_string.removesuffix(", ")
        return return_string + "]"
    
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
    
    @staticmethod
    def invert(root: Node) -> None:
        """
            Inverts the tree, swapping every `Node` with its counter-part `left -> right | right -> left`.
            
            ## Example:
            ```py
            tree = BinaryTree()
            tree.root = Node(value=4, left=None, right=None)
            tree.root.left = Node(value=7, left=None, right=None)
            tree.root.right = Node(value=2, left=None, right=None)
            tree.invert(root=tree.root)
            assert tree.root.right.value == 7
            assert tree.root.left.value == 2
            ```
        """
        
        if not root:
            return
        
        temp: Node = root
        BinaryTree.invert(root=root.left)
        BinaryTree.invert(root=root.right)
        
        temp = root.left
        root.left = root.right
        root.right = temp