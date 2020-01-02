"""
观察者模式

定义的是一对多的关系,主要有两个角色——被观察者(又名主题,发布者等等)和观察者(又名订阅者等等)

它和 发布-订阅模式还是 有区别的
观察者模式两个角色耦合性比较高,两个角色互相知道对方.
发布-订阅模式两个角色耦合性比较低, 因为两个角色之间增加了一个新的角色--中转站,发布者发消息到中转站,由中转站通知订阅者.两个角色不用互相知道.
"""

from abc import ABC, abstractmethod


class BaseSubject(ABC):
    """抽象主题"""

    @abstractmethod
    def add_obsever(self, observer):  # 每一位观察者都要注册到主题
        """增加观察者"""
        pass

    @abstractmethod
    def remove_observer(self, observer):
        """删除观察者"""
        pass

    @abstractmethod
    def notify(self, msg):
        """通知观察者"""
        pass


class BaseObserver(ABC):
    """抽象观察者"""

    def update(self, msg):
        """接收消息"""
        pass


class FootballMatchSubject(BaseSubject):
    """足球比赛主题"""

    def __init__(self):
        self.observers = []

    def add_obsever(self, observer):
        assert isinstance(observer, BaseObserver)  # 确保都实现了update方法
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify(self, msg):
        for observer in self.observers:
            observer.update(msg)


class BreakNewsSubject(BaseSubject):
    """突发新闻主题"""

    def __init__(self):
        self.observers = []

    def add_obsever(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify(self, msg):
        for observer in self.observers:
            observer.update(msg)


class FootBallLover(BaseObserver):
    """足球比赛爱好者"""

    def __init__(self, name):
        self.name = name

    def update(self, msg):
        print("啦啦啦啦...")
        print(f"{self.name}, 你收到一条新消息:{msg} ")


class NewsLover(BaseObserver):
    """新闻爱好者"""

    def __init__(self, name):
        self.name = name

    def update(self, msg):
        print("专心学习中...")
        print(f"滴滴滴滴~~ {self.name}, 你收到一条新消息:{msg} ")


if __name__ == '__main__':
    sub_football = FootballMatchSubject()
    xiaogang = FootBallLover('小刚')
    xiaoming = FootBallLover('小明')
    sub_football.add_obsever(xiaogang)
    sub_football.add_obsever(xiaoming)

    sub_news = BreakNewsSubject()
    xiaohong = NewsLover('小红')
    sub_news.add_obsever((xiaohong))

    print("++++ 国足丢了一球 +++")
    sub_football.notify("国足丢了一球")

    print("++++ 国足又丢了一球 +++")
    sub_football.notify("国足又丢了一球")

    print("+++ 小刚气死了 +++")
    sub_football.remove_observer(xiaogang)
    sub_football.notify("对不起,我们的一位球迷不幸逝世")

    print("+++ 球迷被气死,成了突发新闻 +++")
    sub_news.notify("有一位球迷被气死了...")
