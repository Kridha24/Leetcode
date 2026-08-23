class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        
        s1, s2 = 0, 0
        q1, q2 = 0, 0
        
        # Calculate sums and '?' counts for the first half
        for i in range(mid):
            if num[i] == '?':
                q1 += 1
            else:
                s1 += int(num[i])
                
        # Calculate sums and '?' counts for the second half
        for i in range(mid, n):
            if num[i] == '?':
                q2 += 1
            else:
                s2 += int(num[i])
        
        # If the total number of '?' is odd, Alice always wins
        if (q1 + q2) % 2 != 0:
            return True
            
        # If even, Alice wins if Bob's winning condition is NOT met
        return (s1 - s2) != (q2 - q1) * 9 // 2

