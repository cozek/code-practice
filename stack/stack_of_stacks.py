#!/usr/bin/env python3

from stack import MyStack
from stack_using_array import stack

class StackOfStacks:

    def __init__(self, substack_capacity = None) -> None:
        if substack_capacity is not None:
            self.__capacity: int = substack_capacity
        else:
            self.__capacity: int = 3 # DEFAULT substack capacity
        self.__stack_of_stacks = None
        self.__top = -1

    def __str__(self) -> str:
        string = ''
        for stk_num,stk in enumerate(self.__stack_of_stacks):
            string = string + f'Stack num: {stk_num} | {stk.__str__()} \n'
        return string

    def set_capacity(self, capacity: int):
        if self.__stack_of_stacks is not None:
            raise Exception('Cannot change capacity \
             after substack is initialized')
        else:
            self.__capacity = capacity

    def is_empty(self) -> bool:
        if self.__stack_of_stacks in  ([], None) :
            return True
        else:
            return False

    def push(self, item: int) -> None:
        if self.is_empty():
            self.__stack_of_stacks = []
            new_stack = stack(self.__capacity)
            new_stack.push(item)
            self.__stack_of_stacks.append(new_stack)
            self.__top = self.__top + 1
        else:
            current = self.__stack_of_stacks[self.__top]
            if current.is_full():
                new_stack = stack(self.__capacity)
                new_stack.push(item)
                self.__stack_of_stacks.append(new_stack)
                self.__top = self.__top + 1
            else:
                self.__stack_of_stacks[self.__top].push(item)

    def remove_empty_top(self) -> None:
        self.__stack_of_stacks.pop()
        self.__top = self.__top - 1

    def pop(self) -> int:
        popped_item = self.__stack_of_stacks[self.__top].pop()
        if self.__stack_of_stacks[self.__top].is_empty():
            self.remove_empty_top()
        return popped_item

    def top(self) -> int:
        return self.__stack_of_stacks[self.__top].top()


    def pop_at(self, substack_index: int) -> int:
        substack = self.__stack_of_stacks[substack_index - 1]
        popped_item = substack.pop()
        if substack.is_empty():
            self.__stack_of_stacks.pop(substack_index - 1)
        return popped_item

def main():
    s = StackOfStacks()
    s.set_capacity(5)

    [s.push(num) for  num in range(13)]

    print(s)

    print(s)
    print(s.top())

    s.pop_at(1)

    print(s)


if __name__ == '__main__':
    main()
