class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        return "al".join(("o".join(command.split("()"))).split("(al)"))