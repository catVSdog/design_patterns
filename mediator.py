"""
中介模式/代理人模式

一个中介对象封装一系列对象交互, 有点类似于发布-订阅模式
"""


class Sender:
    def __init__(self, name):
        self.name = name
        self.mediator = None

    def set_mediator(self, mediator):
        self.mediator = mediator

    def nodified(self, msg):
        print(f"{self.name} get msg: {msg}")

    def tell(self, msg):
        self.mediator.send_msg(msg, self)


class Mediator:
    def __init__(self):
        self.teacher = None  # 知道每一个sender
        self.student = None

    def set_teacher_sender(self, sender):
        self.teacher = sender

    def set_student_sender(self, sender):
        self.student = sender

    def send_msg(self, msg, sender):
        if sender == self.teacher:  # 根据sender做出相应的操作
            self.student.nodified(msg)
        elif sender == self.student:
            self.teacher.nodified(msg)
        else:
            print("没有找到影响的处理方式")


if __name__ == '__main__':
    mem = Mediator()

    t = Sender('李老师')
    t.mediator = mem

    s = Sender('刘同学')
    s.mediator = mem

    mem.set_teacher_sender(t)
    mem.set_student_sender(s)

    t.tell("留作业啦.留作业啦...")
    s.tell("不听不听, 老和尚念经..")
