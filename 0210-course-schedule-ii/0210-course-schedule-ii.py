class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        premap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            premap[crs].append(pre)
        visit,cycle = set(),set()
        output = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)

            for pre in premap[crs]:
                if not dfs(pre):
                    return []
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return output

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output
            

