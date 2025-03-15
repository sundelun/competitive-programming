def precompute_factorials(max_n: int, mod: int) -> tuple[list[int], list[int]]:
    fact = [1] * (max_n + 1)
    invfact = [1] * (max_n + 1)
    for i in range(1, max_n + 1):
        fact[i] = fact[i - 1] * i % mod
    invfact[max_n] = pow(fact[max_n], mod - 2, mod)  # Fermat inverse
    for i in range(max_n - 1, -1, -1):
        invfact[i] = invfact[i + 1] * (i + 1) % mod
    return fact, invfact
 
def nCr(n: int, r: int, fact: list[int], invfact: list[int], mod: int) -> int:
    if r < 0 or r > n:
        return 0
    return fact[n] * invfact[r] % mod * invfact[n - r] % mod
 
MOD = 10 ** 9 + 7
MX = 2 * 10 ** 5 + 1
fact, invfact = precompute_factorials(MX, MOD)
 
"""
Example call:
ways1 = nCr(n1, r1, fact, invfact, MOD)
ways0 = nCr(n2, r2, fact, invfact, MOD)
"""