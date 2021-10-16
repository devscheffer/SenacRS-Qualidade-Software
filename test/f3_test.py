import os
import sys

cwd = os.getcwd()
sys.path.append(cwd)

from function.f3 import fn_sum, fn_mul, fn_div, fn_sub

class Test_F3_1:
    def test_answer1(self):
        assert fn_sum(1,3) == 4

    def test_answer2(self):
        assert fn_sub(1,3) == -2

class Test_F3_2:
    def test_answer3(self):
        assert fn_mul(1,3) == 3

    def test_answer4(self):
        assert fn_div(15,3) == 5
