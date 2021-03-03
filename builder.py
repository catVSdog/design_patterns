"""
建造者模式:
分离建造代码和表示代码,用于创建复杂对象,这些对象的创造步骤比较固定,但是每个具体环节的创建又比较复杂
"""
from abc import ABC, abstractmethod


class BuildStructure(ABC):
    @abstractmethod
    def choice_area(self):
        pass

    @abstractmethod
    def choice_color(self):
        pass

    @abstractmethod
    def choice_style(self):
        pass

    @abstractmethod
    def choice_material(self):
        pass

    def building(self):
        print("建造中...")
        print("盖好了...")


class BuildSupermarket(BuildStructure):
    def choice_area(self):
        print("地界： 市中心")

    def choice_color(self):
        print("颜色： 红屋顶黄墙")

    def choice_style(self):
        print("类型: 三层大楼")

    def choice_material(self):
        print("材质：钢铁")


class BuildHouse(BuildStructure):
    def choice_area(self):
        print("地界： 市郊")

    def choice_color(self):
        print("颜色： 灰色")

    def choice_style(self):
        print("类型: 一层平房,带个小院")

    def choice_material(self):
        print("材质：钢筋水泥")


class BuilderWroker:
    def __init__(self, shema):
        assert isinstance(shema, BuildStructure)
        self.shema = shema

    def work_gogogo(self):  # 严格按照步骤来建造,具体的的部件构建过程由不同的方案决定
        self.shema.choice_area()
        self.shema.choice_color()
        self.shema.choice_style()
        self.shema.choice_material()
        self.shema.building()


if __name__ == '__main__':
    print("建造一个小房子。。。")
    house_shema = BuildHouse()
    worker = BuilderWroker(house_shema)  # 客户端只需要提出想法即可,工人会去自行建造
    worker.work_gogogo()

    print("建造一个超市。。。。")
    market_shema = BuildSupermarket()
    worker = BuilderWroker(market_shema)
    worker.work_gogogo()
