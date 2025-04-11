#代码来自0x3f，灵茶山艾府
MX = 32000
is_prime = [True] * (MX + 1)
for i in range(2, MX + 1):
    if is_prime[i]:
        for j in range(i * i, MX + 1, i):
            is_prime[j] = False