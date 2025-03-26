# https://codeforces.com/contest/2085/problem/C
def solve():
    x, y = map(int, input().split())
    # (x + k) + (y + k) = (x + k) xor (y + k) is equivalant to (x + k) and (y + k) = 0
    # a number that is a power of 2 does not share any digits with number that is less than him
    # if x == y then no possible k value
    if x == y:
        print(-1)
        return
    if x & y == 0:
        print(0)
        return
    # to make x < y
    if x > y:
        x, y = y, x
    st = 1
    while st <= y:
        st <<= 1
    # the answer to k is 2 ** n - max(x, y)
    print(st - y)
for _ in range(int(input())):
    solve()