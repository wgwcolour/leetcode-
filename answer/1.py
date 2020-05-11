# leetcode-
# 两数之和
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            num = target-nums[i]
            for a in range(len(nums)):
                if nums[a] == num and i != a:
                    return [i,a]
