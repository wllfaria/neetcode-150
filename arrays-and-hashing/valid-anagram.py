from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars: dict[str, int] = {}

        for c in s:
            chars[c] = chars.get(c, 0) + 1

        for c in t:
            chars[c] = chars.get(c, 0) - 1

        return all(v == 0 for v in chars.values())

    def isAnagramZip(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        chars: dict[str, int] = {}
        for c1, c2 in zip(s, t):
            chars[c1] = chars.get(c1, 0) + 1
            chars[c2] = chars.get(c2, 0) - 1

        return all(v == 0 for v in chars.values())

    def isAnagramCounter(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
