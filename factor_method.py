"""
工厂方法模式

简单工厂方法耦合性更高,如果新增加一个操作,除了增加操作的类,还要不得不修改生产操作的if语句,需要修改旧代码
简单工厂方法来说,只要增加一个操作类,及其工厂类就可以了，对旧代码不需要做修改.
"""
from abc import ABC, abstractmethod


class BaseOperator(ABC):
    @abstractmethod
    def get_result(self, x, y):
        pass


class ADD(BaseOperator):
    def get_result(self, x, y):
        return x + y


class SUB(BaseOperator):
    def get_result(self, x, y):
        return x - y


class MUL(BaseOperator):
    def get_result(self, x, y):
        return x * y


class DIV(BaseOperator):
    def get_result(cls, x, y):
        if y == 0:
            raise ZeroDivisionError
        return x / y


class Factor(ABC):
    @abstractmethod
    def get_operation(self):
        pass


class AddFactor(Factor):  # ~~ 一个类,对应一个工厂类 ~~
    def get_operation(self):
        return ADD()


class SubFactor(Factor):
    def get_operation(self):
        return SUB()


class MulFactor(Factor):
    def get_operation(self):
        return MUL()


class DivFactor(Factor):
    def get_operation(self):
        return DIV()


if __name__ == '__main__':
    add_factor = AddFactor()
    add_operator = add_factor.get_operation()
    assert add_operator.get_result(1, 2) == 3

    sub_factor = SubFactor()
    sub_operator = sub_factor.get_operation()
    assert sub_operator.get_result(1, 2) == -1

    mul_factor = MulFactor()
    mul_operator = mul_factor.get_operation()
    assert mul_operator.get_result(1, 2) == 2

    div_factor = DivFactor()
    div_operator = div_factor.get_operation()
    assert div_operator.get_result(1, 2) == 0.5
