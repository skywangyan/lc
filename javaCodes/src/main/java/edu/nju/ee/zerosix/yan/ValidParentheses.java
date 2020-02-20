package edu.nju.ee.zerosix.yan;
import java.util.Stack;
/*
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
 */
public class ValidParentheses implements Solution {
    @Override
    public void run() {
        System.out.println(isValid("{[]}"));
    }

    public boolean isValid(String s) {
        Stack<Character> st = new Stack();
        char prev;
        for(char ch: s.toCharArray()){
            switch (ch){
                case ')':
                    if(st.empty()) return false;
                    prev = st.pop();
                    if(prev != '(') return false;
                    break;
                case ']':
                    if(st.empty()) return false;
                    prev = st.pop();
                    if(prev != '[') return false;
                    break;
                case '}':
                    if(st.empty()) return false;
                    prev = st.pop();
                    if(prev != '{') return false;
                    break;
                default:
                    st.push(ch);
                    break;
            }
        }
        return st.empty();
    }
}
