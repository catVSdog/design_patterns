"""
命令模式
将一个请求封装成一个对象，从而让你使用不同的请求把客户端参数化，对请求排队或者记录日志，可以提供命令的撤销和恢复功能。
"""
from abc import ABC, abstractmethod


class BaseCommand(ABC):
    """抽象命令"""

    @abstractmethod
    def exec(self):
        pass


class FixCarWorker:
    def fix(self):
        print("修车中...")


class CleanCarWorker:
    def clean(self):
        print("洗车中...")


class FixCarCommand(BaseCommand):
    def __init__(self, worker):
        assert isinstance(worker, FixCarWorker)
        self.worker = worker  # 命令对象持有相应的命令执行者...

    def exec(self):
        self.worker.fix()


class CleanCarCommand(BaseCommand):
    def __init__(self, worker):
        assert isinstance(worker, CleanCarWorker)
        self.worker = worker

    def exec(self):
        self.worker.clean()


class Waiter:
    def __init__(self):
        self.commands = []  # 接受/删除命令

    def add_command(self, comm):
        assert isinstance(comm, BaseCommand)
        self.commands.append(comm)

    def remove_command(self, comm):
        self.commands.remove(comm)

    def nofify(self):
        for com in self.commands:
            com.exec()


if __name__ == '__main__':
    fix_worker = FixCarWorker()
    clean_worker = CleanCarWorker()

    fix_command = FixCarCommand(fix_worker)  # 把命令封装为一个对象,每个命令持有相应的执行者
    clean_comman = CleanCarCommand(clean_worker)

    waiter = Waiter()
    waiter.add_command(fix_command)
    waiter.add_command(clean_comman)

    waiter.nofify()
