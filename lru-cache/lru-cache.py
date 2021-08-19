# https://www.youtube.com/watch?v=NDpwj0VWz1U&ab_channel=NickWhite

class ListNode(object):
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """    
        # doubly linked list to store order of usage
        # head and tail are dummy nodes which dont actually represent anything
        self.head = ListNode()
        self.tail = ListNode()
        # to initialize an empty dll
        self.head.next = self.tail
        self.tail.prev = self.head

        # hashmap of listnodes
        self.map = {}
        self.capacity = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map: 
            node = self.map[key]
            res = node.val
            self.remove(node)
            self.add(node)
            return res
        
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # overriding the previous value of the node and moving it to the front of the dll
        if key in self.map:
            node = self.map[key]
            self.remove(node)
            node.val = value
            self.add(node)
        else:
            if len(self.map.keys()) == self.capacity:
                del self.map[self.tail.prev.key]
                self.remove(self.tail.prev)
            
            new_node = ListNode(key,value)
            self.map[key] = new_node
            self.add(new_node)
    
    def add(self, node):
        # add to the front of the list
        head_next = self.head.next
        self.head.next = node
        
        node.prev = self.head
        node.next = head_next
        head_next.prev = node

    def remove(self, node):
        # remove from the back of the list
        next_node = node.next
        prev_node = node.prev
        
        next_node.prev = prev_node
        prev_node.next = next_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)