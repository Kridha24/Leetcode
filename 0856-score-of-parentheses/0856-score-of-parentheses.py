class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                value = stack.pop()

                if value == 0:
                    score = 1
                else:
                    score = 2 * value

                stack[-1] += score

        return stack[0]