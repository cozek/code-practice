# Is Unique: Implement an algorithm to determine if a string has all
# unique characters. What if you cannot use additional data structures?

class StringChecker:
    def is_unique(self, string:str) -> bool:
        """
        Checks if all chars in string is unique
        using a set/hashtable
        """
        buffer = set();
        for char in string:
            if char not in buffer:
                buffer.add(char)
            elif char in buffer:
                return False
        return True

    def is_unique2(self, string:str) -> bool:
        """
        Checks if all chars in string is unique
        using a list/array
        """
        total_chars = 256 #128 ASCII, 256 for UNICODE
        buffer = [0 for i in range(total_chars)]
        for char in string:
            if buffer[ord(char)] == 0:
                buffer[ord(char)] = 1
            elif buffer[ord(char)] == 1:
                return False
        return True

    def is_unique3(self, string:str) -> bool:
        """
        Checks if all chars in string is unique
        without using any extra data structures
        """
        string = ''.join(sorted(string))
        for i in range(len(string)):
            if string[i] == string[i-1]:
                return False
        return True


if __name__ == '__main__':
    words = ("abcde", "hello", "apple", "kite", "padle")
    checker = StringChecker();
    for word in words:
        print(f"{word} : {checker.is_unique(word)}\
        {checker.is_unique2(word)} {checker.is_unique3(word)}")