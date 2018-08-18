# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
# github: https://github.com/skrcoder
#!/usr/bin/python

"""
// 面试题3（一）：找出数组中重复的数字
// 题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，
// 也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。例如，如果输入长度为7的数组{2, 3, 1, 0, 2, 5, 3}，
// 那么对应的输出是重复的数字2或者3。
"""
# case:[9, 1, 1, 2, 3, 4, 5, 6, 7, 8]

def duplicate(numbers):
    """
    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    if not numbers:
        return None
    for item in numbers:
        if item < 0 or item > len(numbers):
            return None

    id = 0
    for index in range(len(numbers)):
        while numbers[index] != index:
            if numbers[index] == numbers[numbers[index]]:
                # 这条语句保证while循环会结束
                return numbers[index]
            else:
                # ！！！本题重点注意这里list中交换元素的区别,采用方案二交换会有bug:死循环
                print "bef:", numbers
                # case1
                #tmp = numbers[index]
                #numbers[index] = numbers[tmp]
                #numbers[tmp] = tmp
                # case2
                #numbers[index], numbers[numbers[index]] = \
                #        numbers[numbers[index]], numbers[index]
                # case 3
                tmp = numbers[index]
                numbers[index], numbers[tmp] = \
                        numbers[tmp], numbers[index]
                print "aft:", numbers
    return None

if __name__ == "__main__":
    numbers = [0, 0, 2]
    print duplicate(numbers)
    numbers = [9, 1, 1, 2, 3, 4, 5, 6, 7, 8]
    print duplicate(numbers)
    numbers = [2, 1, 3, 0, 4]
    print duplicate(numbers)
    numbers = [4, 0, 1, 2, 3]
    print duplicate(numbers)
