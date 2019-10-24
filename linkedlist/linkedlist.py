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

    def push(self, data: int):
        """Add item to the head of the LinkedList"""
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

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

    def __str__(self) -> str:
        current = self.head
        string = f"{current.data} -> "
        while current.next_node != None:
            current = current.next_node
            string += f"{current.data.__str__()} -> "
        return string + "END"


def main():
    data = [num for num in range(9)]
    mylinkedlist = LinkedList(data)
    print(mylinkedlist)
    mylinkedlist.push(20)
    print(mylinkedlist)
    mylinkedlist.append(15)
    print(mylinkedlist)


if __name__ == "__main__":
    main()
