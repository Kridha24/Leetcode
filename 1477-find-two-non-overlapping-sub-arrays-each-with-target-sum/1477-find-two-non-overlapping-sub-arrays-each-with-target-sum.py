from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        inf = float("inf")
        best = [inf] * (n + 1)

        left = 0
        window_sum = 0
        answer = inf

        for right, value in enumerate(arr):
            window_sum += value

            while window_sum > target:
                window_sum -= arr[left]
                left += 1

            best[right + 1] = best[right]

            if window_sum == target:
                length = right - left + 1

                # best[left] uses only elements before this window.
                answer = min(answer, best[left] + length)

                best[right + 1] = min(best[right + 1], length)

        return -1 if answer == inf else answer