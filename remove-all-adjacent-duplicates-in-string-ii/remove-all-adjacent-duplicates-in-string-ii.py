class Solution(object):
    def removeDuplicates(self, S, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(S)
        stack = []
        
        for i in s:
            if stack and stack[-1][0] == i:
                if stack[-1][1] == k - 1:
                    stack.pop()
                else:
                    stack[-1][1] += 1
            else:
                stack.append([i,1])
        
        return "".join([i[0]*i[1] for i in stack])
        