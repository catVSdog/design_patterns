"""
简单工厂模式
"""
from abc import ABC, abstractmethod


class BaseOperator(ABC):
    @classmethod
    @abstractmethod
    def get_result(cls, x, y):
        pass


class ADD(BaseOperator):
    @classmethod
    def get_result(cls, x, y):
        return x + y


class SUB(BaseOperator):
    @classmethod
    def get_result(cls, x, y):
        return x - y


class MUL(BaseOperator):
    @classmethod
    def get_result(cls, x, y):
        return x * y


class DIV(BaseOperator):
    @classmethod
    def get_result(cls, x, y):
        if y == 0:
            raise ZeroDivisionError
        return x / y


class OperatorFactor:
    @classmethod
    def create_operator(cls, operator_name):
        if operator_name == '+':
            return ADD
        if operator_name == '-':
            return SUB
        if operator_name == '/':
            return DIV
        if operator_name == '*':
            return MUL


if __name__ == '__main__':
    op = OperatorFactor.create_operator('+')
    print(op.get_result(1, 2))

    op = OperatorFactor.create_operator('-')
    print(op.get_result(1, 2))

    op = OperatorFactor.create_operator('*')
    print(op.get_result(1, 2))

    op = OperatorFactor.create_operator('/')
    print(op.get_result(1, 2))
