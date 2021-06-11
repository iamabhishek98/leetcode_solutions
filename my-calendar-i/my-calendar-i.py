class MyCalendar(object):

    def __init__(self):
        self.arr = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for i in self.arr:
            # ()[] []()
            if not (start<=i[0] and end<=i[0] or start>=i[1]): return False
        self.arr.append([start,end])
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)