#!/usr/bin/env python3


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self, data: list):
        self.head = None
        for item in data:
            if self.head == None:
                self.head = Node(item)
            else:
                self.append(item)

    def append(self, data: int):
        """Appends data to the LinkedList as a new node"""
        current = self.head
        while current.next_node != None:
            current = current.next_node
        current.next_node = Node(data)

    def reverse(self):
        """Reverses the LinkedList"""
        previous = self.head
        ptr = previous.next_node
        previous.next_node = None

        while ptr.next_node != None:
            print(previous.data, ptr.data)
            temp = ptr.next_node
            ptr.next_node = previous
            previous = ptr
            ptr = temp

        ptr.next_node = previous
        self.head = ptr

    def __str__(self):
        current = self.head
        def recurse(node,string = ''):
            if node.next_node == None:
                string += 'END'
                return string
            else:
                string += f'{node.data} -> '
                return recurse(node.next_node, string)
        return recurse(current)


if __name__ == "__main__":
    data = [num for num in range(9)]
    mylinkedlist = LinkedList(data)
    print(mylinkedlist)
