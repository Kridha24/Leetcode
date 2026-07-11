#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        // Step 1: Extract sorted unique values from nums
        vector<int> U = nums;
        sort(U.begin(), U.end());
        U.erase(unique(U.begin(), U.end()), U.end());
        
        int M = U.size();
        
        // Step 2: Form connected components
        vector<int> comp(M, 0);
        for (int i = 1; i < M; ++i) {
            if (U[i] - U[i - 1] <= maxDiff) {
                comp[i] = comp[i - 1];
            } else {
                comp[i] = comp[i - 1] + 1;
            }
        }
        
        // Step 3: Binary Lifting Table preparation
        int LOG = 20;
        vector<vector<int>> up(M, vector<int>(LOG, 0));
        
        // Compute base case (1 optimal jump i.e., 2^0 jumps)
        int right = 0;
        for (int left = 0; left < M; ++left) {
            while (right + 1 < M && U[right + 1] - U[left] <= maxDiff) {
                right++;
            }
            up[left][0] = right;
        }
        
        // Populate the rest of the binary lifting table
        for (int j = 1; j < LOG; ++j) {
            for (int i = 0; i < M; ++i) {
                up[i][j] = up[up[i][j - 1]][j - 1];
            }
        }
        
        // Step 4: Process Queries
        vector<int> ans;
        ans.reserve(queries.size());
        
        for (const auto& q : queries) {
            int u = q[0];
            int v = q[1];
            
            // Distance from a node to itself is 0
            if (u == v) {
                ans.push_back(0);
                continue;
            }
            
            int valU = nums[u];
            int valV = nums[v];
            
            // If the nodes have the same value but are different nodes, the difference is 0 <= maxDiff.
            // A direct edge undeniably exists between them.
            if (valU == valV) {
                ans.push_back(1);
                continue;
            }
            
            int A = min(valU, valV);
            int B = max(valU, valV);
            
            // Locate their positions in the unique sorted values array
            int idxA = lower_bound(U.begin(), U.end(), A) - U.begin();
            int idxB = lower_bound(U.begin(), U.end(), B) - U.begin();
            
            // If they belong to different components, there's no available pathway
            if (comp[idxA] != comp[idxB]) {
                ans.push_back(-1);
                continue;
            }
            
            // Jump processing iteratively bringing "curr" right behind idxB
            int curr = idxA;
            int steps = 0;
            for (int k = LOG - 1; k >= 0; --k) {
                if (up[curr][k] < idxB) {
                    curr = up[curr][k];
                    steps += (1 << k);
                }
            }
            
            // One final jump crosses the boundary yielding reaching 'idxB' 
            ans.push_back(steps + 1);
        }
        
        return ans;
    }
};