class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        l = 0
        r = len(letters)-1 
        m = "{"
        while l<=r:
            mid = (l+r)/2
            if letters[mid]>target:
                m = min(m,letters[mid])
                r = mid-1
            else:
                l = mid+1
        if m == "{":
            l = 0
            r = len(letters)-1 
            while l<=r:
                mid = (l+r)/2
                if letters[mid]>upper(target):
                    m = min(m,letters[mid])
                    r = mid-1
                else:
                    l = mid+1
        return m