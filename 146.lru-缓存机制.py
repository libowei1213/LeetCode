#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

# @lc code=start

class Node:
    def __init__(self,key=0,value=0):
        self.key = key
        self.val = value
        self.pre = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):

        dummyHead = Node()
        dummyTail = Node()

        self.size = 0

        self.head = dummyHead
        self.tail = dummyTail

        self.head.next = self.tail
        self.tail.pre = self.head

        self.hashmap = {}
        self.capacity = capacity


    def move_to_tail(self,node):

        node.pre.next = node.next
        node.next.pre = node.pre

        node.pre = self.tail.pre
        node.next = self.tail

        self.tail.pre.next = node
        self.tail.pre = node


    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        
        node = self.hashmap[key]

        self.move_to_tail(node)

        return node.val


    def put(self, key: int, value: int) -> None:
        
        if key not in self.hashmap:
            
            node = Node(key,value)
            
            node.pre = self.tail.pre
            node.next = self.tail

            self.tail.pre.next = node
            self.tail.pre = node

            self.hashmap[key] = node

            self.size+=1

            if self.size>self.capacity:
                node = self.head.next
                del self.hashmap[node.key]
                self.size-=1

                self.head.next = self.head.next.next
                node.next.pre = self.head
                node = None

        else:

            node = self.hashmap[key]
            node.val = value
            self.move_to_tail(node)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

