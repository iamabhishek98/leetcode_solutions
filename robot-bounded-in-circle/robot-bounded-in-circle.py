class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        # direction vector for facing north initially
        d = [0,1]
        
        # start position
        i = 0
        j = 0
        for instr in instructions:
            if instr == 'G':
                i += d[0]
                j += d[1]
            
            # changing signs because the direction is being switched so going straight should be relative to that axis
            elif instr == 'L':
                d = [-d[1],d[0]]
            elif instr == 'R':
                d = [d[1],-d[0]]

        # has to be either start position 
        # or any other position after from facing north 
        # (because that means the robot is not turning in any direction so there will never be a cycle)
        return (i == 0 and j == 0) or d != [0,1]