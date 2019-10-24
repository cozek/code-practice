#!/usr/bin/env python3

"""
This script implements code for finding the k-th element from the end of the
linked list.
"""

from linkedlist import LinkedList


class LinkedListMod(LinkedList):
    def __init__(self, data: list):
        super().__init__(data)

    def __str__(self):
        return super().__str__()

    def delele_from_end(self, k):
        """
        Deletes third element from the end of the LinkedList
        """

        ptr_1 = self.head
        ptr_2 = self.head

        distance = 0
        while distance != k:
            ptr_2 = ptr_2.next_node
            if ptr_2 == None:
                print(f"Cannot be done")
                return

            distance += 1

        if ptr_2.next_node is None:
            self.head = self.head.next_node
        else:
            prev = None
            while ptr_2.next_node is not None:
                print("p")
                prev = ptr_1
                ptr_1 = ptr_1.next_node
                ptr_2 = ptr_2.next_node

            prev.next_node = ptr_1.next_node
            del ptr_1


def main():
    data = [1, 3]

    mylinkedlist = LinkedListMod(data)
    print(mylinkedlist)
    mylinkedlist.delele_from_end(1)
    print(mylinkedlist)


if __name__ == "__main__":
    main()
