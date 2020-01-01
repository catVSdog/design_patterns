"""
代理模式

代理模式和装饰器模式颇像,都是对类方法进行扩展,但二者不同在于：
装饰器时增强自身, 代理模式是让代理去做一些与自己业务无关的工作.
又或者不能直接访问类时,通过代理来访问
"""
from abc import ABC, abstractmethod


class GiveGift(ABC):
    @abstractmethod
    def give(self):
        pass


class Pursuit(GiveGift):
    def give(self):
        print("give you a gift")


class Proxy(GiveGift):
    def __init__(self):
        self.rc = Pursuit()  # 代理需要持有对被代理的引用

    def give(self):  # 二者要实现同样的接口
        self.before()
        self.rc.give()
        self.after()

    def before(self):
        print("包装一下礼物")

    def after(self):
        print("成功送达")


if __name__ == '__main__':
    pr = Proxy()
    pr.give()
