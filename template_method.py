"""
模板方法模式
定义一个算法的骨架,而将一些步骤延迟到子类中,模板方法使得子类不需要改变一个算法的结构,即可重新定义算法的某些特定步骤
"""
from abc import ABC, abstractmethod


class SelfIntroduce(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_age(self):
        pass

    def introduce(self):
        return f"my name is {self.get_name()},i am {self.get_age()} years old"


class LimingSelfIntroduce(SelfIntroduce):
    def get_name(self):
        return "LiMing"

    def get_age(self):
        return 20


class XiaohongSelfIntroduce(SelfIntroduce):
    def get_name(self):
        return 'XiaoHong'

    def get_age(self):
        return 18


if __name__ == '__main__':
    p_1 = LimingSelfIntroduce()
    assert p_1.introduce() == 'my name is LiMing,i am 20 years old'

    p_2 = XiaohongSelfIntroduce()
    assert p_2.introduce() == 'my name is XiaoHong,i am 18 years old'
