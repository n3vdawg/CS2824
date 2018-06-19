#! /usr/bin/python
import math
import random

def computePow (m,n,e):
    """ The idea is to compute m^e mod n """
    p = m # p will hold m^{2^j}
    r = 1 # r is the result
    while ( e > 0):
        if (e %2 == 1):
            r = (r * p)%n
        p = (p*p) % n
        e = e // 2
    return r %n


def encodeMessageString (s, n, e):
    """ Encode a string as a sequence of RSA numbers """
    l = list(s)
    l1 = list(map ( lambda c: ord(c), l))
    l2 = list(map ( lambda j: computePow(j,n,e), l1))
    return l2


def decodeMessageList (l, n, d):
    l = list(map( lambda j: computePow(j,n,d) % 256, l))
    l1 = list(map ( chr, l))
    s = ''.join(l1)
    return s

def factorize_Rho(n):
    i = 2
    j = 2
    x = 1
    size = 2
    p = 1
    while p == 1:
        while x <= size and p <= 1:    
            i = (i**2 + 1) % n
            p = math.gcd(abs(i-j), n)
            x = x + 1
        size = size * 2
        j = i
    return p

def factorize7(n):
    i = int(math.sqrt(n)//1)
    if n % i == 0:
        return i
    if i % 2 == 0:
        i = i-1
    
    while i > 0:
        if i % 30 == 0:
            i = i + 5
            break
        else:
            i = i - 1
    
    while i > 0:
        # skip if n % i == 0:
           
        if n % (i+2)== 0:
            return i+2
      #  if n % (i+2*2)== 0:
       #     return i+4
        if n % (i+2*3)== 0:
            return i+6
        if n % (i+2*4)== 0:
            return i+8
       # if n % (i+2*5)== 0:
        #    return i+10
        if n % (i+2*6)== 0:
            return i+12
        if n % (i+2*7)== 0:
            return i+14
        #if n % (i+2*8)== 0:
         #   return i+16
        if n % (i+2*9)== 0:
            return i+18
       # if n % (i+2*10)== 0:
        #    return i+20
      #  if n % (i+2*11)== 0:
       #     return i+22
        if n % (i+2*12)== 0:
            return i+24
        if n % (i+2*13)== 0:
            return i+26
        #if n % (i+2*14)== 0:
         #   return i+28
        #if n % (i+2*15)== 0:
         #   return i+30
                
        i = i - 30

def euclid(m , n):
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1
    k = m % n
    while k > 0:
        k = m % n
        q = m // n
        m = n 
        n = k
        s1prev = s1
        t1prev = t1
        s2prev = s2
        t2prev = t2        
        s2 = s1prev - q*s2prev
        t2 = t1prev - q*t2prev
        s1 = s2prev
        t1 = t2prev 
        if k == 0:
            break
    return t1

def theD(n, e):
    p = int(factorize7(n))
    q = int(n / p)
    eu = euclid((p-1)*(q-1), e)
    d = int(((p-1)*(q-1)) + eu)
    return d

# if __name__ == "__main__":
#     import sys
#     l = encodeMessageString(str(sys.argv[1]),int(sys.argv[2]), int(sys.argv[3]))
#     print l

if __name__ == "__main__":
    import sys
    print('Enter filename to decode:', end='')
    encFile = input()
    f1 = open (encFile,'r')
    dlist = []
    for line in f1:
        dlist.append(int(line))
    print ('   >> OK! Encoded msg:', str(dlist))
    f1.close()
    print('Enter public key file path for decryption use:', end='')
    pubFile = input()
    pubOpen = open(pubFile,'r')
    nvl = int(pubOpen.readline())
    evl = int(pubOpen.readline())
    dvl = theD(nvl, evl)
    pubOpen.close()
    prvkey = open('privatekey.txt', 'w')
    prvkey.write(str(nvl))
    prvkey.write('\n')
    prvkey.write(str(dvl))
    prvkey.close()
    print('Enter key file: ', end='')
    keyFile = input()
    print ('   >> I will read keys from: ', keyFile)
    f = open(keyFile,'r')
    n = int(f.readline())
    e = int(f.readline())
    print ('   >> n=',n,' d= ',e)
    s = decodeMessageList(dlist,n,e)
    print ('   >> decoded message: ', s)
    f.close()
