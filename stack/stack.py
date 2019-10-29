#!/usr/bin/env python3


class StackNode:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class MyStack:
    def __init__(self):
        self.__top = None

    def __str__(self):
        if self.is_empty():
            return "Empty Stack!"

        current = self.__top

        def loop(node: StackNode, string: str):
            if node.next_node is None:
                return string + f"{node.data} -> END"
            else:
                return loop(node.next_node, string + f"{node.data} -> ")

        return loop(current, "")

    def push(self, item):
        if self.__top is None:
            self.__top = StackNode(item)
        else:
            new_node = StackNode(item)
            new_node.next_node = self.__top
            self.__top = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Empty Stack!")
        data = self.__top.data
        self.__top = self.__top.next_node
        return data

    def peek(self):
        return self.__top.data

    def is_empty(self):
        if self.__top is None:
            return True
        else:
            return False

    def sort(self):
        r = MyStack()  # TEMP: MyStack
        while not self.is_empty():
            temp = self.pop()
            while not r.is_empty() and r.peek() > temp:
                self.push(r.pop())
            r.push(temp)
        while not r.is_empty():
            self.push(r.pop())


def main():
    stack = MyStack()
    [stack.push(num) for num in range(10)]
    print(stack)
    stack.sort()
    print(stack)


if __name__ == "__main__":
    main()
