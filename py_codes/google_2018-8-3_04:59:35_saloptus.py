#!/usr/bin/python
# -*- coding: utf-8 -*-
# 第一轮：1. insert a number in ordered array. 应该是 利口伞舞 变形，有duplicates。binary search解决。. 1point 3acres 论坛
# 2. find the center of mass in a 2D array. 就是找出数字左边sum和右边sum相差最小的那个position。dp解决。
# 第二轮： delete a node from a doubly linked list. 注意各种边界条件。
# 第三轮：设计电梯系统，有若干个电梯，讨论了一些OOdesign和key methods，最后让实现find_best_elevator。
# 第四轮：stock price update，给定的是一系列的entries：symbol(stock_name), price, time_of_price. 自己设计class和数据结构，要求可以query到任何一只股票的max_price, min_price和latest_price. 注意后加入的同一只股票的time_of_price可能比先加入的时间更早，time_of_price不是entry_time。后加进来的同一只股票也可能同样时间不同price，这时认为是更改覆盖前面同样时间的entry。
# 第五轮：给定一个Quack class。基本上就是一个a stack or queue，已经按升序排好， .pop() will randomly pop from head or tail of this data structure. 要求返利用这个.pop()，返回降序排列的array。

round 5: use a stack as a buffer, as long as there is number smaller than the previous one, pop previous element, it must be the largest, put it into the response array.
