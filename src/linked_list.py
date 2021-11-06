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
        root: Node | None
        ```
    """
    
    root: Node | None
    
    def __init__(self) -> None:
        self.root = None