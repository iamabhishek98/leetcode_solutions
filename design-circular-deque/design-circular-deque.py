class MyCircularDeque(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.size = k
        self.deque = [None]*k
        self.front = -1
        self.rear = -1
        

    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull(): return False
        
        if self.isEmpty():
            self.front = 0
            self.rear = 0
        # when front is at first position of queue
        elif self.front == 0:
            self.front = self.size - 1
        else:
            self.front = self.front - 1
        
        self.deque[self.front] = value
        
        return True
            

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull(): return False
        
        if self.isEmpty():
            self.front = 0
            self.rear = 0
        # when rear is at the end of the queue
        elif self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear += 1
        
        self.deque[self.rear] = value
        
        return True
    

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty(): return False
        
        # when queue has only one element
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        # when front is at last position of queue
        elif self.front == self.size - 1:
            self.front = 0
        else:
            self.front += 1
        
        return True

    
    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty(): return False

        # when queue has only one element
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        # when rear is at the front of the queue
        elif self.rear == 0:
            self.rear = self.size - 1
        else:
            self.rear -= 1
        
        return True
    
    
    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty(): return -1
        return self.deque[self.front]
     
        
    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty(): return -1
        return self.deque[self.rear]

    
    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.front == -1
        

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        return (self.front == 0 and self.rear == self.size - 1) or (self.front == self.rear + 1)
    

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()