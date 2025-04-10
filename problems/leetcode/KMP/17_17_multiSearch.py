# https://leetcode.cn/problems/multi-search-lcci/description/
from typing import List
class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        # almost same as question #28 in templates
        def lps(s: str) -> List[int]:
            m = len(s)
            ans = [0] * m
            i, j = 0, 1
            while j < m:
                if s[i] == s[j]:
                    i += 1
                    ans[j] = i
                    j += 1
                else:
                    if i != 0:
                        i = ans[i - 1]
                    else:
                        ans[j] = 0
                        j += 1
            return ans
        ans = []
        n = len(big)
        for word in smalls:
            lps_arr = lps(word)
            i = j = 0
            res = []
            m = len(word)
            # empty word case
            if m == 0:
                ans.append(res)
                continue
            while n - i >= m - j:
                if big[i] == word[j]:
                    i += 1
                    j += 1
                # add to answer the index
                if j == m:
                    res.append(i - m)
                    j = lps_arr[j - 1]
                elif i < n and big[i] != word[j]:
                    if j > 0:
                        j = lps_arr[j - 1]
                    else:
                        i += 1
            ans.append(res)
        return ans
                