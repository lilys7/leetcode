class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        courses = {i : [] for i in range(numCourses)}
        for course, pre in prerequisites:
            courses[course].append(pre)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if courses[crs] == []:
                return True #all prereqs met
            
            visited.add(crs)
            #iterate through every course in the prereqs, running dfs
            for pre in courses[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            courses[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True



