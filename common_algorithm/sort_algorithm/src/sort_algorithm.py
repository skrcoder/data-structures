# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
#!/usr/bin/python

def quick_sort(seq, left, right):
    if left >= right:
        return seq
    key = seq[left]
    low, hight = left, right
    while left < right:

