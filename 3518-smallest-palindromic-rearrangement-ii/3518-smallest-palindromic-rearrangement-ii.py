import math
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Step 1: Get counts of all characters
        counts = Counter(s)
        half_counts = {}
        mid_char = ""
        L = 0
        
        for char, freq in counts.items():
            # If the frequency is odd, this character must be in the middle
            if freq % 2 != 0:
                mid_char = char
            
            # Divide frequencies by 2 for the first half of the palindrome
            if freq // 2 > 0:
                half_counts[char] = freq // 2
                L += freq // 2
                
        # Step 2: Calculate the total number of permutations of the first half
        T = math.factorial(L)
        for freq in half_counts.values():
            T //= math.factorial(freq)
            
        # If k is greater than the total number of unique permutations, return empty string
        if k > T:
            return ""
            
        # Step 3: Build the first half character by character
        first_half = []
        chars = sorted(half_counts.keys())
        curr_L = L
        
        for _ in range(L):
            for c in chars:
                if half_counts[c] > 0:
                    # Calculate permutations available if we choose character `c`
                    # Mathematically this is equivalent to: T_c = T * (half_counts[c] / curr_L)
                    T_c = T * half_counts[c] // curr_L
                    
                    if k <= T_c:
                        first_half.append(c)
                        half_counts[c] -= 1
                        T = T_c
                        break
                    else:
                        k -= T_c
                        
            curr_L -= 1
                        
        # Step 4: Combine the first half, middle character, and the reversed first half
        res = "".join(first_half)
        return res + mid_char + res[::-1]