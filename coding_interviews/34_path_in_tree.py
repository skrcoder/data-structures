# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
# github: https://github.com/skrcoder
#!/usr/bin/python

"""
// 面试题34：二叉树中和为某一值的路径
// 题目：输入一棵二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所
// 有路径。从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

"""
import sys
sys.path.append("../data_structures_implement/")

from binary_tree import BinaryTree

def find_path(root_node, expected_sum):
    if not root_node:
        return
    path_list = []
    current_sum = 0
    find_path_help(root_node, expected_sum, path_list, current_sum)

def find_path_help(root_node, expected_sum, path_list, current_sum):
    current_sum += root_node.key
    path_list.append(root_node.key)
    is_leaf = not root_node.leftChild and not root_node.rightChild
    if is_leaf and current_sum == expected_sum:
        print path_list
    elif root_node.leftChild:
        find_path_help(root_node.leftChild, expected_sum, path_list, current_sum)
    elif root_node.rightChild:
        find_path_help(root_node.rightChild, expected_sum, path_list, current_sum)
    path_list.pop()

if __name__ == "__main__":
    my_binary_tree = BinaryTree(1)
    my_binary_tree.insertLeft(2)
    my_binary_tree.insertRight(3)
    my_binary_tree.insertLeft(4)
    my_binary_tree.pre_order()

    find_path(my_binary_tree, 7)
