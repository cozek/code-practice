"""
Palindrome Permutation: Given a string, write a function to check if it
is a permutation of a palindrome. A palindrome is a word or phrase that is the
same forwards and backwards. A permutation is a rearrangement of letters. The
palindrome does not need to be limited to just dictionary words.
"""

from typing import List


class PalinChecker:
    """
    There can be only one char in the string with odd frequency
    for it to be palindrome
    """

    def check(self, string: str) -> bool:
        """
        Uses a array as map
        """

        def _create_char_arrmap(string: str) -> List:
            num_chars = ord("z") - ord("a")
            map_arr = [0 for i in range(num_chars + 1)]
            for char in string:
                map_arr[ord(char) - ord("a")] += 1
            return map_arr

        def _get_index(char_id: int) -> int:
            idx = char_id - ord("a")
            return idx

        got_odd = False
        map_arr = _create_char_arrmap(string)

        for char in string:
            val = map_arr[_get_index(ord(char))]
            if val != -1:
                map_arr[_get_index(ord(char))] = -1
                if val % 2 == 1:
                    if got_odd:
                        return False
                    got_odd = True
        return True

    def check2(self, string: str) -> bool:
        """
        Uses a dict to map
        """
        map = {}
        for char in string:
            if char in map:
                map[char] += 1
            else:
                map[char] = 1

        got_odd = False
        for key, val in map.items():
            if val % 2 == 1:
                if got_odd:
                    return False
                got_odd = True
        return True

    def check3(self, string: str) -> bool:
        """
        Some optimzation
        """
        odd_count = 0
        map = {}
        for char in string:
            if char not in map:
                map[char] = 1
            else:
                map[char] += 1
            if map[char] % 2 == 1:
                odd_count += 1
            else:
                odd_count -= 1

        if odd_count == 0 or odd_count == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    words = ["l", "lla", "ll", "aal", "abccb", "abc", "aaabbbc"]
    chk = PalinChecker()
    for word in words:
        print(f"{word} -> {chk.check3(word)}")
