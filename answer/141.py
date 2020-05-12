# 给定一个链表，判断链表中是否有环。
"""
给定一个链表，判断链表中是否有环。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 快慢指针解法,如果有环，早晚会相遇。如果有尾结点，那就没环
        p = head
        q = head
        while p:
            if p.next:
                p = p.next.next
                q = q.next
            else:
                return False
            if p is q:
                return True
        return False
