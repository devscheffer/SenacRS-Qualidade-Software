import os
import sys

cwd = os.getcwd()
sys.path.append(cwd)

from src.f5 import fn_error_code
import pytest

def test_code():
    with pytest.raises(ValueError, match=r".*Code\[1234\]:.*"):
        fn_error_code(-3)
