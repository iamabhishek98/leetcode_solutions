# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

# https://www.youtube.com/watch?v=PtJ6APpEhOU&ab_channel=TimothyHChang
from collections import deque

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def flatten(li = nestedList):
            curr_li = []
            for i in li:
                if i.isInteger():
                    curr_li.append(i)
                else:
                    curr_li.extend(flatten(i.getList()))
            return curr_li
        
        self.n = deque(flatten())

    def next(self):
        """
        :rtype: int
        """
        return self.n.popleft()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.n)
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())