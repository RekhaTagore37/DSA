class Solution(object):
    def sortColors(self, nums):
      zeroes=[]
      ones=[]
      twos=[]
      for i in nums:
        if i==0:
          zeroes.append(i)
        elif i==1:
          ones.append(i)
        else:
          if i==2:
            twos.append(i)
      nums[:]=zeroes+ones+twos
      return nums
