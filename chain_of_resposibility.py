"""
职责链模式:
链条上的每个环节有自己的职责范围,在自己的职责范围内就立即处理,入股超过自己的职业,那么就传给链条的一下环节
"""
from abc import ABC, abstractmethod


class BaseHandler(ABC):
    @abstractmethod
    def hande(self, money):
        pass


class Kuaiji(BaseHandler):
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, next_handler):
        assert isinstance(next_handler, BaseHandler)
        self.next_handler = next_handler

    def hande(self, money):
        if 0 < money <= 100:
            print(f"区区{money}块,我这个会计批了")
        else:
            print("超过100了,这个我没有权限,等等,我问问上级...")
            self.next_handler.hande(money)


class CuWuJingLi(BaseHandler):
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, next_handler):
        assert isinstance(next_handler, BaseHandler)
        self.next_handler = next_handler

    def hande(self, money):
        if 100 < money <= 1000:
            print(f"哦,{money}块呀,行吧,我这个财务经理准了")
        else:
            print("超过1000了,这个我没有权限,等等,我问问上级...")
            self.next_handler.hande(money)


class Dongshizhang(BaseHandler):
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, next_handler):
        assert isinstance(next_handler, BaseHandler)
        self.next_handler = next_handler

    def hande(self, money):
        if 1000 < money <= 10000:
            print(f"额,{money}块呀,花都花了,我这个董事长也没办法啊,准了")
        else:
            print(f"都超过10000了,我这个董事长也花不了这么多啊,不准！")  # 链条要有一个终点,不能无休止的传递下去.


if __name__ == '__main__':
    kuaiji_1 = Kuaiji()
    jingli_1 = CuWuJingLi()
    dongshizhag_1 = Dongshizhang()

    kuaiji_1.set_next_handler(jingli_1)
    jingli_1.set_next_handler(dongshizhag_1)


    print("++ 申请报销50 ++")
    money = 50
    kuaiji_1.hande(money)

    print("++ 申请报销500 ++")
    money = 500
    kuaiji_1.hande(money)

    print("++ 申请报销5000000 ++")
    money = 5000000
    kuaiji_1.hande(money)