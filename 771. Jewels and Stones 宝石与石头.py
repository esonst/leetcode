"""
 给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。

J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。

示例 1:

输入: J = "aA", S = "aAAbbbb"
输出: 3
示例 2:

输入: J = "z", S = "ZZ"
输出: 0
"""
class Solution:
    """
    利用基数排序解决
    """
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        if J=='' or S=='':
            return 0
        num=0
        index=[0]*100
        for i in J:
            index[ord(i)-ord('A')]+=1
        for s in S:
            if(index[ord(s)-ord('A')]==1):
                num+=1
        return num
if __name__=='__main__':
    ans=Solution
    ans.numJewelsInStones(self=ans,J = "z", S = "ZZ")