"""
单例模式
每个类只实例化一次
"""


# use __new__
class Sun:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


# use method decorator
def singletone(cls):
    _instance = {}

    def inner(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
            # print(__instance)
        return _instance[cls]

    return inner


@singletone
class ChairMan:
    def __init__(self, name):
        self.name = name


# use class decorator
class Singleton:
    def __init__(self, cls):
        self.cls = cls
        self._instance = {}

    def __call__(self, *args, **kwargs):
        if self.cls not in self._instance:
            self._instance[self.cls] = self.cls(*args, **kwargs)
        return self._instance[self.cls]


@Singleton
class Emperor:
    def __init__(self, name):
        self.name = name


# use metaclass
class SingletonFirst(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonFirst, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Queen(metaclass=SingletonFirst):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    sun_a = Sun()
    sun_b = Sun()
    assert id(sun_a) == id(sun_b)

    mao_1 = ChairMan('毛泽东')
    mao_2 = ChairMan('毛泽东')
    assert id(mao_1) == id(mao_2)
    print(mao_1.name)

    emp_1 = Emperor('秦始皇')
    emp_2 = Emperor('秦始皇')
    assert id(emp_1) == id(emp_2)
    print(emp_1.name)

    qyeen_1 = Queen("武则天")
    qyeen_2 = Queen("武则天")
    assert id(qyeen_1) == id(qyeen_2)
    print(qyeen_1.name)


    # 类装饰类似于如下
    class Cls():
        pass


    singletone_obj = Singleton(Cls)  # 一般为了方便使用,singleton_obj 还是会被命名为 Cls,但二者其实是不同的,一个是singleton的实例,一个是类
    cls1 = singletone_obj()  # 调用singleton_obj 的 __call__ 方法
    cls2 = singletone_obj()
    assert id(cls1) == id(cls2)
