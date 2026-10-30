import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        if n == 1:
            return 0
            
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            
        # min_c[u] tracks the minimum consecutive count for which node u 
        # has already been settled with a smaller or equal distance.
        min_c = [k + 1] * n
        
        # best_dist[(u, c)] stores the shortest distance found so far for state (u, c)
        best_dist = {}
        
        # Priority queue stores tuples of (current_distance, u, consecutive_count)
        pq = [(0, 0, 1)]
        best_dist[(0, 1)] = 0
        
        while pq:
            d, u, c = heapq.heappop(pq)
            
            # Target reached
            if u == n - 1:
                return d
                
            # Dominance pruning: skip if node u was already settled with a smaller/equal count
            if c >= min_c[u]:
                continue
            min_c[u] = c
            
            u_label = labels[u]
            for v, w in adj[u]:
                nc = c + 1 if labels[v] == u_label else 1
                
                # Check if the new consecutive count is valid and not dominated at v
                if nc <= k and nc < min_c[v]:
                    nd = d + w
                    state = (v, nc)
                    if nd < best_dist.get(state, float('inf')):
                        best_dist[state] = nd
                        heapq.heappush(pq, (nd, v, nc))
                        
        return -1