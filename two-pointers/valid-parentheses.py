class Solution:
    def isValid(self, s: str) -> bool:
        pair = {
            "}": "{",
            ")": "(",
            "]": "[",
        }

        stack: list[str] = []

        for char in s:
            if pair.get(char) == None:
                stack.append(char)
                continue

            if len(stack) == 0 or pair[char] != stack[-1]:
                return False

            stack.pop()

        return len(stack) == 0
