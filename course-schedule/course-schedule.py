class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # https://www.youtube.com/watch?v=kXy0ABd1vwo&ab_channel=TECHDOSE
        
        courseMap = {}
        self.visited = [0 for i in range(numCourses)]
        # 0 - not visited, 1 - processing, 2 - visited
        
        def detectCycle(i):
            if self.visited[i] == 1: return True
            self.visited[i] = 1
            if i in courseMap:
                for j in courseMap[i]: 
                    if self.visited[j] != 2 and detectCycle(j): return True
            self.visited[i] = 2
            return False
            
        for i in prerequisites:
            if i[0] not in courseMap: 
                courseMap[i[0]] = set()
                courseMap[i[0]].add(i[1])
            else: courseMap[i[0]].add(i[1])
        for i in range(numCourses):
            if self.visited[i] == 0 and detectCycle(i): return False
        return True