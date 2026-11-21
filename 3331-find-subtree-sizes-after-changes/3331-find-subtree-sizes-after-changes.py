
class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)

        # Build the original tree
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = [-1] * 26

        # Find the nearest matching ancestor
        def dfs(node):
            ch = ord(s[node]) - ord('a')
            old = last[ch]

            if old != -1:
                new_parent[node] = old

            last[ch] = node

            for child in children[node]:
                dfs(child)

            last[ch] = old

        dfs(0)

        # Build the final tree
        final_children = [[] for _ in range(n)]
        for i in range(1, n):
            final_children[new_parent[i]].append(i)

        # Calculate subtree sizes
        answer = [1] * n

        def calculate(node):
            for child in final_children[node]:
                calculate(child)
                answer[node] += answer[child]

        calculate(0)
        return answer
