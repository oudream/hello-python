#!/usr/bin/env python3
# coding: utf-8

"""
ygct_common
"""
#装饰器
def method(prototype):
    class MethodDescriptor(object):
        def __init__(self, func):
            self.func = func
            self.bound_funcs = {} # hold on to references to prevent gc
        def __get__(self, obj, type=None):
            assert obj is not None # always require an instance
            try: return self.bound_funcs[obj,type]
            except KeyError:
                ret = self.bound_funcs[obj,type] = prototype(
                    self.func.__get__(obj, type))
                return ret
    return MethodDescriptor

