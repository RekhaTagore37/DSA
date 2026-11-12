class Solution(object):
    def longestCommonPrefix(self, strs):
        strs.sort()
        ans=''
        left,right=strs[0],strs[-1]
        for i in range(min(len(left),len(right))):
            if left[i]==right[i]:
                ans+=left[i]
                i+=1
            else:
                break
        return ans
        
        