class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        int n = nums.size();

        // {value, original index}
        vector<pair<int, int>> elements;
        elements.reserve(n);

        for (int i = 0; i < n; i++) {
            elements.push_back({nums[i], i});
        }

        sort(elements.begin(), elements.end());

        int start = 0;

        while (start < n) {
            int end = start;

            /*
             Consecutive values whose difference <= limit belong to
             the same connected component.
            */
            while (end + 1 < n &&
                   (long long)elements[end + 1].first -
                   elements[end].first <= limit) {
                end++;
            }

            vector<int> indices;

            for (int i = start; i <= end; i++) {
                indices.push_back(elements[i].second);
            }

            // Put smaller values at smaller indices.
            sort(indices.begin(), indices.end());

            for (int i = 0; i < (int)indices.size(); i++) {
                nums[indices[i]] = elements[start + i].first;
            }

            start = end + 1;
        }

        return nums;
    }
};