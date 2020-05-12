# 整数反转
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321

示例 2:

输入: -123
输出: -321

示例 3:

输入: 120
输出: 21
"""
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            b = ""
            a = str(x)[1:]
            for i in a:
                b = i + b
            num = int("-" + b)
            if num < -2**31:
                return 0
            else:
                return num
        elif x > 0:
            c = ""
            a = str(x)
            for i in a:
                c = i + c
            num = int(c)
            if num > 2**31:
                return 0
            else:
                return num
        elif x == 0:
            return 0
