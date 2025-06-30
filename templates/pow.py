MOD = 10 ** 9 + 7
MX = 10 ** 5

pow2 = [1] * MX  # pow2[i] = 2 ** i % MOD
for i in range(1, MX):
    pow2[i] = pow2[i - 1] * 2 % MOD