package edu.nju.ee.zerosix.yan;

import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.util.*;

@SpringBootApplication
public class LeetCodePros {
    public static void main(String[] args) {
        System.out.println("happy coding Yan!");
        LinkedList<String> ls = new LinkedList<>(Arrays.asList("a a a a a a a","a a a a a aa","a a a a aa a","a a a aa a a","a aa a a aa","a a a aaaa","a a aa a a a","aa a a a aa","a a aa aa a","a a aaaa a","a aa a a a a","aa a a a aa","a a aa aa a","aa a aa a a","aa aa a aa","a aa aaaa","a aaaa a a","aaaa a aa","aa a a a a a","aa a a a aa","a a aa aa a","aa a aa a a","aa aa a aa","a aa aaaa","aa aa a a a","aa aa a aa","aa aa aa a","aa aaaa a","aaaa a a a","aaaa a aa","aaaa aa a"));
        LinkedList<String> ls2 = new LinkedList<>(Arrays.asList("a a a a a a a","aa a a a a a","a aa a a a a","a a aa a a a","aa aa a a a","aaaa a a a","a a a aa a a","aa a aa a a","a aa aa a a","a aaaa a a","a a a a aa a","aa a a aa a","a aa a aa a","a a aa aa a","aa aa aa a","aaaa aa a","a a aaaa a","aa aaaa a","a a a a a aa","aa a a a aa","a aa a a aa","a a aa a aa","aa aa a aa","aaaa a aa","a a a aa aa","aa a aa aa","a aa aa aa","a aaaa aa","a a a aaaa","aa a aaaa","a aa aaaa"));
        System.out.println(ls.size() + " " + ls2.size());
        System.out.println(ls == ls2);
        Collections.sort(ls2);
        System.out.println(ls2);
        System.out.println(ls == ls2);
        Set<String> hs1 = new HashSet<>(ls);
        Set<String> hs2 = new HashSet<>(ls2);
        System.out.println(hs1.size() + " " + hs2.size());
        System.out.println(hs1 == hs2);
    }
}
