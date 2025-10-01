class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j,k = i+1 , n-1
            while j<k:
                currentsum = nums[i] + nums[j] + nums[k]
                if currentsum > 0:
                    k -=1
                elif currentsum < 0:
                    j +=1
                else:
                    res.append([nums[i],nums[j],nums[k]])

                    while j < k and nums[j] == nums[j+1]:
                        j +=1
                    while j < k and nums[k] == nums[k-1]:
                        k -=1
                    j +=1
                    k -=1
        return res
            


        



