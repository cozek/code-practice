#!/usr/bin/env python3
import stack

"""
Implements code to get the min from the stack in O(1)
"""


class StackNode(stack.StackNode):
    def __init__(self, data):
        self.minimum = None
        super().__init__(data)


class MyStack(stack.MyStack):
    def __init__(self):
        super().__init__()

    def __str__(self):
        current = self.__top

        def loop(node: StackNode, string: str):
            if node.next_node is None:
                return string + f"[{node.data}|({node.minimum})] -> END"
            else:
                return loop(
                    node.next_node, string + f"[{node.data}|({node.minimum})] -> "
                )

        return loop(current, "")

    def push(self, data):
        if self.__top is None:
            self.__top = StackNode(data)
            self.__top.minimum = data
        else:
            new_node = StackNode(data)
            new_node.next_node = self.__top
            self.__top = new_node
            if new_node.data > new_node.next_node.data:
                new_node.minimum = new_node.next_node.data
            else:
                new_node.minimum = data

    def get_min(self):
        return self.__top.minimum


def main():
    tack = MyStack()
    [tack.push(num) for num in range(10)]
    print(tack)
    print(tack.get_min())
    tack.pop()
    tack.pop()
    print(tack)
    print(tack.get_min())
    tack.push(-1)
    print(tack)
    print(tack.get_min())


if __name__ == "__main__":
    main()
