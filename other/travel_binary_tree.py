# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
# github: https://github.com/skrcoder
#!/usr/bin/python

"""
非递归前中后序遍历二叉树, 实现方案与求二叉树深度类似
"""
import sys
sys.path.append("../data_structures_implement/")
from binary_tree import BinaryTree

class TreeNode():
    """
    二叉树定义
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def pre_order_iter(root):
    if not root:
        return None
    p_node, tree_stack = root, []
    while p_node or tree_stack:
        while p_node:
            print p_node.key
            tree_stack.append(p_node)
            p_node = p_node.leftChild
        if tree_stack:
            p_node = tree_stack.pop()
            p_node = p_node.rightChild

def pre_order_recur(root):
    if root:
        print root.key
        pre_order_recur(root.leftChild)
        pre_order_recur(root.rightChild)

def in_order_iter(root):
    if not root:
        return None
    p_node, tree_stack = root, []
    while p_node or tree_stack:
        while p_node:
            tree_stack.append(p_node)
            p_node = p_node.leftChild
        if tree_stack:
            p_node = tree_stack.pop()
            print p_node.key
            p_node = p_node.rightChild

def in_order_recur(root):
    if root:
        in_order_recur(root.leftChild)
        print root.key
        in_order_recur(root.rightChild)

def post_order_iter(root):
    if not root:
        return None
    p_node, pre_visted, tree_stack = root, None, []
    tree_stack.append(root)
    while tree_stack:
        p_node = tree_stack[-1]
        if (not p_node.leftChild and not p_node.rightChild) \
                or (pre_visted and (p_node.leftChild == pre_visted or p_node.rightChild == pre_visted)):
            print p_node.key
            pre_visted = tree_stack.pop()
        else:
            if p_node.rightChild:
                # 先增加右节点
                tree_stack.append(p_node.rightChild)
            if p_node.leftChild:
                tree_stack.append(p_node.leftChild)

def post_order_recur(root):
    if root:
        post_order_recur(root.leftChild)
        post_order_recur(root.rightChild)
        print root.key

if __name__ == "__main__":
    r = BinaryTree('a')
    r.insertLeft('b')
    r.insertRight('c')
    r.insertLeft("d")
    r.insertLeft("e")
    r.insertRight('f')
    r.insertRight('g')
    print "pre order iter:"
    pre_order_iter(r)
    print "in order iter:"
    in_order_iter(r)
    print "post iter:"
    post_order_iter(r)
