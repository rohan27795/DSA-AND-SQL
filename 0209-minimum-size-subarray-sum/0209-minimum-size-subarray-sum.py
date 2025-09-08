class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        sum_ = 0
        minimum = float("inf")

        n = len(nums)
    
        while j < n:
            sum_ += nums[j]

            while sum_ >= target:  # shrink whenever valid
                minimum = min(minimum, j - i + 1) #size of window
                sum_ -= nums[i]
                i += 1

            j += 1

        return 0 if minimum == float("inf") else minimum

        