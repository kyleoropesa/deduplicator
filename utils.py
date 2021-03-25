from typing import List
import functools
import time
import random
import string


def timer(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        start_time = time.time()
        ref = func(*args, **kwargs)
        end_time = time.time()
        print('{:s} function took {:.3f} ms to execute'.format(func.__name__, (end_time - start_time) * 1000.0))

        return ref

    return wrap


def create_random_email() -> str:
    random_username = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return f'{random_username}@sample.com'


def create_list_of_unique_emails(size: int) -> List[str]:
    return [create_random_email() for _ in range(size)]
