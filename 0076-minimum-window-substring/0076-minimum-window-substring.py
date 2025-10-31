class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """ 
        if not s or not t:
            return ""
        freqmap = {}
        for char in t:
            freqmap[char] = freqmap.get(char,0) +1
        
        count = len(freqmap)
        start = 0
        left = 0
        minlen = float('inf')
        ans = ""
        for right in range(len(s)):
            if s[right] in freqmap:
                freqmap[s[right]] -=1
                if freqmap[s[right]] == 0:
                    count -=1

            while count == 0:
                windowlen = right - left + 1
                if windowlen < minlen:
                    minlen = windowlen
                    ans = s[left:right+1]
        

                if s[left] in freqmap:
                    freqmap[s[left]] += 1
                    if freqmap[s[left]] > 0:
                         count += 1
                left += 1

        return ans

            

        
        


        
        