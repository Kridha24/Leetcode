class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        # Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        count = 0

        # Count last word
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1

        return count