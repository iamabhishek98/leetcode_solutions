class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        def isVowel(s):
            return s in set(["a","e","i","o","u"])
        
        curr_count = 0
        
        # first substring
        for x in range(k):
            curr_count += isVowel(s[x])
        
        max_count = curr_count
        i = 0
        j = k
        
        # sliding window for rest of substrings
        while j < len(s):
            j += 1
            # slide window by 1
            # remove first character vowel count while adding new character vowel count
            curr_count += (isVowel(s[j - 1]) - isVowel(s[i]))
            i += 1
            max_count = max(max_count, curr_count)
        
        return max_count