class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed = set(list(allowed))
        
        count = 0
        for word in words:
            status = True
            for i in word:
                if i not in allowed:
                    status = False
                    break
            if status:
                count += 1
        
        return count