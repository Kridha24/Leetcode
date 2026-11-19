class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()
        return min(
            nums[-1] - nums[2],   # Change the 2 smallest elements
            nums[-2] - nums[1],   # Change the smallest and largest elements
            nums[-3] - nums[0],   # Change the 2 largest elements
        )