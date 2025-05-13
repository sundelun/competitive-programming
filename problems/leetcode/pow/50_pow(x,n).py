class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        # if n < 0 then we treat n = -n and x = 1/x which is same as positive n pow calculation
        if n < 0:
            n = -n
            x = 1 / x
        # the idea of this question is if we want to cauculate x ^ 13
        # 13 = 1101 in binary, the result is x * (x ^ 4) * (x ^ 8)
        # so we multiply all bits with 1 with its corresponding pow(x)
        while n:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1
        return ans