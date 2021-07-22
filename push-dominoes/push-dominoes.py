class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        # https://www.youtube.com/watch?v=Z2x-zalsebs&ab_channel=NickWhite
        
        forces = [0 for _ in range(len(dominoes))]
        force = 0
        
        # loop from left to right to account for right force
        for i in range(len(dominoes)):
            if dominoes[i] == 'R':
                force = len(dominoes)
            elif dominoes[i] == 'L':
                force = 0
            else:
                # after each domino is knocked down, the force decrements by one
                force = max(force-1, 0)
            # since the force is initially 0, this is the net positive force added to it
            forces[i] += force
        
        # loop from right to left to account for left force:
        for i in range(len(dominoes)-1,-1,-1):
            if dominoes[i] == 'L':
                force = len(dominoes)
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force-1,0)
            # since the right forces are already in the arr, the left force must be subtracted from it
            forces[i] -= force

        ans = ""
        for i in forces:
            if i > 0: ans+="R"
            elif i < 0: ans+="L"
            else: ans+="."
        
        return ans
            