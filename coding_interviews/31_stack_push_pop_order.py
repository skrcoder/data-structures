# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
# github: https://github.com/skrcoder
#!/usr/bin/python

"""
// 面试题31：栈的压入、弹出序列
// 题目：输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是
// 否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列1、2、3、4、
// 5是某栈的压栈序列，序列4、5、3、2、1是该压栈序列对应的一个弹出序列，但
// 4、3、5、1、2就不可能是该压栈序列的弹出序列。
"""

def is_pop_order(push_list, pop_list):
    if not push_list or not pop_list:
        return None
    stack = []
    for item in push_list:
        stack.append(item)
        # 这里不能有item来比较，而要用stack[-1],即辅助栈顶值
        #while stack and item == pop_list[0]:
        while stack and stack[-1] == pop_list[0]:
            stack.pop()
            pop_list.pop(0)

    if stack:
        # 所有数字压入栈之后，依然没有找到下一个要弹出的数字
        return False
    else:
        return True

if __name__ == "__main__":
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 5, 3, 2, 1]
    popVF = [4, 5, 2, 1, 3]
    print is_pop_order(pushV, popV)
    print is_pop_order(pushV, popVF)
