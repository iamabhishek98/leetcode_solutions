class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def check(word):
            m1, m2 = {}, {}
            if len(word) != len(pattern): return False
            for i in range(len(word)):
                if word[i] not in m1: m1[word[i]] = pattern[i]
                if pattern[i] not in m2: m2[pattern[i]] = word[i]
                if (word[i], pattern[i]) != (m2[pattern[i]], m1[word[i]]): return False
            return True
        
        return filter(check, words)