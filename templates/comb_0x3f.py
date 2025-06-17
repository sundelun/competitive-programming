MOD = 10 ** 9 + 7
MX = 10 ** 5

f = [0] * MX  # f[i] = i!
f[0] = 1
for i in range(1, MX):
    f[i] = f[i - 1] * i % MOD

inv_f = [0] * MX  # inv_f[i] = i!^-1
inv_f[-1] = pow(f[-1], -1, MOD)
for i in range(MX - 1, 0, -1):
    inv_f[i - 1] = inv_f[i] * i % MOD

def comb(n: int, m: int) -> int:
    return f[n] * inv_f[m] * inv_f[n - m] % MOD

def perm(n: int, m: int) -> int:
    if m > n or m < 0: 
        return 0
    return f[n] * inv_f[n - m] % MOD

"""
example call: 
ans_comb = comb(10, 5) same as 10C5
ans_perm = perm(9, 5) same as 9P5 (9 * 8 * 7 * 6 * 5)
"""