# coding=utf-8
# Author: zhengxiongfeng
# mail: 657019943@qq.com
# github: https://github.com/skrcoder
#!/usr/bin/python

"""
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

    Input: [[1,1,0],[1,0,1],[0,0,0]]
    Output: [[1,0,0],[0,1,0],[1,1,1]]
    Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
    Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

    Example 2:

    Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
    Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
    Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

    Notes:

        1 <= A.length = A[0].length <= 20
        0 <= A[i][j] <= 1
"""
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for index in range(len(A)):
            for inner_index in range(len(A[index])):
                left, right = inner_index, len(A[index]) - 1 - inner_index
                if left < right:
                    if A[index][left] == A[index][right]:
                        A[index][left] = 1 - A[index][left]
                        A[index][right] = 1 - A[index][right]
                    else:
                        continue
                elif left == right:
                    A[index][left] = 1 - A[index][left]
                else:
                    break
        return A

if __name__ == "__main__":
    s = Solution()
    a = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    print a
    s.flipAndInvertImage(a)
    print a


