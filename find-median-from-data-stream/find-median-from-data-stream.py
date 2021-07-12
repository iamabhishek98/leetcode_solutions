class MedianFinder(object):
    # https://leetcode.com/problems/find-median-from-data-stream/discuss/1330808/Python-2-heaps-solution-explained
    def __init__(self):
        """
        initialize your data structure here.
        """
        # small is max heap while large is min heap
        self.small, self.large = [],[]

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # always add number to small pq
        # num is negative to keep descending order (heap is by default min heap)
        heappush(self.small, -num)
        # pop largest element from small pq and add to large pq 
        # to make sure elements in small pq are always smaller than large pq
        largest = heappop(self.small)
        heappush(self.large, -largest)
        
        # we need to make sure size of small pq >= large pq 
        # because if the len of list is odd, the median comes from small pq, 
        # so if the size of small pq gets smaller, we take the smallest element 
        # in the large pq and add it to the small pq
        if len(self.small)<len(self.large):
            smallest = heappop(self.large)
            heappush(self.small, -smallest)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small)!=len(self.large): return -self.small[0]
        # dividing 2.0 to do float division
        else: return (-self.small[0]+self.large[0])/2.0 
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()