from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Convert initial string to bitmasks
        masks = [1 << (ord(c) - 97) for c in s]
        
        tin = [0] * n
        tout = [0] * n
        first_pos = [0] * n
        
        # Array for Euler Tour LCA (stores packed (depth << 16) | node)
        # An Euler tour on n nodes has exactly 2*n - 1 states
        euler = []
        
        # Iterative DFS to avoid recursion limit and build Euler Tour + Subtree ranges
        stack = [(0, -1, 0, 0)]  # (u, parent, depth, child_index)
        timer = 0
        init_xor = [0] * (n + 1)
        cur_xor = 0
        
        while stack:
            u, p, d, idx = stack[-1]
            if idx == 0:
                timer += 1
                tin[u] = timer
                cur_xor ^= masks[u]
                init_xor[timer] = cur_xor
                first_pos[u] = len(euler)
                euler.append((d << 16) | u)
                
            if idx < len(adj[u]):
                v = adj[u][idx]
                stack[-1] = (u, p, d, idx + 1)
                if v != p:
                    stack.append((v, u, d + 1, 0))
            else:
                tout[u] = timer
                cur_xor ^= masks[u]
                stack.pop()
                if stack:
                     parent_u, _, parent_d, _ = stack[-1]
                     euler.append((parent_d << 16) | parent_u)

        # Build Fenwick Tree (Binary Indexed Tree) in O(n) time
        # Point query at tin[u] gives root-to-u XOR sum
        bit = [0] * (n + 2)
        for i in range(1, n + 1):
            bit[i] ^= init_xor[i] ^ init_xor[i - 1]
            j = i + (i & -i)
            if j <= n + 1:
                bit[j] ^= bit[i]
                
        def bit_add(idx: int, val: int):
            while idx <= n:
                bit[idx] ^= val
                idx += idx & -idx
                
        def bit_query(idx: int) -> int:
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & -idx
            return res

        # Build Iterative Segment Tree for fast RMQ (LCA) over Euler tour
        m = len(euler)
        seg = [0] * (2 * m)
        seg[m:2 * m] = euler
        for i in range(m - 1, 0, -1):
            seg[i] = seg[2 * i] if seg[2 * i] < seg[2 * i + 1] else seg[2 * i + 1]
            
        def get_lca(u: int, v: int) -> int:
            l, r = first_pos[u], first_pos[v]
            if l > r:
                l, r = r, l
            l += m
            r += m + 1
            res = seg[l]
            while l < r:
                if l & 1:
                    if seg[l] < res:
                        res = seg[l]
                    l += 1
                if r & 1:
                    r -= 1
                    if seg[r] < res:
                        res = seg[r]
                l >>= 1
                r >>= 1
            return res & 0xFFFF

        # Process queries
        ans = []
        for q in queries:
            parts = q.split()
            if parts[0][0] == 'u':  # "update u c"
                u = int(parts[1])
                new_mask = 1 << (ord(parts[2]) - 97)
                diff = masks[u] ^ new_mask
                if diff:
                    masks[u] = new_mask
                    # Range XOR update on [tin[u], tout[u]]
                    bit_add(tin[u], diff)
                    bit_add(tout[u] + 1, diff)
            else:  # "query u v"
                u = int(parts[1])
                v = int(parts[2])
                lca = get_lca(u, v)
                
                # Path XOR = dist_xor(u) ^ dist_xor(v) ^ mask[lca]
                path_mask = bit_query(tin[u]) ^ bit_query(tin[v]) ^ masks[lca]
                
                # Check if at most 1 bit is set
                ans.append((path_mask & (path_mask - 1)) == 0)
                
        return ans