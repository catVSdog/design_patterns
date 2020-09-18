"""
抽象工厂模式:
工厂方法模式升级版: 工厂方法模式只是针对某一种产品(例如：生产电冰箱),每个具体工厂生产的是某个具体的种类.(例如：海尔工厂生产海尔电视,海信工厂生产海信电视)
抽象工厂模式针对是多个产品种类(如：电冰箱,电视机,豆浆机),每个具体的工厂会生产同一个产品族下不同的产品种类。

产品等级结构 ：产品等级结构即产品的继承结构，如一个抽象类是电视机，其子类有海尔电视机、海信电视机、TCL电视机，
    则抽象电视机与具体品牌的电视机之间构成了一个产品等级结构，抽象电视机是父类，而具体品牌的电视机是其子类。
产品族 ：在抽象工厂模式中，产品族是指由同一个工厂生产的，位于不同产品等级结构中的一组产品，
    如海尔电器工厂生产的海尔电视机、海尔电冰箱，海尔电视机位于电视机产品等级结构中，海尔电冰箱位于电冰箱产品等级结构中。
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


# 以下为工厂类
class SuperFactory(ABC):  # ~~ 多个类对应一个工厂类 ~~
    @abstractmethod
    def get_tv_flow(self):  # 一般来说,工厂方法只会有这一个方法
        pass

    @abstractmethod
    def get_refrigerator_flow(self):  # 抽象工厂方法会有多个
        pass


class HaierSuperFactory(SuperFactory):
    def get_tv_flow(self):
        return HaierTVFlow()

    def get_refrigerator_flow(self):
        return HaierRefrigeratorFlow()


class HisenseSuperFactory(SuperFactory):
    def get_tv_flow(self):
        return HisenseTVFlow()

    def get_refrigerator_flow(self):
        return HisenseRefrigeratorFlow()


if __name__ == '__main__':
    print("++ 访问海尔超级工厂,参观他们的流水线 ++")
    haier_factor = HaierSuperFactory()
    haier_tv_flow = haier_factor.get_tv_flow()
    haier_tv_flow.produce_tv()
    haier_refrigerator_flow = haier_factor.get_refrigerator_flow()
    haier_refrigerator_flow.produce_refrigerator()

    print("++ 访问海信超级工厂,参观他们的流水线 ++")
    hisense_factor = HisenseSuperFactory()
    hisense_tv_flow = hisense_factor.get_tv_flow()
    hisense_tv_flow.produce_tv()
    hisense_refrigerator_flow = hisense_factor.get_refrigerator_flow()
    hisense_refrigerator_flow.produce_refrigerator()
