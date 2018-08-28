# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
# github: https://github.com/skrcoder
#!/usr/bin/python

"""
// 面试题42：连续子数组的最大和
// 题目：输入一个整型数组，数组里有正数也有负数。数组中一个或连续的多个整
// 数组成一个子数组。求所有子数组的和的最大值。要求时间复杂度为O(n)。
"""
def greatest_sum_of_subarrays(nums):
    """
    方法一：利用数组的规则
    """
    if not nums:
        return None
    curr_sum, max_sum = 0, 0
    for index in range(len(nums)):
        if curr_sum <=0:
            curr_sum = nums[index]
        else:
            curr_sum += nums[index]
        max_sum = max(curr_sum, max_sum)
    return max_sum

def greatest_sum_of_subarrays_2(nums):
    """
    方法二：动态规划?
    """
    if not nums:
        return None
    a_list = [0] * len(nums)
    for index in range(len(nums)):
        if index == 0 or a_list[index - 1] <= 0:
            a_list[index] = nums[index]
        else:
            a_list[index] += a_list[index - 1] + nums[index]
    print a_list
    return max(a_list)

if __name__ == "__main__":
    alist = [1, -2, 3, 10, -4, 7, 2, -5]
    print greatest_sum_of_subarrays(alist)
    print greatest_sum_of_subarrays_2(alist)


