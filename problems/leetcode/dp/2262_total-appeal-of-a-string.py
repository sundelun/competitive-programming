# https://leetcode.cn/problems/total-appeal-of-a-string/description/
class Solution:
    def appealSum(self, s: str) -> int:
        # the record of all character's last position, we set all to -1 for convenience
        record = [-1] * 26
        ans = 0
        res = 0
        # we will calculate the answer by iterating all adding s[i] to end of s[i - 1]'s count
        # start thinking of if all characters are distinct, for example "abcde"
        # then the answer is 1 + (1 + 2) + (1 + 2 + 3) + (1 + 2 + 3 + 4) + (1 + 2 + 3 + 4 + 5)
        # so if they are not meet before, then all of their substring will be increased by 1
        # what if there are some duplicate? for example "bcdazfga", there are 2 a's
        # a at index 3, 7
        # when we reach the 2nd a, we notice that the subarray at s[0...7], s[1...7], s[2..7], s[3..7] their appeal won't get increase because they have seen a before
        # the string with s[4..7], s[5...7] and s[6...7], s[7..7] will get increased
        # so we need to record each character's last occurence index
        # if s[i] has occur before, then ending with s[i] will increased by i - j(also inclusing a substring as itself)
        # each time the res is being increased by current index - last occurence of current character's index
        for i, ch in enumerate(map(ord, s)):
            ch -= ord('a')
            # add the total count of ending wich ch by i minus last character's occurence
            res += i - record[ch]
            ans += res
            record[ch] = i
        return ans
