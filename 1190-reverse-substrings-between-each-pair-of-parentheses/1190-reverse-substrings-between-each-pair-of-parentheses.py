class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for char in s:
            if char == ')':
                reversed_chars = []

                while stack[-1] != '(':
                    reversed_chars.append(stack.pop())

                stack.pop()
                stack.extend(reversed_chars)
            else:
                stack.append(char)

        return ''.join(stack)