"""
状态模式
状态模式允许一个对象在其内部状态改变的时候改变其行为。这个对象看上去就像是改变了它的类一样。
状态模式主要解决的是: 当控制一个对象状态转换的条件表达式过于复杂时,把状态的判断逻辑转移到表示不同状态的一系列类中,从而使逻辑简化
"""
from abc import ABC, abstractmethod


class Context:
    def __init__(self):
        self.status = None

    def set_status(self, status):
        self.status = status

    def check(self):
        self.status.handle(self)   # 传入自身,以被状态类持有


class BaseApprovalStatus(ABC):
    """报销审批基类"""

    @abstractmethod
    def handle(self, status):
        pass


class LeaderApprovalStatus(BaseApprovalStatus):
    def handle(self, context):
        print("直属领导审批意见: 同意")
        context.set_status(DivisionManagerApprovalStatus())


class DivisionManagerApprovalStatus(BaseApprovalStatus):
    def handle(self, context):
        print("部门领导审批意见: 同意")
        context.set_status(FinancialApprovalStatus())


class FinancialApprovalStatus(BaseApprovalStatus):
    def handle(self, context):
        print("财务部门审批意见: 同意")
        print("放款...")
        context.set_status(CloseApprovalStatus())


class CloseApprovalStatus(BaseApprovalStatus):
    def handle(self, context):
        print("关闭报销流程")
        context.status = None


if __name__ == '__main__':
    print("+++ 开始一段报销流程 ++")
    leader_approval = LeaderApprovalStatus()
    context = Context()
    context.set_status(leader_approval)
    context.check()
    context.check()
    context.check()
    context.check()
