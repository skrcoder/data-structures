# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
#!/usr/bin/python

def select_sort(alist):
    for index in range(len(alist) - 1, 0, -1):
        index_of_max = 0
        # 找到值最大的索引位置
        for i in range(1, index + 1):
            if alist[i] > alist[index_of_max]:
                index_of_max = i
        # 交换,把当前的最大值归位,对比冒泡排序交换次数更少
        alist[index], alist[index_of_max] = \
            alist[index_of_max], alist[index]

if __name__ == "__main__":
    l = [4, 3, 6, 9]
    print l
    select_sort(l)
    print l
