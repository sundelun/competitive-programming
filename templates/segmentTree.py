class FenwickTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.fw = [0] * (n + 1) # by using index from 1 to n
    
    # a[i] add delta, O(logN)
    def update(self, i: int, delta: int):
        while i <= self.n:
            self.fw[i] += delta
            i += i & -i
    
    # calculate the prefix sum of a[1] + a[2] + .. +a[i], O(logN)
    def prefix(self, i: int) -> int:
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & -i
        return s
    
    # calculate the inerval sum of a[l] + a[l + 1] .... + a[r], O(logN)
    def query(self, l: int, r: int) -> int:
        if r < l:
            return 0
        return self.prefix(r) - self.prefix(l - 1)
