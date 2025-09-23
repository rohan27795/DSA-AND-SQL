class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row,col = len(board),len(board[0])
        path = set()
        def dfs(r,c,i):
            if i == len(word):
                return True
            if (r<0 or c<0 or r >= row or 
                c >= col or (r,c) in path or word[i] != board[r][c]):
                return False
        
            path.add((r,c))
            res = (dfs(r+1,c,i+1)or
                  dfs(r-1,c,i+1)or
                  dfs(r,c+1,i+1)or
                  dfs(r,c-1,i+1))
            path.remove((r,c))
            return res

        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False
        