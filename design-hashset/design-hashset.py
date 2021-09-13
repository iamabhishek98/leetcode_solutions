class ListNode():
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class MyHashSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.MAX_VALUE = 10**6
        self.BUCKET_SIZE = 1000
        
        self.buckets = [ListNode() for _ in range(self.BUCKET_SIZE)]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % self.BUCKET_SIZE
        
        head = self.buckets[index]
        
        while head.next:
            if head.val == key: return
            head = head.next
        
        if head.val == key: return
        
        head.next = ListNode(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        index = key % self.BUCKET_SIZE
        
        head = self.buckets[index]
        
        while head:
            if head.val == key:
                if head.next:
                    head.val = head.next.val
                    head.next = head.next.next
                else:
                    head.val = None
                    head.next = None
                return
            head = head.next

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        index = key % self.BUCKET_SIZE
        
        head = self.buckets[index]
        
        while head:
            if head.val == key: return True
            head = head.next
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)