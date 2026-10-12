
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        count = [0] * 30

        # Count frequency of each set bit
        for num in nums:
            for bit in range(30):
                if num & (1 << bit):
                    count[bit] += 1

        ans = 0

        # Construct k maximum possible numbers
        for _ in range(k):
            x = 0

            for bit in range(30):
                if count[bit] > 0:
                    x |= (1 << bit)
                    count[bit] -= 1

            ans = (ans + x * x) % MOD

        return ans
