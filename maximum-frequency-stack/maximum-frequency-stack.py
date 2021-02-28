import operator

class FreqStack(object):

    def __init__(self):
        self.freq_m = {}
        self.arr_m = {}
        self.max_f = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x not in self.freq_m: self.freq_m[x] = 0
        f = self.freq_m[x] + 1
        self.freq_m[x] = f
        if f not in self.arr_m: self.arr_m[f] = []
        self.arr_m[f].append(x)
        if f > self.max_f:
            self.max_f = f

    def pop(self):
        """
        :rtype: int
        """
        x = self.arr_m[self.max_f].pop()
        if not len(self.arr_m[self.max_f]):
            self.max_f -= 1
        self.freq_m[x] -= 1
        return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()