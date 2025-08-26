class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        premap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            premap[crs].append(pre)
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if premap[crs] == []:
                return True
            
            visit.add(crs)

            for pre in premap[crs]:
                if not dfs(pre):
                    return False

            visit.remove(crs)  #backtrack
            #premap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
            
            





        