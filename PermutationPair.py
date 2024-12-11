# cook your dish here

MOD = 10**9 + 7
def factorial_precompute(n, MOD):
    fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = fact[i-1] * i % MOD
    return fact

def inverse_precompute(n, fact, MOD):
    inv = [1] * (n + 1)
    inv[n] = pow(fact[n], MOD-2, MOD)
    for i in range(n-1, -1, -1):
        inv[i] = inv[i+1] * (i+1) % MOD
    return inv

def binomial(n, k, fact, inv, MOD):
    if k > n or k < 0:
        return 0
    return fact[n] * inv[k] % MOD * inv[n - k] % MOD 

def solve():
    n, k = map(int, input().split())
    m = 0
    for a in range(1, min(k//2 + 1, n+1)):
        b = k - a
        if a < b <= n:
            m += 1

    fact = factorial_precompute(n, MOD)
    inv = inverse_precompute(n, fact, MOD)
    result = 0
    for t in range(1, m+1):
        comb = binomial(m, t, fact, inv, MOD)
        term = comb * pow(2, t, MOD) % MOD
        term = term * fact[n - t] % MOD
        if t % 2 == 1:
            result = (result + term) % MOD
        else:
            result = (result - term + MOD) % MOD
    print(result)

t = int(input())

for _ in range(t):

    solve()
