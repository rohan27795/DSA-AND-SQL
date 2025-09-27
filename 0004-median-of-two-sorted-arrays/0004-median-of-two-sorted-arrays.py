class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #if len(nums1) > len(nums2):
           # nums1,nums2 = nums2,nums1
        n1,n2 = len(nums1),len(nums2)
        low = 0
        high = n1
        while low <= high:
            mid1 = (high+low) // 2
            mid2 = (n1+n2+1) //2 - mid1

            l1 = float('-inf') if mid1 == 0 else nums1[mid1-1]
            r1 = float('inf')  if mid1 == n1 else nums1[mid1]
            l2 = float('-inf') if mid2 == 0 else nums2[mid2-1]
            r2 = float('inf')  if mid2 == n2 else nums2[mid2]

            if l1 <= r2 and l2 <= r1:
                if (n1+n2) % 2 == 0:
                    return (max(l1,l2) + min(r1,r2)) / 2.0   #even
                else:
                    return max(l1,l2)                               #odd
            elif l1 > r2:
                high = mid1-1
            else:
                low = mid1+1

        return 0.0




            


        