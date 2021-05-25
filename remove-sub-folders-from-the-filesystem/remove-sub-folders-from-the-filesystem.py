class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        folder.sort()
        s = set()
        for i in folder:
            arr = i.split("/")
            if len(arr)>1:
                key = ""
                status = True
                for j in range(1,len(arr)):
                    key+="/"
                    key += arr[j]
                    if key in s: 
                        status = False
                        break
                if status: s.add(i)
        return list(s)
                    
                    