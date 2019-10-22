#!/usr/bin/env python3


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self, data: int):
        self.head = Node(data)

    def append(self, data: int):
        current = self.head
        while current.next_node != None:
            current = current.next_node
        current.next_node = Node(data)
        new_node = current.next_node

    def __str__(self) -> str:
        current = self.head
        string = f'[ HEAD {current.data} ] -> '
        while current.next_node != None:
            current = current.next_node
            string += f'{current.data.__str__()} -> '

        return string +'END'

