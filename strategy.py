"""
策略模式
定义一组算法，将每个算法都封装起来，并且使他们之间可以互换
"""

# 以下以商场收费算法为例子(分为正常收费,5折,满300减100)
from abc import ABC, abstractmethod


class BaseCash(ABC):
    @abstractmethod
    def accept_cash(self, value):
        pass


class NormalCash(BaseCash):
    def accept_cash(self, value):
        return value


class HalfOffCash(BaseCash):
    def accept_cash(self, value):
        return value * 0.5


class ThreeOneCash(BaseCash):
    def accept_cash(self, value):
        if value > 300:
            return value - 100
        return value


class ContextA:
    def __init__(self, cash):
        assert isinstance(cash, BaseCash)
        self.cash = cash

    def get_money(self, money):
        return self.cash.accept_cash(money)


# 策略模式 + 简单工厂模式
class ContextB:
    def __init__(self, cash_doc):
        if cash_doc == "正常收费":
            self.cash = NormalCash()
        if cash_doc == '半价':
            self.cash = HalfOffCash()
        if cash_doc == '满300减100':
            self.cash = ThreeOneCash()

    def get_money(self, money):
        return self.cash.accept_cash(money)


if __name__ == '__main__':
    # 正常收费
    cc = ContextA(NormalCash())
    assert cc.get_money(100) == 100

    # 5折
    cc = ContextA(HalfOffCash())
    assert cc.get_money(100) == 50

    # 满300减100
    cc = ContextA(ThreeOneCash())
    assert cc.get_money(500) == 400

    cc = ContextA(ThreeOneCash())
    assert cc.get_money(100) == 100

    # 正常收费
    cc = ContextB("正常收费")
    assert cc.get_money(100) == 100

    # 5折
    cc = ContextB('半价')
    assert cc.get_money(100) == 50

    # 满300减100
    cc = ContextB('满300减100')
    assert cc.get_money(500) == 400

    cc = ContextB('满300减100')
    assert cc.get_money(100) == 100
