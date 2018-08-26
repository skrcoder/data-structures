# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
# github: https://github.com/skrcoder
#!/usr/bin/python

"""
// 面试题55（一）：二叉树的深度
// 题目：输入一棵二叉树的根结点，求该树的深度。从根结点到叶结点依次经过的
// 结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
"""
import sys
sys.path.append("../data_structures_implement/")
from binary_tree import BinaryTree

def binary_tree_depth_recur(root):
    if not root:
        return 0
    left_depth = binary_tree_depth_recur(root.leftChild)
    right_depth = binary_tree_depth_recur(root.rightChild)
    return max(left_depth, right_depth) + 1

def binary_tree_depth_iter(root):
    # 非递归算法，需要增加两个栈（stack, tag）
    if not root:
        return 0
    depth = 0
    stack, tag = [], []
    p_node = root
    while p_node or stack: # 注意这里是or
        while p_node:
            stack.append(p_node)
            tag.append(0)
            p_node = p_node.leftChild
        if tag[-1] == 1:
            depth = max(depth, len(stack))
            stack.pop()
            tag.pop()
            p_node = None  #一条路径结束
        else:
            p_node = stack[-1] # 注意这里的赋值
            p_node = p_node.rightChild # 到叶子节点时的，通过stack的判断继续
            tag.pop()
            tag.append(1)
    return depth

if __name__ == "__main__":
    r = BinaryTree('a')
    r.insertLeft('b')
    r.insertRight('c')
    r.insertLeft("d")
    r.insertLeft("e")
    r.insertRight('f')
    r.insertRight('g')
    print "pre order of tree:"
    r.pre_order()
    print "in order of tree:"
    r.in_order()
    print "depth of iter:",
    print binary_tree_depth_iter(r)
    print "depth of recur:",
    print binary_tree_depth_recur(r)
