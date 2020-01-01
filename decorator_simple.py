"""
装饰模式
参考python装饰器, 在执行前后添加一些别的操作
单个装饰器
"""

class PrintComponent:
    def operator(self):
        print("啦～啦啦啦～, 追不上我吧～")


class Decorator:
    def __init__(self, cc):
        self.cc = cc

    def operator(self):
        self.before()
        self.cc.operator()
        self.after()

    def before(self):
        print("before...")

    def after(self):
        print("after...")


if __name__ == '__main__':
    cc = PrintComponent()
    de = Decorator(cc)
    de.operator()