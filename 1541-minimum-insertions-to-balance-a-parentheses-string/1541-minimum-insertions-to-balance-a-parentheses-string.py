class Solution:
    def minInsertions(self, s: str) -> int:
        open_count = 0
        insertions = 0
        i, n = 0, len(s)

        while i < n:
            if s[i] == '(':
                open_count += 1
            else:
                # If the next character is not ')',
                # insert one ')' to complete the pair.
                if i + 1 < n and s[i + 1] == ')':
                    i += 1
                else:
                    insertions += 1

                # Match the closing pair with an opening bracket.
                if open_count > 0:
                    open_count -= 1
                else:
                    # No opening bracket exists; insert '('.
                    insertions += 1
            i += 1

        # Each remaining '(' needs two ')'.
        insertions += open_count * 2

        return insertions



'''
class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        need = 0

        for ch in s:

            if ch == '(':

                # Previous '(' has received only one ')'
                # Insert another ')' to complete '))'
                if need % 2 == 1:
                    insertions += 1
                    need -= 1

                # Current '(' needs two ')'
                need += 2

            else:
                need -= 1

                # No '(' available for this ')'
                if need < 0:
                    # Insert '('
                    insertions += 1

                    # Inserted '(' needs '))'
                    # Current ')' counts as one of them
                    need = 1

        return insertions + need        

'''        