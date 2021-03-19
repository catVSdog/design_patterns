"""
备忘录模式
在不破坏封装的前提下,捕获对象的状态,并在对象外保存状态,就可以在需要时恢复对象原有的状态
"""


class Memento:
    def __init__(self, blood, angry, magic):
        self.blood = blood
        self.angry = angry
        self.magic = magic


class Game:
    def __init__(self, blood, angry, magic):
        self.blood = blood
        self.angry = angry
        self.magic = magic

    def fight(self):
        self.blood = self.blood / 2
        self.angry = self.angry / 2
        self.magic = self.magic / 2

    def save_point(self):
        return Memento(self.blood, self.angry, self.magic)

    def recover(self, memento):
        self.blood = memento.blood
        self.angry = memento.angry
        self.magic = memento.magic


class Manager:
    """管理备忘录的银.."""

    def __init__(self):
        self.mem = None

    def set_men(self, mem):
        self.mem = mem

    def get_mem(self):
        return self.mem


if __name__ == '__main__':
    print("++ 开始一个新的游戏.... ++")
    game = Game(100, 0, 100)
    print("++ 一路无损闯关,终于到关底了 ++ ")
    print("++ 怂一波,保存一下状态 ++")
    print(f"当前血量：{game.blood}, 怒气值：{game.angry}, 魔法值：{game.magic}")
    mem = game.save_point()
    manger = Manager()
    manger.set_men(mem)
    print("++  开搞大boss ++")
    game.blood = 10
    game.angry = 100
    game.magic = 0
    print(f"当前血量：{game.blood}, 怒气值：{game.angry}, 魔法值：{game.magic}")
    print("++ 扛不住了...回退吧... ++")
    recove_meme = manger.get_mem()
    game.recover(recove_meme)
    print(f"当前血量：{game.blood}, 怒气值：{game.angry}, 魔法值：{game.magic}")
