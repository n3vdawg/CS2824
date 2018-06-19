import sys
import random


# Copied from Rosetta Code Online
def is_probable_prime(n, s=50):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.

    >>> is_probable_prime(1)
    Traceback (most recent call last):
        ...
    AssertionError
    >>> is_probable_prime(2)
    True
    >>> is_probable_prime(3)
    True
    >>> is_probable_prime(4)
    False
    >>> is_probable_prime(5)
    True
    >>> is_probable_prime(123456789)
    False

    >>> primes_under_1000 = [i for i in range(2, 1000) if is_probable_prime(i)]
    >>> len(primes_under_1000)
    168
    >>> primes_under_1000[-10:]
    [937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    >>> is_probable_prime(6438080068035544392301298549614926991513861075340134\
3291807343952413826484237063006136971539473913409092293733259038472039\
7133335969549256322620979036686633213903952966175107096769180017646161\
851573147596390153)
    True

    >>> is_probable_prime(7438080068035544392301298549614926991513861075340134\
3291807343952413826484237063006136971539473913409092293733259038472039\
7133335969549256322620979036686633213903952966175107096769180017646161\
851573147596390153)
    False
    """
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)

    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite

    for i in range(s+1):
        a = random.randrange(2, n)
        if try_composite(a):
            return False

    return True # no base tested showed n as composite


def computeGCD(u,v):
    """ The euclidean GCD algorithm """
    # if (u > v):
    #     u,v = v,u
    u1,u2,u3 = 1,0,u
    v1,v2,v3 = 0,1,v
    while (v3 > 0):
        q = u3//v3
        t1 = u1 - q * v1
        t2 = u2 - q * v2
        t3 = u3 - q * v3
        u1,u2,u3 = v1,v2,v3
        v1,v2,v3 = t1,t2,t3
    return u1,u2,u3


def computePublicKey(k):
    e = 3
    i = k//3
    iLim = 2*k//3
    while ( i < iLim):
        e = i
        i = i +1
        (a,b,l) = computeGCD(e,k)
        if (l == 1):
            return e
    print ('Finding public key fail.')
    assert False
    return e


def computePrivateKey(k,e):
    (d,v,l) = computeGCD(e,k)
    assert (l == 1)
    assert( d * e + v * k == 1)
    # d * e + v * k = 1
    # k * e - e * k = 0
    # therefore (d + m* k)  * e + (v - m * e) k = 1
    if ( d < 0):
        m = (-d//k) + 1
        d = d + m * k
    return d


def generateRandomPrimes(s = 5):
  """ fun. generateRandomPrimes: int -> (int,int)
      generate a pair of random prime numbers """
  x = random.randint(10**(s-1), 10 ** s)
  i = x
  while ( i < 2 * x):
    if (is_probable_prime(i,5)):
      return i
    i = i + 1

  print ('Prime Number Gen. Failed')
  assert False
  return -1





if __name__ == "__main__":
    import sys
    if (len(sys.argv) >= 3):
      p,q = int(sys.argv[1]),int(sys.argv[2])
    elif (len(sys.argv) >= 2):
      p = generateRandomPrimes(int(sys.argv[1]))
      q = generateRandomPrimes(int(sys.argv[1]))
    else:
      p = generateRandomPrimes()
      q = generateRandomPrimes()

    assert(is_probable_prime(p))
    assert(is_probable_prime(q))
    prvkey = open('privatekey_1.txt', 'w')
    pubkey = open('publickey_1.txt', 'w')
    print ('p = ',p,' q = ', q)
    pubkey.write(str(p * q))
    pubkey.write('\n')
    k = (p-1) * (q-1)
    prvkey.write(str(p * q))
    prvkey.write('\n')
    e = computePublicKey(k)
    pubkey.write(str(e))
    d = computePrivateKey(k,e)
    prvkey.write(str(d))
    pubkey.close()
    prvkey.close()
