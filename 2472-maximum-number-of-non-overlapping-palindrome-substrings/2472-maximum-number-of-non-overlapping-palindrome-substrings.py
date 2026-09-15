class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        count = 0
        start = 0  # First available index after the last selection

        for end in range(k - 1, n):
            # Check a palindrome of length k ending here
            left = end - k + 1
            if left >= start and is_palindrome(left, end):
                count += 1
                start = end + 1
                continue

            # Check a palindrome of length k + 1 ending here
            left = end - k
            if left >= start and is_palindrome(left, end):
                count += 1
                start = end + 1

        return count