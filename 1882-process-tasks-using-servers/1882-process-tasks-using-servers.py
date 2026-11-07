
import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)

        # (free_time, weight, server_index)
        busy = []
        ans = []
        time = 0

        for i, duration in enumerate(tasks):
            # Task i arrives at second i
            time = max(time, i)

            # Release every server that is free now
            while busy and busy[0][0] <= time:
                free_time, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

            # If all servers are busy, wait for the earliest one
            if not available:
                time = busy[0][0]

                # Release ALL servers that become free at this time
                while busy and busy[0][0] <= time:
                    free_time, weight, idx = heapq.heappop(busy)
                    heapq.heappush(available, (weight, idx))

            # Choose the server with the smallest weight, then index
            weight, idx = heapq.heappop(available)
            ans.append(idx)

            # This server becomes free after processing the task
            heapq.heappush(busy, (time + duration, weight, idx))

        return ans
