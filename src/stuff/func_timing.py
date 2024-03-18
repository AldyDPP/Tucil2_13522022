from functools import wraps
from time import perf_counter

# Courtesy of GeeksForGeeks
def timethis(func): 
    def wrap_func(*args, **kwargs): 
        t1 = perf_counter() 
        result = func(*args, **kwargs) 
        t2 = perf_counter() 
        print(f'Executed in {1000*(t2-t1):.2f}ms') 
        return result 
    return wrap_func