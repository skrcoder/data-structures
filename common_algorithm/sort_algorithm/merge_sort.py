# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
#!/usr/bin/python

def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    middle_index = len(alist) // 2
    left_list = merge_sort(alist[: middle_index])
    right_list = merge_sort(alist[middle_index:])
    return merge_two_list(left_list, right_list)

def merge_two_list(left, right):
    result_list = []
    i, j= 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result_list.append(left[i])
            i += 1
        else:
            result_list.append(right[j])
            j += 1
    if i == len(left):
        # left遍历完成
        for item in right[j:]:
            result_list.append(item)
    else:
        for item in left[i:]:
            result_list.append(item)
    return result_list

# 解法二，merge两个list时候不需要额外空间
def merge_sort_2(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    left_list = alist[: mid]
    right_list = alist[mid:]
    merge_sort_2(left_list)
    merge_sort_2(right_list)
    # 合并
    i, j, k = 0, 0, 0
    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            alist[k] = left_list[i]
            i += 1
        else:
            alist[k] = right_list[j]
            j += 1
        k += 1

    while i < len(left_list):
        alist[k] = left_list[i]
        i += 1
        k += 1
    while j < len(right_list):
        alist[k] = right_list[j]
        j += 1
        k += 1

if __name__ == "__main__":
    """
    case:
    0 3 6
    1 4 7
    2 5 8
    """
    l = [4, 3, 6, 9, 1, 2, 5, 8, 7]
    print l
    l_other = merge_sort(l)
    print l_other
    print l
    merge_sort_2(l)
    print l
