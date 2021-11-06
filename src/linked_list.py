from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    """
        ## Fields:
        ```py
        value: any
        next: Node | None
        prev: Node | None
        ```
    """
    
    value: any
    next: Node | None
    prev: Node | None


class LinkedList:
    """
        ## Fields:
        ```py
        head: Node | None
        tail: Node | None
        len: int
        ```
    """
    
    head: Node | None
    tail: Node | None
    len: int
    
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.len = 0
    
    def __len__(self) -> int:
        return self.len

    def push_front(self, value: any) -> None:
        """
            Pushes a new `Node` to the front of the list.
            
            ## Example:
            ```py
            linked_list = LinkedList()
            linked_list.push_front(value=1)
            linked_list.push_front(value=2)
            linked_list.push_front(value=3)
            assert len(linked_list) == 3
            assert linked_list.head.value == 3
            assert linked_list.tail.value == 1
            ```
        """
        
        if self.head == None:
            self.head = Node(value=value, next=None, prev=None)
            self.tail = self.head
        else:
            new_node = Node(value=value, next=self.head, prev=None)
            self.head.prev = new_node
            self.head = new_node
        
        self.len += 1
    
    def push_back(self, value: any) -> None:
        """
            Pushes a new `Node` to the back of the list.
            
            ## Example:
            ```py
            linked_list = LinkedList()
            linked_list.push_back(value=1)
            linked_list.push_back(value=2)
            linked_list.push_back(value=3)
            assert len(linked_list) == 3
            assert linked_list.head.value == 1
            assert linked_list.tail.value == 3
            ```
        """
        
        if self.head == None:
            self.head = Node(value=value, next=None, prev=None)
            self.tail = self.head
        else:
            new_node = Node(value=value, next=None, prev=self.tail)
            self.tail.next = new_node
            self.tail = new_node
        
        self.len += 1