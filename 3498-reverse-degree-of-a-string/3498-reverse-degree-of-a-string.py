class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0

        for position, ch in enumerate(s, start=1):
            value = ord('z') - ord(ch) + 1
            total += value * position

        return total