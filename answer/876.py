
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # 使用快慢指针即可
        p = head
        q = head
        while p:
            if p.next:
                p = p.next.next
                q = q.next
            # 搞不懂为什么这里一定要加else，按说p is None以后不应该进到循环里了，但是leetcode必须加上才能跑通
            else:
                break

        return q