#!/usr/bin/env python3

from array import array

"""
implements stack using array
"""


class stack:
    def __init__(self, capacity: int) -> None:
        self.__array_stack = array("i", [0 for i in range(capacity)])
        self.__capacity = capacity
        self.__top = -1

    def __str__(self) -> str:
        top = self.__top
        if top == -1:
            return "Empty!"
        string = "TOP "
        while top != -1:
            string += f"{self.__array_stack[top]} -> "
            top = top - 1
        return string + "END"

    def push(self, item: int) -> None:
        if self.is_empty():
            self.__top = 0
            self.__array_stack[self.__top] = item
        elif self.is_full():
            raise Exception("Stack full")
        else:
            self.__top = self.__top + 1
            self.__array_stack[self.__top] = item

    def pop(self) -> int:
        if self.is_empty():
            raise Exception("Stack Empty")
        else:
            popped_item: int = self.__array_stack[self.__top]
            self.__top = self.__top - 1
            return popped_item

    def top(self) -> int:
        if self.is_empty():
            raise Exception("Stack Empty")
        else:
            return self.__array_stack[self.__top]

    def is_full(self) -> bool:
        if self.__top == self.__capacity - 1:
            return True
        else:
            return False

    def is_empty(self) -> bool:
        if self.__top == -1:
            return True
        else:
            return False


def main():
    stk: stack = stack(capacity=3)
    stk.push(1)
    print(stk)
    print("top", stk.top())


if __name__ == "__main__":
    main()
