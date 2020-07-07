"""
给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。

请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        摘抄大神题解：在有序数组中求中位数，相当于求第k小的数。只要知道中位数是第几小的数字计算出来的就可以了。
        :param nums1:
        :param nums2:
        :return:
        """
        # 这里取两个数是为了兼容奇数和偶数的情况，如果是奇数，同一个数就取两次
        k1 = (len(nums1) + len(nums2) + 1) // 2
        k2 = (len(nums1) + len(nums2) + 2) // 2

        def getKth(nums1, start1, end1, nums2, start2, end2, k):
            """
            从两个数组中取第k小的数
            :param nums1: 数组1
            :param start1: 数组1的起始位置
            :param end1: 数组1的结束位置
            :param nums2: 数组2
            :param start2: 数组2的起始位置
            :param end2: 数组2的结束位置
            :param k: 要取第k小的数
            :return:
            """
            l1 = end1 - start1 + 1
            l2 = end2 - start2 + 1
            # 让l1小于l2，这样如果有一个数组为空了，那一定是l1的数组
            if l1 > l2: return getKth(nums2, start2, end2, nums1, start1, end1, k)
            # 如果l1数组空了，那么直接返回l2数组第k小的数就行了
            if l1 == 0: return nums2[start2 + k - 1]
            # 如果k=1,那么l1和l2数组谁小返回谁
            if k == 1:
                return min(nums2[start2 + k - 1], nums1[start1 + k - 1])  # 这里(start + k -1)易读，由于k=1，其实只取start位置就可以

            i = start1 + min(l1, k // 2) - 1
            j = start2 + min(l2, k // 2) - 1
            if nums2[j] < nums1[i]:
                return getKth(nums1, start1, end1, nums2, j + 1, end2, k - min(l2, k // 2))
            else:
                return getKth(nums1, i + 1, end1, nums2, start2, end2, k - min(l1, k // 2))

        return (getKth(nums1, 0, len(nums1) - 1, nums2, 0, len(nums2) - 1, k1) + getKth(nums1, 0, len(nums1) - 1, nums2,
                                                                                        0,
                                                                                        len(nums2) - 1, k2)) / 2.0

if __name__ == '__main__':
    nums1 = [1, 3, 4, 9]
    nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(Solution().findMedianSortedArrays(nums1, nums2))
