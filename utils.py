import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        start_time = time.time()
        ref = func(*args, **kwargs)
        end_time = time.time()
        print('{:s} function took {:.3f} ms to execute'.format(func.__name__, (end_time - start_time) * 1000.0))

        return ref

    return wrap
