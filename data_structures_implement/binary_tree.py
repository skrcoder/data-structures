# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
#!/usr/bin/python

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    # 二叉树的前序遍地
    def pre_order(self):
        print self.key
        if self.leftChild:
            self.leftChild.pre_order()
        if self.rightChild:
            self.rightChild.pre_order()

    # 二叉树的中序遍地
    def in_order(self):
       if self.leftChild:
            self.leftChild.in_order()
       print self.key
       if self.rightChild:
            self.rightChild.in_order()

# 二叉树的后序遍地(非BinaryTree的类函数实现)
def post_order(binary_tree):
    if binary_tree:
        post_order(binary_tree.getLeftChild())
        post_order(binary_tree.getRightChild())
        print binary_tree.getRootVal()

if __name__ == "__main__":
    r = BinaryTree('a')
    print(r.getRootVal())
    print(r.getLeftChild())
    r.insertLeft('b')
    print(r.getLeftChild())
    print(r.getLeftChild().getRootVal())
    r.insertRight('c')
    print(r.getRightChild())
    print(r.getRightChild().getRootVal())
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())

    # 二叉树的遍历
    print "iter of tree:"
    r.pre_order()
    r.in_order()
    post_order(r)
