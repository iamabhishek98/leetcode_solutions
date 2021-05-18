class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        m = {}
        for path in paths:
            contents = path.split()
            dir = contents[0]
            for i in range(1,len(contents)):
                a = contents[i].split('txt(')
                key = a[1][0:len(a[1])-1]
                if key in m: m[key].append(dir+"/"+a[0]+"txt")
                else: m[key] = [(dir+"/"+a[0]+"txt")]
        arr = []
        for i in m:
            if len(m[i])>1:
                arr.append(m[i])
        return arr