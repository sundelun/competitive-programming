from functools import cache
class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        def calc(f2: str) -> int:
            n = len(f2)
            # digits dp
            # i represent the current number of digits we are woking on
            # isnum represent whether we have filled a number before
            # islimit represent whether our previoud are filled to limit
            # add other parameters by problem
            # we start with dfs(i = 0, isnum = False, islimit = True)
            @cache
            def dfs(i: int, isnum: bool, islimit: bool, s: int, p: int) -> int:
                # return if we reached max number of digits
                if i == n:
                    return 1 if s != 0 and p % s == 0 else 0
                res = 0
                # if previously we have not filled a number, we can continue do not fill a number
                if not isnum:
                    # in this case both isnum and islimit are false
                    res += dfs(i + 1, False, False, s, p)
                # if previously are all reaching limit
                # for example if we have number 954 and previously we filled 95, then we can only fill up tp 4
                # otherwise we can fill up to 9
                up = int(f2[i]) if islimit else 9
                # the lower boound is 1 if previously we do not fill a number
                # otherwise we can start from 0
                for d in range(1 if not isnum else 0, up + 1):
                    # add the result, isnum is True now after filling a number, and islimit depends on whether the current is upper bound
                    res += dfs(i + 1, True, islimit and up == d, s + d, p * d)
                return res
            return dfs(0, False, True, 0, 1)
        # typically, if we want number of solutions in range [l, r] then calc(r) - calc(l - 1) will give us result
        return calc(str(r)) - calc(str(l - 1))