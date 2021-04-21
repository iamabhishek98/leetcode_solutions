class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.i = 0
        self.arr = [None]*n
        
    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.arr[idKey-1] = value
        ans = []
        while self.i < len(self.arr) and self.arr[self.i] is not None:
            ans.append(self.arr[self.i])
            self.i+=1
        return ans
        
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)