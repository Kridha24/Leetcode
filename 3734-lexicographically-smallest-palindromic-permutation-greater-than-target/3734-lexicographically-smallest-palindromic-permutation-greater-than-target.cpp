class Solution {
private:
    // Smallest permutation of the given multiset strictly greater than bound.
    string nextGreaterHalf(vector<int> freq, const string& bound) {
        int n = bound.size();
        string prefix;
        int matched = 0;

        // Create the longest prefix equal to bound.
        while (matched < n && freq[bound[matched] - 'a'] > 0) {
            prefix.push_back(bound[matched]);
            freq[bound[matched] - 'a']--;
            matched++;
        }

        // Try the latest possible position, then backtrack.
        for (int pos = min(matched, n - 1); pos >= 0; pos--) {
            if (pos < matched) {
                char restored = prefix.back();
                prefix.pop_back();
                freq[restored - 'a']++;
            }

            // Choose the smallest available character greater than bound[pos].
            for (int c = bound[pos] - 'a' + 1; c < 26; c++) {
                if (freq[c] == 0) {
                    continue;
                }

                string result = prefix;
                result.push_back(char('a' + c));
                freq[c]--;

                // Minimum possible suffix.
                for (int letter = 0; letter < 26; letter++) {
                    result.append(freq[letter], char('a' + letter));
                }

                return result;
            }
        }

        return "";
    }

    string createPalindrome(const string& half, char middle) {
        string result = half;

        if (middle != '\0') {
            result.push_back(middle);
        }

        result.append(half.rbegin(), half.rend());
        return result;
    }

public:
    string lexPalindromicPermutation(string s, string target) {
        int n = s.size();
        vector<int> count(26, 0);

        for (char ch : s) {
            count[ch - 'a']++;
        }

        int oddCount = 0;
        char middle = '\0';

        for (int i = 0; i < 26; i++) {
            if (count[i] % 2 == 1) {
                oddCount++;
                middle = char('a' + i);
            }
        }

        // Palindrome validity check.
        if ((n % 2 == 0 && oddCount != 0) ||
            (n % 2 == 1 && oddCount != 1)) {
            return "";
        }

        int halfLength = n / 2;
        vector<int> halfFreq(26);

        for (int i = 0; i < 26; i++) {
            halfFreq[i] = count[i] / 2;
        }

        string targetHalf = target.substr(0, halfLength);

        // First check whether targetHalf itself can be created.
        vector<int> remaining = halfFreq;
        bool exactHalfPossible = true;

        for (char ch : targetHalf) {
            int index = ch - 'a';

            if (remaining[index] == 0) {
                exactHalfPossible = false;
                break;
            }

            remaining[index]--;
        }

        /*
         If the same first half is possible, there is exactly one palindrome
         corresponding to it. It may already be greater because of the middle
         or mirrored second half.
        */
        if (exactHalfPossible) {
            string candidate = createPalindrome(targetHalf, middle);

            if (candidate > target) {
                return candidate;
            }
        }

        // Otherwise, find the smallest left half greater than targetHalf.
        string greaterHalf = nextGreaterHalf(halfFreq, targetHalf);

        if (greaterHalf.empty()) {
            return "";
        }

        return createPalindrome(greaterHalf, middle);
    }
};