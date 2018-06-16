class Solution2:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        index = 0
        i = 0
        dir = 1
        word = [''] * numRows
        for x in s:
            word[i] += x
            if i >= numRows - 1:
                dir = -1
            if i == 0:
                dir = 1
            i += dir
        return ''.join(word)
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if(s==''):
            return s
        if(numRows==1):
            return s
        ans=""
        for i in range(numRows):
            if(i==0):
                ans+=(s[::numRows*2-2])
                pass
            elif(i==numRows-1):
                ans+=(s[numRows-1::numRows*2-2])
                pass
            else:
                flag=0
                j=i
                while(j<len(s)):
                    ans+=s[j]
                    flag+=1
                    if(flag%2):
                        j+=(numRows-i-1)*2
                    else:
                        j+=i*2
                #up-loop
        return ''.join(ans)


if __name__=='__main__':
    ss=Solution2
    print(ss.convert(ss,"PAYPALISHIRING",4))