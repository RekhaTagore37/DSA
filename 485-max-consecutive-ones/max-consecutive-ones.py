class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        x=0
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                x=max(x,count)
            else:
                if nums[i]==0:
                    count=0
        return x

        