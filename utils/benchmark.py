#!/usr/bin/env python
# -*- coding: utf8 -*-
#   _                    _                       _           _    _  _     
#  | |__  ___  _ _   __ | |_   _ __   __ _  _ _ | |__  _  _ | |_ (_)| | ___
#  | '_ \/ -_)| ' \ / _|| ' \ | '  \ / _` || '_|| / / | || ||  _|| || |(_-<
#  |_.__/\___||_||_|\__||_||_||_|_|_|\__,_||_|  |_\_\  \_,_| \__||_||_|/__/
#
# 2012 - Federico Mendez
import random

def benchmark(func):
    """
    A decorator that prints the time a function takes
    to execute.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print "\t%s" % func.__name__, time.clock()-t
        return res
    return wrapper


def logging(func):
    """
    A decorator that logs the activity of the script.
    (it actually just prints it, but it could be logging!)
    """
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print func.__name__, args, kwargs
        return res
    return wrapper


def counter(func):
    """
    A decorator that counts and prints the number of times a function has been executed
    """
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print "{0} has been used: {1}x".format(func.__name__, wrapper.count)
        return res
    wrapper.count = 0
    return wrapper

@benchmark
def random_tree(n):
    temp = [n for n in range(n)]
    for i in range(n+1):
        temp[random.choice(temp)] = random.choice(temp)
    return temp

