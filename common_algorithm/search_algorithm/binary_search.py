# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
#!/usr/bin/python

def binary_search(sorted_seq, val):
    """
    对已排序的序列，进行二分查找
    """
    low = 0
    high = len(sorted_seq) - 1
    while low <= high:
        mid = (low + high) / 2
        if sorted_seq[mid] == val:
            return mid
        elif sorted_seq[mid] > val:
            high = mid - 1
        else:
            low = mid + 1
    return None

def binary_search_recursive(sorted_seq, item):
    if len(sorted_seq)) == 0:
        return None
    else:
        mid_index = len(sorted_seq) // 2
        if sorted_seq[mid_index] == item:
            return mid_index
        elif sorted_seq[mid_index] > item:
            return binary_search_recursive(sorted_seq[: mid_index], item)  
        else:
            return binary_search_recursive(sorted_seq[mid_index + 1:], item)

if __name__ == "__main__":

    a = [1, 3, 5]
    result = binary_search(a, 2)
    result2 = binary_search(a, 3)
    print result, result2
