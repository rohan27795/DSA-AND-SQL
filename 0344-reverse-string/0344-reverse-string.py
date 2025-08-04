class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        stack = []

        for char in s:
            stack.append(char)

        for i in range(len(s)):
            s[i] = stack.pop()




