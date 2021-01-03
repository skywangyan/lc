package edu.nju.ee.zerosix.yan;
/*
 Implement an iterator over a binary search tree (BST). Your iterator will be
 initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.



Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false


Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory,
where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at
 least a next smallest number in the BST when next() is called.
 */
/*
 * Definition for a binary tree node.
 */

import java.util.Stack;

class BSTIterator {
    Stack<TreeNode> st = new Stack<>();
    public BSTIterator(TreeNode root) {
        TreeNode curr = root;
        while(curr != null) {
            st.push(curr);
            curr = curr.left;
        }
    }

    /** @return the next smallest number */
    public int next() {
        TreeNode ret = st.pop();
        TreeNode curr = ret.right;
        while(curr != null){
            st.push(curr);
            curr = curr.left;
        }
        return  ret.val;
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !st.isEmpty();
    }
}

public class BinarySearchTreeIterator implements Solution {
    @Override
    public void run() {
        TreeNode n1 = new TreeNode(1);
        TreeNode n2 = new TreeNode(5);
        n1.right = new TreeNode(3);
        TreeNode root = new TreeNode(4);
        root.left = n1;
        root.right = n2;
        BSTIterator bstIt = new BSTIterator(root);
        while (bstIt.hasNext()){
            System.out.println(bstIt.next());
        }
    }
}
