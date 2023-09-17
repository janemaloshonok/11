import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self,12,4) == 16

    def test_subtraction_success(self):
        assert self.calc.subtraction(self,12,4) == 8

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self,1,0)

    def teardown(self):
        print('Выполнение метода Teardown')

