import bisect
# https://codeforces.com/contest/2075/problem/C
def solve():
    n, m = map(int, input().split())
    arr = [int(x) for x in input().split()]
    arr.sort()
    # [2, 4]
    # left = 1, right = 4
    # cntleft = 2, cntright = 1
    ans = 0
    # iterate over all possible number of first elememtn, which is left, and right = m - left
    for left in range(1, n):
        right = n - left
        # we count the number of elements that are satisfy by number of left and right, respectively
        # m - bisect_left will give us the number that satisfy
        cntleft = bisect.bisect_left(arr, left)
        cntright = bisect.bisect_left(arr, right)
        cntleft = m - cntleft
        cntright = m - cntright
        if cntleft == 0 or cntright == 0: continue
        # we need to minus the overlapping count 
        # for example consider 5 8 9 and n = 12, if left = 5 and right = 7
        # then cntleft = 3 and cntright = 2
        # if we just add answer by 3 * 2, the case of nums' left = nums' right = 8 and nums' left = nums'right = 9 will be counted, which is invalid
        # so we need to minus the minimum of (cntleft, cntright)
        mn = min(cntleft, cntright)
        ans += (cntleft * cntright) - mn
    print(ans)
for _ in range(int(input())):
    solve()