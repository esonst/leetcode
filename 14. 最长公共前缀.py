class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs)==0 or strs[0]==''):
            return ''
        if(len(strs)==1):
            return strs[0][0]
        num=len(strs[0])
        for str in strs:
            num=len(str) if(num>len(str)) else num
        for i in range(num):
            for j in range(len(strs))[:len(strs)-1]:
                if(strs[j][i]!=strs[j+1][i]):
                    return strs[0][0:i]
        return strs[0][0:num]
if __name__=='__main__':
    ss=Solution
    print(ss.longestCommonPrefix(ss,["flower","flow","flight"]))