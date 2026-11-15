
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7

        odd = 0
        even = 1
        prefix_sum = 0
        ans = 0

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2 == 1:
                ans += even
                odd += 1
            else:
                ans += odd
                even += 1

        return ans % MOD
