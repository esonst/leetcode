class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if A==[]:
            return A
        for index in A:
            index.reverse()
            for i in range(len(index)):
                index[i]=1-index[i]
        return A
if __name__=='__main__':
    ans=Solution
    print(ans.flipAndInvertImage(ans,[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))