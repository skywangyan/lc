class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        h = []
        head = curr = ListNode(0)
        for node in lists:
            if node:
                heapq.heappush(h, (node.val, node))
        while h:
            item = heapq.heappop(h)
            curr.next = item[1]
            if item[1].next:
                heapq.heappush(h, (item[1].next.val, item[1].next))
            curr = curr.next
        return head.next
