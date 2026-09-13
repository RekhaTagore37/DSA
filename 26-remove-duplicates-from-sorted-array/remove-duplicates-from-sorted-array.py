class Solution(object):
    def removeDuplicates(self, nums):
        k = []

        for i in nums:
            if i not in k:
                k.append(i)

        nums[:] = k

        return len(k)
        
             

                


            


        