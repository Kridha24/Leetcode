class Solution {
public:
    vector<string> ans;

    vector<string> phone = {
        "", "", "abc", "def", "ghi",
        "jkl", "mno", "pqrs",
        "tuv", "wxyz"
    };

    void dfs(int index, string &digits, string &path) {

        if (index == digits.size()) {
            ans.push_back(path);
            return;
        }

        string &letters = phone[digits[index] - '0'];

        for (char ch : letters) {
            path.push_back(ch);
            dfs(index + 1, digits, path);
            path.pop_back();
        }
    }

    vector<string> letterCombinations(string digits) {

        if (digits.empty())
            return {};

        string path;

        dfs(0, digits, path);

        return ans;
    }
};