# Your names:
# Tyler Nevell
# Cody Hegwer
#
#

# Did you copy and paste code from any online source?
"""
No copy and paste, but code and queries were referrenced in order to understand
pollard's rho and eliptical curve.
   
https://www.pythoncentral.io/how-to-use-pythons-xrange-and-range/
https://crypto.stackexchange.com/questions/5774/choosing-good-parameter-for-lenstras-elliptic-curve-factorization
https://stackoverflow.com/questions/30017367/lenstras-elliptic-curve-factorization-problems
https://www.youtube.com/watch?v=ZEyr-rUNSRU
https://gist.github.com/thomdixon/dd1e280681f16535fbf1
https://en.wikipedia.org/wiki/Lenstra_elliptic-curve_factorization
https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
"""


# Note: you are not allowed to do so for this assignment.
# Your answer should generally be "no". But if you did,
# mark the code clearly and explain here why you needed to do so.

# Did you collaborate with someone outside your team?
# If yes, explain what you obtained from the collaboration.

# Did you post queries on online forums (such as stackoverflow, ..)
# related to this assignment?
# If yes, post the links here.

#----------- IMPORTS ---------------------

# If you have import statements, please explain in comments
# why you need them. You can be very brief.

from __future__ import print_function
# I import this just for compatibility with python2 please use python3
# though.

import sys
# sys has useful utilities I need.

from time import clock as time_clock
# Time is being imported to measure
# running time for the factorize
# function.

import math
# for gcd
import random
# for randrange
# -------------------------------------------



# This is the brute force algorithm.
# You are being asked to improve upon this
def factorize(n):
    for i in range(2, n-1):
        if n % i == 0:
            return i
    assert False, 'You gave me a prime number to factor'
    return -1


# Improve on factorize function above:
# Call your functions factorize1, factorize2, ...
# Please write a brief comment before each function to describe
# the improvements you are trying out.
def factorize1(n):
    if n % 2 == 0:
        return 2
    
    i = 3
    nSquareRoot = math.sqrt(n)
    while i <= nSquareRoot:
        if n % i == 0:
            return i
        else:
            i = i + 2
    assert False, 'You gave me a prime number to factor'
    return -1


def factorize2(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    
    i = 3
    nSquareRoot = math.sqrt(n)
    while i <= nSquareRoot:
        # skip n % i == 0:
        
        if n % (i+2)== 0: #i + 2*1
            return i+2
        if n % (i+4)== 0: #i + 2*2
            return i+4
        
        #skip n % (i+2*3) == 0:
        
        i = i + 6
            
    assert False, 'You gave me a prime number to factor'
    return -1
    
def factorize3(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    if n % 5 == 0:
        return 5
    
    i = 5
    nSquareRoot = math.sqrt(n)
    while i <= nSquareRoot:
        # skip if n % i == 0:
           
        if n % (i+2)== 0:
            return i+2
        if n % (i+4)== 0:
            return i+4
        if n % (i+6)== 0:
            return i+6
        if n % (i+8)== 0:
            return i+8
        
        #skip n % (i+2*5) == 0:
        
        i = i + 10
            
    assert False, 'You gave me a prime number to factor'
    return -1



def factorize4(n):
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    if n % 5 == 0:
        return 5
    
    i = 5
    nSquareRoot = math.sqrt(n)
    while i <= nSquareRoot:
        # skip if n % i == 0:
           
        if n % (i+2)== 0:
            return i+2
      #  if n % (i+2*2)== 0:
       #     return i+4
        if n % (i+6)== 0:
            return i+6
        if n % (i+8)== 0:
            return i+8
       # if n % (i+2*5)== 0:
        #    return i+10
        if n % (i+12)== 0:
            return i+12
        if n % (i+14)== 0:
            return i+14
        #if n % (i+2*8)== 0:
         #   return i+16
        if n % (i+18)== 0:
            return i+18
       # if n % (i+2*10)== 0:
        #    return i+20
      #  if n % (i+2*11)== 0:
       #     return i+22
        if n % (i+24)== 0:
            return i+24
        if n % (i+26)== 0:
            return i+26
        #if n % (i+2*14)== 0:
         #   return i+28
        #if n % (i+2*15)== 0:
         #   return i+30
                
        i = i + 30
            
    assert False, 'You gave me a prime number to factor'
    return -1


# Pollard's Rho: p will remain = 1 until a factor of n is found.
# Follows Wikipedia example. Reason: Couldn't find a more efficient design
# that didn't look nearly the same.
def factorize_Rho(n):
    """i = 2
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
    i = 2
    j = 2
    while i <= math.sqrt(n):
        i = (i**2 + 1) % n 
        p = math.gcd(abs(i-j), n)
    return p"""

    #assert False, 'You gave me a prime number to factor'
      



# Below we have test code:
# to test your function say factorize2, you would simply call

# python3 factorize_main.py factorize2

if __name__ == '__main__':
    # First parse command line arguments and figure out which
    # function we want to test
    if len(sys.argv) <= 1:
        fun = factorize4
    else:
        fun_to_call_string = sys.argv[1]
        assert fun_to_call_string in globals(), ('You did not implement '+fun_to_call_string)
        globals_copy= globals().copy()
        fun = globals_copy.get(fun_to_call_string)
    # Open the file with list of numbers
    f = open('composite_list.txt', 'r')
    # test each number
    for line in f:
        n = int(line)
        print('Factoring', n, '(', len(line), 'digits ): ', end='')
        t1 = time_clock() # Record time
        p = fun(n)
        t2 = time_clock() # Record time
        time_elapsed = t2 - t1  # seconds
        print('Factor = ', p, ' other factor = ', n/p, ' Time Elapsed: ', time_elapsed)
        if n % p != 0:
            print('Factorization failed for: ', n)
            sys.exit(1)
    f.close()
