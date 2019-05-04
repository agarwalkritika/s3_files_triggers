import random


def create_random_string(length=3):
    original_string = 'abcdefghijklmnopqrstuvwxyz'
    a = ''
    for random_string in range(0, length):
        a += random.choice(original_string)
    return a

class Custom_Exception(BaseException):
     pass

