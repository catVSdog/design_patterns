"""
享元模式
采用一个共享对象来避免大量拥有相同内容对象的开销,将不同的地方,放于外部
"""

from abc import ABC, abstractmethod


class BaseQizi(ABC):
    @abstractmethod
    def down(self, msg):
        pass


class Qizi(BaseQizi):
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def down(self, msg):
        print(msg)


class QiziFactor:
    def __init__(self):
        self.qizi_map = {}

    def get_qize(self, color):
        if color not in self.qizi_map:
            self.qizi_map[color] = Qizi(color)
        return self.qizi_map[color]


if __name__ == '__main__':
    factor = QiziFactor()
    white_qizi_1 = factor.get_qize('white')
    black_qizi_1 = factor.get_qize('black')

    white_qizi_2 = factor.get_qize('white')
    black_qizi_2 = factor.get_qize('black')

    white_qizi_3 = factor.get_qize('white')
    black_qizi_3 = factor.get_qize('black')

    white_qizi_1.down("白1子 置于 1,1")
    white_qizi_2.down("白2子 置于 2,2")
    white_qizi_3.down("白3子 置于 3,3")

    black_qizi_1.down("黑1子 置于 11,11")
    black_qizi_2.down("黑2子 置于 22,22")
    black_qizi_3.down("黑3子 置于 33,33")

    assert len(list(factor.qizi_map)) == 2
