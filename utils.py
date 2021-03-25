from typing import List
from math import ceil
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


def create_list_of_duplicate_email_pairs(size: int) -> List[str]:
    if size <= 1:
        raise ValueError('size should be greater than 1')

    if size % 2 == 0:
        return [create_random_email() for _ in range(ceil(size / 2))] * 2
    else:
        get_lower_half_of_size = size - ceil(size / 2)
        list_of_duplicate_emails = [create_random_email() for _ in range(get_lower_half_of_size)] * 2
        first_item_in_list = list_of_duplicate_emails[0]
        list_of_duplicate_emails.append(first_item_in_list)

        return list_of_duplicate_emails


def create_list_of_unique_and_duplicate_emails(size: int = 100000, duplicate_percent: float = .50) -> List[str]:
    unique_email_count = ceil(size * duplicate_percent)
    duplicate_email_count = size - unique_email_count
    duplicate_email_list = create_list_of_duplicate_email_pairs(duplicate_email_count)
    unique_emails_list = create_list_of_unique_emails(unique_email_count)

    lists_with_unique_and_duplicate_emails = duplicate_email_list + unique_emails_list
    random.shuffle(lists_with_unique_and_duplicate_emails)

    return lists_with_unique_and_duplicate_emails
