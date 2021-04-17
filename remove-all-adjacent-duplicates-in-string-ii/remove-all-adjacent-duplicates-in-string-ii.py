class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # sol - https://www.youtube.com/watch?v=Rq4-1LonjaQ&ab_channel=babybear4812
        i = 0
        stack = []
        S = list(s)
        for i in S:
            if len(stack) and stack[-1][0] == i and stack[-1][1] == k-1:
                stack.pop()
            elif len(stack) and stack[-1][0] == i:
                stack[-1][1] += 1
            else: stack.append([i,1])
        
        ans = ""
        for i in stack:
            for j in range(i[1]):
                ans+=i[0]
        return ans
        