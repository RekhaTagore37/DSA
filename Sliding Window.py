class Solution(object):
  def slidingwindow(self,nums,k):
    curr_sum=sum(nums[:k])
    max_sum=curr_sum
    for i in range(k,len(nums)):
      curr_sum=currsum-nums[i-k]+nums[i]
      max_sum=max(max_sum,curr_sum)
    return float(max_sum)
