
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        # Case 1: Already sorted
        if all(nums[i] == i for i in range(n)):
            return 0

        # Case 2: Rotation of sorted array
        k = nums[0]
        if all(nums[i] == (k + i) % n for i in range(n)):
            return min(n - k, k + 2)

        # Case 3: Rotation of reversed sorted array
        k = n - 1 - nums[0]
        if all(nums[i] == (n - 1 - k - i) % n for i in range(n)):
            return 1 + min(k, n - k)

        return -1
