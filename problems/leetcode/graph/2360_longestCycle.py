from typing import List
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        ans = -1
        vis = [0] * n # the time that each node start with
        time = 1
        for i in range(n):
            x = i
            # the start time for each iteration
            st = time
            # to the end of a path and all nodes on path must be not visited
            while x != -1 and vis[x] == 0:
                vis[x] = time
                time += 1
                x = edges[x]
            # if vis[x] < st, then x is not found in this iteration of loop
            if x != -1 and vis[x] >= st:
                ans = max(ans, time - vis[x])
        return ans