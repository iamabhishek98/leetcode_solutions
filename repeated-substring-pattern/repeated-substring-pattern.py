class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hashset = set()
        curr = ""
        for i in range(len(s)//2):
            curr += s[i]
            if len(s)%(i+1) == 0:
                hashset.add(curr)

        for i in hashset:
            a = 0
            status = True
            for j in range(len(s)/len(i)):
                b = 0
                for b in i:
                    if s[a] != b: 
                        status = False
                        break
                    a += 1
                if not status: break
            if status: return True
        return False