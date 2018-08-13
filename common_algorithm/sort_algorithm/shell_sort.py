# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
#!/usr/bin/python

def shell_sort(alist, divide_num):
    sub_list_gap = len(alist) // divide_num
    while sub_list_gap > 0:
        for index in range(sub_list_gap):
            # 每个gap序列中都进行插入排序
            gap_insert_sort(alist, index, sub_list_gap)
        sub_list_gap = sub_list_gap // divide_num


def gap_insert_sort(alist, index, gap):
    # 插入排序[index, index+gap, index+2gap,...]
    for i in range(index + gap, len(alist), gap):
        current_value = alist[i]
        current_index = i
        while current_index >= gap and alist[current_index - gap] > current_value:
            alist[current_index] = alist[current_index - gap]
            current_index -= gap
        alist[current_index] = current_value
            
if __name__ == "__main__":
    """
    case:
    0 3 6
    1 4 7
    2 5 8
    """
    l = [4, 3, 6, 9, 1, 2, 5, 8, 7]
    print l
    shell_sort(l, 3)
    print l
