"""
组合模式
使对象组成树形结构以表示‘部分-整体’的层次关系,组合模式使用户对单独对象和组合对象的使用具有一致性.
"""

from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def add(self, component):
        pass

    @abstractmethod
    def remove(self, component):
        pass

    @abstractmethod
    def display_organization(self, depth):
        pass

    @abstractmethod
    def show_duty(self):
        pass


class Company(Component):
    """公司"""

    def __init__(self, name, duty):
        self.name = name
        self.duty = duty
        self.son_parts = []

    def add(self, componeny):
        self.son_parts.append(componeny)

    def remove(self, componeny):
        self.son_parts.remove(componeny)

    def display_organization(self, depth=1):
        print(f"{'-' * depth}{self.name}")
        for com in self.son_parts:
            com.display_organization(depth + 2)  # 递归调用子节点

    def show_duty(self):
        print(self.duty)
        for dep in self.son_parts:
            dep.show_duty()  # 递归调用子节点


class Department(Component):
    """部门"""

    def __init__(self, name, duty):
        self.name = name
        self.duty = duty

    def add(self, componeny):
        raise Exception("部门不应该有下属部门或者下属公司")

    def remove(self, componeney):
        raise Exception("部门不应该有下属部门或者下属公司")

    def display_organization(self, depth=1):
        print(f"{'-' * depth}{self.name}")

    def show_duty(self):
        print(self.duty)


if __name__ == '__main__':
    zonggongsi = Company("北京总公司", "管理总部事务")

    zonggongsi_renli = Department("人力资源总部", "管理总部人事")
    zonggongsi_caiwu = Department("财务资源总部", "管理总部财务")
    zonggongsi.add(zonggongsi_renli)
    zonggongsi.add(zonggongsi_caiwu)

    fengongsi_1 = Company("上海分公司", "管理上海分公司事务")
    fengongsi_1_renli = Department("上海人力资源部", "管理上海分公司人事")
    fengongsi_1_caiwu = Department("上海财务部", "管理上海分公司财务")
    fengongsi_1.add(fengongsi_1_renli)
    fengongsi_1.add(fengongsi_1_caiwu)

    fengongsi_2 = Company("成都分公司", "管理成都分公司事务")
    fengongsi_2_renli = Department("成都人力资源部", "管理成都分公司人事")
    fengongsi_2_caiwu = Department("成都财务部", "管理成都分公司财务")
    fengongsi_2.add(fengongsi_2_renli)
    fengongsi_2.add(fengongsi_2_caiwu)

    zonggongsi.add(fengongsi_1)  # 将分公司加入总公司管理
    zonggongsi.add(fengongsi_2)

    fengongsi_1_1 = Company("上海分公司宁波办事处", "管理上海分公司宁波办事处事务")
    fengongsi_1_1_renli = Department("上海分公司宁波办事处人力资源部", "管理上海分公司宁波办事处人事")
    fengongsi_1_1_caiwu = Department("上海分公司宁波办事处财务部", "管理上海分公司宁波办事处财务")
    fengongsi_1_1.add(fengongsi_1_1_renli)
    fengongsi_1_1.add(fengongsi_1_1_caiwu)

    fengongsi_1.add(fengongsi_1_1)  # 将办事处加入到子公司管理

    zonggongsi.display_organization()
    zonggongsi.show_duty()
