class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph.lower()
        para=paragraph.split(' ')
        for str in banned:
            para.remove(str)
        para.sort()
        index=[0]*len(para)
        for str in para:

if __name__=="__main__":
    s=Solution
    s.mostCommonWord()
