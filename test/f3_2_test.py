import os
import sys

cwd = os.getcwd()
sys.path.append(cwd)

from src.f3 import fn_sum
import pytest

@pytest.mark.parametrize(('v1','v2','res'), [
    (1, 2,3),
    (2, 3,5),
    (3, 4,7),
    (4, 5,9)
])
def test_sum1(v1,v2,res):
    assert fn_sum(v1,v2) == res

@pytest.mark.parametrize(('v1','v2','res'), [
    pytest.param(1, 2,3,id='test1'),
    pytest.param(2, 3,5,id='test2'),
    pytest.param(3, 4,7,id='test3'),
    pytest.param(4, 5,9,id='test4')
])
def test_sum2(v1,v2,res):
    assert fn_sum(v1,v2) == res
