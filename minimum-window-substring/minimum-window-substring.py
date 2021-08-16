from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_map = Counter(t)
        required = len(t_map.keys())
        
        formed = 0
        curr_window = {}
        min_size = sys.maxint
        min_i = min_j = 0
        
        
        i = 0
        j = 0
        while j < len(s):
            c = s[j]
            curr_window[c] = curr_window.get(c, 0) + 1
            
            if c in t_map and t_map[c] == curr_window[c]:
                formed += 1
                
            while i <= j and formed == required:
                c = s[i]
                
                if j - i + 1 < min_size:
                    min_size = j - i + 1
                    min_i = i
                    min_j = j
                
                curr_window[c] -= 1
                if curr_window[c] < t_map[c]:
                    formed -= 1
                    
                i += 1
            
            j += 1
        
        if min_size != sys.maxint:
            return s[min_i:min_j+1]
        
        return ""
                    
                
        