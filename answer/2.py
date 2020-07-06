"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 满10进1，千万不要忘了最后一位也要满10进1
        add = 0
        l = ListNode(0)
        ll = l
        while l1 or l2:
            one = l1.val if l1 else 0
            two = l2.val if l2 else 0
            if (one+two + add) % 10 == (one+two + add):
               this = one+two + add
               add = 0
            else:
                this = (one+two + add) % 10
                add = 1
            l.next = ListNode(this)
            l = l.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if add:
            l.next = ListNode(1)
        return ll.next

if __name__ == '__main__':
    l1 = ListNode(5)
    l2 = ListNode(5)
    Solution().addTwoNumbers(l1,l2)