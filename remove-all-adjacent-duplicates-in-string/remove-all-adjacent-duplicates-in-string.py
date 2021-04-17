class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        i = 0
        stack = []
        for i in S:
            if not len(stack) or stack[-1] != i: stack.append(i)
            else:
                while len(stack) and stack[-1] == i:
                    stack.pop()
        return ''.join(stack)