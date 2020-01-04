"""
访问者模式
如果系统的数据结构是比较稳定的(且比较少)，但其操作（算法）是易于变化的，那么使用访问者模式是个不错的选择
例如 男，女在不同情绪下的表现: 数据结构比较稳定,只有男女, 但是情绪是比较多种多样的
将各种情绪定义为类,再其内部实现不同性别的表现,然后由不同性别调用.这样去掉了大量if..else..语句
"""

from abc import ABC, abstractmethod


class BaseStatus(ABC):
    @abstractmethod
    def get_man_status(self):
        pass

    @abstractmethod
    def get_woman_status(self):
        pass


class Persion(ABC):
    @abstractmethod
    def set_status(self, status):
        pass


class Man(Persion):
    def set_status(self, status):
        status.get_man_status()  # 调用某个状态类的属于男性的方法


class Woman(Persion):
    def set_status(self, status):
        status.get_woman_status()  # 调用某个状态类的属于女性的方法


class Happy(BaseStatus):  # 不同的状态类, 对男女两性分别定义不同的方法.这就要求数据结构种类不能太多且稳定,不然数据结构相对应的方法不好写
    def get_man_status(self):
        print("男人高兴时,跳起来啊..")

    def get_woman_status(self):
        print("女人高兴时,捂嘴呵呵笑..")


class Sad(BaseStatus):
    def get_woman_status(self):
        print("女人悲伤时,哭泣..")

    def get_man_status(self):
        print("男人悲伤时,沉默不语..")


class Angry(BaseStatus):
    def get_man_status(self):
        print("男人生气时,暴跳如雷...")

    def get_woman_status(self):
        print("女人生气时,横眉冷对..")


class Store:
    def __init__(self):
        self.objs = []

    def add_obj(self, obj):
        self.objs.append(obj)

    def remove_obj(self, obj):
        self.objs.remove(obj)

    def display(self, status):
        for obj in self.objs:
            obj.set_status(status)


if __name__ == '__main__':
    h = Happy()
    s = Sad()
    a = Angry()

    m = Man()
    w = Woman()

    store = Store()
    store.add_obj(m)
    store.add_obj(w)

    store.display(h)
    store.display(s)
    store.display(a)
