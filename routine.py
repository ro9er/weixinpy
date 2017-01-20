#!/usr/bin/env python

import logging

class Routine(object):

    def __init__(self):
        self.mapping = dict()

    def routine(self, path, **kw):
        route = self.mapping.get(path, None)
        if route is None:
            raise ValueError('No such method to routing')
        else:
            return route(**kw)

    def add_routine(self, path, routine):
        self.mapping[path] = routine


global_routine = Routine()


def routine(path):
    def decorator(func):
        def wrapper(*args, **kw):
            print("access to url, args:{}, kw:{}".format(args, kw))
            return func(*args, **kw)
        global_routine.add_routine(path, wrapper)
        return wrapper
    return decorator
