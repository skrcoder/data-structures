# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
#!/usr/bin/python

def del_char(s, c=" "):
    """
    原地删除字符串中指定字符
    abc  def g -> abcdefg
    """
    if not s:
        return None
    s = list(s)
    left, right = 0, 0
    for index in range(right, len(s)):
        #找到字符串第一个空格的位置
        if s[index] == c:
            right = index
            break
    left = right
    for index in range(right, len(s)):
        #  找到第一个需要向前替换的位置
        if s[right] != c:
            right = index
            break
    for index in range(right, len(s)):
        # 依次向前替换
        if s[index] != c:
            s[left], s[index] = \
                    s[index], s[left]
            left += 1
    return s[:left]


def del_char_2(s, c=" "):
    """
    原地删除字符串中指定连续的字符: 连续出现才删除,
    区别：right不需要找到第一个向前替换的位置
    abc   def g  hi -> abcdef ghi
    """
    if not s:
        return None
    s = list(s)
    left, right = 0, 0
    for index in range(right, len(s)):
        #找到字符串第一个空格的位置
        if s[index] == c:
            right = index
            break
    left = right

    while right < len(s):
        if s[right] == c:
            if right + 1 < len(s) and s[right + 1] == c:
                while s[right] == c:
                    # 找到连续空格之后的第一个需要向前替换的位置
                    right += 1
                s[left], s[right] = s[right], s[left]
                left += 1
                right += 1
        s[left], s[right] = s[right], s[left]
        left += 1
        right += 1
    return s[:left]



if __name__ == "__main__":
    s = "abc  def g"
    print list(s)
    print del_char(s)
    s = "abc   def g  hi"
    print list(s)
    print del_char_2(s)
