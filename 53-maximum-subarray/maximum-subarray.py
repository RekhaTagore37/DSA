class Solution(object):
    def maxSubArray(self, nums):
        m=nums[0]
        count=0
        for i in nums:
            count=max(i,count+i)
            m=max(m,count)
        return m
        