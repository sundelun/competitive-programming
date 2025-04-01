# https://leetcode.cn/problems/largest-rectangle-in-histogram/
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # the key idea is to use a monotonic stack to record each index i's left side closest index and right side closest index that is smaller than heights[i]
        ans = 0
        st = []
        n = len(heights)
        # record the index that closest to left of i and is smaller than heights[i] 
        left = [-1] * n
        for i, num in enumerate(heights):
            while st and num <= heights[st[-1]]:
                st.pop()
            if st: left[i] = st[-1]
            st.append(i)
        # record the index that closest to right of i and is smaller than heights[i]
        right = [n] * n
        st = []
        for i in range(n - 1, -1, -1):
            while st and heights[i] <= heights[st[-1]]:
                st.pop()
            if st: right[i] = st[-1]
            st.append(i)
        ans = 0
        for num, l, r in zip(heights, left, right):
            # the answer for using num as the height is num * (right side closest - left side closest - 1)
            ans = max(ans, num * (r - l - 1))
        return ans