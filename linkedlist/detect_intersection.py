#!/usr/bin/env python3
from linkedlist import LinkedList, Node

import random

random.seed(42)


class IntersectingLinkedList(LinkedList):
    def __init__(self, data_a: list, data_b: list):
        self.head_a = self.__build_list(data_a)
        self.head_b = self.__build_list(data_b)
        self.intersect()

    def intersect(self):
        intersection_point = 5
        current_b = self.head_b
        for i in range(intersection_point):
            current_b = current_b.next_node

        current_a = self.head_a
        while current_a.next_node != None:
            current_a = current_a.next_node
        current_a.next_node = current_b

    def __build_list(self, data: list):
        head = None
        for item in data:
            if head == None:
                head = Node(item)
                current = head
            else:
                current.next_node = Node(item)
                current = current.next_node
        current.next_node = None
        return head

    def get(self, head=None):
        if head == None:
            return
        elif head == "a":
            current = self.head_a
        elif head == "b":
            current = self.head_b

        def recurse(node, string=""):
            if node.next_node == None:
                string += f"{node.data} -> END"
                return string
            else:
                string += f"{node.data} -> "
                return recurse(node.next_node, string)

        return recurse(current)


class Detector:
    def __init__(self, head_a: Node, head_b: Node):
        self.head_a = head_a
        self.head_b = head_b

    def detect(self):
        current_a = self.head_a
        len_a = 1
        while current_a.next_node != None:
            len_a += 1
            current_a = current_a.next_node

        current_b = self.head_b
        len_b = 1
        while current_b.next_node != None:
            len_b += 1
            current_b = current_b.next_node

        if current_a != current_b:
            return f"No Intersections"

        ptr_a = self.head_a
        ptr_b = self.head_b
        if len_a > len_b:
            moves = len_a - len_b
            for move in range(moves):
                ptr_a = ptr_a.next_node
        elif len_b > len_a:
            moves = len_b - len_a
            for move in range(moves):
                ptr_b = ptr_b.next_node

        while id(ptr_a) != id(ptr_b):
            ptr_a = ptr_a.next_node
            ptr_b = ptr_b.next_node

        return f"Intersects at: {ptr_a}"


def main():
    data_a = [num for num in range(11, 18)]
    data_b = [random.randint(0, 10) for num in range(8)]
    print(f"{data_a}\n{data_b}")
    myll = IntersectingLinkedList(data_a, data_b)
    print(myll.get("a"))
    print(myll.get("b"))

    d = Detector(myll.head_a, myll.head_b)
    print(d.detect())

    myll2 = LinkedList([i for i in range(5)])
    myll3 = LinkedList([i for i in range(5)])
    d = Detector(myll2.head, myll3.head)
    print(d.detect())


if __name__ == "__main__":
    main()
