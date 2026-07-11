class Solution {
public:
    vector<vector<int>> graph;
    vector<bool> visited;

    int nodes;
    int degreeSum;

    void dfs(int node) {
        visited[node] = true;
        nodes++;

        degreeSum += graph[node].size();

        for (int nei : graph[node]) {
            if (!visited[nei])
                dfs(nei);
        }
    }

    int countCompleteComponents(int n, vector<vector<int>>& edges) {

        graph.resize(n);
        visited.assign(n, false);

        for (auto &e : edges) {
            graph[e[0]].push_back(e[1]);
            graph[e[1]].push_back(e[0]);
        }

        int ans = 0;

        for (int i = 0; i < n; i++) {

            if (!visited[i]) {

                nodes = 0;
                degreeSum = 0;

                dfs(i);

                int edgeCount = degreeSum / 2;

                if (edgeCount == nodes * (nodes - 1) / 2)
                    ans++;
            }
        }

        return ans;
    }
};