"""
装饰模式
参考python装饰器, 在执行前后添加一些别的操作
多个装饰器
"""
from abc import ABC, abstractmethod


class BaseComponent(ABC):
    @abstractmethod
    def operator(self):
        pass


class PrintComponent(BaseComponent):
    def operator(self):
        print("啦～啦啦啦～, 追不上我吧～")


class Decorator(BaseComponent):  # 也可以不需要BaseComponent, Decorator直接继承PrintComponent
    def __init__(self, cc):
        assert isinstance(cc,
                          BaseComponent)  # 要求必须 cc 必须是 BaseComponent/PrintComponent 的子类,只有这样才能重写operator方法,实际调用cc的operator
        self.cc = cc

    def operator(self):  # 要求方法名必须也是operator,这样多个装饰器嵌套的的时候,就可以不需要关注其他装饰器的方法名,降低耦合,可以随意组织装饰器的顺序
        raise NotImplemented


class DecoratorA(Decorator):
    def do_before(self):
        print("In Decorator A, befor operator...")

    def operator(self):
        self.do_before()
        self.cc.operator()


class DecoratorB(Decorator):
    def do_after(self):
        print("In Decorator B, after operator...")

    def operator(self):  # 假设decoratorA的方法不叫operator,而是叫别的,那么decoratorB只有在被decoratorA之前调用才能这么写,
        self.cc.operator()  # 否则,这里就不能调用self.cc.operator,而是去调用decoratorA中相应的方法名self.cc.xxx,那么这两个装饰器就有了调用顺序,耦合太深了,
        self.do_after()  # 也就没有必要分开写了


if __name__ == '__main__':
    pc = PrintComponent()
    da = DecoratorA(pc)  # da.cc == pc
    db = DecoratorB(da)  # db.cc == da(pc)
    db.operator()
