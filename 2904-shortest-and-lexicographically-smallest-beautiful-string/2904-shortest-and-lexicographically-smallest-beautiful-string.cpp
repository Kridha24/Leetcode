class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        int n = s.length();
        string ans = "";

        for (int i = 0; i < n; i++) {
            int ones = 0;

            for (int j = i; j < n; j++) {

                if (s[j] == '1') {
                    ones++;
                }

                if (ones == k) {
                    string current = s.substr(i, j - i + 1);

                    // Shorter substring
                    if (ans == "" || current.length() < ans.length()) {
                        ans = current;
                    }
                    // Same length but lexicographically smaller
                    else if (current.length() == ans.length() && current < ans) {
                        ans = current;
                    }

                    break;
                }
            }
        }

        return ans;
    }
};