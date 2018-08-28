# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
# github: https://github.com/skrcoder
#!/usr/bin/python

"""
// 面试题39：数组中出现次数超过一半的数字
// 题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例
// 如输入一个长度为9的数组{1, 2, 3, 2, 2, 2, 5, 4, 2}。由于数字2在数组中
// 出现了5次，超过数组长度的一半，因此输出2。
"""

def find_more_than_half(nums):
    """
    方法一：基于partition的方法,找到数组中的中间值：O(n)
    找到数组中第k大的树和Top(k)都能用这种方法
    """
    if not nums:
        return None
    middle = (len(nums) - 1) // 2
    start, end = 0, len(nums) - 1
    pivot_index = partition(nums, start, end)
    while pivot_index != middle:
        if pivot_index > middle:
            end = pivot_index - 1
            pivot_index = partition(nums, start, end)
        else:
            start = pivot_index + 1
            pivot_index = partition(nums, start, end)
    return nums[pivot_index]

def find_more_than_half_2(nums):
    """
    方法二：基于数组的规律：O(n)
    """
    if not nums:
        return None
    result = nums[0]
    result_count = 1
    for index in range(1, len(nums)):
        if nums[index] == result:
            result_count += 1
        elif result_count == 0:
            result = nums[index]
            result_count = 1
        else:
            result_count -= 1
    return result

def partition(nums, start, end):
    if not nums:
        return None
    left, right = start + 1, end
    pivot_index, pivot_value = start, nums[start]
    exchange_done = False
    while not exchange_done:
        while left <= right and nums[left] <= pivot_value:
            left += 1
        while right >= left and nums[right] >= pivot_value:
            right -= 1
        if left > right:
            # 如果左指针超过右指针，则不交换且退出，返回右指针位置
            exchange_done = True
        else:
            nums[left], nums[right] = nums[right], nums[left]
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    return right

if __name__ == "__main__":
    nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print find_more_than_half(nums)
    print find_more_than_half_2(nums)
