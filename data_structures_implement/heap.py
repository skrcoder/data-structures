# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
#!/usr/bin/python

class Heap:
    """
    最小堆的实现
    """
    def __init__(self):
        # 保证heap_list[0]时有值
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, k):
        # 在二叉堆中插入一个，依赖perc_up函数
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

    def perc_up(self, index):
        while index // 2 > 0:
            if self.heap_list[index] < self.heap_list[index // 2]:
                self.heap_list[index], self.heap_list[index // 2] = \
                        self.heap_list[index // 2], self.heap_list[index]
            index = index // 2

    def del_min(self):
        # 在最小堆中删除最小值,依赖perc_down函数
        ret_val = self.heap_list[1]
        # 用二叉堆中最后一个值替换最小值
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        # 弹出最后一个值
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val

    def perc_down(self, index):
        while index * 2 <= self.current_size:
            # 至少包含一个左子树
            min_child_index = self.min_child(index)
            if self.heap_list[index] > self.heap_list[min_child_index]:
                self.heap_list[index], self.heap_list[min_child_index] = \
                        self.heap_list[min_child_index], self.heap_list[index]
            index = min_child_index

    def min_child(self, index):
        if index * 2 + 1 > self.current_size:
            # 没有右子树
            return index * 2
        else:
            if self.heap_list[index * 2] < self.heap_list[index * 2 + 1]:
                return index * 2
            else:
                return index * 2 + 1

    def build_heap(self, alist):
        # 建堆操作时间复杂度为O(n), 所以堆排序的时间复杂度为O(nlogn)
        i = len(alist) // 2 # 从中间值开始perc_down, 一直到根节点
        self.current_size = len(alist)
        self.heap_list = [0] + alist[:]
        while i > 0:
            self.perc_down(i)
            i -= 1

if __name__ == "__main__":
    heap = Heap()
    #heap.insert(4)
    #heap.insert(4)
    heap.build_heap([9, 6, 5, 2, 3])
    print heap.del_min()
    print heap.del_min()
    print heap.del_min()
    print heap.del_min()
    print heap.del_min()

