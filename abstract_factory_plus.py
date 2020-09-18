"""
简单工厂 + 抽象工厂:

抽象工厂虽然可以一次性实例化多个类,但是每增加一个类,就要创建相应的工厂类,修改抽象工厂类,很麻烦.
使用简单工厂方法,自动生成相应的类
"""

from abc import ABC, abstractmethod


class TVFlow(ABC):
    @abstractmethod
    def produce_tv(self):
        pass


class HaierTVFlow(TVFlow):
    def produce_tv(self):
        print("海尔电视生产线: 生产一台海尔电视...")


class HisenseTVFlow(TVFlow):
    def produce_tv(self):
        print("海信电视生产线: 生产一台海信电视...")


class RefrigeratorFlow(ABC):
    @abstractmethod
    def produce_refrigerator(self):
        pass


class HaierRefrigeratorFlow(RefrigeratorFlow):
    def produce_refrigerator(self):
        print("海尔冰箱生产线: 买一台海尔冰箱...")


class HisenseRefrigeratorFlow(RefrigeratorFlow):
    def produce_refrigerator(self):
        print("海信冰箱生产线: 生产一台海信冰箱...")


class SimpleFactor:
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    def get_tv_flow(self):
        if self.manufacturer == 'haier':
            return HaierTVFlow()
        elif self.manufacturer == 'hisense':
            return HisenseTVFlow()

    def get_refrigerator_flow(self):
        if self.manufacturer == 'haier':
            return HaierRefrigeratorFlow()
        elif self.manufacturer == 'hisense':
            return HisenseRefrigeratorFlow()


if __name__ == '__main__':
    print("++ 访问海尔超级工厂,参观他们的流水线 ++")
    factor = SimpleFactor('haier')
    tv_flow = factor.get_tv_flow()
    tv_flow.produce_tv()
    re_flow = factor.get_refrigerator_flow()
    re_flow.produce_refrigerator()

    print("++ 访问海信超级工厂,参观他们的流水线 ++")
    factor = SimpleFactor('haier')
    tv_flow = factor.get_tv_flow()
    tv_flow.produce_tv()
    re_flow = factor.get_refrigerator_flow()
    re_flow.produce_refrigerator()
