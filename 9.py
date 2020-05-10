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
