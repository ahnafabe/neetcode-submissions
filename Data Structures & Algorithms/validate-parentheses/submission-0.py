class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        mapping = {")": "(", "]": "[", "}": "{"}
        for element in s:
            if element in "([{ ":
                stack.append(element)
            elif not stack or mapping[element] != stack.pop():
                return False
        return not stack