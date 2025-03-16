#https://leetcode.cn/problems/substring-with-largest-variance/description/
import math
# Time complexity: O(N*26^2)
# Space complexity: O(1)
class Solution:
    def largestVariance(self, s: str) -> int:
        # aabaaab
        # if we only have two distinct characters, then the problem becomes the
        # maxmium subarray problem with a = 1 and b = -1
        n = len(s)
        ans = 0
        for f in range(26):
            for s2 in range(26):
                if f == s2: continue
                # dp[i][0] reperesent may or may not have s2, dp[i][1] represent have s2
                # recall formula from 53 maximum subarray: dp[i] = max(dp[i - 1] + a[i], a[i])
                # so dp[i + 1][0] = max(dp[i][0] + v, v); v = 1 or 0 or -1
                # v = 1 if s[i] == f, v = -1 if s[i] == s2, else v = 0
                # if s[i] != s2: then dp[i + 1][1] = dp[i][1] + v because it can't be ended by s2
                # else if s[i] == s2: then dp[i + 1][1] = max(dp[i][0], dp[i][1], 0) + v or same as dp[i + 1][1] = dp[i + 1][0] because it can be ended by s2
                # we can optimize the space complexity!
                f0, f1 = 0, -math.inf
                for ch in s:
                    val = ord(ch) - ord('a')
                    if val == f: 
                        f0, f1 = max(f0 + 1, 1), f1 + 1
                    elif val == s2: 
                        f0, f1 = max(f0 - 1, -1), max(f0 - 1, f1 - 1, -1)
                    ans = max(ans, f1)
        return ans
# Optimize time complexity version
# Notice that the status of dp won't be updated if we do not meet ch == f or ch == s2
# So we are wasting lots of time during the computation from previous method
# we can create two 26 * 26 matrix f0[a][b] and f1[a][b]
class Solution2:
    def largestVariance(self, s: str) -> int:
        # aabaaab
        # if we only have two distinct characters, then the problem becomes the
        # maxmium subarray problem with a = 1 and b = -1
        f0 = [[0] * 26 for _ in range(26)]
        f1 = [[-math.inf] * 26 for _ in range(26)]
        ans = 0
        for ch in map(ord, s):
            ch -= ord('a')
            # we only need to calculate when a = ch or b = ch
            for i in range(26):
                if i == ch: continue
                # ch = a
                f0[ch][i] = max(f0[ch][i], 0) + 1 # same as max(f0[ch][i] + 1, 1)
                f1[ch][i] = f1[ch][i] + 1

                # ch = b
                #f0[i][ch], f1[i][ch] = max(f0[i][ch], 0) - 1, max(f0[i][ch], f1[i][ch], 0) - 1
                f1[i][ch] = f0[i][ch] = max(f0[i][ch], 0) - 1
                ans = max(ans, f1[i][ch], f1[ch][i])
        return ans  
                    