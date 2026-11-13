from typing import List
from collections import deque

class Solution:
    def countNonDecreasingSubarrays(
        self, nums: List[int], k: int
    ) -> int:
        n = len(nums)
        ans = 0
        cost = 0
        dq = deque()
        j = n - 1

        for i in range(n - 1, -1, -1):
            num = nums[i]

            # Merge smaller values into the current maximum.
            while dq and nums[dq[-1]] < num:
                idx = dq.pop()
                right = dq[-1] if dq else j + 1
                cost += (right - idx) * (num - nums[idx])

            dq.append(i)

            # Remove elements from the right until cost is valid.
            while cost > k:
                cost -= nums[dq[0]] - nums[j]

                if dq[0] == j:
                    dq.popleft()

                j -= 1

            ans += j - i + 1

        return ans