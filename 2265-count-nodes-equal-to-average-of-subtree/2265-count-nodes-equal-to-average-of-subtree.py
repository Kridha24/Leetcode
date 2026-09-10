class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0, 0

            ls, lc, la = dfs(node.left)
            rs, rc, ra = dfs(node.right)

            total = ls + rs + node.val
            count = lc + rc + 1
            matches = la + ra + (total // count == node.val)

            return total, count, matches

        return dfs(root)[2]