'''
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0

        i = 1
        while i * i <= n:
            if n % i == 0:
                total += nums[i - 1] ** 2

                j = n // i
                if i != j:
                    total += nums[j - 1] ** 2

            i += 1

        return total
'''

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        total_sum = 0
        n = len(nums)
        for i in range(1,len(nums)+1):
            if n%i == 0:
                total_sum = total_sum + nums[i-1]**2
        return total_sum        
