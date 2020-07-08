"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 使用双指针法，先给list排序...好强啊
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            l= i+1
            r = n-1
            if nums[i]>0:
                return res
            if i>0 and nums[i]==nums[i-1]:
                continue
            while l<r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                    continue
                if nums[i] + nums[l] + nums[r] > 0:
                    r-=1
                else:
                    l+=1
        return res

if __name__ == '__main__':
    li = [-1, 0, 1, 2, -1, -4]

    # print(li)
    print(Solution().threeSum(li))