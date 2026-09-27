class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()
        cycle = set()
        res = [] # append everytime valid, anytime have invalid we just return empty list
        def dfs(crs):
            if crs in visited:
                return True
            if crs in cycle:
                return False
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre) : return False
            visited.add(crs)
            cycle.remove(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        return res
        
        for crs in range(numCourses):
            if not dfs(crs): return []
        return res

