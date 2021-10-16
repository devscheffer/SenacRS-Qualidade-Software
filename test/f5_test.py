import os
import sys

cwd = os.getcwd()
sys.path.append(cwd)

from function.f3 import fn_sum
import pytest

@pytest.mark.parametrize('v1,v2,res', [
    (1, 2,3),
    (2, 3,5),
    (3, 4,1),
    (4, 5,9)
])
def test_sum(v1,v2,res):
    assert fn_sum(v1,v2) == res
