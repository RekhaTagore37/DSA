class Solution(object):
    def sortedSquares(self, nums):
        nums[:]=list(map(lambda x:x**2,nums))
        nums.sort()
        return nums
        