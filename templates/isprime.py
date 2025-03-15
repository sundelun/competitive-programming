MX = 32000
is_prime = [True] * (MX + 1)
for i in range(2, MX):
    if is_prime[i]:
        for j in range(i * i, MX, i):
            is_prime[j] = False