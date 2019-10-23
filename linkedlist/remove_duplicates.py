#!/usr/bin/env python3

from linkedlist import LinkedList

"""
This scripts implements code to remove duplicates from sorted and
unsorted linked list
"""


class LinkedListSorted(LinkedList):
    def __init__(self, data: list):
        super().__init__(data)

    def __str__(self):
        return super().__str__()

    def remove_duplicates(self):
        """removes duplicates"""
        unique_ptr = self.head
        ptr = self.head
        data_in_ptr = ptr.data
        while ptr.next_node is not None:
            ptr = ptr.next_node
            if ptr.data == data_in_ptr:
                continue
            else:
                data_in_ptr = ptr.data
                unique_ptr.next_node = ptr
                unique_ptr = ptr

class LinkedListUnsorted(LinkedList):
    def __init__(self, data: list):
        super().__init__(data)

    def __str__(self):
        return super().__str__()

    def remove_duplicates(self):
        """removes duplicates using a hashset"""
        hashset = set()
        ptr = self.head
        hashset.add(ptr.data)

        while ptr.next_node is not None:
            next = ptr.next_node
            if next.data in hashset:
                ptr.next_node = next.next_node
            else:
                ptr = ptr.next_node
                hashset.add(ptr.data)

    def remove_duplicates_nobuffer(self):
        """removes duplicates without a buffer"""
        ptr_1 = self.head
        ptr_2 = self.head

        while ptr_1 != None:
            unique = ptr_1.data
            while ptr_2 != None:
                next = ptr_2.next_node
                if next == None:
                    break
                if next.data == unique:
                    ptr_2.next_node = next.next_node
                ptr_2 = ptr_2.next_node
            ptr_1 = ptr_1.next_node
            ptr_2 = ptr_1


if __name__ == "__main__":
    data = [5,4,5,4,3,2,1,1,5,9,0,9]
    mylist = LinkedListUnsorted(data)
    print(mylist)
    mylist.remove_duplicates_nobuffer()
    print(mylist)
