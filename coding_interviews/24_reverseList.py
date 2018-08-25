# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
# github: https://github.com/skrcoder
#!/usr/bin/python

"""
// 面试题24：反转链表
// 题目：定义一个函数，输入一个链表的头结点，反转该链表并输出反转后链表的
// 头结点。
"""
import sys
sys.path.append("../data_structures_implement/")
from link import Link

def reverse_iteratively(head_node):
    reversed_head = None
    current_node = head_node
    pre_node = None
    while current_node != None:
        next_node = current_node.get_next()
        if not next_node:
            reversed_head = current_node
        current_node.set_next(pre_node)
        pre_node = current_node
        current_node = next_node
    return reversed_head

def reverse_recursively(head_node):
    if not head_node or not head_node.get_next():
        return head_node
    else:
        # reversed_head 用来保留递归结束后，想要输出的头节点
        reversed_head = reverse_recursively(head_node.get_next())
        head_node.get_next().set_next(head_node)
        head_node.set_next(None)
        return reversed_head


if __name__ == "__main__":
    my_link = Link()
    my_link.add(2)
    my_link.add(3)
    my_link.add(4)
    my_link.show()
    #out_link_head = reverse_iteratively(my_link.head)
    out_link_head = reverse_recursively(my_link.head)
    while out_link_head:
        print out_link_head.data
        out_link_head = out_link_head.get_next()
