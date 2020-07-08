from typing import List


class Solution:
    dic = {"2": "abc",
           "3": "def",
           "4": "ghi",
           "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        temp = []
        for i in digits:
            if res:
                for j in self.dic[i]:
                    for it in res:
                        temp.append(it+j)
                res = temp
                temp = []
            else:
                for j in self.dic[i]:
                    res.append(j)
        return res
    # 真不明白为什么下面这个在编辑器里执行就可以，到leetcode上就不行了。
    # def letterCombinations(self, digits: str) -> List[str]:
    #     if digits == '':
    #         return []
    #     if len(digits) == 1:
    #         for ii in self.dic[digits]:
    #             self.res.append(ii)
    #     else:
    #         for z in self.dic[digits[0]]:
    #             self.get_result(digits[1:], z)
    #     return self.res
    #
    # def get_result(self, s, st):
    #     if len(s) == 1:
    #         for ii in self.dic[s]:
    #             self.res.append(st + ii)
    #         return
    #
    #     for z in self.dic[s[0]]:
    #         self.get_result(s[1:], st+z)
if __name__ == '__main__':
    print(Solution().letterCombinations("234"))