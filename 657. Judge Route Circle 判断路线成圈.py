class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return (moves.count('R')==moves.count('L')and moves.count('U')==moves.count('D'))


if __name__=='__main__':
    ans=Solution
    print(ans.judgeCircle(ans,"UDRL"))