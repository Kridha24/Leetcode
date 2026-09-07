class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        # dp = number of distinct subsequences, including empty subsequence
        dp = 1
        last = {}

        for ch in s:
            new_dp = (2 * dp) % MOD

            # Remove subsequences duplicated because of a previous same character
            if ch in last:
                new_dp = (new_dp - last[ch]) % MOD

            last[ch] = dp
            dp = new_dp

        # Exclude the empty subsequence
        return (dp - 1) % MOD