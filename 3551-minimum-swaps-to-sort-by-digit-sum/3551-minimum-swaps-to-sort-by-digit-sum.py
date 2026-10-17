
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        def digitSum(x):
            return sum(int(d) for d in str(x))

        sorted_nums = sorted(
            nums,
            key=lambda x: (digitSum(x), x)
        )

        pos = {
            val: i for i, val in enumerate(sorted_nums)
        }

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or pos[nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps
