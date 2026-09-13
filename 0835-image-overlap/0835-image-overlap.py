from typing import List
from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        
        n = len(img1)

        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c] == 1]

        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c] == 1]

        shifts = defaultdict(int)
        answer = 0

        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift = (r2 - r1, c2- c1)
                shifts[shift] += 1
                answer = max(answer, shifts[shift])

        return answer        