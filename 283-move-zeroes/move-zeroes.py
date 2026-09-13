class Solution(object):
    def moveZeroes(self, nums):
        zeroes=[]
        nonzeroes=[]
        for i in nums:
            if i==0:
                zeroes.append(i)
            else:
                nonzeroes.append(i)
        nums[:]=nonzeroes+zeroes
        return nums
        