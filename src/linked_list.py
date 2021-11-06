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
    
    def __init__(self, from_list: list[any] = [  ]) -> None:
        """
            ## Parameters:
            ```py
            from_list: list[any] = [  ] # List to create a LinkedList from.
            ```
        """
        
        self.head = None
        self.tail = None
        self.len = 0
        
        if len(from_list) != 0:
            for x in from_list:
                self.push_back(x)
    
    def __len__(self) -> int:
        return self.len
    
    def is_empty(self) -> bool:
        return self.head == None
    
    def clear(self) -> None:
        """
            Clears the linked list, removing all nodes and resetting its length to zero.
            
            ## Example:
            ```py
            linked_list = LinkedList(from_list=[1, 2, 3])
            linked_list.clear()
            assert len(linked_list) == 0
            assert linked_list.head == None
            assert linked_list.tail == None
            ```
        """
        
        self.head = None
        self.tail = None
        self.len = 0

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
    
    def append(self, other: LinkedList) -> None:
        """
            Appends a linked list to the end of this linked list, clearing the other list.
            ## Example:
            ```py
            linked_list_one = LinkedList(from_list=[1, 2, 3])
            linked_list_two = LinkedList(from_list=[4, 5, 6])

            linked_list_one.append(other=linked_list_two)
            
            assert len(linked_list_one) == 6
            assert linked_list_one.head.value == 1
            assert linked_list_one.tail.value == 6
            assert len(linked_list_two) == 0
            ```
        """
        
        if self.tail != None:
            self.tail.next = other.head
            other.head.prev = self.tail
            self.tail = other.tail
        else:
            self.head = other.head
            self.tail = other.tail
        self.len += len(other)
        other.clear()