from functools import wraps
from time import perf_counter


def timethis(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = perf_counter()
        result = f(*args, **kw)
        te = perf_counter()
        print('func:%r args:[%r, %r] took: %2.4f ms' % \
          (f.__name__, args, kw, (te-ts)*1000))
        return result
    return wrap