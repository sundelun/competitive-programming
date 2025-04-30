# https://leetcode.cn/problems/subsequence-with-the-minimum-score/
class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        # if we are deleting substring between t[left:right], it will not effect our final score
        # so when we are deleting we only need to consider t's substring
        # after deleting we are left with t's two parts, prefix and suffix
        # the matching part is prefix of s[:i] and suffix of s[i:] string s's subsequence here
        # we can iterate over all i to find the answer of prefix + suffix
        # suf[i] means s[i:]'s suffix part starting index
        # pre[i] meand s[:i]'s prefix part ending index
        # the answer is min(suf[i] - pre[i])
        n, m = len(s), len(t)
        suf = [m] * (n + 1)
        j = m
        # same process as find subsequence of t from s by iterating in reverse order
        for i in range(n - 1, -1, -1):
            # if we have a match
            if s[i] == t[j - 1]:
                j -= 1
            # record which index s[i] can be reached
            suf[i] = j
            # j is a subsequence of s
            if j == 0: return 0
        # left index
        j = 0
        # answer of deleting s[:suf[0]]
        ans = suf[0]
        # combine parts of calculate pre list and answer together
        for i, ch in enumerate(s):
            # if we have a match from prefix
            if ch == t[j]:
                j += 1
                # calculate answer of deleting t[j: suf[i + 1]]
                ans = min(ans, suf[i + 1] - j)
        return ans