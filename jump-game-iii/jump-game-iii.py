class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        self.visited = [0 for i in range(len(arr))]
        self.dp = {}
        def dfs(i):
            if i in self.dp: return self.dp[i]
            if i<0 or i>=len(arr) or self.visited[i]: return False
            if arr[i] == 0: return True
            self.visited[i] = 1
            a = dfs(i+arr[i])
            b = dfs(i-arr[i])
            self.dp[i] = a or b
            return self.dp[i]
        return dfs(start)