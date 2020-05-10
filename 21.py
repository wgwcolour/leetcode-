# 合并两个有序链表

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 递归法
    # 只关注一层的逻辑：每次找到比较小的值，把小的拿出来放到前面，至于后面的，继续递归处理
    # 输出逻辑：如果l1还存在，那么就相当于还应该继续递归，这时候就返回l1(因为l1是比较小的值)，如果l1不存在了,说明递归结束，返回
    # 剩余的有序l2
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val: l1,l2 = l2,l1
            l1.next = self.mergeTwoLists(l1.next,l2)
        return l1 or l2

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        ps = ListNode(0)
        p = ps
        while l1 or l2:
            if l1 and l2:
                a1 = l1.val
                a2 = l2.val
                if a1 < a2:
                    p.next = ListNode(a1)
                    l1 = l1.next
                else:
                    p.next = ListNode(a2)
                    l2 = l2.next
            elif l1:
                p.next = l1
                break
            elif l2:
                p.next = l2
                break
            p = p.next
        return ps.next
