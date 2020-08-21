"""
单例模式

一般情况下，一个类每次实例化都会产生一个单独的对象。而单例模式的要求是：多次实例化，只产生一个对象。
这就要求对类的实例化过程进行干预，使其只有在第一次实例化时产生一个对象，以后的多次实例化，都是返回第一次创建的对象。
这就需要两个步骤：
1.是否已经有了实例了。
2.1 如果没有，那么创建实例，存储实例，将实例返回
2.2 如果已经有了，那么取出实例，将其返回

首先说，如何存储实例，一般利用具有唯一性的东西， 如 类变量

在说，如何干预实例化：
1.将类视作类，类实际通过 __new__ 方法，创建新对象，那么就重写 __new__方法。
2.有一个对象object, 当 object()时，其实调用的是 object的类的 __call__ 方法.python中一切皆对象，类也是其他类(又叫元类, 默认是type) 的对象。
因此可以重写类的元类的 __call__ 方法

> 以上两种都是从类创建对象的角度，进行干预， 还有一种方法是将类创建对象的过程，转换为一个函数调用的过程，在函数调用的过程中，创建/查找 返回类.
即:使用装饰器，将 cls() 操作转换为函数调用过程. 具体又分:
3.函数装饰器
4.类装饰器


还有一种是利用 python 包导入特性——每个包只导入一次，在一个模块中实例化一个类，然后在其他模块中直接导入该实例。
"""


### 第一种，重写 __new__

class Sun:
    __instance__ = None  # 使用类变量指代实例

    def __new__(cls, *args, **kwargs):
        if cls.__instance__ is None:
            cls.__instance__ = super().__new__(cls)
        return cls.__instance__


sun_1 = Sun()
sun_2 = Sun()
assert sun_1 == sun_2


class Changjiang:
    __instance__ = {}  # 使用类变量存储实例

    def __new__(cls, *args, **kwargs):
        if cls not in cls.__instance__:
            cls.__instance__[cls] = super().__new__(cls)
        return cls.__instance__[cls]


changjiang_1 = Changjiang()
changjiang_2 = Changjiang()
assert changjiang_1 == changjiang_2


# 第二种， 重写 __call__

class Person(type):
    __instance__ = None  # 使用类变量指代实例

    def __call__(self, *args, **kwargs):  # 这里的self 其实是 ChairMan 这个类
        if self.__instance__ is None:
            self.__instance__ = super().__call__(*args, **kwargs)
        return self.__instance__


class ChairMan(metaclass=Person):
    pass


chairman_1 = ChairMan()
chairman_2 = ChairMan()
assert chairman_1 == chairman_2


class River(type):  # 注意这里， 元类继承自 type
    __instance__ = {}  # 使用类变量存储实例

    def __call__(cls, *args, **kwargs):  # 为了更明显，我们将 self 改为了 cls.
        if cls not in cls.__instance__:
            cls.__instance__[cls] = super().__call__(*args, **kwargs)
        return cls.__instance__[cls]


class Huanghe(metaclass=River):  # 更改元类为 River
    pass


huanghe_1 = Huanghe()
huanghe_2 = Huanghe()
assert huanghe_1 == huanghe_2


# 第三种 函数装饰器

def singletone(cls):
    __instance__ = {}

    def wrapper(*args, **kwargs):
        if cls not in __instance__:
            __instance__[cls] = cls(*args, **kwargs)
        return __instance__[cls]

    return wrapper


@singletone
class Beijing:  # 经过装饰以后，通过访问 globals()，可以看到 Beijing 已经不是类了，而是一个函数
    pass


beijing_1 = Beijing()  # 其实是 wrapper()
beijing_2 = Beijing()

assert beijing_1 == beijing_2


# print(globals())  # {'Beijing': <function singletone.<locals>.wrapper at 0x7f5df7d88f70> }


# def singletone(cls):
#     __instance__ None
#
#     def wrapper(*args, **kwargs):
#         if __instance__ is None:  # 这么做是不行的，这涉及到作用域的嵌套与覆盖,以及变量的遮罩
#             __instance__ = cls(*args, **kwargs)
#         return __instance__[cls]
#     return wrapper


# 第四种 类装饰器. 被类装饰器装饰的东西(类/函数)，都会作为装饰器类的初始化参数，创建一个装饰器类的实例。通过重写装饰器类的__call__方法，
# 干预类实例化的过程

class Singletone1:
    __instance__ = None  # 使用类变量指向实例

    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        if self.__instance__ is None:
            self.__instance__ = self.cls(*args, **kwargs)
        return self.__instance__


@Singletone1
class Guangzhou:  # 这里的Guangzhou已经不是类了，而是Singletone1的一个对象  'Guangzhou': <__main__.Singletone1 object at 0x7fcc0cdfd430>
    pass


guangzhou_1 = Guangzhou()
guangzhou_2 = Guangzhou()
assert guangzhou_1 == guangzhou_2


class Singletone2:
    __instance__ = {}  # 使用类变量存储实例

    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        if self.cls not in self.__instance__:
            self.__instance__[self.cls] = self.cls(*args, **kwargs)
        return self.__instance__[self.cls]


@Singletone2
class Shanghai:  # 这里的 Shanghai 已经不是类了，而是 Singletone2的一个对象 'Shanghai': <__main__.Singletone2 object at 0x7fcc0cdfd520>
    pass


shanghai_1 = Shanghai()
shanghai_2 = Shanghai()
assert shanghai_1 == shanghai_2


class Singletone3:
    def __init__(self, cls):
        self.cls = cls
        self.__instance = None  # 使用实例变量指向实例

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = self.cls(*args, **kwargs)
        return self.__instance


@Singletone3
class Shenzhen:
    pass


shenzhen_1 = Shenzhen()
shenzhen_2 = Shenzhen()
assert shenzhen_1 == shenzhen_2


class Singletone4:
    def __init__(self, cls):
        self.cls = cls
        self.__instance = {}  # 使用实例变量存储实例

    def __call__(self, *args, **kwargs):
        if self.cls not in self.__instance:
            self.__instance[self.cls] = self.cls(*args, **kwargs)
        return self.__instance[self.cls]


@Singletone4
class Hangzhou:
    pass


hangzhou_1 = Hangzhou()
hangzhou_2 = Hangzhou()
assert hangzhou_1 == hangzhou_2


# 第五种

# a.py

class A:
    pass


aa = A()

# b.py
# from a import aa
# aa.xxxx
