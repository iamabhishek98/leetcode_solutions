from collections import Counter

class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        m = Counter(sentence)
        a = Counter("thequickbrownfoxjumpsoverthelazydog")
        count = 0
        for i in a:
            if i in m: count += 1
        return count == 26
        