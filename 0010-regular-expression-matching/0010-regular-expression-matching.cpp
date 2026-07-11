class Solution {
public:

    int dp[25][25];

    bool solve(int i, int j, string &s, string &p) {

        if (dp[i][j] != -1)
            return dp[i][j];

        if (j == p.size())
            return dp[i][j] = (i == s.size());

        bool firstMatch =
            (i < s.size() &&
            (s[i] == p[j] || p[j] == '.'));

        if (j + 1 < p.size() && p[j + 1] == '*') {

            return dp[i][j] =
                solve(i, j + 2, s, p) ||
                (firstMatch && solve(i + 1, j, s, p));
        }

        return dp[i][j] =
            firstMatch &&
            solve(i + 1, j + 1, s, p);
    }

    bool isMatch(string s, string p) {

        memset(dp, -1, sizeof(dp));

        return solve(0, 0, s, p);
    }
};