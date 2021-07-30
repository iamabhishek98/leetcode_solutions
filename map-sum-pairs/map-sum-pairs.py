class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.prefix_map = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        existing = -1
        if key in self.map:
            existing = self.map[key]
        
        s = ""
        for i in key:
            s += i
            if existing != -1: self.prefix_map[s] -= existing 
            if s in self.prefix_map: self.prefix_map[s] += val
            else: self.prefix_map[s] = val
                
        self.map[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        if prefix in self.prefix_map: return self.prefix_map[prefix]
        return 0
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)