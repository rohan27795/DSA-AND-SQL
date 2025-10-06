class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set(nums)
        longest = 0

        for n in numset:  # iterate over set instead of nums to avoid duplicates
            if n - 1 not in numset:  # start of a sequence
                curr = n
                length = 1
                while curr + 1 in numset:
                    curr += 1
                    length += 1
                longest = max(longest,length)

        return longest
        