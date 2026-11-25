from collections import Counter

class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        MOD1, BASE1 = 10**9 + 7, 100003
        MOD2, BASE2 = 10**9 + 9, 100019

        def has_unique(length: int) -> bool:
            h1 = h2 = 0
            for i in range(length):
                h1 = (h1 * BASE1 + nums[i]) % MOD1
                h2 = (h2 * BASE2 + nums[i]) % MOD2

            p1 = pow(BASE1, length - 1, MOD1)
            p2 = pow(BASE2, length - 1, MOD2)

            counts = Counter()
            counts[(h1 << 32) | h2] += 1

            for i in range(length, n):
                h1 = ((h1 - nums[i - length] * p1) * BASE1 + nums[i]) % MOD1
                h2 = ((h2 - nums[i - length] * p2) * BASE2 + nums[i]) % MOD2
                counts[(h1 << 32) | h2] += 1

            return any(c == 1 for c in counts.values())

        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo