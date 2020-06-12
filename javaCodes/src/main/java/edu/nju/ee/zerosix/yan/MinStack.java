package edu.nju.ee.zerosix.yan;
/*
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:

Methods pop, top and getMin operations will always be called on non-empty stacks.
 */
import java.util.Stack;
public class MinStack implements Solution {
    Stack<Integer> s;
    Stack<Integer> smallest;
    @Override
    public void run() {
        this.push(-2);
        this.push(0);
        this.push(-3);
        System.out.println(this.getMin());
        this.pop();
        System.out.println(this.top());
        System.out.println(this.getMin());
    }
    /** initialize your data structure here. */
    public MinStack() {
        s = new Stack<>();
        smallest = new Stack<>();
    }

    public void push(int x) {
        s.push(x);
        if (smallest.empty()) {
            smallest.push(x);
        } else {
            smallest.push(x < smallest.peek() ? x : smallest.peek());
        }
    }

    public void pop() {
        smallest.pop();
        s.pop();
    }

    public int top() {
        return s.peek();
    }

    public int getMin() {
        return smallest.peek();
    }
}
