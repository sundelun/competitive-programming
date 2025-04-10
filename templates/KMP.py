from typing import List
# problem from https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
# find the first index in haystack that match needle
# time complexity: O(N + M) N = len(haystack), M = len(needle)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        # calculate the array where the needle's prefix is also needle's suffix
        # lps[i] is the longest suffix that match the prefix from string ending with s[i]
        # lps[i] will point to an index
        # for example if we are given string "abcabc", then the lps should return [0, 0, 0, 1, 2, 3]
        # where lps[i] points to the index of matching prefix in the original string's next index
        # if s = "abc" then the lps_array should be [0, 0, 0] because all strings are unique
        def lps(s: str) -> List[int]:
            ans = [0] * m
            i, j = 0, 1
            while j < m:
                if s[j] == s[i]:
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
        lps_array = lps(needle)
        i = j = 0
        while n - i >= m - j:
            # macth a character
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            # find an answer
            # if required all matching then ans.append(i - m) then j = lps_array[j - 1]
            if j == m: return i - m
            # if does not match the character
            elif i < n and haystack[i] != needle[j]:
                # if we started traverse the needle
                if j != 0:
                    # go back to the matching prefix that end with needle[j]'s suffix
                    j = lps_array[j - 1]
                # just go to the next index of haystack
                else:
                    i += 1
        return -1