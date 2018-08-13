# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
#!/usr/bin/python

def bubble_sort(alist):
    for index in range(len(alist) - 1, 0, -1):
        for i in range(index):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = \
                    alist[i + 1], alist[i]

def short_bubble_sort(alist):
    # 如果某一轮没有交换，则表示排序完成
    exchange = True
    index = len(alist) - 1
    while index > 0 and exchange:
        exchange = False
        for i in range(index):
            if alist[i] > alist[i + 1]:
                exchange = True
                alist[i], alist[i + 1] = \
                    alist[i + 1], alist[i]
        index -= 1


if __name__ == "__main__":
    l = [4, 3, 6, 9]
    print l
    #bubble_sort(l)
    short_bubble_sort(l)
    print l
