# https://leetcode.cn/problems/maximal-rectangle/
from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        # prefix sum for each col[j]
        prefix = [0] * n
        ans = 0
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                # if it is zero we have to set it to because each col's 1 should be consecutive
                prefix[j] = prefix[j] + 1 if matrix[i][j] == '1' else 0
            # the same as question #84 below to calc answer
            right = [n] * n
            st = []
            for a in range(n - 1, -1, -1):
                while st and prefix[a] <= prefix[st[-1]]:
                    st.pop()
                if st: right[a] = st[-1]
                st.append(a)
            st = []
            for a in range(n):
                while st and prefix[a] <= prefix[st[-1]]:
                    st.pop()
                l = st[-1] if st else -1
                ans = max(ans, prefix[a] * (right[a] - l - 1))
                st.append(a)
        return ans