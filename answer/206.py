# 反转链表
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = None
        while head:
            # tmp = ListNode(head.val)
            # tmp.next = head.next
            # 不使用上边这两行不应该内存降低点吗？不太懂为什么都是14.6MB
            tmp = head.next  # 给tmp赋值为下一个结点
            head.next = new_head  # 把head的next结点赋值为new_head（新链表）
            new_head = head  # 更新new_head链表，方便下次循环到这里的时候把更新后的新链表放到head的后面再次更新
            head = tmp  # 更新head为下一个结点，直到下一个结点为None的时候就跳出循环了
        return new_head

