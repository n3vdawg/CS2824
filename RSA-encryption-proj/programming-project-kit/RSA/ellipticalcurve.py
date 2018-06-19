# list of primes in n
import math
import random

def primes(n):
    b, p, ps = [True] * (n+1), 2, []
    for p in range(2, n+1):
        if b[p]:
            ps.append(p)
            for i in range(p, n+1, p):
                b[i] = False
    return ps

def bezout (a, b):
    if b==  0: 
        return 1, 0, a
    q, r = divmod(a, b)
    x, y, g = bezout(b, r)
    return y, x-q*y, g

def add(a, q, a, b, m):
    if p[2] == 0:
        return q
    if q[2] == 0:
        return p
    if p[0] == q[0]:
        if (p[1]+q[1]) % m == 0:
            return 0, 1, 0 # P_infinity
        n = (3 * p[0] * p[0] + a) % m
        d = (2 * p[1]) % m
    else:
        n = (q[1] - p[1]) % m
        d = (q[0] - p[0]) % m
    x, y, g = bezout(d,m)
    if g > 1:
        return 0, 0, d 
    z = (n*x*n*x - p[0] - q[0]) % m 
    return z, (n * x * (p[0] - z) - p[1]) % m, 1

def multip(k, p, a, b, m):
    r = (0, 1, 0)
    while k > 0:
        if p[2] > 1:
            return p
        if k % 2 == 1:
            r = add(p, r, a, b, m)
        k = k // 2
        p = add(p, p, a, b, m)
    return r

def factorize_lenstra(n):
    g = n
    while g == n:
        q = random.randint(0, n-1),random.randint(0, n-1), 1
        a = random.randint(0, n-1)
        b = (q[1]*q[1] - q[0]*q[0]*q[0] - a*q[0]) % n

    return

