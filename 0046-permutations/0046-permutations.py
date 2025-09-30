class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def getpermute(idx):
            if idx == len(nums):
                res.append(nums[:])
                return 

            for i in range(idx,len(nums)):
                nums[i],nums[idx] = nums[idx],nums[i] #swap
                getpermute(idx + 1)             #recursion
                nums[i],nums[idx] = nums[idx],nums[i] #backtrack

        getpermute(0)
        return res
             




        

            
            

        