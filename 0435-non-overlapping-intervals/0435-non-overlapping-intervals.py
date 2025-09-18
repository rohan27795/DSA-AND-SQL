class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:x[1])
        count = 1
        last_end = intervals[0][1]
        #i = 1
        #n = len(intervals)

        for i in range(1,len(intervals)): #while i < n
            if intervals[i][0] >= last_end:
                count +=1
                last_end = intervals[i][1]
            #i +=1

        return len(intervals) - count  # instead of len(intervals) write n


        