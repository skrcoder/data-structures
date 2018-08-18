# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
# github: https://github.com/skrcoder
#!/usr/bin/python

"""
// 面试题26：树的子结构
// 题目：输入两棵二叉树A和B，判断B是不是A的子结构。

"""
import sys
sys.path.append("../data_structures_implement/")
from binary_tree import BinaryTree

def has_sub_tree(root1, root2):
    result = False
    if root1 and root2:
        if root1.key == root2.key:
            result = is_tree1_have_tree2(root1, root2)
        if not result:
            result = has_sub_tree(root1.leftChild, root2)
        if not result:
            result = has_sub_tree(root1.rightChild, root2)
    return result

def is_tree1_have_tree2(root1, root2):
    if not root2:
        return True
    if not root1:
        return False
    if root1.key != root2.key:
        return False
    return is_tree1_have_tree2(root1.leftChild, root2.leftChild) \
            and is_tree1_have_tree2(root1.rightChild, root2.rightChild)

if __name__ == "__main__":
    my_binary_tree = BinaryTree(3)
    my_binary_tree.insertLeft("4")
    my_binary_tree.insertRight("5")
    my_binary_tree.insertLeft("6")
    my_binary_tree.insertRight("7")
    my_binary_tree.pre_order()

    my_binary_tree2 = BinaryTree("6")
    my_binary_tree2.insertLeft("4")
    my_binary_tree2.pre_order()

    print has_sub_tree(my_binary_tree, my_binary_tree2)
