class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        if(len(nums)<3):
            return ans
        nums.sort()
        for i in range(len(nums)-2):
            if i==0 or nums[i]>nums[i-1]:
                head = i + 1
                rear = len(nums) - 1
                while head<rear:
                    if(nums[head]+nums[rear]+nums[i]==0):
                        ans.append([nums[i],nums[head],nums[rear]])
                        head+=1
                        rear-=1
                        while(head<rear and nums[head]==nums[head-1]):
                            head+=1
                        while(head<rear and nums[rear]==nums[rear+1]):
                            rear-=1
                    elif(nums[head]+nums[rear]+nums[i]>0):
                        rear-=1
                    else:
                        head+=1

        return ans


if __name__=='__main__':
    print(Solution.threeSum(Solution,[-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))