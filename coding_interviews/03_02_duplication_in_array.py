# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
# github: https://github.com/skrcoder
#!/usr/bin/python

"""
// 面试题3（二）：不修改数组找出重复的数字
// 题目：在一个长度为n+1的数组里的所有数字都在1到n的范围内，所以数组中至
// 少有一个数字是重复的。请找出数组中任意一个重复的数字，但不能修改输入的
// 数组。例如，如果输入长度为8的数组{2, 3, 5, 4, 3, 2, 6, 7}，那么对应的
// 输出是重复的数字2或者3。
"""
# case:[9, 1, 1, 2, 3, 4, 5, 6, 7, 8]

def duplicate_1(numbers):
    """
    时间复杂度：O(N)
    空间负责度：O(N)
    """
    if not numbers:
        return None
    for item in numbers:
        if item < 1 or item > len(numbers):
            raise Exception("input data error")
    temp = [0] * len(numbers)
    for item in numbers:
        if temp[item] !=0:
            return item
        else:
            temp[item] = item
    return None

def duplicate_2(numbers):
    """
    时间复杂度：O(nlogn)
    空间负责度：O(1)
    """
    if not numbers:
        return None
    for item in numbers:
        if item < 1 or item > len(numbers):
            raise Exception("input data error")

    start, end = 1, len(numbers) - 1
    while end >= start:
        middle = (end + start) // 2
        range_count = count_range(numbers, start, middle)
        if end == start:
            if range_count > 1:
                return start
            else:
                break
        if range_count > middle - start + 1:
            end = middle
        else:
            start = middle + 1
    return None

def count_range(numbers, start, end):
    if not numbers:
        return 0
    count = 0
    for item in numbers:
        if start <= item <= end:
            count += 1
    return count


if __name__ == "__main__":
    numbers = [1, 2, 2]
    print duplicate_1(numbers)
    print duplicate_2(numbers)
