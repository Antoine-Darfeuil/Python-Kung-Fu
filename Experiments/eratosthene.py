
import os, sys
import math
import time

toolsModulePath = os.path.abspath("../Tools")
sys.path.append(toolsModulePath)
from performance_tools import timeit



##############################################################
#           FIND ALL PRIME NUMBERS BELOW NMAX                #
##############################################################   

def eratosthene_sieve_wrong(n_max, verbose=False):
    primes = []
    nb_loop = 0
    for n in range(2, n_max+1):
        for p in primes[:math.floor(math.sqrt(n))]: # !!WARNING!!: works with pretty good speed but is wrong
            nb_loop += 1
            if n % p == 0: break
        else:
            primes.append(n)
            if verbose: print(n, "is prime")
    return nb_loop

@timeit(1)
def eratosthene_sieve(n_max, verbose=False):
    primes = []
    nb_loop = 0
    for n in range(2, n_max+1):
        search_limit = math.ceil(math.sqrt(n)) # warning: must be computed as less as possible for speed
        for p in primes:
            nb_loop += 1
            if n % p == 0: break
            if p > search_limit:
                primes.append(n)
                break
        else:
            primes.append(n)
        if verbose and n%10000 == 0: print("progress: {:.3f} %".format(n/n_max*100))
    return primes

###############################################################################
# W A R N I N G  -  P Y T H O N   U N F O R S E E N   C O N S E Q U E N C E S #
# mutable default value as argument                                           #
###############################################################################

def primo_fact(x, primes=[2]):
    #_____________________ ^ _____________________________________________________
    # M A J O R  -  E R R O R                                                     #
    # mutable default value as argument                                           # 
    
    prime_factors = []
    print("starting:", primes)
    print(primes[-1], math.ceil(math.sqrt(x)))

    for n in range(primes[-1], math.ceil(math.sqrt(x))):
        search_limit = math.ceil(math.sqrt(n))
        next_prime = primes[-1]
        for p in primes:
            if n % p == 0: break # exit 'for p' loop --> means n is not prime --> go to next n
            if p > search_limit:
                primes.append(n)
                next_prime = n
                break
        else:
            primes.append(n)
            next_prime = n
            
        if x % next_prime == 0:
            while x % next_prime == 0:
                prime_factors.append(next_prime)
                x = x / next_prime
            prime_factors += primo_fact(x, primes)
            break # exit 'for n' loop --> means x is not prime --> go to function end
    else:
        prime_factors.append(int(x))

    return prime_factors

def bad_function(l=[5]):
    '''Try me.'''
    print(l)
    for i in range(10):
        l.append(10)           
###############################################################################
# W A R N I N G  -  P Y T H O N   U N F O R S E E N   C O N S E Q U E N C E S #
# mutable default value as argument                                           # 
###############################################################################           


        
##############################################################
#               FIND PRIME FACTORIZATION                     #
##############################################################        

@timeit(1)
def prime_factorization(x, primes=None, verbose=False):
    
    if primes is None: primes = [2]
    prime_factors = []

    for n in range(primes[-1], math.ceil(math.sqrt(x))):
        if verbose and n % 100==0:
            print("progress: {:.4f}%".format(n/math.ceil(math.sqrt(x))*100))
        search_limit = math.ceil(math.sqrt(n))
        next_prime = primes[-1]
        for p in primes:
            if n % p == 0: break # exit 'for p' loop --> means n is not prime --> go to next n
            if p > search_limit:
                primes.append(n)
                next_prime = n
                break
        else:
            primes.append(n)
            next_prime = n
            
        if x % next_prime == 0:
            while x % next_prime == 0:
                prime_factors.append(next_prime)
                x = x / next_prime
            prime_factors += prime_factorization(x, primes)
            break # exit 'for n' loop --> means x is not prime --> go to function end
    else:
        prime_factors.append(int(x))

    return prime_factors

##############################################################
#                   CHECK IF PRIME                           #
##############################################################
AVERAGE_ON = 1
              
@timeit(AVERAGE_ON)
def isPrime(x, verbose=False, print_every=1000000):
    primes = []
    max_nb_loop = math.ceil(math.sqrt(x))
    
    for n in range(2, math.ceil(math.sqrt(x))):
        search_lim = math.ceil(math.sqrt(n))
        for p in primes:
            if n % p == 0: break
            if p > search_lim:
                primes.append(n)
                next_prime = n
                break
        else:
            primes.append(n)
            next_prime = n

        if x % next_prime == 0:
            return False, next_prime
        
        if verbose and n % print_every == 0: print("progress: {:.4f}%".format(n/max_nb_loop*100))
    else:
        return True
        
@timeit(AVERAGE_ON)
def isprime(x, verbose=False, print_every=1000000):
    max_nb_loop = math.ceil(math.sqrt(x))
    if verbose: print("nb loops", max_nb_loop)

    for n in range(2, math.ceil(math.sqrt(x))):
        if x % n == 0: return False, n
        if verbose and n % print_every == 0: print("progress: {:.4f}%".format((n+1)/max_nb_loop*100))

    else:
        return True

@timeit(AVERAGE_ON)
def isitprime(x, verbose=False, print_every=1000000):
    max_nb_loop = math.ceil(math.sqrt(x))
    if verbose: print("nb loops", max_nb_loop)
    
    for n in range(2, math.ceil(math.sqrt(x))):
        if verbose and n % print_every == 0: print("progress: {:.4f}%".format((n+1)/max_nb_loop*100))
        if n%2==0 or n%5==0: continue
        if x % n == 0: return False, n
    else:
        return True



#############################
#          OTHERS           #
#############################

def mult(l):
    res = 1
    for elt in l:
        res *= elt
    return res
        

if __name__ == '__main__':

    nmax = 200000
    verbose = False if nmax < 20000 else True
    print("Prime numbers: < %s" % nmax)
    plist = eratosthene_sieve(nmax, verbose=verbose)

    print(isPrime(89))
    print(prime_factorization(567890))
    print(prime_factorization(678768909))

    print(isPrime(2486333))
    print(isprime(2486333))

    
# 567989763678920087 is a prime number (took 6min to check)

