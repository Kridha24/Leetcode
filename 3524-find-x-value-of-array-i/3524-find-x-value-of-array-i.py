from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dp = [0] * k

        for num in nums:
            current = [0] * k

            current[num % k] += 1

            for remainder in range(k):
                new_remainder = (remainder * num) % k
                current[new_remainder] += dp[remainder]

            for remainder in range(k):
                    result[remainder] += current[remainder]

            dp = current

        return result        