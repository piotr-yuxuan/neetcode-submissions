class Solution:
    def isValid(self, s: str) -> bool:
        opening_delimiters = {x for x in '{[('}
        closing_delimiters = {
            '}': '{',
            ']': '[',
            ')': '(',
            }

        stack = list([])

        for c in s:
            if c in opening_delimiters:
                stack.append(c)
            elif stack and stack[-1] == closing_delimiters.get(c, None):
                stack.pop()
            else:
                return False
        return True and not stack
