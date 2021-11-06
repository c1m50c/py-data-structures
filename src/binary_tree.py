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


class BinaryTree:
    """
        ## Fields:
        ```py
        root: Node | None
        ```
    """
    
    root: Node | None
    
    def __init__(self) -> None:
        self.root = None