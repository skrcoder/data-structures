# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
#!/usr/bin/python

def insert_sort(alist):
    for index in range(1, len(alist)):
        current_index = index
        current_value = alist[current_index]
        while current_index > 0 and current_value < alist[current_index - 1]:
            # 移位操作，相比交换操作简单
            alist[current_index] = alist[current_index - 1]
            current_index -= 1
        # 赋值
        alist[current_index] = current_value

if __name__ == "__main__":
    l = [4, 3, 6, 9]
    print l
    insert_sort(l)
    print l
