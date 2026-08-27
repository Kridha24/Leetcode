class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        int n = s.size();
        vector<int> freq(26, 0);

        for (char ch : s) {
            freq[ch - 'a']++;
        }

        string prefix;
        int matched = 0;

        // Match the longest possible prefix with target.
        while (matched < n && freq[target[matched] - 'a'] > 0) {
            prefix.push_back(target[matched]);
            freq[target[matched] - 'a']--;
            matched++;
        }

        /*
         Try to make the current position greater.
         If impossible, backtrack to an earlier position.
        */
        for (int pos = min(matched, n - 1); pos >= 0; pos--) {
            // target[pos] was previously used in the matched prefix.
            if (pos < matched) {
                char restored = prefix.back();
                prefix.pop_back();
                freq[restored - 'a']++;
            }

            // Pick the smallest available character greater than target[pos].
            for (char ch = target[pos] + 1; ch <= 'z'; ch++) {
                if (freq[ch - 'a'] == 0) {
                    continue;
                }

                string answer = prefix;
                answer.push_back(ch);
                freq[ch - 'a']--;

                // Smallest possible suffix.
                for (int letter = 0; letter < 26; letter++) {
                    answer.append(freq[letter], char('a' + letter));
                }

                return answer;
            }
        }

        return "";
    }
};