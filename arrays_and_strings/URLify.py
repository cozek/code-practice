"""
URLify: Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the
end to hold the additional characters, and that you are given
the "true" length of the string.
"""


class URLify:
    def convert(self, string: str) -> str:
        return "%20".join(string.split())


if __name__ == "__main__":
    conv = URLify()
    string = "Mr John Smith"
    print(f"{string} -> {conv.convert(string)}")
