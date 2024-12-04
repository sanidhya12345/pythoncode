import math

def SieveOfEratosthenes(num):
    prime = [True for _ in range(num+1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    prime[0] = prime[1] = False  # 0 and 1 are not prime numbers
    return prime

def segmentedSieve(l, r):
    limit = int(math.sqrt(r)) + 1
    prime = SieveOfEratosthenes(limit)
    primes = []

    for i in range(l, r+1):
        primes.append(True)
    if l == 1:
        primes[0] = False  # 1 is not a prime number

    for p in range(2, limit):
        if prime[p]:
            # Find the minimum number in [l..r] that is a multiple of p
            start = max(p * p, (l + p - 1) // p * p)
            for j in range(start, r+1, p):
                primes[j - l] = False

    return primes

t = int(input())
results = []
for _ in range(t):
    l, r = map(int, input().split())
    primes = segmentedSieve(l, r)
    test_case_result = []
    for i in range(l, r+1):
        if primes[i - l]:
            test_case_result.append(i)
    results.append(test_case_result)

for result in results:
    for prime in result:
        print(prime)
    print()
