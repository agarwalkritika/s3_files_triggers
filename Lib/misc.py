import random

DEBUG = False

def create_random_string(length=3):
    original_string = 'abcdefghijklmnopqrstuvwxyz'
    a = ''
    for random_string in range(0, length):
        a += random.choice(original_string)
    return a

class Custom_Exception(BaseException):
     pass


def custom_log(message, level="INFO"):
    if level == "DEBUG" and DEBUG is not True:
        return
    print(message)
