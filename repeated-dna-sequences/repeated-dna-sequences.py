class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)<10: return []
        
        char = { 'A':0,'C':1,'G':2,'T':3 }
        
        existing_hash = set()
        repeated_str = set()
        
        hash_val = 0
        base = 4
        shift_hash = pow(base,9)
        
        for i in range(10):
            hash_val = hash_val*base+char[s[i]]
            
        existing_hash.add(hash_val)
        
        for i in range(10, len(s)):
            hash_val -= char[s[i-10]]*shift_hash
            hash_val = hash_val*base+char[s[i]]
            
            if hash_val in existing_hash: repeated_str.add(s[i-9:i+1])
            else: existing_hash.add(hash_val)
        
        return repeated_str