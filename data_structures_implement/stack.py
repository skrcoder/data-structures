# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
# github: https://github.com/skrcoder
#!/usr/bin/python

class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    s = Stack()
    print s.is_empty()
    s.push(4)
    s.push(5)
    s.push(6)
    print s.pop()
    print s.peek()
    print s.size()
    print s.is_empty()
