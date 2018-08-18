# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
#!/usr/bin/python

def find_lcs_len(s1, s2):
    """
    获得最长公共子字符串长度算法
    """
    m = [[0 for x in s2] for y in s1]
    for p1 in range(len(s1)):
        for p2 in range(len(s2)):
            if s1[p1] == s2[p2]:
                if p1 == 0 or p2 == 0:
                    m[p1][p2] = 1
                else:
                    m[p1][p2] = m[p1 - 1][p2 - 1] + 1
            elif m[p1 - 1][p2] < m[p1][p2 - 1]:
                m[p1][p2] = m[p1][p2 - 1]
            else:  
                # m[p1-1][p2] > m[p1][p2-1]
                m[p1][p2] = m[p1 - 1][p2]
    return m[-1][-1]

if __name__ == "__main__":
    s1 = "eabc"
    s2 = "rabe"
    s3 = "eabd"
    print find_lcs_len(s1, s2)
    print find_lcs_len(s1, s3)
