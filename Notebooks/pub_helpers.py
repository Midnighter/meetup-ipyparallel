# -*- coding: utf-8 -*-

from __future__ import absolute_import

"""
Informative helper functions for illustrative purposes.
"""

def size(shape):
    return shape[0] * shape[1]

def format_memory(num, dtype_size=8):
    return "{0:G} bytes.".format(num * dtype_size)

def num_pairs(shape):
    return shape[0] * (shape[0] - 1) // 2

def format_pairs(num):
    return "{0:G} pairwise comparisons.".format(num)
