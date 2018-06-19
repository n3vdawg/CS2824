from __future__ import print_function

def computePow (m,n,e):
    """ The idea is to compute m^e mod n """
    p = m # p will hold m^{2^j}
    r = 1 # r is the result
    while ( e > 0):
        if (e % 2 == 1):
            r = (r * p) % n
        p = (p * p) % n
        e = e // 2
    return r %n


def encodeMessageString (s, n, e):
    """ Encode a string as a sequence of RSA numbers """
    l = list(s)
    l1 = list(map ( lambda c: ord(c), l))
    print(list(l1))
    l2 = list(map ( lambda j: computePow(j,n,e), l1))
    return l2


def decodeMessageList (l, n, d):
    l = list(map(lambda j: computePow(j,n,d), l))
    print(l)
    l1 = list(map ( chr, l))
    s = ''.join(l1)
    return s


# if __name__ == "__main__":
#     import sys
#     l = encodeMessageString(str(sys.argv[1]),int(sys.argv[2]), int(sys.argv[3]))
#     print l

if __name__ == "__main__":
    import sys
    print('Enter the string to encode:', end ='')
    st = input()
   ## print 'You entered <- ', st
    print ('Enter key file: ', end ='')
    keyFile = input()
    print (' >> I will read keys from: ', keyFile)
    f = open(keyFile,'r')
    n = int(f.readline())
    e = int(f.readline())
    print (' >> n=',n,' e= ',e)
    dlist = encodeMessageString(st,n,e)
    print (' >> Encoded Message Stream: ', dlist)
    f.close ()
    print ('Where should I write the encoded message to? ',end = '')
    outFile = input()
    f = open(outFile, 'w')
    for n in dlist:
        f.write(str(n))
        f.write('\n')
    #f.write(str(dlist))
    f.close()
    print (' >> done. ')
