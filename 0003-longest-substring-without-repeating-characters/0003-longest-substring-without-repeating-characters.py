class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = 0
        j = 0
        max_len = 0
        freq = {}
        
        while j<n:
            freq[s[j]] = freq.get(s[j],0) +1
            
            if len(freq) == j-i+1:
                max_len = max(max_len,j-i+1)
                j +=1

            else: 
                while len(freq) < j-i+1:
                    freq[s[i]] -=1

                    if freq[s[i]] == 0:
                        del freq[s[i]]
                    i +=1
                j +=1
        
        return max_len





        