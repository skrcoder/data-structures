# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
#!/usr/bin/python

import random

def quick_sort(alist):
    quick_sort_helper(alist, 0, len(alist) - 1)

def quick_sort_helper(alist, start, end):
    if start < end:
        split_index = partition(alist, start, end)
        quick_sort_helper(alist, start, split_index - 1)
        quick_sort_helper(alist, split_index + 1, end)

def partition(alist, first, last):
    # TODO：建议随机选择中轴点
    pivot_value = alist[first]
    left_index = first + 1
    right_index = last
    exchange_done = False
    while not exchange_done:
        while left_index <= right_index and alist[left_index] <= pivot_value:
            left_index += 1
        while right_index >= left_index and alist[right_index] >= pivot_value:
            right_index -= 1
        if left_index > right_index:
            exchange_done = True
        else:
            alist[left_index], alist[right_index] = \
                alist[right_index], alist[left_index]
    # 把pivot_value 与right_index 交换
    alist[first], alist[right_index] = alist[right_index], alist[first]
    return right_index

if __name__ == "__main__":
    """
    case:
    0 3 6
    1 4 7
    2 5 8
    """
    l = [4, 3, 6, 9, 1, 2, 5, 8, 7]
    print l
    quick_sort(l)
    print l
