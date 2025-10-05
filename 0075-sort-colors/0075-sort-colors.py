class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        mid = 0
        low = 0
        high = len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[mid],nums[low] = nums[low],nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid],nums[high] = nums[high],nums[mid]
                high -= 1



                
        