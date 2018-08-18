# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
# github: https://github.com/skrcoder
#!/usr/bin/python

"""
// 面试题6：从尾到头打印链表
// 题目：输入一个链表的头结点，从尾到头反过来打印出每个结点的值。
"""
import sys
sys.path.append("../data_structures_implement/")
from stack import Stack
from link import Link

def print_iteratively(head_node):
    if not head_node:
        return None
    tmp_stack = Stack()
    while head_node:
        tmp_stack.push(head_node.get_data())
        head_node = head_node.get_next()
    print "output:"
    while not tmp_stack.is_empty():
        print tmp_stack.pop()

def print_recursively(head_node):
    if not head_node:
        return None
    else:
        print_recursively(head_node.get_next())
    print head_node.get_data()

if __name__ == "__main__":
    my_link = Link()
    my_link.add(2)
    my_link.add(3)
    my_link.add(4)
    my_link.show()
    print_iteratively(my_link.head)
    my_link2 = Link()
    my_link2.add(5)
    my_link2.add(6)
    my_link2.add(7)
    my_link2.show()
    print_iteratively(my_link2.head)
