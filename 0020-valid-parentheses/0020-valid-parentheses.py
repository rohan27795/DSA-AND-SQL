class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        matching_bracket ={')':'(',']':'[','}':'{'}
        for char in s:
            if char in matching_bracket.values():
                stack.append(char)
            elif char in matching_bracket.keys():
                if stack == [] or matching_bracket[char] != stack.pop():
                    return False
        return len(stack)==0





        