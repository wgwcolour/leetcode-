# 回文数
"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x > 0:
            pass
        elif x < 0:
            return False
        else:
            return True
        a = str(x)
        l = len(a)
        if l%2 == 0:
            s = l//2
            s1 = a[:s]
            s2 = a[s:]
            c = ""
            for i in s2:
                c = i + c
            if s1 == c:
                return True
            else:
                return False
        else:
            s = (l-1)//2
            s1 = a[:(s + 1)]
            s2 = a[s:]
            c = ""
            for i in s2:
                c = i + c
            if s1 == c:
                return True
            else:
                return False
