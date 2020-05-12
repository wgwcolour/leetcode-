# 反转链表
"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
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

