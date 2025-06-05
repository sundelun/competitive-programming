#代码来自0x3f，灵茶山艾府
class FenwickTree:
    def __init__(self, n: int):
        self.n = n
        self.fw = [0] * (n + 1) # by using index(1-indexed) from 1 to n
        pw = 1
        # Precompute the largest power of two ≤ n, to accelerate find_kth
        while pw <= n:
            pw <<= 1
        self._top = pw >> 1 # highest power of two ≤ n

    # a[i](0-indexd for input-parameter) add delta, O(logN)
    def update(self, i: int, delta: int) -> None:
        # changed to 1-indexed
        i += 1
        while i <= self.n:
            self.fw[i] += delta
            i += i & -i
    
    # calculate the prefix sum of a[0] + a[1] + .. +a[i] (0-indexed for input-paramater), O(logN)
    def prefix(self, i: int) -> int:
        # change to 1-indexed
        i += 1
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s
    
    # calculate the inerval sum of a[l] + a[l + 1] .... + a[r] (0-indexed for input-paramater), O(logN)
    def query(self, l: int, r: int) -> int:
        if r < l:
            return 0
        return self.prefix(r) - self.prefix(l - 1)

    # return the sum over a[0...n - 1]
    def total(self) -> int:
        return self.prefix(self.n - 1)
    
    # Return the smallest index i (0-based) such that sum[0..i] >= k.
    def find_kth(self, k: int) -> int:
        idx = 0
        bit_mask = self._top
        while bit_mask > 0:
            t = idx + bit_mask
            if t <= self.n and self.fw[t] < k:
                idx = t
                k -= self.fw[t]
            bit_mask >>= 1
        # The desired Fenwick index is idx+1, so the 0-based position is (idx).
        return idx
