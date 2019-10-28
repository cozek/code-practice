#!/usr/bin/env python3

from array import array
import math
from typing import NewType


class ArrayStack:
    def __init__(self, array_size: int, num_stacks: int):
        self.__array_stack = array("i", [0 for i in range(array_size)])
        self.num_stacks = num_stacks
        self.sizes = array("i", [0 for i in range(num_stacks)])
        self.stack_max_items = math.floor(array_size / num_stacks)

    def __str__(self) -> str:
        return str(self.__array_stack)

    def push(self, stack_num: int, data: int) -> None:
        stack_num -= 1  # indexing
        if self.is_full(stack_num):
            raise Exception("Stack Full!")
        else:
            index = self.get_index(stack_num)
            self.__array_stack[index] = data
            self.sizes[stack_num] += 1

    def top(self, stack_num: int) -> int:
        stack_num = stack_num - 1
        if self.sizes[stack_num] == 0:
            top_index = self.get_index(stack_num)
        else:
            top_index = self.get_index(stack_num) - 1
        return self.__array_stack[top_index]

    def pop(self, stack_num: int) -> int:
        stack_num = stack_num - 1
        if self.sizes[stack_num] == 0:
            raise ('Trying to pop empty stack!')
        else:
            top_index = self.get_index(stack_num) - 1
            popped_item = self.__array_stack[top_index]
            self.__array_stack[top_index] = 0
            self.sizes[stack_num] -= 1
            return popped_item

    def get_index(self, stack_num: int) -> int:
        return self.sizes[stack_num] + (self.stack_max_items * stack_num)

    def is_full(self, stack_num: int) -> bool:
        if self.sizes[stack_num] == self.stack_max_items:
            return True
        else:
            return False


def main():
    arr_stk = ArrayStack(10, 3)
    print(arr_stk)
    print(arr_stk.sizes)
    arr_stk.push(1, 11)
    print("1", arr_stk, arr_stk.sizes)
    arr_stk.push(1, 12)
    print("2", arr_stk, arr_stk.sizes)
    arr_stk.push(1, 13)
    print("3", arr_stk, arr_stk.sizes)

    arr_stk.push(2, 21)
    print("1", arr_stk, arr_stk.sizes)
    arr_stk.push(2, 22)
    print("2", arr_stk, arr_stk.sizes)
    arr_stk.push(2, 23)
    print("3", arr_stk, arr_stk.sizes)

    arr_stk.push(3, 31)
    print("1", arr_stk, arr_stk.sizes)
    arr_stk.push(3, 32)
    print("1", arr_stk, arr_stk.sizes)
    arr_stk.push(3, 33)
    print("1", arr_stk, arr_stk.sizes)

    print(arr_stk.top(3))

    pop:int = arr_stk.pop(3)
    print("pop",pop, arr_stk, arr_stk.sizes)



if __name__ == "__main__":
    main()
