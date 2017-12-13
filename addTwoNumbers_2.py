from utils import logger

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumber(self, l1, l2):
        flag = 0
        Dummy = curr = ListNode(0)
        while l1 or l2:
            addition = ((l1.val if l1 else 0) + (l2.val if l2 else 0) + flag)
            temp = addition % 10
            flag = addition / 10
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
            curr.next = ListNode(temp)
            curr = curr.next

        if flag:
            curr.next = ListNode(flag)
        return Dummy.next

if __name__ == "__main__":
    ins = Solution()
    l1 = ListNode(5)
    l1.next = ListNode(6)
    l2 = ListNode(7)
    l2.next = ListNode(7)
    head =  ins.addTwoNumber(l1, l2)
    while head:
        print head.val
        head = head.next
