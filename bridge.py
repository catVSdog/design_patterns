"""
桥接模式:
又名：柄体模式、 接口模式
使抽象部分与实现部分分离,使他们可以各自变化
但是根据UML类图看,感觉更像两个聚合关系类之间的结合
一个类作为另一个类实例的一个属性
"""


class Car:
    def __init__(self):
        self.color = None  # A类持有 B类 二者时聚合关系, color类是Car类的一个属性.
        # 当然也可以反过来,让car类作为color类的属性,但是颜色拥有汽车在尝试上讲不通啊.还是汽车拥有颜色比较合适

    def set_color(self, color):
        assert isinstance(color, Color)
        self.color = color

    def get_color(self):
        return self.color.name

    def __repr__(self):
        return f"{self.get_color()} {self.__class__.__name__}"


class Color:
    def __init__(self, name):
        self.name = name


class Red(Color):
    pass


class Blue(Color):
    pass


class BMW(Car):
    pass


class WW(Car):
    pass


if __name__ == '__main__':
    red = Red('浅红色')
    blue = Blue("星空蓝")
    car_1 = BMW()
    car_1.set_color(red)
    print(car_1)
    car_1.set_color(blue)
    print(car_1)

    car_2 = WW()
    car_2.set_color(blue)
    print(car_2)
    car_2.set_color(red)
    print(car_2)
