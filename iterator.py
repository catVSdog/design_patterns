"""
迭代器模式
"""


class Iterator:
    def __init__(self, any_list):
        self.any_list = any_list  # 需要持有需要迭代的对象
        self.current = 0
        self.is_done = False

    def set_begin(self, num):
        self.current = num

    def next(self):
        try:
            result = self.any_list[self.current]
            self.current += 1
            return result
        except IndexError:
            self.is_done = True


class ItemList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def create_iterator(self):
        return Iterator(self.items)


if __name__ == '__main__':
    num_list = ItemList()
    num_list.add_item(1)
    num_list.add_item(2)
    num_list.add_item(3)
    num_list.add_item(4)

    num_ite = num_list.create_iterator()

    while (not num_ite.is_done):
        print(num_ite.next())
