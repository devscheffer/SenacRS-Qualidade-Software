import os
import sys

cwd = os.getcwd()
sys.path.append(cwd)

from src.f1 import fn_sum

def test_answer():
    assert fn_sum(1,3) == 4, "Descricao opcional"

