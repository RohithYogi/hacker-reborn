'''
import math
def fact(n):
    for j in range(2,int(math.sqrt(n)+1)):
        if(n%j==0):
            return 0
    return 1
t=input()
for i in range(0,t):
    p=input()
    if(fact(p)==0):
        print 'NO'
    else:
        print 'YES'
'''
Time limit exceeded
#!/usr/bin/env python
import re
import random
 
_mrpt_num_trials = 5 # number of bases to test
 
def is_probable_prime(n):
    """
    Miller-Rabin primality test.
 
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n == 1:
        return False
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
 
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite
 
if __name__ == '__main__':
    while (1):
        testcases = int(raw_input().strip())
        while (testcases > 0):
            n = int(raw_input().strip())
            if is_probable_prime(n) == True:
                print ("YES")
            else:
                print ("NO")
            testcases -= 1
        break
