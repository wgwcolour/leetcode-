"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        看了题解：利用双指针，分别为l=0和r=len(height),面积=(r-l)*(min(height[l],height[r])),
        因为移动的时候(r-l)变小，那只有移动短的那边使min(height[l],height[r])的值变大，才有可能面积变大，否则短板不变，长板再长也没用。
        :param height:
        :return:
        """
        l = 0
        r = len(height)
        S = 0
        while l < r:
            h1 = height[l]
            h2 = height[r-1]
            S = (r-l-1) * min(h1,h2) if S < (r-l-1) * min(h1,h2) else S
            if h1 <= h2:
                l+=1
            else:
                r-=1
        return S
if __name__ == '__main__':
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))