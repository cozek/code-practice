#!/usr/bin/env python3

from typing import Any,Deque,Union
from collections import deque


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.right = None
        self.left = None

    def is_childless(self) -> bool :
        if self.right is None and self.left is None:
            return True
        else:
            return False


class BinarySearchTree:
    def __init__(self) -> None:
        self.__root = None

    def insert(self, data: int) -> None:
        """Inserts data into the tree"""
        if self.__root is None:
            self.__root = Node(data)
        else:
            current = self.__root
            def loop(current:Node, data: int) -> None:
                if current.data == data:
                    return None
                if current.data > data :
                    if current.left is None:
                        current.left = Node(data)
                    else:
                        return loop(current.left,data)
                if current.data < data:
                    if current.right is None:
                        current.right = Node(data)
                    else:
                        return loop(current.right,data)
            loop(current,data)

    def in_order(self):
        """Prints the tree in-order
           Left Child - Node - Right Child
        """
        current = self.__root
        def loop(current: Node):
            if current is not None:
                loop(current.left)
                print(current.data)
                loop(current.right)
        loop(current)

    def post_order(self):
        """Prints the tree in-order
           Left Child - Node - Right Child
        """
        current = self.__root
        def loop(current: Node):
            if current is not None:
                loop(current.left)
                loop(current.right)
                print(current.data)

        loop(current)

    def pre_order(self):
        """Prints the tree in-order
           Left Child - Node - Right Child
        """
        current = self.__root
        def loop(current: Node):
            if current is not None:
                print(current.data)
                loop(current.left)
                loop(current.right)
        loop(current)



def main() -> None:
    tree = BinarySearchTree()
    datas = [8,20,5,1,6,22,21]
    [tree.insert(item) for item in datas]
    tree.pre_order()


if __name__ == "__main__":
    main()
