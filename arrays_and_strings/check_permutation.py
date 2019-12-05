"""
Check Permutation: Given two strings,
write a method to decide if one is a permutation of the other.
"""
from typing import Tuple, Callable


class CheckPerm:
    @staticmethod
    def check_using_sort(string_a: str, string_b: str) -> bool:
        """
        Checks by sorting two string and comparing if they are equal
        """
        string_a = sorted(string_a)
        string_b = sorted(string_b)
        if string_a == string_b:
            return True
        else:
            return False

    @staticmethod
    def check_using_count(string_a: str, string_b: str) -> bool:
        """
        Checks by comparing the frequency of the characters in each string
        """
        letters = [0 for i in range(256)]  # 256 for UNICODE, 128 for ASCII
        for i in range(len(string_a)):
            idx = ord(string_a[i])
            letters[idx] += 1

        for i in range(len(string_b)):
            idx = ord(string_b[i])
            letters[idx] -= 1
            if letters[idx] < 0:
                return False
        return True

    def check(
        self, string_pair: Tuple[str, str], check_func: Callable[[str, str], bool]
    ) -> bool:
        string_a, string_b = string_pair
        if len(string_a) != len(string_b):
            return False
        return check_func(string_a, string_b)


if __name__ == "__main__":
    word_pairs = (("apple", "papel"), ("carrot", "tarroc"), ("hello", "llloh"))
    ck = CheckPerm()
    for pair in word_pairs:
        print(f"Using sort on {pair}: {ck.check(pair, ck.check_using_sort)}")
        print(f"Using count on {pair}:", ck.check(pair, ck.check_using_count))
