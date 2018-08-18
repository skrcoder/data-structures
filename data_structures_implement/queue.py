# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
# github: https://github.com/skrcoder
#!/usr/bin/python

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    queue = Queue()
    print queue.is_empty()
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print queue.is_empty()
    print queue.dequeue()
    print queue.size()
