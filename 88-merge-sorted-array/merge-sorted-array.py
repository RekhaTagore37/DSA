class Solution(object):
    def merge(self, nums1, m, nums2, n):
       n1=nums1[:m]
       n2=nums2[:n]
       nums1[:]=n1+n2
       nums1.sort()
       return nums1