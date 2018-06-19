import os, sys, time
import math
from functools import wraps

def timeit(average_on):
    def decorator(decorated_function):
        @wraps(decorated_function)
        def new_function(*args, **kwargs):
            exec_times = []
            for i in range(average_on):
                start  = time.time()
                res    = decorated_function(*args, **kwargs)
                dt     = time.time() - start
                exec_times.append(dt)
            print("{:} : {:f}s".format(res, dt))
            return res
        return new_function
    return decorator
    
        
