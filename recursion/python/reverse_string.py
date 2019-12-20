"""
Reverse a string using recursion
"""

from typing import List
class Solution:
    def reverse_string(self, string: List[str]) -> str:
        def reverse(low: int,high:int, string: List[str]):
            if (low==high or low > high):
                return string
            else:
                temp = string[low]
                string[low] = string[high]
                string[high] = temp
                return reverse(low+1, high-1,string)

        low ,high = 0, len(string)-1
        return reverse(low,high,string)

if __name__ == "__main__":
    sol = Solution()
    strings = [["h","e","l","l","o"],['a','b','c'], ['a'],['a','b']]

    for string in strings:
        print(f"{string} -> {sol.reverse_string(string)}")
