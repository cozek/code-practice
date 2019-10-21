#!/usr/bin/env python3


class Hourglass:
    """
    >>> arr = [
    ...    [1, 1, 1, 0, 0, 0],
    ...    [0, 1, 0, 0, 0, 0],
    ...    [1, 1, 1, 0, 0, 0],
    ...    [0, 0, 2, 4, 4, 0],
    ...    [0, 0, 0, 2, 0, 0],
    ...    [0, 0, 1, 2, 4, 0] ]
    >>> obj = Hourglass(arr)
    >>> obj.get_max()
    19
    """
    def __init__(self, glass):
        self.glass = glass
        self.iter_glass()

    def __str__(self):
        string = ""
        for row in self.glass:
            string += row.__str__() + "\n"
        return string

    def iter_glass(self):
        ptr_common = 0
        ptr_mid = 1

        self.__max_glass = -1e10
        for row in range(4):
            for idx in range(4):
                top = self.glass[row][idx : idx + 3]
                mid = [self.glass[row + 1][ptr_mid]]
                bot = self.glass[row + 2][idx : idx + 3]
                glass_total = sum(top + mid + bot)
                if glass_total > self.__max_glass:
                    self.__max_glass = glass_total
                ptr_mid += 1
            ptr_mid = 1

    def get_max(self):
        return self.__max_glass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
