class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.permutehelper(nums, 0, result)
        return result

    def permutehelper(self,nums,start,result):
        if start == len(nums) -1:
            result.append(nums[:])
            return 

        used = set()

        for i in range(start,len(nums[:])):
            if nums[i] in used:
                continue
            used.add(nums[i])

            nums[start],nums[i] = nums[i],nums[start] #swap

            self.permutehelper(nums,start+1,result)
            
            nums[start],nums[i] = nums[i],nums[start] #racktract

            
            

        