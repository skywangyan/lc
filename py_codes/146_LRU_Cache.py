'''
Design and implement a data structure for Least Recently Used (LRU) cache. 
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should 
invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''

class Node(object):
    def __init__(self, v, key):
        self.val = v   
        self.prev = None
        self.next = None
        self.key = key
    
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.dict = {}
        self.head = None
        self.tail = None
        self.num = 0
        
    def promote(self,key):
        if self.num == 1:
            return
        node = self.dict[key]
        if node == self.head:
            self.head = node.next
            self.head.prev = None
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        elif node != self.tail:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            self.promote(key)
            return self.tail.val
        else:
            return -1
            

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dict:
            self.promote(key)
            self.tail.val = value
            return
        elif self.num >= self.cap: 
            del self.dict[self.head.key]
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else :
                self.tail = None
            self.num -= 1
            
        self.dict[key] = Node(value, key)
        self.num += 1
        if not self.tail:
            self.head = self.tail = self.dict[key]
        else:
            self.tail.next = self.dict[key]
            self.dict[key].prev = self.tail
            self.tail = self.dict[key]

cache = LRUCache(2) 

cache.put(2, 1)
cache.put(2,2)
print cache.get(2)   
cache.put(1,1)
cache.put(4,1)
print cache.get(2);  

