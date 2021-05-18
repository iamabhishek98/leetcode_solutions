def check(curr, nxt):
    if len(nxt) != len(curr)+1: return False
    i = 0
    j = 0
    diff = 0
    while i < len(curr) and j < len(nxt):
        if curr[i] == nxt[j]:
            i+=1
            j+=1
        else:
            if diff==1: return False
            j+=1
            diff+=1
    return True

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        len_map = {}
        self.dp = {}
        def recurse(curr, chain_len):
            key = str(curr)+":"+str(chain_len)
            if key in self.dp: return self.dp[key]
            l = len(curr)
            if l+1 not in len_map: return chain_len
            m = chain_len
            for nxt in len_map[l+1]:
                if check(curr, nxt):
                    m = max(m, recurse(nxt, chain_len+1))
            self.dp[key] = m
            return m
        
        for i in words:
            l = len(i)
            if l not in len_map: len_map[l] = [i]
            else: len_map[l].append(i)
        
        
        m = 1
        for c in len_map:
            for word in len_map[c]:
                m = max(m, recurse(word, 1))
                if m == 3: print word
                
        return m
        