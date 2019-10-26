import stack

"""
This script implements MinStack which allows one to retrieve the
min of the stack in O(1) and uses less space.
"""


class MinStack(stack.MyStack):
    def __init__(self):
        super().__init__()
        self.__min_top = None

    def push(self, item):
        super().push(item)
        if self.__min_top == None:
            self.__min_top = stack.StackNode(item)
        else:
            if self.__min_top.data > item:
                new_min = stack.StackNode(item)
                new_min.next_node = self.__min_top
                self.__min_top = new_min

    def pop(self):
        popped_item = super().pop()
        if popped_item == self.get_min():
            self.__min_top = self.__min_top.next_node

    def get_min(self):
        return self.__min_top.data


def main():
    arr = [5, 3, 2, 10, 100]
    stk = MinStack()
    [stk.push(num) for num in arr]
    print(stk)
    for i in range(4):
        stk.pop()
        print(stk)
        print(stk.get_min())
    print(stk.get_min())


if __name__ == "__main__":
    main()
