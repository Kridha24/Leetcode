class Solution:
    def generateParenthesis(self, n: int):
        result = []

        def backtrack(current, open_count, close_count):
            # complete string
            if len(current) == 2 * n:
                result.append(current)
                return

            # add '(' if available
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # add ')' only if it can match an existing '('
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)

        return result