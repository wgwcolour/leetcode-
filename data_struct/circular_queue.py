# 循环队列

class CircularQueue():
    def __init__(self, nums):
        """
        使用数组实现顺序的循环队列
        :param nums: 队列限制的长度
        """
        self.head = 0
        self.tail = 0
        self.nums = nums
        self.items = []

    def enqueue(self, item):
        """
        入队
        :param item:
        :return:
        """
        flag = (self.tail + 1) % self.nums
        if flag == self.head:  # 队列满了
            return False
        self.items[self.tail] = item
        self.tail = flag
        return True

    def dequeue(self):
        """
        出队
        :return:
        """
        if self.head == self.tail:  # 队列空了
            return None
        ret = self.items[self.head]
        self.head = (self.head + 1) % self.nums
        return ret
