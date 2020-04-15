package edu.nju.ee.zerosix.yan;
import java.util.Comparator;
import java.util.List;
import java.util.PriorityQueue;
/*
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

        Example:

        Input:
        [
        1->4->5,
        1->3->4,
        2->6
        ]
        Output: 1->1->2->3->4->4->5->6
 */
public class MergeKSortedList implements Solution{
    @Override
    public void run(){
        ListNode n1 = new ListNode(1);
        ListNode n2 = new ListNode(4);
        ListNode n3 = new ListNode(5);
        n1.next = n2;
        n2.next = n3;

        ListNode n4 = new ListNode(1);
        ListNode n5 = new ListNode(3);
        ListNode n6 = new ListNode(4);
        n4.next = n5;
        n5.next = n6;

        ListNode n7 = new ListNode(2);
        ListNode n8 = new ListNode(6);
        n7.next = n8;

        ListNode head = mergeKLists(new ListNode[]{n1,n4,n8});

        ListNode currNode = head;
        while(currNode != null) {
            System.out.println(currNode.val);
            currNode = currNode.next;
        }
    }


    public class ListNode {
         int val;
         ListNode next;
         ListNode(int x) { val = x; }
    }

    public ListNode mergeKLists(ListNode[] lists) {
        Comparator<ListNode> cmp = new Comparator<ListNode>() {
            @Override
            public int compare(ListNode listNode, ListNode t1) {
                return listNode.val - t1.val;
            }
        };

        PriorityQueue<ListNode> heap = new PriorityQueue<ListNode>(cmp);
        ListNode dummy = new ListNode(-1);
        ListNode curr = dummy;
        for(ListNode headNode: lists) {
            if (headNode != null) {
                heap.add(headNode);
            }
        }
        while(!heap.isEmpty()){
            curr.next = heap.poll();
            curr = curr.next;
            if (curr.next != null) {
                heap.add(curr.next);
            }
        }
        return dummy.next;
    }
}
