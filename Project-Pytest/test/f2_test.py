import os
import sys

cwd = os.getcwd()
sys.path.append(cwd)

from src.f2 import fn_div

'''Assert that a certain exception is raised
'''

import pytest

def test_answer1():
    with pytest.raises(ZeroDivisionError):
        fn_div(1, 0)

@pytest.mark.xfail(raises=ZeroDivisionError,reason="This test is expected to fail")
def test_answer2():
    fn_div(1, 0)

@pytest.mark.xfail(raises=IndexError)#ZeroDivisionError
def test_hello7():
    x = []
    x[1] = 1
