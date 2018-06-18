import sys, os, time


#######################################################
# Examples                                            #
#######################################################
# See PEP318 for examples

# Simple function decorator:
# =========================
def deprecated(function):
    name = function.__name__
    def newfunction(*args, **kwargs):
        print("Calling:", name)
        print("!!WARNING!! : This feature is deprecated.")
        return function(*args, **kwargs)
    return newfunction

# Simple function decorator:
# =========================
def timeit(function):
    def newfunc(*args, **kwargs):
        start = time.time()
        res = function(*args, **kwargs)
        dt = time.time() - start
        print("{:} : {:f}s".format(res, dt))
        return res
    return newfunc

'''
def timeit(function):
    def newfunc(*args, **kwargs):
        dts = []
        for i in range(10):
            start = time.time()
            res = function(*args, **kwargs)
            dts.append(time.time() - start)
        print("average dt:", sum(dts)/10)
        return res
    return newfunc
'''

# Function decorator with parameters:
# ==================================
def repeat(n):
    def decorator(function):
        def newfunction(*args, **kwargs):
            for _ in range(n):
                function(*args, **kwargs)
        return newfunction
    return decorator
        
# Class decorator:
# ================
def singleton(Class):
    instance = {}
    def get_instance():
        if Class not in instance:
            instance[Class] = Class()
        return instance[Class]
    return get_instance

# Function decorator with parameters:
# ==================================
def control_types(*type_args, **type_kwargs):
    def decorator(function):
        def newfunc(*args, **kwargs):
            if len(type_args) != len(args): raise RuntimeError("...")
            for idx, arg in enumerate(args):
                if type(arg) is not type_args[idx]:
                    raise TypeError("Argument {} is not of type {}".format(arg, type_args[idx]))
            for key in kwargs:
                if key not in type_kwargs: raise KeyError("...")
                if type(kwargs[key]) is not type_kwargs[key]:
                    raise TypeError("{} Invalid type: {} must be of type {}".format(args[key], key, type_args[key]))
            return function(*args, **kwargs)
        return newfunc
    return decorator
                       
# Function decorator using @wraps:
# ===============================
from functools import wraps
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__, "was called.")
        return func(*args, **kwargs)
    return with_logging


############################################################################
#                                                                           #
#                                                                           #
#                                                                           #
#                                                                           #
#############################################################################

@deprecated
@repeat(5)
def pprint(string):
    print(string)

@timeit
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

@logged
def poly2(x):
    '''Compute polynomial expression x**2+x+1'''
    return x**2 + x + 1

@logged
def poly3(x):
    '''Compute polynomial expression x**3+x**2+x+1'''
    return x**3 + x**2 + x + 1

@logged
@timeit
def polyn(x, n):
    ''' Compute polynomial expression x**n+x**(n-1)+...+x+1'''
    res = 0
    if n >= 1:
         return x**n + polyn(x, n-1)
    else:
        return 1
        
def ppd(d, tab=0):
    for k, v in d.items():
        if type(v) is dict:
            ppd(v, tab+1)
        else:
            print(k, ":", v)

def ppl(l):
    for elt in l:
        print(str(elt))

def prettyprint(*agrs):
    '''Pretty print function.'''
    for elt in agrs:
        if type(elt) is dict:
            ppd(elt)
        elif type(elt) is list:
            ppl(elt)
        else:
            print(elt)

#############################################################################
#                                                                           #
#                                                                           #
#                                                                           #
#                                                                           #
#############################################################################

if __name__ == '__main__':

    print("test1".center(25, "="))
    pprint("allo")
    time.sleep(1)

    print("test1".center(25, "="))
    f10 = factorial(10)
    print(f10)
    print(hex(f10))
    poly2(50)
    print(poly2.__name__)
    print(poly2.__doc__)
    time.sleep(1)

    print("test2".center(25, "="))
    print(polyn.__doc__)
    res = polyn(2, 10)
    print(res == 2**11-1)
    print(bin(res))

    
