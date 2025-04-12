# https://codeforces.com/problemset/problem/446/A
def solve():
    n = int(input())
    arr = [int(x) for x in input().split()]
    f = [[0] * 2 for _ in range(n)]
    # f[i][0] represents ending with a[i]'s longest increasing subarray
    # f[i][1] represents we have changed one element that ending with a[i]'s longest increasing subarray(not changing a[i])
    # 2 3 5 1
    # initial set of one element not changing to 1
    f[0][0] = 1
    ans = 1
    for i in range(1, n):
        # if arr[i] > arr[i - 1] then f[i][j] = f[i - 1][j] + 1
        if arr[i] > arr[i - 1]:
            f[i][0] = f[i - 1][0] + 1
            f[i][1] = f[i - 1][1] + 1
        else:
            # f[i][0] can only be 1
            f[i][0] = 1
            # by changing a[i - 1] to a very small number
            f[i][1] = 2
        # by changing a[i - 1] such that a[i] > a[i - 1] > a[i - 2]
        if i > 1 and arr[i] > arr[i - 2] + 1:
            f[i][1] = max(f[i][1], f[i - 2][0] + 2)
        # there is another case such that we can change a[i] to a very large number so that f[i][1] = f[i - 1][0] + 1
        # but then the calculation afterwards will not work, i.e. f[i] = f[i - 1] + 1 might not be true since
        # arr[i] might not be strictly greater than arr[i - 1]
        # therefore we can only use f[i - 1][0] + 1 to update answer
        # update the answer with all possible cases
        ans = max(ans, f[i][0], f[i][1], f[i - 1][0] + 1)
    print(ans)
#for _ in range(int(input())):
solve()