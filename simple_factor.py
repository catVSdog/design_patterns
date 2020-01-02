"""
简单工厂模式
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


class OperatorFactor:
    @classmethod
    def create_operator(cls, operator_name):  # 此处耦合性较高,每增加一个操作类,就要修改这里.改进版：工厂方法模式
        if operator_name == '+':  # ~~ 一个类,对应一个工厂case语句 ~~
            return ADD()
        if operator_name == '-':
            return SUB()
        if operator_name == '/':
            return DIV()
        if operator_name == '*':
            return MUL()


if __name__ == '__main__':
    op = OperatorFactor.create_operator('+')
    assert op.get_result(1, 2) == 3

    op = OperatorFactor.create_operator('-')
    assert op.get_result(1, 2) == -1

    op = OperatorFactor.create_operator('*')
    assert op.get_result(1, 2) == 2

    op = OperatorFactor.create_operator('/')
    assert op.get_result(1, 2) == 0.5
