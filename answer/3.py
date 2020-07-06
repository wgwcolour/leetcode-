"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 解题思路 滑动窗口，例如把字符串放入一个队列，当队列中进来一个重复字符串时，从最前面开始移除,直到满足题目要求
        # 遍历整个字符串后，返回过程中队列最长时候的长度
        lookup = set()
        left = 0
        l = 0
        for i in s:
            while i in lookup:
                lookup.remove(s[left])
                left += 1
            lookup.add(i)
            l = len(lookup) if len(lookup) > l else l
        return l



if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("aabaab!bb"))