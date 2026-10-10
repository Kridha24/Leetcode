
class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        # Find minimum achievable maximum difference
        while left < right:
            mid = (left + right) // 2

            operations = sum(max(0, d - mid) for d in diff)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        threshold = left

        # Reduce differences above threshold
        remaining = k

        for i in range(len(diff)):
            if diff[i] > threshold:
                remaining -= diff[i] - threshold
                diff[i] = threshold

        # Spend remaining operations on largest differences
        answer = sum(d * d for d in diff)

        answer -= remaining * (2 * threshold - 1)

        return answer
