from collections import deque

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        self.curr_len = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.curr_len+=1
        self.q2.append(x)
        while(len(self.q1)):
            self.q2.append(self.q1[0])
            self.q1.popleft()
        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if (not len(self.q1)): return
        temp = self.q1[0]
        self.q1.popleft()
        self.curr_len-=1
        return temp
        
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if (not len(self.q1)): return -1
        return self.q1[0]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return (self.curr_len) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()