"""
门面模式
"""


class Tv:
    def open_color(self):
        print("打开液晶电视")

    def open_pure(self):
        print("打开黑白电视")


class Lamp:
    def roof(self):
        print("打开吊灯")

    def bed(self):
        print("打开床头灯")


class Drinks:
    def water(self):
        print("倒一杯白开水")

    def coffee(self):
        print("冲一杯咖啡")


class Facade:
    def __init__(self):  # 知道所有子系统
        self.tv = Tv()
        self.lamp = Lamp()
        self.drinks = Drinks()

    def watch_football(self):  # 组合出各种方法,以备调用
        self.tv.open_color()
        self.lamp.roof()
        self.drinks.coffee()

    def sleep(self):
        self.lamp.bed()

    def feel_bad(self):
        self.tv.open_pure()
        self.lamp.bed()
        self.drinks.water()


if __name__ == '__main__':
    print("xiaoming watch football")
    xiaoming = Facade()
    xiaoming.watch_football()  # 调用者不知道具体的子系统

    print("xiaohong want cry")
    xiaohong = Facade()
    xiaohong.feel_bad()

    print("xiaogang work 996")
    xiaogang = Facade()
    xiaogang.sleep()
