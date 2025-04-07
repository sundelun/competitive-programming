# https://codeforces.com/contest/1883/problem/E

# if arr[i - 1] > arr[i] then we must make arr[i] bigger
# to make arr[i - 1] <= arr[i], we need ((arr[i - 1] - 1) // arr[i]).bit_length() (p2)number of operations
# if arr[i - 1] make pre times operations, then we need pre + p2 number of operations
# if arr[i - 1] <= arr[i], we will first find the minimum of arr[i] such that arr[i - 1] <= arr[i] still holds
# this require (arr[i] // arr[i - 1]).bit_length() (p1) number of operations
# if arr[i - 1] make pre number of operations, then we need max(pre - p1, 0)
# Consider the example 11 2 15 
# We first make to 11 16 15 and pre = 3
# next we calculate the new pre
# the number of operations of to make min of arr[2] and still >= 2 is 2
# which is equivalent to (arr[i] // arr[i - 1]).bit_length() - 1
# so p1 = (arr[i] // arr[i - 1]).bit_length() - 1
# if we make pre numebr of operations on arr[i - 1]
# for this one, we need max(pre - p1, 0) number of operations
# because a[i - 1] takes pre number of operations to make a[i - 1] * pow(2, pre)
# and our intend is to make a[i] // pow(2, p1) >= a[i - 1] * pow(2, pre)
# so we need a total of pre - p1 number of operations!
# 8 2 15 -> 8 8 15
def solve():
    n = int(input())
    arr = [int(x) for x in input().split()]
    ans = 0
    pre = 0
    for i in range(1, n):
        if arr[i - 1] > arr[i]:
            val = ((arr[i - 1] - 1) // arr[i]).bit_length()
            ans += pre + val
            pre += val
        else:
            pre = max(pre - (arr[i] // arr[i - 1]).bit_length() + 1, 0)
            ans += pre
    print(ans)
for _ in range(int(input())):
    solve()