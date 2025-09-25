class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return[]
        res = []
        maping = {"2":"abc",
                  "3":"def",
                  "4":"ghi",
                  "5":"jkl",
                  "6":"mno",
                  "7":"pqrs",
                  "8":"tuv",
                  "9":"wxyz"}

        def helper(idx,curr_str):
            if idx == len(digits):
                res.append(curr_str)
                return res
            
            for letter in maping[digits[idx]]:
                helper(idx+1,curr_str + letter)

        helper(0,"")

        return res


        