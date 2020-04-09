# -*- coding: utf-8 -*-

import pytest
from deliveroo_project.skeleton import fib

__author__ = "Jay Jay"
__copyright__ = "Jay Jay"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
