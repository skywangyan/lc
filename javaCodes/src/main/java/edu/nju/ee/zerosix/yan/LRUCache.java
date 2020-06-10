package edu.nju.ee.zerosix.yan;

import java.util.HashMap;
import java.util.Map;
/*
* allocate a dummy head and a dummy tail for ease of operation, do not need to check boundaries anymore which is dirty work.
* */
public class LRUCache implements Solution {

    @Override
    public void run() {
        LRUCache cache = new LRUCache(2);
        System.out.println(cache.get(2));
        cache.put(2, 6);
        System.out.println(cache.get(1));
        cache.put(1, 5);
        cache.put(1, 2);
        System.out.println(cache.get(1));
        System.out.println(cache.get(2));
    }

    class ListNode {
        ListNode prev;
        ListNode next;
        int data;
        int key;
        public ListNode(int k, int i) {
            key = k;
            data = i;
        }
    }
    Map<Integer, ListNode> m = new HashMap<>();
    int currSize;
    int cacheCap;
    ListNode head;
    ListNode tail;

    public LRUCache(int capacity) {
        head = new ListNode(-1,-1);
        tail = new ListNode(-2, -2);
        cacheCap = capacity;
        currSize = 0;
        head.next = tail;
        tail.prev = head;
    }

    public void promote(ListNode curr) {
        curr.prev.next = curr.next;
        curr.next.prev = curr.prev;
        //add to head
        head.next.prev = curr;
        curr.next = head.next;
        head.next = curr;
        curr.prev = head;
    }
    public int get(int key) {
        if(m.containsKey(key)) {
            ListNode cur = m.get(key);
            promote(cur);
            return cur.data;
        } else {
            return -1;
        }
    }

    public void put(int key, int value) {
        if (m.containsKey(key)){
            ListNode curr = m.get(key);
            promote(curr);
            curr.data = value;

        } else {
            if (currSize < cacheCap) {
                ListNode newNode = new ListNode(key, value);
                head.next.prev = newNode;
                newNode.next = head.next;
                head.next = newNode;
                newNode.prev = head;
                m.put(key, head.next);
                currSize++;

            } else { //currsize >= cacheCap,full
                ListNode curr = new ListNode(key, value);
                ListNode toBeDel = tail.prev;
                //delete in map
                m.remove(toBeDel.key);
                //del in linkedlist
                toBeDel.prev.next = tail;
                tail.prev = toBeDel.prev;
                //add to head
                head.next.prev = curr;
                curr.next = head.next;
                head.next = curr;
                curr.prev = head;
                m.put(key,head.next);
            }
        }
    }
}
