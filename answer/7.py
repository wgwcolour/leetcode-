# 整数反转
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
