import os
import sys

cwd = os.getcwd()
sys.path.append(cwd)
from function.f2 import fn_div

import pytest
def test_answer():
    with pytest.raises(ZeroDivisionError):
        fn_div(1, 0)

