# coding: utf-8
"""
Test cases for testing results
"""

import random


def test_always_pass():
    pass


def test_always_fails():
    raise Exception("This just fails")


def test_randomly_fails():
    if random.choice([True, False]):
        raise Exception("Random fail")


def test_randomly_fails2():
    if random.choice([True, False]):
        raise Exception("Random fail")

