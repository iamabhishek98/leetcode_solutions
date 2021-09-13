class ListNode(object):
    def __init__(self, key = None, val = None, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.BUCKET_SIZE = 100
        
        self.buckets = [ListNode() for _ in range(self.BUCKET_SIZE)]
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        index = key % self.BUCKET_SIZE
        
        head = self.buckets[index]
        
        while head.next:
            if head.key == key: 
                head.val = value
                return
            head = head.next
        
        if head.key == key: 
            head.val = value
            return
        
        head.next = ListNode(key, value)
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key % self.BUCKET_SIZE
        
        head = self.buckets[index]
        
        while head:
            if head.key == key:
                return head.val
            head = head.next
        
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        index = key % self.BUCKET_SIZE
        
        head = self.buckets[index]
        
        while head:
            if head.key == key:
                if head.next:
                    head.key = head.next.key
                    head.val = head.next.val
                    head.next = head.next.next
                else:
                    head.key = None
                    head.val = None
                    head.next = None
                return
            head = head.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)