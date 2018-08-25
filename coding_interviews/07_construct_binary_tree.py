# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
# github: https://github.com/skrcoder
#!/usr/bin/python

"""
// 面试题7：重建二叉树
// 题目：输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输
// 入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序遍历序列{1,
// 2, 4, 7, 3, 5, 6, 8}和中序遍历序列{4, 7, 2, 1, 5, 3, 8, 6}，则重建出
// 图2.6所示的二叉树并输出它的头结点。
"""

import sys
sys.path.append("../data_structures_implement/")
from binary_tree import BinaryTree

def construct(preorder, inorder):
    if not preorder or not inorder:
        return None
    return construct_help(preorder, inorder)

def construct_help(preorder, inorder):
    if not preorder and not inorder:
        return None
    root_value = preorder[0]
    root_index = inorder.index(root_value)
    root = BinaryTree(root_value)
    root.leftChild = construct_help(preorder[1: root_index  + 1], \
            inorder[: root_index])
    root.rightChild = construct_help(preorder[root_index + 1:], \
            inorder[root_index + 1:])

    return root

if __name__ == "__main__":
    pre = [1, 2, 3, 5, 6, 4]
    tin = [5, 3, 6, 2, 4, 1]
    newTree = construct(pre, tin)
    newTree.pre_order()
    newTree.in_order()
