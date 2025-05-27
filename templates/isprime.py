#代码来自0x3f，灵茶山艾府
MX = 32000
is_prime = [True] * (MX + 1)
for i in range(2, MX + 1):
    if is_prime[i]:
        for j in range(i * i, MX + 1, i):
            is_prime[j] = False

import math
# check if number n is prime helper-function
def is_prime(n: int) -> bool:
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return n >= 2

# if an integer m is not divisible by any prime numbers within math.isqrt(m), then m is prime number as well
